#!/usr/bin/env python

import os


class NeoStatus(object):
    def __init__(self, path=None):
        if path is None:
            for dev in os.listdir('/dev/serial/by-id/'):
                if dev.startswith('usb-Adafruit_Industries_LLC_NeoPixel_Trinkey_M0') and \
                        dev.endswith('if02'):
                    path = '/dev/serial/by-id/' + dev
                    break
        if path is None:
            raise FileNotFoundError('Could not find any NeoPixel Trinkey')
        self.dev = open(path, 'wb')

    def set_color(self, color):
        r, g, b = color
        self.dev.write(f'RGB {r},{g},{b}\r\n'.encode('ascii'))
        self.dev.flush()
