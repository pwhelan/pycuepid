import struct
from PyQt4 import QtCore
from PyQt4.QtGui import *

class WaveFormWidget(QWidget):
	def setWaveForm(self, waveform):
		self._waveform = waveform
	
	def paintEvent(self, QPaintEvent):
		if self._waveform == None:
			return
		
		painter = QPainter(self)
		
		for spos in xrange(1, 600):
			wpos = spos * 512
			prevsample = self._waveform[wpos]
			sample = self._waveform[wpos+512]
			x1 = spos-1
			y1 = (float(prevsample+32768)/65536.0) * 300
			x2 = spos
			y2 = (float(sample+32768)/65536.0) * 300
			
			#print "Prev:", prevsample, "Sample:", sample
			#print "Coordinates:", x1, y1, "=>", x2, y2 
			painter.drawLine(QtCore.QLineF(x1, y1, x2, y2))
			
		


