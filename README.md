# mkpilfont

this is a utility for converting old microsoft windows bitmap fonts into bitmap fonts that can be used with [Pillow](https://python-pillow.org/)

this is done using another tool as a dependency, [mkwinfont](https://github.com/juanitogan/mkwinfont), so be sure to place its two python files in the same directory as this python file

the only other dependency is [Pillow](https://python-pillow.org/) itself, which, way back when i wrote this tool, for whatever reason (now lost to the shifting sands of time), i chose to use version 5.1.0 of

example usage:

```
./dewinfont.py -p DIALOGH DIALOGH.FON # first deconstruct the .FON file into FD files

./mkpilfont.py DIALOGH05.fd # make the 1x version
./mkpilfont.py -s 2 DIALOGH05.fd # make the 2x version
./mkpilfont.py -s 3 DIALOGH05.fd # make the 3x version
./mkpilfont.py -s 4 DIALOGH05.fd # make the 4x version
```
