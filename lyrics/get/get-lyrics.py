#!/usr/bin/env python
import urllib2

def getCorpus(url):
    f = urllib2.urlopen(url)
    data = f.read()
    return data


url='http://www.gutenberg.org/cache/epub/100/pg100.txt'
getCorpus(url)
