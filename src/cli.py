import argparse

from generator import generate

parser = argparse.ArgumentParser()
parser.add_argument('--width', type=int, default=1440)
parser.add_argument('--height', type=int, default=2560)
parser.add_argument('--gapsize', type=int, default=5)
parser.add_argument('--wallsize', type=int, default=3)
parser.add_argument('--border', type=int, default=20)
parser.add_argument('--outfile', type=str, default='out.png')

if __name__ == '__main__':
    args = parser.parse_args()
    im = generate(args.width, args.height, args.wallsize, args.gapsize, args.border)
    im.save(args.outfile)
