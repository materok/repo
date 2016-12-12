import numpy as np
import matplotlib.pyplot as plt
from helper.laufen import *

def main():
    t5,km5,bpm,bpm_max,day= np.genfromtxt('../../dataLight.txt', unpack=True)
    gew,day1= np.genfromtxt('../../stats.txt', unpack=True)
    t5,t5min = tConvert(t5)
    vel5=calcVelo(km5,t5)


    MakeKMPlots(day,t5min,vel5)
    makeStats(day1,gew,2016,day)
    MakeBPMPlots(day,bpm)
    MakeBPMPlots(day,bpm_max,option="max")
    MakeCumulPlot(day,km5)
    MakePercPlot(day)

if __name__=="__main__":
    main()
