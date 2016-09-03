import numpy as np
from ROOT import *
#from helper.helper import tConvert,calcVelo,makeCumul,percentage,new_arr,diff,delta
from helper.laufen import *
#import os
#import time
#from datetime import date
def main():

    t5,km5,bpm,bpm_max,day= np.genfromtxt('../dataLight.txt', unpack=True)
    day=day.astype('d')
    gew,day1= np.genfromtxt('../stats.txt', unpack=True)
    #km5 and t5 are complete distance traveled and time needed
    gew=gew.astype('d')
    day1=day1.astype('d')

    c1 = TCanvas("gewicht","gewicht",200,9,1400,500)
    MakeStats(c1,day1,gew,day)


if __name__=="__main__":
    main()
