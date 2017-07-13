import numpy as np
from helper.laufen import *

def main(version=17):

    if version==16:
        t5,km5,bpm,bpm_max,day= np.genfromtxt('../../dataLight.txt', unpack=True)
        gew,day1= np.genfromtxt('../../stats.txt', unpack=True)
        t5,t5min = tConvert(t5)
        vel5=calcVelo(km5,t5)
        MakeKMPlots(day,t5min,vel5)
        MakeKMHPlot(day,vel5,km5,2016,savepng=True)
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
        day=dayAndMonthToBin(day,month,year)
        gew17,day17,month17= np.genfromtxt('../../stats17.txt',missing_values=",", filling_values = -1, unpack=True)
        gew17/=10.
        fillEmpty(month17)
        #t5,t5min = tConvert(t5)
        vel5=calcVelo(km5,t5/60)
        print vel5
        print 60./vel5
        MakePercPlot(day,month,year)
        MakeKMHPlot(day,vel5,km5,year,savepng=True)
        MakeBPMPlots(day,bpm,year=year)
        MakeBPMPlots(day,bpm_max,option="max",year=year)
        MakeCumulPlot(day,km5,year)
        MakeKMPlots(day,t5,vel5,year)
        MakeStats17(day17,month17,gew17,year,runDay=day,savepng=True,showMin=True)
        MakeCombinedStats(day17,month17,gew17,year,runDay=day,savepng=True)
        MakeDeltaPlot(day17,month17,gew17,year,savepng=True)
        #~ MakeDeltaPlots(day17,month17,gew17,year,savepng=True)


if __name__=="__main__":
    main()
    #main(16)
