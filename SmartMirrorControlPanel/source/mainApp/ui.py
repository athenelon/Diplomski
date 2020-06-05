from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem, QColorDialog, QMainWindow

class ui(QMainWindow):
	def __init__( self, x, y ):
		super( ).__init__( )
		self.setupUi( x, y )

	def setupUi( self, x, y ):
		self.setObjectName("MainWindow")
		self.setFixedSize(x, y)#805, 573
		
		self.centralwidget = QtWidgets.QWidget(self)
		self.centralwidget.setObjectName("centralwidget")
		self.eventGroupBox = QtWidgets.QGroupBox(self.centralwidget)
		self.eventGroupBox.setGeometry(QtCore.QRect(10, 210, 351, 321))
		font = QtGui.QFont()
		font.setPointSize(11)
		self.eventGroupBox.setFont(font)
		self.eventGroupBox.setObjectName("eventGroupBox")
		self.hourComboBox = QtWidgets.QComboBox(self.eventGroupBox)
		self.hourComboBox.setGeometry(QtCore.QRect(100, 40, 51, 22))
		self.hourComboBox.setObjectName("hourComboBox")
		self.hourComboBox.addItem("")
		self.hourComboBox.addItem("")
		self.hourComboBox.addItem("")
		self.hourComboBox.addItem("")
		self.hourComboBox.addItem("")
		self.hourComboBox.addItem("")
		self.hourComboBox.addItem("")
		self.hourComboBox.addItem("")
		self.hourComboBox.addItem("")
		self.hourComboBox.addItem("")
		self.hourComboBox.addItem("")
		self.hourComboBox.addItem("")
		self.hourComboBox.addItem("")
		self.hourComboBox.addItem("")
		self.hourComboBox.addItem("")
		self.hourComboBox.addItem("")
		self.hourComboBox.addItem("")
		self.hourComboBox.addItem("")
		self.hourComboBox.addItem("")
		self.hourComboBox.addItem("")
		self.hourComboBox.addItem("")
		self.hourComboBox.addItem("")
		self.hourComboBox.addItem("")
		self.hourComboBox.addItem("")
		self.dateLabel = QtWidgets.QLabel(self.eventGroupBox)
		self.dateLabel.setGeometry(QtCore.QRect(10, 110, 141, 21))
		font = QtGui.QFont()
		font.setPointSize(11)
		self.dateLabel.setFont(font)
		self.dateLabel.setObjectName("dateLabel")
		self.addEventButton = QtWidgets.QPushButton(self.eventGroupBox)
		self.addEventButton.setGeometry(QtCore.QRect(280, 40, 51, 23))
		self.addEventButton.setObjectName("addEventButton")
		self.removeEventButton = QtWidgets.QPushButton(self.eventGroupBox)
		self.removeEventButton.setGeometry(QtCore.QRect(270, 100, 61, 31))
		self.removeEventButton.setObjectName("removeEventButton")
		self.selectHourLabel = QtWidgets.QLabel(self.eventGroupBox)
		self.selectHourLabel.setGeometry(QtCore.QRect(10, 40, 81, 21))
		font = QtGui.QFont()
		font.setPointSize(11)
		self.selectHourLabel.setFont(font)
		self.selectHourLabel.setObjectName("selectHourLabel")
		self.eventTableWidget = QtWidgets.QTableWidget(self.eventGroupBox)
		self.eventTableWidget.setGeometry(QtCore.QRect(10, 140, 321, 161))
		self.eventTableWidget.setObjectName("eventTableWidget")
		self.eventTableWidget.setColumnCount(2)
		self.eventTableWidget.setRowCount(0)
		self.lineEdit = QtWidgets.QLineEdit(self.eventGroupBox)
		self.lineEdit.setGeometry(QtCore.QRect(10, 70, 321, 21))
		self.lineEdit.setObjectName("lineEdit")
		self.minuteSpinBox = QtWidgets.QSpinBox(self.eventGroupBox)
		self.minuteSpinBox.setGeometry(QtCore.QRect(160, 40, 42, 22))
		self.minuteSpinBox.setMinimum(0)
		self.minuteSpinBox.setMaximum(59)
		self.minuteSpinBox.setProperty("value", 0)
		self.minuteSpinBox.setObjectName("minuteSpinBox")
		self.calendarWidget = QtWidgets.QCalendarWidget(self.centralwidget)
		self.calendarWidget.setGeometry(QtCore.QRect(10, 10, 351, 191))
		font = QtGui.QFont()
		font.setPointSize(10)
		self.calendarWidget.setFont(font)
		self.calendarWidget.setFirstDayOfWeek(QtCore.Qt.Monday)
		self.calendarWidget.setGridVisible(False)
		self.calendarWidget.setHorizontalHeaderFormat(QtWidgets.QCalendarWidget.ShortDayNames)
		self.calendarWidget.setVerticalHeaderFormat(QtWidgets.QCalendarWidget.NoVerticalHeader)
		self.calendarWidget.setNavigationBarVisible(True)
		self.calendarWidget.setDateEditEnabled(True)
		self.calendarWidget.setObjectName("calendarWidget")
		font = QtGui.QFont()
		font.setPointSize( 10 )
		self.calendarWidget.setFont(font)
		self.fontGroupBox = QtWidgets.QGroupBox(self.centralwidget)
		self.fontGroupBox.setGeometry(QtCore.QRect(370, 10, 221, 111))
		self.fontGroupBox.setObjectName("fontGroupBox")
		self.fontComboBox = QtWidgets.QFontComboBox(self.fontGroupBox)
		self.fontComboBox.setGeometry(QtCore.QRect(10, 31, 201, 21))
		font = QtGui.QFont()
		font.setFamily("Times New Roman")
		font.setPointSize(11)
		self.fontComboBox.setFont(font)
		font = QtGui.QFont()
		font.setFamily("Liberation Serif")
		font.setPointSize(11)
		self.fontComboBox.setCurrentFont(font)
		self.fontComboBox.setObjectName("fontComboBox")
		self.fontComboBox.addItem( "" )
		self.fontSizeSpinBox = QtWidgets.QSpinBox(self.fontGroupBox)
		self.fontSizeSpinBox.setGeometry(QtCore.QRect(170, 60, 42, 22))
		self.fontSizeSpinBox.setMinimum(10)
		self.fontSizeSpinBox.setMaximum(50)
		self.fontSizeSpinBox.setProperty("value", 11)
		self.fontSizeSpinBox.setObjectName("fontSizeSpinBox")
		self.colorChangeButton = QtWidgets.QPushButton(self.fontGroupBox)
		self.colorChangeButton.setGeometry(QtCore.QRect(70, 60, 91, 41))
		font = QtGui.QFont()
		font.setPointSize(10)
		self.colorChangeButton.setFont(font)
		self.colorChangeButton.setObjectName("colorChangeButton")
		self.boldCheckBox = QtWidgets.QCheckBox(self.fontGroupBox)
		self.boldCheckBox.setGeometry(QtCore.QRect(10, 60, 51, 23))
		self.boldCheckBox.setObjectName("boldCheckBox")
		self.italicCheckBox = QtWidgets.QCheckBox(self.fontGroupBox)
		self.italicCheckBox.setGeometry(QtCore.QRect(10, 80, 61, 23))
		self.italicCheckBox.setObjectName("italicCheckBox")
		self.brightnessGroupBox = QtWidgets.QGroupBox(self.centralwidget)
		self.brightnessGroupBox.setGeometry(QtCore.QRect(370, 130, 221, 71))
		self.brightnessGroupBox.setObjectName("brightnessGroupBox")
		self.brightnessSlider = QtWidgets.QSlider(self.brightnessGroupBox)
		self.brightnessSlider.setGeometry(QtCore.QRect(10, 40, 201, 22))
		self.brightnessSlider.setMaximum(255)
		self.brightnessSlider.setSingleStep(2)
		self.brightnessSlider.setOrientation(QtCore.Qt.Horizontal)
		self.brightnessSlider.setObjectName("brightnessSlider")
		self.newsGroupBox = QtWidgets.QGroupBox(self.centralwidget)
		self.newsGroupBox.setGeometry(QtCore.QRect(370, 210, 421, 321))
		self.newsGroupBox.setObjectName("newsGroupBox")
		self.editNewsButton = QtWidgets.QPushButton(self.newsGroupBox)
		self.editNewsButton.setGeometry(QtCore.QRect(10, 40, 101, 23))
		self.editNewsButton.setObjectName("editNewsButton")
		self.sourceListWidget = QtWidgets.QListWidget(self.newsGroupBox)
		self.sourceListWidget.setGeometry(QtCore.QRect(10, 70, 191, 211))
		self.sourceListWidget.setObjectName("sourceListWidget")
		item = QtWidgets.QListWidgetItem()
		self.sourceListWidget.addItem(item)
		item = QtWidgets.QListWidgetItem()
		self.sourceListWidget.addItem(item)
		self.newsListWidget = QtWidgets.QListWidget(self.newsGroupBox)
		self.newsListWidget.setGeometry(QtCore.QRect(210, 70, 201, 211))
		self.newsListWidget.setObjectName("newsListWidget")
		self.newsLabel = QtWidgets.QLabel(self.newsGroupBox)
		self.newsLabel.setGeometry(QtCore.QRect(10, 290, 191, 17))
		font = QtGui.QFont()
		font.setPointSize(10)
		self.newsLabel.setFont(font)
		self.newsLabel.setObjectName("newsLabel")
		self.label = QtWidgets.QLabel(self.newsGroupBox)
		self.label.setGeometry(QtCore.QRect(210, 40, 91, 17))
		self.label.setObjectName("label")
		self.countryLabel = QtWidgets.QLabel(self.newsGroupBox)
		self.countryLabel.setGeometry(QtCore.QRect(300, 40, 111, 17))
		self.countryLabel.setObjectName("countryLabel")
		self.pingLabel = QtWidgets.QLabel( self )
		self.pingLabel.setGeometry( QtCore.QRect( 15, 555, 300, 17 ))
		self.pingLabel.setObjectName("pingLabel")
		self.pingLabel.setStyleSheet( "color:red" )
		self.readNewsButton = QtWidgets.QPushButton( self.newsGroupBox )
		self.readNewsButton.setGeometry( QtCore.QRect(320, 290, 89, 25))
		self.readNewsButton.setObjectName( "readnewsButton" )
		self.weatherGroupBox = QtWidgets.QGroupBox(self.centralwidget)
		self.weatherGroupBox.setGeometry(QtCore.QRect(600, 10, 191, 191))
		self.weatherGroupBox.setObjectName("weatherGroupBox")
		self.weatherLabel = QtWidgets.QLabel(self.weatherGroupBox)
		self.weatherLabel.setGeometry(QtCore.QRect(10, 170, 171, 17))
		font = QtGui.QFont()
		font.setPointSize(9)
		self.weatherLabel.setFont(font)
		self.weatherLabel.setObjectName("weatherLabel")
		self.setCentralWidget(self.centralwidget)
		self.menubar = QtWidgets.QMenuBar(self)
		self.menubar.setGeometry(QtCore.QRect(0, 0, 805, 22))
		self.menubar.setObjectName("menubar")
		self.setMenuBar(self.menubar)
		self.statusbar = QtWidgets.QStatusBar(self)
		self.statusbar.setObjectName("statusbar")
		self.setStatusBar(self.statusbar)

		self.label_2 = QtWidgets.QLabel( self.weatherGroupBox )
		self.label_2.setGeometry( QtCore.QRect( 10, 30, 67, 17 ))
		self.label_2.setObjectName( "label_2" )

		self.cityLineEdit = QtWidgets.QLineEdit( self.weatherGroupBox )
		self.cityLineEdit.setGeometry( QtCore.QRect( 10, 50, 171, 25 ))
		self.cityLineEdit.setObjectName( "cityLineEdit" )

		self.celsiusRadioButton = QtWidgets.QRadioButton( self.weatherGroupBox )
		self.celsiusRadioButton.setGeometry( QtCore.QRect( 10, 80, 112, 23 ))
		self.celsiusRadioButton.setObjectName( "celsiusRadioButton" )

		self.fahrenheitRadioButton = QtWidgets.QRadioButton( self.weatherGroupBox )
		self.fahrenheitRadioButton.setGeometry( QtCore.QRect( 10, 100, 112, 23 ))
		self.fahrenheitRadioButton.setObjectName( "fahrenheitRadioButton" )

		self.submitButton = QtWidgets.QPushButton( self.weatherGroupBox )
		self.submitButton.setGeometry( QtCore.QRect( 10, 130, 89, 25 ))
		self.submitButton.setObjectName( "submitButton" )

		self.celsiusRadioButton.setChecked( True )

		self.eventTableWidget.setHorizontalHeaderLabels(["Time", "Event"])
		#self.eventTableWidget.setHorizontalScrollMode( QtWidgets.QAbstractItemView.ScrollPerPixel )
		self.eventTableWidget.setWordWrap( True )

		self.eventTableWidget.horizontalHeader( ).setSectionResizeMode( 0, QtWidgets.QHeaderView.ResizeToContents )
		self.eventTableWidget.horizontalHeader( ).setSectionResizeMode( 1, QtWidgets.QHeaderView.Stretch )

		self.eventTableWidget.setSelectionBehavior( 1 )
		self.eventTableWidget.setSelectionMode( 4 )
		self.eventTableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)


		self.menubar = QtWidgets.QMenuBar(self)
		self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
		self.menubar.setObjectName("menubar")
		self.menuView = QtWidgets.QMenu(self.menubar)
		self.menuView.setObjectName("menuView")
		self.menuScroll_Speed = QtWidgets.QMenu(self.menubar)
		self.menuScroll_Speed.setObjectName("menuScroll_Speed")
		self.menuConfig = QtWidgets.QMenu(self.menubar)
		self.menuConfig.setObjectName("menuConfig")
		self.setMenuBar(self.menubar)
		self.statusbar = QtWidgets.QStatusBar(self)
		self.statusbar.setObjectName("statusbar")
		self.setStatusBar(self.statusbar)
		self.speedAction = []
		for i in range( 7 ):
			self.speedAction.append( QtWidgets.QAction( self ))
			self.speedAction[i].setObjectName("speedAction")
			self.menuScroll_Speed.addAction(self.speedAction[i])
		self.viewAction = []
		for i in range( 6 ):
			self.viewAction.append( QtWidgets.QAction( self ))
			self.viewAction[i].setObjectName("viewAction")
			self.menuView.addAction(self.viewAction[i])

		self.sleepTimerAction = QtWidgets.QAction( self )
		self.sleepTimerAction.setObjectName("sleepTimerAction")
		self.menuConfig.addAction(self.sleepTimerAction)

		self.menubar.addAction(self.menuView.menuAction())
		self.menubar.addAction(self.menuScroll_Speed.menuAction())
		self.menubar.addAction(self.menuConfig.menuAction())


		self.retranslateUi(self)
		QtCore.QMetaObject.connectSlotsByName(self)

	def retranslateUi(self, MainWindow):
		_translate = QtCore.QCoreApplication.translate
		MainWindow.setWindowTitle(_translate("MainWindow", "Smart Mirror"))
		self.eventGroupBox.setTitle(_translate("MainWindow", "Events"))
		self.hourComboBox.setItemText(0, _translate("MainWindow", "00"))
		self.hourComboBox.setItemText(1, _translate("MainWindow", "01"))
		self.hourComboBox.setItemText(2, _translate("MainWindow", "02"))
		self.hourComboBox.setItemText(3, _translate("MainWindow", "03"))
		self.hourComboBox.setItemText(4, _translate("MainWindow", "04"))
		self.hourComboBox.setItemText(5, _translate("MainWindow", "05"))
		self.hourComboBox.setItemText(6, _translate("MainWindow", "06"))
		self.hourComboBox.setItemText(7, _translate("MainWindow", "07"))
		self.hourComboBox.setItemText(8, _translate("MainWindow", "08"))
		self.hourComboBox.setItemText(9, _translate("MainWindow", "09"))
		self.hourComboBox.setItemText(10, _translate("MainWindow", "10"))
		self.hourComboBox.setItemText(11, _translate("MainWindow", "11"))
		self.hourComboBox.setItemText(12, _translate("MainWindow", "12"))
		self.hourComboBox.setItemText(13, _translate("MainWindow", "13"))
		self.hourComboBox.setItemText(14, _translate("MainWindow", "14"))
		self.hourComboBox.setItemText(15, _translate("MainWindow", "15"))
		self.hourComboBox.setItemText(16, _translate("MainWindow", "16"))
		self.hourComboBox.setItemText(17, _translate("MainWindow", "17"))
		self.hourComboBox.setItemText(18, _translate("MainWindow", "18"))
		self.hourComboBox.setItemText(19, _translate("MainWindow", "19"))
		self.hourComboBox.setItemText(20, _translate("MainWindow", "20"))
		self.hourComboBox.setItemText(21, _translate("MainWindow", "21"))
		self.hourComboBox.setItemText(22, _translate("MainWindow", "22"))
		self.hourComboBox.setItemText(23, _translate("MainWindow", "23"))
		self.dateLabel.setText(_translate("MainWindow", "13. Feb 2020 (Thu)"))
		self.addEventButton.setText(_translate("MainWindow", "Add"))
		self.removeEventButton.setText(_translate("MainWindow", "Remove"))
		self.selectHourLabel.setText(_translate("MainWindow", "Select time:"))
		self.fontGroupBox.setTitle(_translate("MainWindow", "Font && Color"))
		self.colorChangeButton.setText(_translate("MainWindow", "Change Color"))
		self.boldCheckBox.setText(_translate("MainWindow", "Bold"))
		self.italicCheckBox.setText(_translate("MainWindow", "Italic"))
		self.brightnessGroupBox.setTitle(_translate("MainWindow", "Brightness"))
		self.newsGroupBox.setTitle(_translate("MainWindow", "News"))
		self.editNewsButton.setText(_translate("MainWindow", "Edit News"))
		self.readNewsButton.setText( _translate( "MainWindow", "Read News" ))
		__sortingEnabled = self.sourceListWidget.isSortingEnabled()
		self.sourceListWidget.setSortingEnabled(False)
		item = self.sourceListWidget.item(0)
		item.setText(_translate("MainWindow", "Cnn"))
		item = self.sourceListWidget.item(1)
		item.setText(_translate("MainWindow", "New York Times"))
		self.sourceListWidget.setSortingEnabled(__sortingEnabled)
		self.newsLabel.setText(_translate("MainWindow", "<a href=\"https://newsapi.org//\">Powered by: News API</a>"))
		self.newsLabel.setOpenExternalLinks( True )
		self.label.setText(_translate("MainWindow", "News From:"))
		self.countryLabel.setText(_translate("MainWindow", "Serbia"))
		self.pingLabel.setText(_translate("MainWindow", "No Connection with Smart Mirror!"))
		self.weatherGroupBox.setTitle(_translate("MainWindow", "Weather"))
		self.weatherLabel.setText(_translate("MainWindow", "<html><head/><body><p><a href=\"https://www.accuweather.com/\"><span style=\" text-decoration: underline; color:#0000ff;\">Powered by: AccuWeather</span></a></p></body></html>"))
		self.weatherLabel.setOpenExternalLinks( True )

		self.label_2.setText( _translate( "MainWindow", "City:" ))
		self.celsiusRadioButton.setText( _translate( "MainWindow", "Celsius" ))
		self.fahrenheitRadioButton.setText( _translate( "MainWindow", "Fahrenheit" ))
		self.submitButton.setText( _translate( "MainWindow", "Submit" ))

		self.menuView.setTitle(_translate("MainWindow", "View"))
		self.menuScroll_Speed.setTitle(_translate("MainWindow", "Scroll Speed"))
		self.menuConfig.setTitle(_translate("MainWindow", "Configuration"))
		
		self.speedAction[0].setText(_translate("MainWindow", "1s"))
		self.speedAction[1].setText(_translate("MainWindow", "2s"))
		self.speedAction[2].setText(_translate("MainWindow", "3s"))
		self.speedAction[3].setText(_translate("MainWindow", "5s"))
		self.speedAction[4].setText(_translate("MainWindow", "10s"))
		self.speedAction[5].setText(_translate("MainWindow", "20s"))
		self.speedAction[6].setText(_translate("MainWindow", "None"))

		self.viewAction[0].setText(_translate("MainWindow", "Default"))
		self.viewAction[1].setText(_translate("MainWindow", "Default+"))
		self.viewAction[2].setText(_translate("MainWindow", "Calendar+Events"))
		self.viewAction[3].setText(_translate("MainWindow", "Calendar+Weather"))
		self.viewAction[4].setText(_translate("MainWindow", "Calendar+Weather+Events"))
		self.viewAction[5].setText(_translate("MainWindow", "Calendar+Weather+Events+"))

		self.sleepTimerAction.setText(_translate("MainWindow", "Set Sleep Time"))