import time
import RPi.GPIO as GPIO
import signal
from readnfc import read_nfc

class FlowControl(object):
    """Controlling FlowControl"""
    def __init__(self):
        super(FlowControl, self).__init__()
        self.previousTime = 0
        self.service = 0
        self.total = 0
        self.nfc = read_nfc()


    def update(self, channel):
        tim = time.time()
        delta = tim - self.previousTime
        if delta < 500:
            self.hertz = 1000.0 / delta
            self.flow = self.hertz / 4380.0  # Liter/Second
            service = self.flow * (delta / 1000.0)
            self.service  += service
            self.total    += service
        else:
            # Guardar a usuari self.service
            self.service = 0
            self.user = self._get_user()

        self.previousTime = tim

    def _get_user(self):
        uid = self.nfc.read()
        return uid



if __name__ == "__main__":
    
    fl = FlowControl()
	GPIO.setmode(GPIO.BCM) # use real GPIO numbering
	GPIO.setup(23,GPIO.IN, pull_up_down=GPIO.PUD_UP)
	GPIO.add_event_detect(23, GPIO.RISING, callback=fl.update, bouncetime=20)

    try:
        while True:
            time.sleep(1)
    except:
        pass
    finally:
        GPIO.cleanup()
