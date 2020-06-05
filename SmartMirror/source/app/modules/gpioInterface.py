import RPi.GPIO as GPIO
import time
import os
from vcgencmd import Vcgencmd
from source.extra.fileIO import fileIO

import pigpio

class gpioInterface:
	__displayFlag = False
	__viewFlag = False
	__viewOptions = [ "Default", "Default+", "Calendar+Events", "Calendar+Weather",
					  "Calendar+Weather+Events", "Calendar+Weather+Events+" ]
	__viewCnt = 0

	__fileIO = fileIO( )
	__viewFile = "/home/pi/SmartMirror/data/configFiles/viewFile.txt"
	__brightnessFile = "/home/pi/SmartMirror/data/configFiles/brightnessFile.txt"

	def __init__( self ):
		self.__vcgencmd = Vcgencmd( )

		GPIO.setmode( GPIO.BOARD )
		GPIO.setwarnings( False )
		GPIO.setup( 11, GPIO.IN, pull_up_down=GPIO.PUD_UP )#PIR data

		GPIO.setup( 15, GPIO.IN, pull_up_down=GPIO.PUD_UP )#View change button
		GPIO.setup( 13, GPIO.IN, pull_up_down=GPIO.PUD_UP )#Display on/off button
		GPIO.setup( 5, GPIO.IN, pull_up_down=GPIO.PUD_UP )#power up/down button

		self.__pwm = pigpio.pi()

		GPIO.add_event_detect( 15, GPIO.FALLING, callback=self.viewChange, bouncetime=250 )
		GPIO.add_event_detect( 13, GPIO.FALLING, callback=self.displayToggle, bouncetime=500 )
		GPIO.add_event_detect( 5, GPIO.FALLING, callback=self.shutdown, bouncetime=2000 )

	def getViewFlag( self ):
		return self.__viewFlag
	def setViewFlag( self, state ):
		self.__viewFlag = state
	def setDisplayFlag( self, state ):
		self.__displaFlag = state

	def pirSensor( self ):
		if( not self.__displayFlag ):
			if( GPIO.input( 11 )):
				return 1
			else:
				return 0

	def displayToggle( self, channel ):
		if( self.__displayFlag ):
			self.__displayFlag = False
			#self.__vcgencmd.display_power_on( 2 )
			self.setBrightness( )
		else:
			self.__displayFlag = True
			#self.__vcgencmd.display_power_off( 2 )
			self.__pwm.set_PWM_dutycycle( 18, 0 )

	def viewChange( self, channel ):
		if( self.__viewCnt >= len( self.__viewOptions ) -1 ):
			self.__viewCnt = 0
		else:
			self.__viewCnt += 1
		print( self.__viewCnt )
		self.__fileIO.simpleWrite( self.__viewFile, self.__viewOptions[self.__viewCnt] )
		self.__viewFlag = True

	def shutdown( self, channel ):
		self.__pwm.write( 18, 0 )
		print( "SHUTDOWN" )
		time.sleep( 1 )
		os.system( "sudo shutdown -h now" )

	def setBrightness( self ):
		brightness = self.__fileIO.simpleRead( self.__brightnessFile )
		self.__pwm.set_PWM_dutycycle( 18, int( brightness ))
		self.__displayFlag = False
