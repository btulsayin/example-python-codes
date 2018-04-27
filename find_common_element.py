#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import json

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

file1 = open('/Documents/file1.txt', 'r')
file2 = open('/Documents/file2.txt', 'r')
file3 = open('/Documents/file3.txt', 'r')
file4 = open('/Documents/file4.txt', 'r')

f1 = json.load(file1)
f2 = json.load(file2)
f3 = json.loads(file3.read().replace('\r\n', '\\r\\n'), strict=False)
f4 = json.load(file4)

f1_keys = [line.lower() for line in f1.keys()]
f2_keys = [line.lower() for line in f2.keys()]
f3_keys = [line.lower() for line in f3.keys()]
f4_keys = [line.lower() for line in f4.keys()]
#key'lerini al 

same = { "data": list(set(set(set(f1_keys).intersection(f2_keys)).intersection(f3_keys)).intersection(f4_keys))}
        #intersection=file1 ve file2 nin kesişimini alır.

file_out = open('/Documents/ortak.txt', 'w')
file_out.write(json.dumps(same, sort_keys=True, indent=2))