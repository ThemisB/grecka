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
        with open(filename,'w') as myfile:
            myfile.write(greeklish_text)

    @staticmethod
    def toGreeklish(text,writeflag=False,outputname='myout.txt'):

        GR = list("ΑΆΒΓΔΕΈΖΗΉΙΊΪΚΛΜΝΞΟΌΠΡΣΤΥΎΫΦΩΏαάβγδεέζηήιίϊκλμνξοόπρσςτυύϋφωώ")
        EN = list("AAVGDEEZIIIIIKLMNXOOPRSTYYYFWWaavgdeeziiiiiklmnxooprsstyyyfww")

        translation_dictionary = dict()

        for i in range (len(GR)):
                translation_dictionary[GR[i]] = EN[i]

        syllables = [
                     ['αυ(?=[θκξπστφχψ])','af'],['ευ(?=[θκξπστφχψ|\s|$])','ef'],
                     ['ηυ(?=[θκξπστφχψ|\s|$])','if'],['(?=^|\s|$)μπ','b'],['μπ(?=^|\s)','b'],
                     ['αι','ai'],['οι','oi'],['ου','ou'],['ει','ei'],['ντ','nt'],['τσ','ts'],
                     ['τζ','tz'],['γγ','ng'],['γκ','gk'],['θ','th'],['χ','ch'],['ψ','ps'],
                     ['αυ','av'],['ευ','ev'],['ηυ','if'],['μπ','mp'],
                     ['Αυ(?=[θκξπστφχψ])','Af'],['Ευ(?=[θκξπστφχψ|\s|$])','Ef'],
                     ['Ηυ(?=[θκξπστφχψ|\s|$])','If'],['(?=^|\s|$)Μπ','B'],['Μπ(?=^|\s)','B'],
                     ['Αι','Ai'],['Οι','Oi'],['Ου','Ou'],['Ει','Ei'],['Ντ','Nt'],['Τς','Ts'],
                     ['Τζ','Tz'],['Γγ','Ng'],['Γκ','Gk'],['Θ(?=[α-ω])','Th'],['Χ(?=[α-ω])','Ch'],['Ψ(?=[α-ω])','Ps'],
                     ['Αυ','Av'],['Ευ','Ev'],['Ηυ','If'],['Μπ','Mp'],
                     ['ΑΥ(?=[ΘΚΞΠΣΤΦΧΨ])','AF'],['ΕΥ(?=[ΘΚΞΠΣΤΦΧΨ|\s|$])','EF'],
                     ['ΗΥ(?=[ΘΚΞΠΣΤΦΧΨ|\s|$])','IF'],['(?=^|\s|$)ΜΠ','B'],['ΜΠ(?=^|\s)','B'],
                     ['ΑΙ','AI'],['ΟΙ','OI'],['ΟΥ','OU'],['ΕΙ','EI'],['ΝΤ','NT'],['ΤΣ','TS'],
                     ['ΤΖ','TZ'],['ΓΓ','NG'],['ΓΚ','GK'],['Θ(?=[Α-Ω|\s|$])','TH'],['Χ(?=[Α-Ω|\s|$])','CH'],['Ψ(?=[Α-Ω|\s|$])','PS'],
                     ['ΑΥ','AV'],['ΕΥ','EV'],['ΗΥ','IF'],['ΜΠ','MP']
                    ]        
        
        for i in range(len(syllables)):
            text = re.sub(syllables[i][0],syllables[i][1],text)

        for key in translation_dictionary:
            text = re.sub(key,translation_dictionary[key],text)

        if writeflag == False:
            return (text)
        else:
            Grecka.writeFile(outputname,text)

