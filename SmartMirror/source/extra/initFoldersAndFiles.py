import os
from pathlib import Path

class initFoldersAndFiles:
	folderNames = [ "/home/pi/SmartMirror/data", "/home/pi/SmartMirror/data/configFiles", "/home/pi/SmartMirror/data/events", "/home/pi/SmartMirror/data/news", "/home/pi/SmartMirror/data/weather" ]
	files = [{ 'Name' : "/home/pi/SmartMirror/data/configFiles/brightnessFile.txt", 'Value' : "255" }, 
			 { 'Name' : "/home/pi/SmartMirror/data/configFiles/colorFile.txt", 'Value' : "#00ffff:#ff0000" }, 
			 { 'Name' : "/home/pi/SmartMirror/data/news/countryFile.txt", 'Value' : "Serbia;~sepa~;rs" }, 
			 { 'Name' : "/home/pi/SmartMirror/data/configFiles/fontFile.txt", 'Value' : "Times New Roman\n32" }, 
			 { 'Name' : "/home/pi/SmartMirror/data/weather/weather.txt", 'Value' : "Celsius\nNovi Sad" },
			 { 'Name' : "/home/pi/SmartMirror/data/news/categoryFile.txt", 'Value' : "General"},
			 { 'Name' : "/home/pi/SmartMirror/data/configFiles/speedFile.txt", 'Value' : "5"},
			 { 'Name' : "/home/pi/SmartMirror/data/configFiles/viewFile.txt", 'Value' : "Default"}]

	def initAllFiles( self ):
		for f in self.files:
			if( not Path( f[ 'Name' ]).exists( )):
				file = open( f[ 'Name' ], "w")
				file.write( f['Value'])
				file.close( )

	def initAllFolders( self ):
		for f in self.folderNames:
			if( not Path( f ).exists( )):
				os.mkdir( f )
