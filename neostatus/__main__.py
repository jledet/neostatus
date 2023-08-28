import argparse

from . import NeoStatus


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('command', default='demo', choices=('reset', 'drive', 'safemode', 'rainbow'), help="Helper command")
    args = parser.parse_args()

    status = NeoStatus()

    match args.command:
        case 'reset':
            status.reset()
        case 'drive':
            status.drive()
        case 'safemode':
            status.safemode()
        case 'rainbow':
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


try:
    main()
except KeyboardInterrupt:
    print()
