from source.extra.fileIO import fileIO
from source.app.drawPygame import drawPygame
import requests
import pygame

from datetime import datetime

class weather(drawPygame):
	__apiKey = "axtloV8pqzpCuvRImrZgGhASPTbDSphV"
	#__iconPath = "/home/pi/SmartMirror/data/weather/icons/"
	__iconPath = "/home/pi/SmartMirror/icons/"
	__weatherFile = "/home/pi/SmartMirror/data/weather/weather.txt"
	__weatherDataFile = "/home/pi/SmartMirror/data/weather/weatherData.txt"

	__fileIO = fileIO( )

	def __init__( self, xOffset, yOffset, move ):
		super( ).__init__( xOffset, yOffset, move )
		pygame.init( )
		self.__weather = []
		self.__data = []
		self.__metricSymbol = "True"

	def saveWeatherFormat( self, weather ):
		self.__data = []
		for hour in weather:
			hourlyData = hour[ 'DateTime' ].split( "T" )[1] + "~" + str( hour[ 'WeatherIcon' ]) + "~" + str( hour[ 'PrecipitationProbability']) + "~" + str( hour[ 'Temperature'][ 'Value' ])
			self.__data.append( hourlyData )

	def getWeather( self ):
		weatherConfig = self.__fileIO.simpleRead( self.__weatherFile, multiLine=True )
		if( weatherConfig[0] in "Celsius"):
			self.__metricSymbol = "True"
		else:
			self.__metricSymbol = "False"
		city = weatherConfig[1]
		try:
			url = "http://dataservice.accuweather.com/locations/v1/cities/RS/search?apikey= " + self.__apiKey + "&q=" + city
			result = requests.get( url ).json( )
			url = "http://dataservice.accuweather.com/forecasts/v1/hourly/12hour/" + result[ 0 ][ 'Key' ] + "?apikey= " + self.__apiKey + "&metric=" + self.__metricSymbol
			weather = requests.get( url ).json( )

			self.saveWeatherFormat( weather )
		except:
			print( datetime.now( ).strftime( "%H:%M:%S"), "IN weather::getWeather: Error getting new weather")

	def renderText( self, color, colorInv, hFont, font, defFont ):
		self.__hour = []
		self.__icon = []
		self.__perc = []
		self.__temp = []
		#self.__data = ["00:11:11" + "~" + str( 1 ) + "~" + str( 20 ) + "~" + str( 20 ),"01:11:11" + "~" + str( 1 ) + "~" + str( 20 ) + "~" + str( 20 ),"02:11:11" + "~" + str( 1 ) + "~" + str( 20 ) + "~" + str( 20 ),"03:11:11" + "~" + str( 1 ) + "~" + str( 20 ) + "~" + str( 20 ),"04:11:11" + "~" + str( 1 ) + "~" + str( 20 ) + "~" + str( 20 ),"05:11:11" + "~" + str( 1 ) + "~" + str( 20 ) + "~" + str( 20 ),"06:11:11" + "~" + str( 1 ) + "~" + str( 20 ) + "~" + str( 20 ),"07:11:11" + "~" + str( 1 ) + "~" + str( 20 ) + "~" + str( 20 ),"08:11:11" + "~" + str( 1 ) + "~" + str( 20 ) + "~" + str( 20 ),"09:11:11" + "~" + str( 1 ) + "~" + str( 20 ) + "~" + str( 20 ),"10:11:11" + "~" + str( 1 ) + "~" + str( 20 ) + "~" + str( 20 ),"11:11:11" + "~" + str( 1 ) + "~" + str( 20 ) + "~" + str( 20 ),"12:11:11" + "~" + str( 1 ) + "~" + str( 20 ) + "~" + str( 20 )]
		for t in self.__data:
			hour, icon, perc, temp = t.split( "~" )
			self.__hour.append( hFont.render( hour.split( ":" )[0] + ":" + hour.split( ":" )[1], True, colorInv ))
			self.__perc.append( font.render( perc + "%", True, color ))
			self.__temp.append( font.render( str(round(float(temp))), True, color ))
			if( self.__metricSymbol == "True" ):
				self.__metric = defFont.render( '\u2103', True, color )#*C
			else:
				self.__metric = defFont.render( '\u2109', True, color )#*F

			self.__icon.append( pygame.image.load( self.__iconPath + icon + ".png" ))

	def drawText( self, screen, numOfHours, everyNumOfHours, numOfColumns ):
		if( super( ).getDrawFlag( ) and len( self.__data )):
			x = 0
			z = 0
			for j, i in enumerate( range( 0, numOfHours, everyNumOfHours )):
				if( not j % numOfColumns and j != 0 ):
					x += 1
					z = 0

				screen.blit( self.__hour[i], ( super( ).getXoffset( ) * super( ).getStep( ) + super( ).getStep( )*1.6 + z*( 3*super( ).getStep( ) - super( ).getMove( )), 
											   super( ).getYoffset( ) * super( ).getStep( ) + x*( 1.7*super( ).getStep( ) - super( ).getMove( ) )))
				screen.blit( self.__perc[i], ( super( ).getXoffset( ) * super( ).getStep( ) + super( ).getStep( )*.5 + z*( 3*super( ).getStep( ) - super( ).getMove( )), 
											   super( ).getYoffset( ) * super( ).getStep( ) + super( ).getStep( )*.66 + x*( 1.7* super( ).getStep( ) - super( ).getMove( ) )))
				screen.blit( self.__temp[i], ( super( ).getXoffset( ) * super( ).getStep( ) + super( ).getStep( )*.5 + z*( 3*super( ).getStep( ) - super( ).getMove( )), 
											   super( ).getYoffset( ) * super( ).getStep( ) + x*( 1.7*super( ).getStep( ) - super( ).getMove( ) )))
				screen.blit( self.__metric,  ( super( ).getXoffset( ) * super( ).getStep( ) + super( ).getStep( )*.5 + z*( 3*super( ).getStep( ) - super( ).getMove( )) + self.__temp[i].get_width( ) +2, 
											   super( ).getYoffset( ) * super( ).getStep( ) + x*( 1.7*super( ).getStep( ) - super( ).getMove( ) ) + ( self.__temp[i].get_height( ) / 2 - self.__metric.get_height( ) / 2 )))
				screen.blit( self.__icon[i], ( super( ).getXoffset( ) * super( ).getStep( ) + super( ).getStep( )*1.4 + z*( 3*super( ).getStep( ) - super( ).getMove( )), 
											   super( ).getYoffset( ) * super( ).getStep( ) + super( ).getStep( )*.5 + x*( 1.7*super( ).getStep(  ) -super( ).getMove( ) )))
				z += 1
