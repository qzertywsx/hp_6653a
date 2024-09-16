from enum import Enum

class HP_6653A(object):
	def __init__(self, gpib, addr):
		self.address = addr
		self.gpib = gpib
		self.firstTime = True
		self.dispMode = self.DisplayMode.NORMAL
		self._preCommand()
	
	class DisplayMode(Enum):
		NORMAL = 0
		TEXT   = 1
	
	def __str__(self):
		return "HP 6653A address: " + str(self.address)
	
	def _preCommand(self):
		"""Command to be executed before every other command"""
		if self.gpib.address != self.address or self.firstTime:
			self.firstTime = False
			self.gpib.set_address(self.address)
			self.gpib.write("++eor 2")
	
	def get_IDN(self):
		"""Return the *IDN? of the instrument"""
		return self.gpib.get_IDN()
	
	def reset(self):
		"""Reset the instrument to the default state"""
		self._preCommand()
		self.gpib.write("*CLS")
	
	def setOutputState(self, on):
		"""Enable the output"""
		self._preCommand()
		if on:
			self.gpib.write("OUTP ON")
		else:
			self.gpib.write("OUTP OFF")
			
	def getOutputState(self):
		"""Get the output state"""
		self._preCommand()
		self.gpib.write("OUTP?")
		return self.gpib.query("++read") == "1"
	
	def setVoltage(self, volt):
		"""Set the voltage"""
		self._preCommand()
		if volt >= 0.0 and volt <= 35.831:
			self.gpib.write("VOLT {:.3f}".format(volt))
			return True
		else:
			return False
		
	def getVoltage(self):
		"""Return the measured voltage or False in case of problem"""
		self._preCommand()
		self.gpib.write("MEAS:VOLT?")
		try:
			return float(self.gpib.query("++read"))
		except:
			return False
		
	def setCurrent(self, amps):
		"""Set the current"""
		self._preCommand()
		if amps >= 0.0 and amps <= 15.356:
			self.gpib.write("CURR {:.3f}".format(amps))
			return True
		else:
			return False
		
	def getCurrent(self):
		"""Return the measured current or False in case of problem"""
		self._preCommand()
		self.gpib.write("MEAS:CURR?")
		try:
			return float(self.gpib.query("++read"))
		except:
			return False
			
	def setVoltageCurrent(self, volt, amps):
		"""Set the output voltage and current"""
		self._preCommand()
		if volt >= 0.0 and volt <= 35.831 and amps >= 0.0 and amps <= 15.356:
			self.gpib.write("VOLT {:.3f};CURR {:.3f}".format(volt, amps))
			return True
		else:
			return False
	
	def setDisplayState(self, on):
		"""Switch the display on or off"""
		self._preCommand()
		if on:
			self.gpib.write("DISP ON")
		else:
			self.gpib.write("DISP OFF")
	
	def setDisplayNormal(self):
		"""Set the display to normal mode (Show the measured value)"""
		self._preCommand()
		self.gpib.write(f"DISP:MODE NORM")
		self.dispMode = self.DisplayMode.NORMAL
		
	def setDisplayText(self, text):
		"""Set a custom text on the display (Max 12 character)"""
		self._preCommand()
		if self.dispMode == self.DisplayMode.NORMAL:
			self.gpib.write(f"DISP:MODE TEXT")
			self.dispMode = self.DisplayMode.TEXT
		self.gpib.write(f"DISP:TEXT \"{text}\"")
	
	def getDisplayText(self):
		"""Get the custom text currently on the display"""
		self._preCommand()
		self.gpib.write("DISP:TEXT?")
		return self.gpib.query("++read")
	
	def local(self):
		"""Go to local mode (Reenable the front panel control)"""
		self._preCommand()
		self.gpib.local()
