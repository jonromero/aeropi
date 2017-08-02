import picamera
from time import sleep
from datetime import datetime
import ftplib

with picamera.PiCamera() as camera:
	camera.resolution = (1280, 720)
	camera.framerate = 24
	filename = '/home/pi/aero/photos/'+str(datetime.now()).replace(' ', '_')+'.png'
	camera.vflip = True
	camera.capture(filename)
    	
	sleep(5)
	camera.annotate_background = picamera.Color('black')
    	camera.annotate_text = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
	camera.capture('/home/pi/aero/photos/latest.png')
	
	print filename

session = ftplib.FTP('ftp.mygeektragedy.com','mygeek@beyourstar.gr','1q2w3e4rgeeky')
file = open(filename,'rb')                  # file to send
file2 = open('/home/pi/aero/photos/latest.png', 'rb')
session.storbinary('STOR '+filename.replace('/home/pi/aero/photos/','') , file)     # send the file
session.storbinary('STOR latest.png', file2)
file.close()                                    # close file and FTP
file2.close()
session.quit()

print "Done", filename
