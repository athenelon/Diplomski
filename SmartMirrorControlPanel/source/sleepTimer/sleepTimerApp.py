from source.extra.fileIO import fileIO
from source.extra.qtBasics import qtBasics, QtCore
from source.sleepTimer.sleepTimerUi import sleepTimerUi

class sleepTimerApp( qtBasics, sleepTimerUi ):
	__fileIO = fileIO( )
	__sleepFile = "data/configFiles/sleepTimer.txt"
	quitSignalExit = QtCore.pyqtSignal( int )
	quitSignalAccept = QtCore.pyqtSignal( int )

	def __init__( self, x, y ):
		sleepTimerUi.__init__( self, x, y )
		qtBasics.__init__( self )

		self.__text = ""

		self.applyButton.clicked.connect( self.applyClicked )
		self.disableCheckBox1.clicked.connect( self.toggleSleep )
		self.disableCheckBox2.clicked.connect( self.toggleWake )

	def applyClicked( self ):
		self.writeToFile( )
		self.setVisible( False )
		self.quitSignalAccept.emit( 1 )

	def writeToFile( self ):
		self.__text = str( self.sleepTimeEdit.text( )) + "\n" + str( self.wakeTimeEdit.text( )) + "\n" + str( self.spinBox.value( )) + "\n" + str( self.disableCheckBox1.isChecked( )) + "\n" + str( self.disableCheckBox2.isChecked( ))
		self.__fileIO.simpleWrite( self.__sleepFile, self.__text )

	def readFromFile( self ):
		text = self.__fileIO.simpleRead( self.__sleepFile, multiLine=True )
		time = text[0].split( ":" )
		self.sleepTimeEdit.setTime( QtCore.QTime( int( time[0] ), int( time[1] )))
		time = text[1].split( ":" )
		self.wakeTimeEdit.setTime( QtCore.QTime( int( time[0] ), int( time[1] )))
		self.spinBox.setValue( int( text[2] ))
		if( text[3] in "True" ):
			self.disableCheckBox1.setChecked( True )
		else:
			self.disableCheckBox1.setChecked( False )
		if( text[4] in "True" ):
			self.disableCheckBox2.setChecked( True )
		else:
			self.disableCheckBox2.setChecked( False )
		self.toggleSleep( )
		self.toggleWake( )
		
	def toggleSleep( self ):
		if( self.disableCheckBox1.isChecked( )):
			self.wakeTimeEdit.setEnabled( False )
			self.sleepTimeEdit.setEnabled( False )
		else:
			self.wakeTimeEdit.setEnabled( True )
			self.sleepTimeEdit.setEnabled( True )

	def toggleWake( self ):
		if( self.disableCheckBox2.isChecked( )):
			self.spinBox.setEnabled( False )
		else:
			self.spinBox.setEnabled( True )