#!/usr/bin/env python2
# -*- coding: utf-8 -*-
### The python code that reads the files in a folder 
####and writes them to the file names in the txt file
import os
import simplejson
path ="/data/faces/filmweb/"
dirlist = os.listdir(path)
dosya = open('/Documents/filmweb_New.txt','w')
simplejson.dump(dirlist, dosya)
dosya.close()
