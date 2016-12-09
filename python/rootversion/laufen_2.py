import numpy as np
from ROOT import *
#from helper.helper import tConvert,calcVelo,makeCumul,percentage,new_arr,diff,delta
from helper.laufen import *
#import os
#import time
#from datetime import date
def main():

    #km5,t5,bpm,day,km1,t1,km2,t2,km3,t3,km4,t4= np.genfromtxt('data.txt', unpack=True)
    minute,second,km,bpm,bpm_max,day,month,year= np.genfromtxt('../../dataLight2.txt', unpack=True)
    bpm=bpm.astype('d')
    bpm_max=bpm_max.astype('d')
    day=day.astype('d')
 #   t1,t1min = tConvert(t1)
 #   vel1=calcVelo(km5,t5)
 #   t2,t2min = tConvert(t2)
 #   vel2=calcVelo(km5,t5)
 #   t3,t3min = tConvert(t3)
 #   vel3=calcVelo(km5,t5)
 #   t4,t4min = tConvert(t4)
 #   vel4=calcVelo(km5,t5)
    t5,t5min = tConvert(t5)
    vel5=calcVelo(km5,t5)

    c1 = TCanvas("LaufKumul","laufkumul",200,9,700,500)
    MakeCumulPlot(c1,day,km5)

    c2 = TCanvas("ProzentGelaufen","anteil",915,9,700,500)
    MakePercPlot(c2,day)

    c3 = TCanvas("bpm_avg","bpm_avg",200,9,700,500)
    MakeBPMPlots(c3,day,bpm)

    c4= TCanvas("ZeitStrecke","ZeitStrecke", 915,567,700,500)
    Make2DPlot(c4,t5min,km5)

    c11= TCanvas("ZeitStrecke_old","ZeitStrecke_old", 915,567,700,500)
    MakeOld2DPlot(c11,t5min,km5)

    c5 = TCanvas("bpm_max","bpm_max",200,9,700,500)
    MakeBPMPlots(c5,day,bpm_max,option="max")

    c6 = TCanvas("laufen2016","laufen",1200,1000)
    MakeFourPlots(c6,day,t5min,vel5)

    c7 = TCanvas("tag", "TagGelaufen",1200,1000)
    MakeDayPlot(c7,day)

    c8 = TCanvas("monat", "MonatGelaufen",1200,1000)
    MakeMonthPlot(c8,day,2016)

    c12 = TCanvas("monat_km", "MonatKMGelaufen",1200,1000)
    MakeMonthKMPlot(c12,day,2016,km5)

    c13 = TCanvas("zeitprokm", "zeitprokm",1200,1000)
    MakeMPKPlot(c13,vel5)

    c10 = TCanvas("LBLcomp", "LBL comparison",1200,1000)
    MakeLBLPlot(c10,day,vel5)

    gew,day1= np.genfromtxt('../../stats.txt', unpack=True)
    gew=gew.astype('d')
    day1=day1.astype('d')

    c9 = TCanvas("gewicht","gewicht",200,9,1400,500)
    MakeStats(c9,day1,gew,day)


if __name__=="__main__":
    main()
