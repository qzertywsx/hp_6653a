from enum import Enum

class HP_6653A(object):
	def __init__(self, gpib, addr):
		self.address = addr
		self.gpib = gpib
		self.firstTime = True
		self.dispMode = self.DisplayMode.NORMAL
		self.preCommand()
	
	class DisplayMode(Enum):
		NORMAL = 0
		TEXT   = 1
	
	def preCommand(self):
		if self.gpib.address != self.address or self.firstTime:
			self.firstTime = False
			self.gpib.set_address(self.address)
			self.gpib.write("++eor 2")
	
	def get_IDN(self):
		return self.gpib.get_IDN()
	
	def reset(self):
		self.preCommand()
		self.gpib.write("*CLS")
	
	def setOutput(self, on):
		self.preCommand()
		if on:
			self.gpib.write("OUTP ON")
		else:
			self.gpib.write("OUTP OFF")
			
	def getOutput(self):
		self.preCommand()
		self.gpib.write("OUTP?")
		return self.gpib.query("++read") == "1"
	
	def setVoltage(self, volt):
		self.preCommand()
		self.gpib.write("VOLT {:.3f}".format(volt))
		
	def getVoltage(self):
		self.preCommand()
		self.gpib.write("MEAS:VOLT?")
		try:
			return float(self.gpib.query("++read"))
		except:
			return False
		
	def setCurrent(self, amps):
		self.preCommand()
		self.gpib.write("CURR {:.3f}".format(amps))
		
	def getCurrent(self):
		self.preCommand()
		self.gpib.write("MEAS:CURR?")
		try:
			return float(self.gpib.query("++read"))
		except:
			return False
			
	def setVoltageCurrent(self, volt, amps):
		self.preCommand()
		self.gpib.write("VOLT {:.3f};CURR {:.3f}".format(volt, amps))
	
	def setDisplay(self, on):
		self.preCommand()
		if on:
			self.gpib.write("DISP ON")
		else:
			self.gpib.write("DISP OFF")
	
	def setDisplayNormal(self):
		self.preCommand()
		self.gpib.write(f"DISP:MODE NORM")
		self.dispMode = self.DisplayMode.NORMAL
	
	def setDisplayText(self, text):
		self.preCommand()
		if self.dispMode == self.DisplayMode.NORMAL:
			self.gpib.write(f"DISP:MODE TEXT")
			self.dispMode = self.DisplayMode.TEXT
		self.gpib.write(f"DISP:TEXT \"{text}\"")
	
	def getDisplayText(self):
		self.preCommand()
		self.gpib.write("DISP:TEXT?")
		return self.gpib.query("++read")
	
	def local(self):
		self.preCommand()
		self.gpib.local()
