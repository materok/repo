import numpy as np
import matplotlib.pyplot as plt
from helper.laufen import *

def main(version=17):

    if version==16:
        t5,km5,bpm,bpm_max,day= np.genfromtxt('../../dataLight.txt', unpack=True)
        gew,day1= np.genfromtxt('../../stats.txt', unpack=True)
        t5,t5min = tConvert(t5)
        vel5=calcVelo(km5,t5)
        MakeKMPlots(day,t5min,vel5)
        MakeStats(day1,gew,2016,day)
        MakeBPMPlots(day,bpm)
        MakeBPMPlots(day,bpm_max,option="max")
        MakeCumulPlot(day,km5)
        MakePercPlot(day)
    elif version==17:
        year=2017
        mins,sec,km5,bpm,bpm_max,day,month= np.genfromtxt('../../dataLight17.txt',missing_values=",", filling_values = -1, unpack=True)
        t5 =mins+sec/60.
        km5/=10.
        fillEmpty(sec)
        t5 =mins+sec/60.
        fillEmpty(month)
        gew17,day17,month17= np.genfromtxt('../../stats17.txt', unpack=True)
        gew17/=10.
        #MakeStats17(day17,month17,gew17,2017,show=True)
        t5,t5min = tConvert(t5)
        vel5=calcVelo(km5,t5)
        MakePercPlot(day,month,year)
        MakeBPMPlots(day,bpm,year=year)
        MakeBPMPlots(day,bpm_max,option="max",year=year)
        MakeCumulPlot(day,km5,year)
        MakeKMPlots(day,t5min,vel5,year)
        MakeStats17(day17,month17,gew17,year)


if __name__=="__main__":
    main()
