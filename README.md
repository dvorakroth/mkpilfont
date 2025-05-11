# mkpilfont

this is a utility for converting old microsoft windows bitmap fonts into bitmap fonts that can be used with [Pillow](https://pypi.org/project/pillow/)

this is done using another tool as a dependency, [mkwinfont](https://github.com/juanitogan/mkwinfont), so be sure to place its two python files in the same directory as this python file

the only other dependency is [Pillow](https://pypi.org/project/pillow/) itself, which, way back when i wrote this tool, for whatever reason (now lost to the shifting sands of time), i chose to use version 5.1.0 of

example usage:

```
./dewinfont.py -p DIALOGH DIALOGH.FON # first deconstruct the .FON file into FD files

./mkpilfont.py DIALOGH05.fd # make the 1x version
./mkpilfont.py -s 2 DIALOGH05.fd # make the 2x version
./mkpilfont.py -s 3 DIALOGH05.fd # make the 3x version
./mkpilfont.py -s 4 DIALOGH05.fd # make the 4x version
```

## why this exists

i really like the default dialog font from the hebrew-enabled and hebrew-localized versions of windows 98 second edition, and i wanted to use them for my [busalon project](https://github.com/dvorakroth/busalon)

the problem is that Pillow, unsurprisingly enough, doesn't actually support loading microsoft's proprietary bitmap font file format! in fact, the only bitmap font format that Pillow **did** support was some weird combo of an image and some random ass binary format that they made up and **didn't actually document**. and the only tools Pillow offered for converting fonts into that format, can only use two ancient X Window System font formats, of course(??)

luckily, [mkwinfont](https://github.com/juanitogan/mkwinfont) exists, so i didn't have to figure out how to read microsoft's bitmap font format -- but to figure out Pillow's binary font files, i had no choice but to trudge through their old C code from the 90s to create this conversion utility
