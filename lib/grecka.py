#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Conversion is based on ELOT 743

import re
import sys
from collections import OrderedDict

if sys.version_info < ( 3 , 0 ):
    sys.exit("This script requires Python 3 and above.")

class Grecka:
    @staticmethod
    def writeFile(filename,greeklish_text):
        myfile = open(filename,'w')
        myfile.write(greeklish_text)
        myfile.close()

    @staticmethod
    def toGreeklish(text,writeflag=False,outputname='myout.txt'):

        GR = list("αάβγδεέζηήιίϊκλμνξοόπρσςτυύϋφωώ")
        EN = list("aavgdeeziiiiiklmnxooprsstyyyfoo")

        translation_dictionary = dict()

        for i in range (len(GR)):
                translation_dictionary[GR[i]] = EN[i]

        syllables = [
                     ['αυ(?=[θκξπστφχψ])','af'],['ευ(?=[θκξπστφχψ|\s|$])','ef'],
                     ['ηυ(?=[θκξπστφχψ|\s|$])','if'],['(?=^|\s|$)μπ','b'],['μπ(?=^|\s)','b'],
                     ['αι','ai'],['οι','oi'],['ου','ou'],['ει','ei'],['ντ','nt'],['τσ','ts'],
                     ['τζ','tz'],['γγ','ng'],['γκ','gk'],['θ','th'],['χ','ch'],['ψ','ps'],
                     ['αυ','av'],['ευ','ev'],['ηυ','if'],['μπ','mp']
                    ]

        for i in range(len(syllables)):
            text = re.sub(syllables[i][0],syllables[i][1],text)

        for key in translation_dictionary:
            text = re.sub(key,translation_dictionary[key],text)

        if writeflag == False:
            print (text)
        else:
            Grecka.writeFile(outputname,text)
