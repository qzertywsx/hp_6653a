# HP_6653A
Python module for the HP 6653A power supply.

You must use my GPIB or GPIB_WIFI module to use this module.

## Supported command:
### get_IDN()
Return the *IDN? of the instrument

### reset()
Reset the instrument to the default state

### setOutput(on)
Set the output
<table>
  <tr><td>on</td><td>Description</td></tr>
  <tr><td>True</td><td>Enable the output</td></tr>
  <tr><td>False</td><td>Disable the output</td></tr>
</table>

### getOutput()
Get the output state
<table>
  <tr><td>Return</td><td>Description</td></tr>
  <tr><td>True</td><td>The output is enabled</td></tr>
  <tr><td>False</td><td>The output is disabled</td></tr>
</table>

### setVoltage(volt)
Set the voltage to `volt`

### getVoltage()
Return the measured voltage or `False` in case of problem

### setCurrent(amps)
Set the current to `amps`

### getCurrent()
Return the measured current or `False` in case of problem

### setVoltageCurrent(volt, amps)
Set the voltage to `volt` and the current to `amps`

### setDisplay(on)
Switch the display on or off
<table>
  <tr><td>on</td><td>Description</td></tr>
  <tr><td>True</td><td>Switch on the display</td></tr>
  <tr><td>False</td><td>Switch off the display</td></tr>
</table>

### setDisplayNormal()
Set the display to normal mode (Show the measured value) 

### setDisplayText(text)
Set a custom `text` on the display (Max 12 character)

### getDisplayText()
Get the custom text currently on the display

### local()
Go to local mode (Reenable the front panel control)

## Usage:
```python
from GPIB_WIFI import AR488_WIFI
from HP_6653A import HP_6653A

gpib = AR488_WIFI('192.168.178.36', timeout=5)
psu = HP_6653A( gpib, 7)
psu.setVoltage(5)
psu.setCurrent(0.5)
psu.setOutput(True)
print("Voltage:", psu.getVoltage(), "V")
print("Current:", psu.getCurrent(), "A")
psu.setOutput(False)
psu.local()
```
## Result of executing the above code (Not done yet):
```
GPIB address: 7, IP: 192.168.178.36
```
