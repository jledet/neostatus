#!/usr/bin/env python

import glob
import pyvisa


class StatusLight(object):
    def __init__(self):
        rm = pyvisa.ResourceManager()
        dev = glob.glob('/dev/serial/by-id/usb-Adafruit_Industries_LLC_NeoPixel_Trinkey_M0_*-if02')[0]
        self.inst = rm.open_resource(f'ASRL{dev}::INSTR')

    def set_color(self, color):
        r, g, b = color
        self.inst.write(f'RGB {r},{g},{b}')

def main():
    status = StatusLight()
    r, g, b = 255, 0, 0
    while True:
        if r > 0 and b == 0:
            r -= 1
            g += 1
        if g > 0 and r == 0:
            g -= 1
            b += 1
        if b > 0 and g == 0:
            b -= 1
            r += 1
        print(f'\r\x1b[30m\x1b[48;2;{r};{g};{b}m{r:3} {g:3} {b:3}\x1b[0m', end='')
        status.set_color((r, g, b))


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print()