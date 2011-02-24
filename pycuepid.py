#!/usr/bin/python

import sys, os.path, ao
import struct
import mad
import urllib

from PyQt4.QtGui import QApplication

from waveform import *


def LoadSet(u):
	mf = mad.MadFile(u)
	if mf.layer() == mad.LAYER_I:
		print "MPEG Layer I"
	elif mf.layer() == mad.LAYER_II:
		print "MPEG Layer II"
	elif mf.layer() == mad.LAYER_III:
		print "MPEG Layer III"
	else:
		print "unexpected layer value"
		
	if mf.mode() == mad.MODE_SINGLE_CHANNEL:
		print "single channel"
	elif mf.mode() == mad.MODE_DUAL_CHANNEL:
		print "dual channel"
	elif mf.mode() == mad.MODE_JOINT_STEREO:
		print "joint (MS/intensity) stereo"
	elif mf.mode() == mad.MODE_STEREO:
		print "normal L/R stereo"
	else:
		print "unexpected mode value"
		
	if mf.emphasis() == mad.EMPHASIS_NONE:
		print "no emphasis"
	elif mf.emphasis() == mad.EMPHASIS_50_15_US:
		print "50/15us emphasis"
	elif mf.emphasis() == mad.EMPHASIS_CCITT_J_17:
		print "CCITT J.17 emphasis"
	else:
		print "unexpected emphasis value"
		
	print "bitrate %lu bps" % mf.bitrate()
	print "samplerate %d Hz" % mf.samplerate()
	#millis = mf.total_time()
	#secs = millis / 1000
	#print "total time %d ms (%dm%2ds)" % (millis, secs / 60, secs % 60)
	
	#dev = ao.AudioDevice('alsa', bits=16, rate=mf.samplerate())
	samples = []
	while 1:
		buf = mf.read()
		if (buf is None) or (len(buf) <= 0) or (len(samples) > (44100*60)):
			print "DONE"
			break
		
		for i in xrange(0, len(buf), 4):
			#print "ADDING SAMPLE:", i, "SAMPLES:", len(samples)
			sample = struct.unpack_from("hh", buf, i)
			samples.append((sample[0]+sample[0])/2)

	print "DONE READING MP3"
	return samples


if __name__ == "__main__":
	
	app = QApplication(sys.argv)
	f = WaveForm()
	
	file = sys.argv[1]
	waveform = LoadSet(file)
	
	f.setWaveForm(waveform)
	f.show()
	sys.exit(app.exec_())


