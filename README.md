# hp_6653a
Python module for the HP 6653A 35 V 15 A power supply.

You must use my GPIB or GPIB_WIFI module to use this module.

## Supported command:
### get_idn()
Return the *IDN? of the instrument

### reset()
Reset the instrument to the default state

### set_output_state(on)
Set the output
<table>
  <tr><td>on</td><td>Description</td></tr>
  <tr><td>True</td><td>Enable the output</td></tr>
  <tr><td>False</td><td>Disable the output</td></tr>
</table>

### get_output_state()
Get the output state
<table>
  <tr><td>Return</td><td>Description</td></tr>
  <tr><td>True</td><td>The output is enabled</td></tr>
  <tr><td>False</td><td>The output is disabled</td></tr>
</table>

### set_voltage(volt)
Set the voltage to `volt`

### get_set_voltage()
Return the set voltage or `False` in case of problem

### get_voltage()
Return the measured voltage or `False` in case of problem

### set_current(amps)
Set the current to `amps`

### get_set_current()
Return the set current or `False` in case of problem

### get_current()
Return the measured current or `False` in case of problem

### set_voltage_current(volt, amps)
Set the voltage to `volt` and the current to `amps`

### set_display_state(on)
Switch the display on or off
<table>
  <tr><td>on</td><td>Description</td></tr>
  <tr><td>True</td><td>Switch on the display</td></tr>
  <tr><td>False</td><td>Switch off the display</td></tr>
</table>

### set_display_normal()
Set the display to normal mode (Show the measured value) 

### set_display_text(text)
Set a custom `text` on the display (Max 12 character)

### get_display_text()
Get the custom text currently on the display

### get_error()
Get the last error

### local()
Go to local mode (Reenable the front panel control)

## Usage:
```python
from gpib_all import AR488Wifi
from hp_6653a import HP6653A

gpib = AR488Wifi('192.168.178.36')
psu = HP6653A(gpib, 7)
print(psu)
psu.set_voltage(5)
psu.set_current(0.5)
psu.set_output_state(True)
print("Voltage:", psu.get_voltage(), "V")
print("Current:", psu.get_current(), "A")
psu.set_output_state(False)
psu.local()
```
## Result of executing the above code:
```
HP 6653A address: 7
Voltage: 4.99663 V
Current: 0.308177 A
```
