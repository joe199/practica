import RPi.GPIO as GPIO
import time, sys


FLOW_SENSOR = 23
print FLOW_SENSOR
GPIO.setmode(GPIO.BCM)
GPIO.setup(FLOW_SENSOR, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
print 'arribo'
global count
count = 0

def countPulse(channel):
   global count
   count = count+1
   litres =float(count/4380.0)
   litres_decimal = '%.3f' % litres
   print litres_decimal
   print (litres_decimal > 1)	
   if (float(litres_decimal) < 0.1):
       print 'holaaa'
       print "Has begut:  %s litres, fas una mica de pena"  % (litres_decimal)
   else:
     print 'Has begut: %s litres, segueixes fent pena ' % (litres_decimal)

GPIO.add_event_detect(FLOW_SENSOR, GPIO.RISING, callback=countPulse)


while True:
    try:
        time.sleep(1)
    except KeyboardInterrupt:
        print '\ncaught keyboard interrupt!, bye'
        GPIO.cleanup()
        sys.exit()
