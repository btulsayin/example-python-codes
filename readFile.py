#!/usr/bin/env python2
# -*- coding: utf-8 -*-
# Finding the repeat number of words in a txt file
from collections import Counter
def main():
    #use open() for opening file.
    #Always use `with` statement as it'll automatically close the file for you.
    with open(r'/home/hp/Documents/image_test.txt') as f:
        #create a list of all words fetched from the file using a list comprehension
        words = [word for line in f for word in line.split(".jpg")]
        print "Toplam kelime sayısı:", len(words)
        #now use collections.Counter
        c = Counter(words)
        for word, count in c.most_common():
           print word," =TekrarSayısı-->", count  
main()




 