#!/usr/bin/env python
import urllib2

def getCorpus(url):
    f = urllib2.urlopen(url)
    data = f.read()
    return data

def cleanCorpus(corpus,front_trim=0, end_trim=1):
    corpus=corpus[front_trim:-end_trim]
    print corpus
url='http://www.gutenberg.org/cache/epub/100/pg100.txt'
corpus=getCorpus(url)
cleanCorpus(corpus,7602)
