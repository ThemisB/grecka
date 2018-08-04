# -*- coding: utf-8 -*-
import sys
import os
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)),"../lib"))
from grecka import Grecka

if __name__ == "__main__":
    greeklishString = Grecka.toGreeklish('η αθήνα είναι η πρωτεύουσα και μεγαλύτερη πόλη της ελλάδας. είναι από τις παλαιότερες πόλεις του κόσμου, με την καταγεγραμμένη ιστορία της να φθάνει ως το 3.200 π.χ.')
    print (greeklishString)
