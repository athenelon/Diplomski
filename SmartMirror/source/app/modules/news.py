from source.extra.fileIO import fileIO
from source.app.drawPygame import drawPygame
from newsapi import NewsApiClient

from datetime import datetime

class news( drawPygame ):
	__newsFile = "/home/pi/SmartMirror/data/news/newsStory.txt"
	__countryFile = "/home/pi/SmartMirror/data/news/countryFile.txt"
	__categoryFile = "/home/pi/SmartMirror/data/news/categoryFile.txt"
	__sourcesFile = "/home/pi/SmartMirror/data/news/sourcesFile.txt"

	__apiKey='4135e2a067ea41d19f8013a073ffc10f'

	__fileIO = fileIO( )

	def __init__( self, xOffset, yOffset, move ):
		self.__newsapi = NewsApiClient( self.__apiKey )
		super( ).__init__( xOffset, yOffset, move )

		self.__text = []

	def getText( self ):
		return self.__text

	def getNews( self ):
		category = self.__fileIO.simpleRead( self.__categoryFile, multiLine=True )
		if( len( category )):
			self.__text = self.getCategoryNews( )
		else:
			self.__text = self.getSourceNews( )

	def getCategoryNews( self ):
		country = self.__fileIO.simpleRead( self.__countryFile, separator=";~sepa~;" )[1]
		category = self.__fileIO.simpleRead( self.__categoryFile, multiLine=True )
		
		news = ''
		try:
			if( "ww" in country ):
				for i in range( len( category )):
					news += self.__newsapi.get_top_headlines( category=category[i].lower(),
															language="en" )
			else:
				for i in range( len( category )):
					news = self.__newsapi.get_top_headlines( category=category[i].lower(),
													   		country=country )

			return self.getTitle( news['articles'] )

		except:
			print( datetime.now( ).strftime( "%H:%M:%S"), "IN news::getCategoryNews: could not get_top_headlines!")
			return []

	def getSourceNews( self ):
		sourceList = self.__fileIO.simpleRead( self.__sourcesFile )
		try:
			news = self.__newsapi.get_everything( sources=','.join( sourceList ))
			return self.getTitle( news['articles'] )
		except:
			print( datetime.now( ).strftime( "%H:%M:%S"), "IN news::getSourceNews: could not get_everything!")
			return []
			
	def getTitle( self, articles ):
		title = []
		for story in articles:
			title.append( story['title'] )
		return title

	def getNewsFromFile( self ):
		news = self.__fileIO.simpleRead( self.__newsFile, multiLine=True, separator=";~sepa~;" )
		self.__text = [i[1] for i in news]
