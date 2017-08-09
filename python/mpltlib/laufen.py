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
        gew17p2,day17p2,month17p2,fett,wasser,muskel,knochen= np.genfromtxt('../../stats17p2.txt',missing_values=",", filling_values = -1, unpack=True)
        gew17=np.append(gew17,gew17p2)
        gew17/=10.
        fett/=10.
        wasser/=10.
        muskel/=10.
        knochen/=10.
        day17=np.append(day17,day17p2)
        month17=np.append(month17,month17p2)
        fillEmpty(month17)
        fillEmpty(month17p2)
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
        MakeComposition(day17p2,month17p2,fett,wasser,muskel,knochen,year,savepng=True)
    elif version==0:
        year=17
        gew17,day17,month17= np.genfromtxt('../../stats17.txt',missing_values=",", filling_values = -1, unpack=True)
        gew17p2,day17p2,month17p2,fett,wasser,muskel,knochen= np.genfromtxt('../../stats17p2.txt',missing_values=",", filling_values = -1, unpack=True)
        gew17=np.append(gew17,gew17p2)
        gew17/=10.
        fett/=10.
        wasser/=10.
        muskel/=10.
        knochen/=10.
        day17=np.append(day17,day17p2)
        month17=np.append(month17,month17p2)
        fillEmpty(month17)
        fillEmpty(month17p2)
        plt.figure(figsize=(20,10))
        y=gew17
        day,month=day17,month17
        x=dayAndMonthToBin(day,month,year)
        yRun=np.zeros(len(y))
        yerrRun=np.zeros(len(y))
        yerr=np.zeros(len(y))
        y_bmi=np.zeros(len(y))
        yerr_bmi=np.zeros(len(y))
        possibleLabels = ['January', 'Febuary', 'March', 'April',
                          'May','June','July','August','September',
                          'Oktober','November', 'December']
        labels=[]
        x_ticks=[]
        for i in range(len(month)):
            if (month[i]==month[i-1]) and i != 0:
                labels.append('')
            else:
                labels.append(possibleLabels[int(month[i])-1])
                x_ticks.append(day[i])
        counter=0
        for i in range(len(y)):
            if i < 5:
                yerr[i]=var(y[:5])**.5
            else:
                yerr[i]=var(y[i-5:i])**.5
                if yerr[i]<0.1:
                    yerr[i]=0.1
        import subprocess
        from scipy.optimize import curve_fit
        def fit_func(x,a,b):
            return a*x+b
        fitStart=np.where(y == y.max())
        print fitStart
        popt, pcov = curve_fit(func, x, y)
        print popt
        #~ plt.plot(xdata, func(xdata, *popt), 'r-', label='fit')
        plt.figure(figsize=(10,10))
        plt.errorbar(x, y, xerr=0.25, yerr=yerr, fmt='o',zorder=1)
        minIndices=np.where(y == y.min())
        plt.plot(x[minIndices], y[minIndices], 'h',zorder=6,color="green")
        plt.xlabel("month")
        plt.xticks(x, labels, rotation='vertical')
        plt.subplots_adjust(bottom=0.175)
        plt.ylabel("weight in kg")#
        plt.show()



if __name__=="__main__":
    main()
    #~ main(0)
    #main(16)
