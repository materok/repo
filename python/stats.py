import numpy as np
from ROOT import *
#from helper.helper import tConvert,calcVelo,makeCumul,percentage,new_arr,diff,delta
from helper.laufen import *
#import os
#import time
#from datetime import date
def main():
    
    #km5,t5,bpm,day,km1,t1,km2,t2,km3,t3,km4,t4= np.genfromtxt('data.txt', unpack=True)
    gew,day= np.genfromtxt('../stats.txt', unpack=True)
    #km5 and t5 are complete distance traveled and time needed
    gew=new_arr(gew)
    day=new_arr(day)
    
    c1 = TCanvas("gewicht","gewicht",200,9,700,500)
    MakeStats(c1,day,gew)


if __name__=="__main__":
    main()
