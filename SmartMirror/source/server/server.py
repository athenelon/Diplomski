import socket
import time
import threading
from source.extra.fileIO import fileIO

from datetime import datetime

class socketServer:
	#__ip = '192.168.0.219'
	#__ip = '127.0.0.1'
	__ip = '10.10.32.138'
	__port = 14036

	def __init__( self ):

		self.__listenFlag = True
		self.__runFlag = True

		self.__eventFlag = False
		self.__configFlag = False
		self.__weatherFlag = False
		self.__newsFlag = False
		self.__weatherGetFlag = False
		self.__serverBound = False

		self.__fileIO = fileIO( )

		self.__server = socket.socket( socket.AF_INET, socket.SOCK_STREAM )

	def getEventFlag( self ):
		return self.__eventFlag
	def getConfigFlag( self ):
		return self.__configFlag
	def getWeatherFlag( self ):
		return self.__weatherFlag
	def getNewsFlag( self ):
		return self.__newsFlag
	def getWeatherGetFlag( self ):
		return self.__weatherGetFlag

	def setEventFlag( self, state ):
		self.__eventFlag = state
	def setConfigFlag( self, state ):
		self.__configFlag = state
	def setWeatherFlag( self, state ):
		self.__weatherFlag = state
	def setNewsFlag( self, state ):
		self.__newsFlag	 = state
	def setWeatherGetFlag( self, state ):
		self.__weatherGetFlag = state

	def bindServer( self ):
		if( not self.__serverBound ):
			try:
				self.__server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
				self.__server.bind(( self.__ip, self.__port ))
				self.__server.listen( 5 )

				delay = 0.1
				listenThread = threading.Thread( target=self.listenForClient, args=(delay,))
				listenThread.start( )

				self.__serverBound = True
			except:
				print( datetime.now( ).strftime( "%H:%M:%S"), "IN server::bindServer: could not open server!" )

			return True
		else:
			return False

	def listenForClient( self, delay ):
		while( self.__listenFlag ):
			print( datetime.now( ).strftime( "%H:%M:%S"), "Server is listening...")
			conn, addr = self.__server.accept( )
			print( "\n\n", datetime.now( ).strftime( "%H:%M:%S"), " Client <" + str(addr[ 1 ]) + "> Connected...", sep='' )
			thread = threading.Thread( target=self.clientThread, args=(conn, addr, delay))
			thread.start( )

	def clientThread( self, conn, addr, delay ):
		runFlag = True
		while( runFlag ):
			data, runFlag = self.getClientData( conn, runFlag )
			runFlag = self.setClientData( data, runFlag )

		print( "\n", datetime.now( ).strftime( "%H:%M:%S"), " Client <" + str( addr[ 1 ]) + "> Disconnected...\n", sep='' )
		time.sleep( delay )
		conn.close( )

	def getClientData( self, conn, runFlag ):#use decode when u have everything
		data = b''
		dataSegment = conn.recv( 4096 )

		while( len( dataSegment ) >= 1 ):
			if( b"clientPing" in dataSegment ):
				print( datetime.now( ).strftime( "%H:%M:%S"), "\033[92m clientPing \033[0m" )
				break

			if( b"~pingDisc~" in dataSegment ):
				print( datetime.now( ).strftime( "%H:%M:%S"), "Disconnecting ping thread")
				runFlag = False
				break

			data += dataSegment
			dataSegment = conn.recv( 4096 )
		return data.decode( ), runFlag

	def setClientData( self, data, runFlag ):
		if( len( data ) >= 1 ):
			data = data.split( ";~;" )
			if( "~file~" in data[ 0 ]):
				print( datetime.now( ).strftime( "%H:%M:%S"), "\033[91m" + data[ 1 ] + "\033[0m" )
				self.__fileIO.makePath( "/home/pi/SmartMirror/" + data[ 1 ] )

			if( "~data~" in data[ 2 ] ):
				self.__fileIO.simpleWrite( "/home/pi/SmartMirror/" + data[ 1 ], data[ 3 ], newLine=True )
				self.updateFlags( data[1] )

			if( "~disc~" in data ):
				runFlag = False
				print( datetime.now( ).strftime( "%H:%M:%S"), "disc")
		return runFlag

	def updateFlags( self, data ):
		if( "data/events" in data ):
			self.__eventFlag = True
		if( "data/configFiles" in data ):
			self.__configFlag = True
		if( "data/weather" in data ):
			self.__weatherFlag = True
			self.__weatherGetFlag = True
		if( "data/news" in data ):
			self.__newsFlag = True

	def stopServer( self ):
		self.__runFlag = False
		self.__listenFlag = False
		self.__server.close( )
