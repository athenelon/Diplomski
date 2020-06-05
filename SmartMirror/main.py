import sys
sys.path.append( "/home/pi/SmartMirror/" )

from source.app.app import app
from datetime import datetime

print( datetime.now( ).strftime( "%H:%M:%S" ), "Starting Mirror...\n\n\n" )
a = app( )
a.runMirror( )

"""
todo:
static ip for rpi
"""
