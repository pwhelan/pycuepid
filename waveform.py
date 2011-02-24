#!/usr/bin/python

from PyQt4.QtCore import pyqtSignature, QString, Qt, QVariant, SIGNAL, SLOT
from PyQt4.QtGui import *
from ui_waveform import Ui_WaveForm

class WaveForm(QMainWindow, Ui_WaveForm):

	def __init__(self, parent = None):
	
		QMainWindow.__init__(self, parent)
		self.setupUi(self)
	
	def setWaveForm(self, waveform):
		self.widget.setWaveForm(waveform)

