import board
import neopixel
import usb_cdc

pixels = neopixel.NeoPixel(board.NEOPIXEL, 4, brightness=1.0)
serial = usb_cdc.data

r, g, b = (0, 0, 0)

while True:
    fields = str(serial.readline().strip(), 'ascii').split(' ')
    if fields[0] == '*IDN?':
        serial.write(b'NeoTrinkeyStatus\r\n')
    elif fields[0] == 'RGB?':
        serial.write(bytes(f'{r},{g},{b}', 'ascii') + '\r\n')
    elif fields[0]:
        try:
            r, g, b = fields[1].split(',')
            pixels.fill((int(r), int(g), int(b)))
        except Exception as e:
            print(e)
    else:
        serial.write(b'Unknown command: ' + fields[0] + '\r\n')
