#!/usr/bin/env python
# -*- coding: utf8 -*-

import RPi.GPIO as GPIO
import spi
import signal
import time
import MFRC522

class read_nfc(object):

    signal.signal(signal.SIGINT, end_read)
    MIFAREReader = MFRC522.MFRC522()

    def read(self):

        # Scan for cards
        print 'Bucle read'
        (status,TagType) = MIFAREReader.MFRC522_Request(MIFAREReader.PICC_REQIDL)
        print 'Hola'
        # If a card is found
        if status == MIFAREReader.MI_OK:
            print "Card detected"

            # Get the UID of the card
            (status,uid) = MIFAREReader.MFRC522_Anticoll()
            print uid
            return uid
        return None
