
from source.extra.fileIO import fileIO
import sys
import pygame

import os
from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from vcgencmd import Vcgencmd #see if this is needed
import pigpio

class config:
	__white = (255, 255, 255)
	__red = (255, 0, 0)
	__color = ( 0, 255, 255 )
	__colorInv = __red
	__colorFile = "/home/pi/SmartMirror/data/configFiles/colorFile.txt"
	__brightnessFile = "/home/pi/SmartMirror/data/configFiles/brightnessFile.txt"
	__fontFile = "/home/pi/SmartMirror/data/configFiles/fontFile.txt"
	__speedFile = "/home/pi/SmartMirror/data/configFiles/speedFile.txt"
	__viewFile = "/home/pi/SmartMirror/data/configFiles/viewFile.txt"
	__sleepFile = "/home/pi/SmartMirror/data/configFiles/sleepTimer.txt"

	__fileIO = fileIO( )
	__defFontName = "Serif"

	def __init__( self ):
		self.__vcgencmd = Vcgencmd( )
		self.__pwm = pigpio.pi( )
		self.__valChange = ["None", "None", "None"]
		self.__fonts = [0] *8
		self.__cSize = 0

		self.__scheduler = BackgroundScheduler( )
		self.__scheduler.start( )

		self.__sleepF1 = True
		self.__sleepF2 = True

		self.__stayOffFlag = False

	def getStayOffFlag( self ):
		return self.__stayOffFlag
	def setStayOffFlag( self, state ):
		self.__stayOffFlag = state

	def restartDim( self ):
		sleep = self.__fileIO.simpleRead( self.__sleepFile, multiLine=True )
		try:
			self.__scheduler.reschedule_job( "dim", trigger='interval', minutes=int( sleep[2] ))
		except:
			print( datetime.now( ).strftime( "%H:%M:%S" ), "IN config::restartDim: cannot reschedule job!" )
			return -1

	def setColor( self ):
		color, colorInv = self.__fileIO.simpleRead( self.__colorFile, separator=":" )
		self.__color = [int( color[ i : i +2 ], 16 ) for i in range( 1, len(color) -1, 2 )]
		self.__colorInv = [int( colorInv[ i : i +2 ], 16 ) for i in range( 1, len(colorInv) -1, 2 )]
		if( self.__color == self.__white ):
			self.__colorInv = self.__red

		return self.__color, self.__colorInv

	def setSleepTime( self ):
		sleep = self.__fileIO.simpleRead( self.__sleepFile, multiLine=True )
		if( len( sleep ) > 4 ):
			if( self.__valChange[0] != sleep[0] or self.__valChange[1] != sleep[1] ):
				try:
					self.__sleepF1 = True
					self.__scheduler.remove_job( 'dpoff' )
					self.__scheduler.remove_job( 'dpon' )
				except:
					print( datetime.now( ).strftime( "%H:%M:%S"), "IN config::setSleepTime: jobs dont exist!" )
			if( self.__valChange[2] != sleep[2] ):
				try:
					self.__sleepF2 = True
					self.__scheduler.remove_job( "dim" )
				except:
					print( datetime.now( ).strftime( "%H:%M:%S"), "IN config::setSleepTime: jobs dont exist!" )

			if( sleep[3] in "False" and self.__sleepF1 ):
				self.__sleepF1 = False
				hr = int( sleep[0].split(":")[0] )
				mi = int( sleep[0].split(":")[1] )
				self.__scheduler.add_job( self.displayOff, "cron", hour=hr, minute=mi, id='dpoff' )
				hr = int( sleep[1].split(":")[0] )
				mi = int( sleep[1].split(":")[1] )
				self.__scheduler.add_job( self.displayOn, "cron", hour=hr, minute=mi, id='dpon' )
			elif( sleep[3] in "True" and not self.__sleepF1 ):
				self.__sleepF1 = True
				self.__scheduler.remove_job( 'dpoff' )
				self.__scheduler.remove_job( 'dpon' )
				self.__vcgencmd.display_power_on( 2 )
			if( sleep[4] in "False" and self.__sleepF2 ):
				self.__sleepF2 = False
				self.__scheduler.add_job( lambda: self.__pwm.set_PWM_dutycycle( 18, 0 ), 'interval', minutes=int( sleep[2] ), id='dim' )
			elif( sleep[4] in "True" and not self.__sleepF2 ):
				self.__sleepF2 = True
				self.__scheduler.remove_job( 'dim' )
				self.__vcgencmd.display_power_on( 2 )
				self.__pwm.set_PWM_dutycycle( 18, int( self.__fileIO.simpleRead( self.__brightnessFile )))
				self.displayOn( )
			self.__valChange = [sleep[0], sleep[1], sleep[2]]

	def displayOn( self ):
		self.__vcgencmd.display_power_on( 2 )
		brightness = self.__fileIO.simpleRead( self.__brightnessFile )
		self.__pwm.set_PWM_dutycycle( 18, int( brightness ))
		self.__stayOffFlag = False

	def displayOff( self ):
		self.__pwm.set_PWM_dutycycle( 18, 0 )
		self.__stayOffFlag = True

	def readFontFromFile( self ):
		font = self.__fileIO.simpleRead( self.__fontFile, multiLine=True )
		font[ 0 ] = font[ 0 ].split( "," )[ 0 ]
		font[ 1 ] = int( font[ 1 ])
		if( len( font ) == 2 ):
			font.append( False )
			font.append( False )
		elif( len( font ) == 3 ):
			if( 'Bold' in font[ 2 ]):
				font[ 2 ] = True
				font.append( False )
			else:
				font[ 2 ] = False
				font.append( True )
		elif( len( font ) == 4 ):
			font[ 2 ] = True
			font[ 3 ] = True
		return font

	def getFont( self, index ):
		return self.__fonts[index]
	def getDefFont( self ):
		return self.__defFont
	def getMetFont( self ):
		return self.__metFont

	def setCSize( self, size ):
		self.__cSize = size

	def getSpeed( self ):
		speed = self.__fileIO.simpleRead( self.__speedFile )
		if( "Non" in speed ):
			return 0
		else:
			return int( speed ) * 1000

	def getView( self ):
		return self.__fileIO.simpleRead( self.__viewFile, multiLine=True )[0]

	def getAllFonts( self ):
		fontName, fontSize, bold, italic = self.readFontFromFile( )
		try:
			self.__defFont  = pygame.font.SysFont( self.__defFontName, fontSize - 12, bold=bold, italic=italic )
			self.__metFont  = pygame.font.SysFont( self.__defFontName, fontSize - 4, bold=bold, italic=italic )
			self.__fonts[0] = pygame.font.SysFont( fontName, fontSize + self.__cSize, bold=bold, italic=italic )#calendar
			self.__fonts[1] = pygame.font.SysFont( fontName, fontSize + 0 , bold=bold, italic=italic )#date
			self.__fonts[2] = pygame.font.SysFont( fontName, fontSize + 32 , bold=bold, italic=italic )#time
			self.__fonts[3] = pygame.font.SysFont( fontName, fontSize - 12 , bold=bold, italic=italic )#events
			self.__fonts[4] = pygame.font.SysFont( fontName, fontSize - 12 , bold=bold, italic=italic )#news
			self.__fonts[5] = pygame.font.SysFont( fontName, fontSize - 4, bold=bold, italic=italic )#weather
			self.__fonts[6] = pygame.font.SysFont( fontName, fontSize - 12 , bold=bold, italic=italic )#hour
			self.__fonts[7] = pygame.font.SysFont( fontName, fontSize - 18 , bold=bold, italic=italic )#hour
		except:
			self.__defFont  = pygame.font.Font( self.__defFontName, fontSize - 12, bold=bold, italic=italic )
			self.__metFont  = pygame.font.Font( self.__defFontName, fontSize - 4, bold=bold, italic=italic )
			self.__fonts[0] = pygame.font.Font( fontName, fontSize , bold=bold, italic=italic )
			self.__fonts[1] = pygame.font.Font( fontName, fontSize + 0 , bold=bold, italic=italic )
			self.__fonts[2] = pygame.font.Font( fontName, fontSize + 32 , bold=bold, italic=italic )
			self.__fonts[3] = pygame.font.Font( fontName, fontSize - 12 , bold=bold, italic=italic )
			self.__fonts[4] = pygame.font.Font( fontName, fontSize - 12 , bold=bold, italic=italic )
			self.__fonts[5] = pygame.font.Font( fontName, fontSize - 4 , bold=bold, italic=italic )
			self.__fonts[6] = pygame.font.Font( fontName, fontSize - 12 , bold=bold, italic=italic )
			self.__fonts[7] = pygame.font.Font( fontName, fontSize - 18 , bold=bold, italic=italic )
		return self.__fonts
