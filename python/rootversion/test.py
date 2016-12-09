#! /usr/bin/python
import os

basedir=os.getcwd()
os.chdir("C:/root_v5.34.36/bin")

import glob
print glob.glob("ROOT*")

from ROOT import *
os.chdir(basedir)


#~ import ROOT
