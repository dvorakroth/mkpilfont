#!/usr/bin/env python3

# mkpilfont -- turning mkwinfont's FD files into a PILfont for use with Pillow

# I, Amit Ron, the original author, hereby release this server's code into the
# public domain; additionally, you may also use it for personal, or religious,
# commercial, or noncommercial use under the terms of the WTFPLv2.

# This code WILL fail. It's not a question of if, but a question of when.
# No warranty, no guarantees, everything provided as-is. If anything happens to
# you because of this code, I won't be held responsible, because now you know lol

# (right?)

from mkwinfont import loadfont as loadfd
from PIL import Image
from struct import pack

import sys
import os.path
import logging

import argparse

MAX_WIDTH = 800

def main(argv):
    logging.basicConfig(level=logging.INFO)

    parser = argparse.ArgumentParser(description='Turn an mkwinfont FD file into a PILfont')
    parser.add_argument('filenames', metavar='FILENAME', type=str, nargs='+',
                        help='file to process')
    parser.add_argument('--scale', '-s', dest='scale', type=int,
                        default=1,
                        help='scale the font up (default: 1)')
    
    args = parser.parse_args()

    for fname in args.filenames:

        convertfont(fname, args.scale)

def convertfont(fd_filename, scale=1):
    if scale != int(scale) or scale < 1:
        logging.error(f"ignoring invalid scale {scale}")
        scale = 1
    
    base_filename = os.path.splitext(fd_filename)[0] + ("" if scale == 1 else f"_{scale}x")
    pil_filename = base_filename + '.pil'
    png_filename = base_filename + '.png'

    font = loadfd(fd_filename)
    logging.info('font definition loaded')

    pixelheight = font.height

    sheetwidth = 0
    sheetheight = pixelheight

    rowwidth = 0

    # calculate size of the image
    for idx, char in enumerate(font.chars):
        if char is None:
            logging.info(f"{fd_filename}: character {idx} is missing")
        
        rowwidth += char.width * scale

        # too wide! make a new row
        if rowwidth > MAX_WIDTH:
            sheetheight += pixelheight
            rowwidth = char.width * scale
        
        # if, after checking for overflow, this is the widest row, then widen the image
        if rowwidth > sheetwidth:
            sheetwidth = rowwidth / scale
    
    logging.info(f"Creating image of size {MAX_WIDTH} x {sheetheight}")
    image = Image.new('1', (MAX_WIDTH, sheetheight), 0)

    with open(pil_filename, "wb") as pil_file:
        pil_file.write("PILfont\n;;;;;;20;\nDATA\n".encode('ascii'))
        logging.info(f"Wrote PILfont header to {pil_filename}")

        x = 0
        y = 0
        for idx, char in enumerate(font.chars):
            if char is None:
                pil_file.write(pack('>hhhhhhhhhh', *([0] * 10)))
                continue
            
            # too wide! make a new row
            if (x + char.width) * scale > MAX_WIDTH:
                y += pixelheight
                x = 0
            
            pil_file.write(pack(
                '>hhhhhhhhhh',
                char.width * scale, 0,
                0, (-font.ascent) * scale, char.width * scale, (pixelheight - font.ascent) * scale,
                x * scale, y * scale, (x + char.width) * scale, (y + pixelheight) * scale
            ))

            for sy in range(pixelheight):
                row = bin(char.data[sy])[2:].zfill(char.width)
                for sx in range(char.width):
                    image.putpixel((x + sx, y + sy), int(row[sx]))

            x += char.width
    
    if scale > 1:
        image = image.resize((image.width * scale, image.height * scale), Image.NEAREST)
        logging.info("resized image to scaled size")
        image = image.crop((0, 0, MAX_WIDTH, image.height))
        logging.info(f"cropped image to {MAX_WIDTH} x {image.height}")
    
    image.save(png_filename)
    logging.info(f"Wrote {png_filename}")


if __name__ == "__main__":
    main(sys.argv)
