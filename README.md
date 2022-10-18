# mkpilfont

this is a utility for converting old microsoft windows bitmap fonts into bitmap fonts that can be used with [Pillow](https://python-pillow.org/)

this is done using another tool as a dependency, [mkwinfont](https://github.com/juanitogan/mkwinfont), so be sure to place its two python files in the same directory as this python file

(NOTE: currently, as of 2022-10-19, i have a [pull request](https://github.com/juanitogan/mkwinfont/pull/2) open for that project, without which it cannot be used as a dependency; so if it wasn't approved yet when you find this, you'll have to use my fork)

the only other dependency is [Pillow](https://python-pillow.org/) itself, which, way back when i wrote this tool, for whatever reason (now lost to the shifting sands of time), i chose to use version 5.1.0 of

example usage:

```
./dewinfont.py -p DIALOGH DIALOGH.FON # first deconstruct the .FON file into FD files

./mkpilfont.py DIALOGH05.fd # make the 1x version
./mkpilfont.py -s 2 DIALOGH05.fd # make the 2x version
./mkpilfont.py -s 3 DIALOGH05.fd # make the 3x version
./mkpilfont.py -s 4 DIALOGH05.fd # make the 4x version
```
