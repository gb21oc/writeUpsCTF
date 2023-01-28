#!/usr/bin/python3
import zlib

str_object1 = open('./_cutie.png.extracted/365.zlib', 'rb').read()
str_object2 = zlib.decompress(str_object1)
f = open('extract', 'wb')
f.write(str_object2)
f.close()
