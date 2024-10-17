"""Module providing an interface to the HP 6653A 35 V 15 A power supply"""
from enum import Enum

class HP6653A():
    """Class to represent the HP 6653A 35 V 15 A power supply"""
    def __init__(self, _gpib, addr):
        self.address = addr
        self.gpib = _gpib
        self.first_time = True
        self.disp_mode = self.DisplayMode.NORMAL
        self._pre_command()

    class DisplayMode(Enum):
        """Enum with the display mode"""
        NORMAL = 0
        TEXT   = 1

    def __str__(self):
        return "HP 6653A address: " + str(self.address)

    def _pre_command(self):
        """Command to be executed before every other command"""
        if self.gpib.address != self.address or self.first_time:
            self.first_time = False
            self.gpib.set_address(self.address)
            self.gpib.write("++eor 2")

    def get_idn(self):
        """Return the *IDN? of the instrument"""
        return self.gpib.get_idn()

    def reset(self):
        """Reset the instrument to the default state"""
        self._pre_command()
        self.gpib.write("*CLS")

    def set_output_state(self, on):
        """Enable the output"""
        self._pre_command()
        if on:
            self.gpib.write("OUTP ON")
        else:
            self.gpib.write("OUTP OFF")

    def get_output_state(self):
        """Get the output state"""
        self._pre_command()
        self.gpib.write("OUTP?")
        return self.gpib.query("++read") == "1"

    def set_voltage(self, volt):
        """Set the voltage"""
        self._pre_command()
        if 0.0 <= volt <= 35.831:
            self.gpib.write(f"VOLT {volt:.3f}")
            return True
        return False

    def get_set_voltage(self):
        """Return the measured voltage or False in case of problem"""
        self._pre_command()
        self.gpib.write("VOLT?")
        try:
            return float(self.gpib.query("++read"))
        except (ValueError, AttributeError):
            return False

    def get_voltage(self):
        """Return the measured voltage or False in case of problem"""
        self._pre_command()
        self.gpib.write("MEAS:VOLT?")
        try:
            return float(self.gpib.query("++read"))
        except (ValueError, AttributeError):
            return False

    def set_current(self, amps):
        """Set the current"""
        self._pre_command()
        if 0.0 <= amps <= 15.356:
            self.gpib.write(f"CURR {amps:.3f}")
            return True
        return False

    def get_set_current(self):
        """Return the measured current or False in case of problem"""
        self._pre_command()
        self.gpib.write("CURR?")
        try:
            return float(self.gpib.query("++read"))
        except (ValueError, AttributeError):
            return False

    def get_current(self):
        """Return the measured current or False in case of problem"""
        self._pre_command()
        self.gpib.write("MEAS:CURR?")
        try:
            return float(self.gpib.query("++read"))
        except (ValueError, AttributeError):
            return False

    def set_voltage_current(self, volt, amps):
        """Set the output voltage and current"""
        self._pre_command()
        if 0.0 <= volt <= 35.831 and 0.0 <= amps <= 15.356:
            self.gpib.write(f"VOLT {volt:.3f};CURR {amps:.3f}")
            return True
        return False

    def set_display_state(self, on):
        """Switch the display on or off"""
        self._pre_command()
        if on:
            self.gpib.write("DISP ON")
        else:
            self.gpib.write("DISP OFF")

    def set_display_normal(self):
        """Set the display to normal mode (Show the measured value)"""
        self._pre_command()
        self.gpib.write("DISP:MODE NORM")
        self.disp_mode = self.DisplayMode.NORMAL

    def set_display_text(self, text):
        """Set a custom text on the display (Max 12 character)"""
        self._pre_command()
        if self.disp_mode == self.DisplayMode.NORMAL:
            self.gpib.write("DISP:MODE TEXT")
            self.disp_mode = self.DisplayMode.TEXT
        self.gpib.write(f"DISP:TEXT \"{text}\"")

    def get_display_text(self):
        """Get the custom text currently on the display"""
        self._pre_command()
        self.gpib.write("DISP:TEXT?")
        return self.gpib.query("++read")

    def get_error(self):
        """Get the last error"""
        self._pre_command()
        self.gpib.write("SYST:ERR?")
        return self.gpib.query("++read")

    def local(self):
        """Go to local mode (Reenable the front panel control)"""
        self._pre_command()
        self.gpib.local()
