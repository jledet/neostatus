import argparse
import time
from datetime import datetime

from . import NeoStatus


def wait_until_sec():

    t = datetime.now()
    sleeptime = 1 - (t.microsecond/1000000.0)
    time.sleep(sleeptime)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('command', default='rainbow', choices=('reset', 'drive', 'safemode', 'set', 'rainbow', 'fade'),
                        help="Helper command")
    parser.add_argument('-r', '--red', type=int, choices=range(0, 256), required=False,
                        help="Red component of RGB set", metavar='')
    parser.add_argument('-g', '--green', type=int, choices=range(0, 256), required=False,
                        help="Green component of RGB set", metavar='')
    parser.add_argument('-b', '--blue', type=int, choices=range(0, 256), required=False,
                        help="Blue component of RGB set", metavar='')
    parser.add_argument('-v', '--verbose', action='store_true', help="Print current color")
    parser.add_argument('--delay', type=float, required=False, default=0,
                        help="Time in seconds between updates (rainbow and fade)", metavar='')
    parser.add_argument('--sync', action='store_true', help="Wait until next second before starting")

    args = parser.parse_args()

    status = NeoStatus()

    match args.command:
        case 'reset':
            status.reset()
        case 'drive':
            status.drive()
        case 'safemode':
            status.safemode()
        case 'set':
            if args.red is None or args.green is None or args.blue is None:
                print("-r, -g and -b must be specified when setting a color")
                exit(1)

            if args.sync:
                wait_until_sec()

            status.set_color((args.red, args.green, args.blue))
        case 'rainbow':
            r, g, b = 255, 0, 0

            if args.sync:
                wait_until_sec()

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

                if args.verbose:
                    print(f'\r\x1b[30m\x1b[48;2;{r};{g};{b}m{r:3} {g:3} {b:3}\x1b[0m', end='')

                status.set_color((r, g, b))
                time.sleep(args.delay)
        case 'fade':
            if args.red is None or args.green is None or args.blue is None:
                print("Initial -r, -g and -b must be specified when fading a color")
                exit(1)
            toggle = True
            r, g, b = args.red, args.green, args.blue
            max_red, max_green, max_blue = r, g, b

            if args.sync:
                wait_until_sec()

            while True:
                if toggle:
                    if r > 0:
                        r -= 1
                    if g > 0:
                        g -= 1
                    if b > 0:
                        b -= 1
                    if r == 0 and g == 0 and b == 0:
                        toggle = not toggle
                else:
                    if r < max_red:
                        r += 1
                    if g < max_green:
                        g += 1
                    if b < max_blue:
                        b += 1
                    if r == max_red and g == max_green and b == max_blue:
                        toggle = not toggle

                if args.verbose:
                    print(f'\r\x1b[30m\x1b[48;2;{r};{g};{b}m{r:3} {g:3} {b:3}\x1b[0m', end='')

                status.set_color((r, g, b))
                time.sleep(args.delay)


try:
    main()
except KeyboardInterrupt:
    print()
