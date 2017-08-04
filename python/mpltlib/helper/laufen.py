import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
from math import ceil

def moment(array, mu, sigma, n):

    nom=0.
    for item in array:
        nom += ( (item-mu) / sigma )**n
    return nom/len(array)

def mean(array):

    res=moment(array,0,1,1)
    return res

def var(array):

    res=moment(array,moment(array,0,1,1),1,2)*len(array)/(len(array)-1)
    return res

def delta(arr):

    arr_new=np.array([],'d')
    for i in range(1,len(arr)):
        arr_new= np.append(arr_new, arr[i]-arr[i-1] )
    return arr_new

def fillEmpty(array):
    if len(array)>0:
        temp=array[0]
        for i,item in enumerate(array):
            if item==-1:
                array[i]=temp
            else:
                temp=item

def dayToMonth(day,year):
    # [january,febuary,march,april,may,june,july,august,september,oktober,november,december]
    month=[31,28,31,30,31,30,31,31,30,31,30,31]
    if year%4==0:
        month[1]=month[1]+1
    i=1
    counter=1
    j=0
    while i<int(day):
        counter+=1
        if counter==month[j]+1:
            j+=1
            counter=1
        i+=1
    return counter,j+1

def dayAndMonthToBin(day,month,year):
    # [january,febuary,march,april,may,june,july,august,september,oktober,november,december]
    monthDict={1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
    dayDict={}
    if year%4==0:
        monthDict[2]+=1

    for key,val in monthDict.iteritems():
        if key ==1:
            dayDict[key]=0
        else:
            dayDict[key]=dayDict[key-1]+monthDict[key-1]
    binNumbers=np.array([],'d')
    for entryDay,entryMonth in zip(day,month):
        binNumbers=np.append(binNumbers,entryDay+dayDict[entryMonth])
    return binNumbers

def convertDayToBin():
    # [january,febuary,march,april,may,june,july,august,september,oktober,november,december]
    month=[31,28,31,30,31,30,31,31,30,31,30,31]
    if year%4==0:
        month[1]=month[1]+1
    month=makeCumul(month)
    binNumber=np.array([],'d')
    for i,j in izip(days,in_month):
        binNumber=np.append(binNumber, j+i-1)
    return binNumber

def tConvert(time):

    time_new=np.array([],'d')
    time_min=np.array([],'d')
    for time_old in time:
        min=int(time_old)
        sec=(time_old-min)
        hour=(min+sec)/60
        timeInMin=(min+sec)
        time_new=np.append(time_new,hour)
        time_min=np.append(time_min,timeInMin)
    return time_new,time_min

def calcVelo(distance,time): #distance and time are arrays

    #distance in km, time in h => vel in km/h
    for entry in time:
        if entry==0:
            entry=1
            print "entry was 0 and has been set to 1"
    vel=distance/time
    return vel

def calcWeightUncert(y):
    yerr=np.zeros(len(y))
    for i in range(len(y)):
        if i < 5:
            yerr[i]=var(y[:5])**.5
        else:
            yerr[i]=var(y[i-5:i])**.5
            if yerr[i]<0.1:
                yerr[i]=0.1
    return yerr

def makeCumul(distance): #distance is an array

    distanceCumul=np.array([],'d')
    cumul=0
    for dist in distance:
        cumul+=dist
        distanceCumul=np.append(distanceCumul,cumul)
    return distanceCumul

def percentage(day,month=[],year=2017): #day is an array

    n=0.
    perc_arr=np.array([],'d')
    if year==2016:
        for run in day:
            print run
            n+=1
            perc=n/run*100
            perc_arr=np.append(perc_arr,perc)
    else:
        binNumbers=dayAndMonthToBin(day,month,year)
        for run in binNumbers:
            n+=1
            perc=n/run*100.
            perc_arr=np.append(perc_arr,perc)
    return perc_arr

def TimeError(time):

    const=20./60.
    errors=np.array([],'d')
    for value in time:
        errors=np.append(errors,const)
    return errors

def VelError(velo):

    const=50./2100.
    errors=np.array([],'d')
    for value in velo:
        errors=np.append(errors,value*const)
    return errors


def MakeStats(x,y,year,runX,height=1.70,height_err=0.01,show=False,savepng=False):

    plt.figure(figsize=(20,10))
    xRun=np.zeros(len(y))
    yRun=np.zeros(len(y))
    yerrRun=np.zeros(len(y))
    yerr=np.zeros(len(y))
    y_bmi=np.zeros(len(y))
    yerr_bmi=np.zeros(len(y))
    xRun_temp=np.zeros(len(x))
    yRun_temp=np.zeros(len(y))
    yerrRun_temp=np.zeros(len(y))
    possibleLabels = ['January', 'Febuary', 'March', 'April',
                      'May','June','July','August','September',
                      'Oktober','November', 'December']
    labels=[]
    x_ticks=[]
    for day in x:
        j,k= dayToMonth(day,year)
        if j==1:
            labels.append(possibleLabels[k-1])
            x_ticks.append(day)
        else:
            labels.append('')
    counter=0
    for i in range(len(y)):
        if i < 5:
            yerr[i]=var(y[:5])**.5
        else:
            yerr[i]=var(y[i-5:i])**.5
            if yerr[i]<0.1:
                yerr[i]=0.1
        if x[i] in runX:
            counter+=1
            xRun_temp[i]=x[i]
            yRun_temp[i]=y[i]
            yerrRun_temp[i]=yerr[i]
        y_bmi[i]=y[i]/(height**2)
        yerr_bmi[i]=y_bmi[i]*np.sqrt((yerr[i]/y[i])**2+(2*height_err/height)**2)
    xRun=np.array([],'d')
    yRun=np.array([],'d')
    yRun_bmi=np.array([],'d')
    for i in range(len(xRun_temp)):
        if xRun_temp[i]>0:
            xRun=np.append(xRun,xRun_temp[i])
            yRun=np.append(yRun,yRun_temp[i])
            yRun_bmi=np.append(yRun_bmi,yRun_temp[i]/(height**2))
    plt.subplot(121)
    plt.errorbar(x, y, xerr=0.25, yerr=yerr, fmt='o')
    plt.plot(xRun, yRun, 'rs')
    plt.xlabel("month")
    plt.xticks(x, labels, rotation='vertical')
    plt.subplots_adjust(bottom=0.175)
    plt.ylabel("weight in kg")
    plt.subplot(122)
    plt.errorbar(x, y_bmi, xerr=0.25, yerr=yerr_bmi, fmt='o')
    plt.plot(xRun, yRun_bmi, 'rs')
    plt.xlabel("month")
    plt.xticks(x, labels, rotation='vertical')
    plt.subplots_adjust(bottom=0.175)
    plt.ylabel("bmi")
    SavePlot(x,year,"stats",savepng)
    if show==True: plt.show()

def MakeStats17(day,month,y,year,runDay=[],runMonth=[],height=1.70,height_err=0.01,show=False,savepng=False,showMin=False):

    plt.figure(figsize=(20,10))
    xRun=np.zeros(len(y))
    x=dayAndMonthToBin(day,month,year)
    runX=dayAndMonthToBin(runDay,runMonth,year)
    if year==2017:
        runX=runDay
    yRun=np.zeros(len(y))
    yerrRun=np.zeros(len(y))
    yerr=np.zeros(len(y))
    y_bmi=np.zeros(len(y))
    yerr_bmi=np.zeros(len(y))
    xRun_temp=np.zeros(len(x))
    yRun_temp=np.zeros(len(y))
    yerrRun_temp=np.zeros(len(y))
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
        if int(x[i]) in [int(entry) for entry in runX]:
            counter+=1
            xRun_temp[i]=x[i]
            yRun_temp[i]=y[i]
            yerrRun_temp[i]=yerr[i]
        y_bmi[i]=y[i]/(height**2)
        yerr_bmi[i]=y_bmi[i]*np.sqrt((yerr[i]/y[i])**2+(2*height_err/height)**2)
    xRun=np.array([],'d')
    yRun=np.array([],'d')
    yRun_bmi=np.array([],'d')
    for i in range(len(xRun_temp)):
        if xRun_temp[i]>0:
            xRun=np.append(xRun,xRun_temp[i])
            yRun=np.append(yRun,yRun_temp[i])
            yRun_bmi=np.append(yRun_bmi,yRun_temp[i]/(height**2))
    plt.subplot(121)
    plt.errorbar(x, y, xerr=0.25, yerr=yerr, fmt='o')
    plt.plot(xRun, yRun, 'rs')
    plt.xlabel("month")
    plt.xticks(x, labels, rotation='vertical')
    plt.subplots_adjust(bottom=0.175)
    plt.ylabel("weight in kg")
    plt.subplot(122)
    plt.errorbar(x, y_bmi, xerr=0.25, yerr=yerr_bmi, fmt='o')
    plt.plot(xRun, yRun_bmi, 'rs')
    for i in range(int(min(y_bmi)),int(max(y_bmi))+2):
        plt.plot((min(x),max(x)),(i,i),  color = 'k')
    plt.xlabel("month")
    plt.xticks(x, labels, rotation='vertical')
    plt.subplots_adjust(bottom=0.175)
    plt.ylabel("bmi")
    SavePlot(x,year,"stats")
    if show==True: plt.show()

    plt.figure(figsize=(10,10))
    plt.subplot(111)
    plt.errorbar(x, y, xerr=0.25, yerr=yerr, fmt='o',zorder=1)
    plt.plot(xRun, yRun, 'rs',zorder=5)
    minIndices=np.where(y == y.min())
    plt.plot(x[minIndices], y[minIndices], 'h',zorder=6,color="green")
    plt.xlabel("month")
    plt.xticks(x, labels, rotation='vertical')
    plt.subplots_adjust(bottom=0.175)
    plt.ylabel("weight in kg")
    SavePlot(x,year,"singleStats",savepng)

def MakeCombinedStats(day,month,y,year,runDay=[],runMonth=[],show=False,savepng=False):

    plt.figure(figsize=(20,10))
    xRun=np.zeros(len(y))
    x=dayAndMonthToBin(day,month,year)
    x=np.append(x,365)
    y=np.append(y,y[-1])
    runX=dayAndMonthToBin(runDay,runMonth,year)
    if year==2017:
        runX=runDay
    yRun=np.zeros(len(y))
    yerrRun=np.zeros(len(y))
    yerr=np.zeros(len(y))
    xRun_temp=np.zeros(len(x))
    yRun_temp=np.zeros(len(y))
    yerrRun_temp=np.zeros(len(y))
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
        if int(x[i]) in [int(entry) for entry in runX]:
            counter+=1
            xRun_temp[i]=x[i]
            yRun_temp[i]=y[i]
            yerrRun_temp[i]=yerr[i]
    xRun=np.array([],'d')
    yRun=np.array([],'d')
    for i in range(len(xRun_temp)):
        if xRun_temp[i]>0:
            xRun=np.append(xRun,xRun_temp[i])
            yRun=np.append(yRun,yRun_temp[i])
    gew16,day16= np.genfromtxt('../../stats.txt', unpack=True)
    xRun16,yRun16,yerr16=prep16Data(gew16,day16)
    plt.figure(figsize=(10,10))
    plt.subplot(111)
    plt.errorbar(x, y, xerr=0.25, yerr=yerr, fmt='^',zorder=3,label="2017",color="blue")
    plt.errorbar(day16, gew16, xerr=0.25, yerr=yerr16, fmt='v',zorder=1,label="2016",color="green")
    plt.plot(xRun, yRun, 'rs',zorder=4)
    plt.plot(xRun16, yRun16, 'rs',zorder=2,marker="p",color="yellow")
    plt.xlabel("month")
    plt.xticks(x, labels, rotation='vertical')
    plt.subplots_adjust(bottom=0.175)
    plt.ylabel("weight in kg")
    plt.legend()
    SavePlot(x,year,"singleCombinedStats",savepng)

def prep16Data(gew16,day16):
    t5,km5,bpm,bpm_max,day= np.genfromtxt('../../dataLight.txt', unpack=True)
    xRun16=np.array([],'d')
    yRun16=np.array([],'d')
    for i,d in enumerate(day16):
        if d in day:
            xRun16=np.append(xRun16,d)
            yRun16=np.append(yRun16,gew16[i])
    yerr16=calcWeightUncert(gew16)
    return xRun16,yRun16,yerr16

def MakeKMPlots(day,time,velo,year=2016,show=False):


    plt.figure(figsize=(30,10))
    plt.subplot(131)
    plt.errorbar(day,time,xerr=np.zeros(len(day)),yerr=TimeError(time), fmt='o')
    plt.xlabel("Nummer des Tages")
    plt.ylabel("Zeit in minuten")

    plt.subplot(132)
    plt.errorbar(day,velo,xerr=np.zeros(len(day)),yerr=VelError(velo), fmt='o')
    plt.xlabel("Nummer des Tages")
    plt.ylabel("Geschwindigkeit in km/h")

    plt.subplot(133)
    deltaVel=delta(velo)
    plt.plot(day[1:len(day)],deltaVel, linestyle='', marker="+")
    plt.xlabel("Nummer des Tages")
    plt.ylabel("Differenz von Geschwindigkeit in km/h")
    SavePlot(day,year,"kmPlots")
    if show==True: plt.show()


def MakeCumulPlot(day,distance,year=2016,show=False):

    import datetime
    today = datetime.date.today()
    lastRun = datetime.date(year,dayToMonth(day[-1],year)[1],dayToMonth(day[-1],year)[0])
    diff = today -lastRun

    cumulDist= makeCumul(distance)

    if diff.days!=0:
        day=np.append(day,day[-1]+diff.days)
        cumulDist=np.append(cumulDist,cumulDist[-1])

    plt.figure(figsize=(10,10))
    plt.plot(day,cumulDist,marker="+")
    maxVal=(int(day[-1]/7.)+1)*20
    x1,x2,y1,y2 = plt.axis()
    #~ plt.axis((x1,x2,0,maxVal+20))
    #~ plt.axhline(maxVal, color='r')
    plt.title("gelaufene Strecke")
    plt.xlabel("Nummer des Tag")
    plt.ylabel("Strecke in km")
    SavePlot(day,year,"cumul")
    if show==True: plt.show()

def MakePercPlot(day,month,year=2016,show=False):

    plt.figure(figsize=(10,10))
    perc=percentage(day,month,year)
    plt.plot(day,perc,marker="+")
    plt.title("Lauf Prozent")
    plt.xlabel("Nummer des Tages")
    plt.ylabel("Prozent")
    SavePlot(day,year,"perc")
    if show==True: plt.show()

def MakeKMHPlot(day,dist,velo,year=2017,savepng=False,show=False):

    plt.figure(figsize=(8, 8))
    from matplotlib.ticker import NullFormatter
    nullfmt = NullFormatter()         # no labels

    # definitions for the axes
    left, width = 0.1, 0.65
    bottom, height = 0.1, 0.65
    bottom_h = left_h = left + width + 0.02

    rect_scatter = [left, bottom, width, height]
    rect_histx = [left, bottom_h, width, 0.2]
    rect_histy = [left_h, bottom, 0.2, height]

    axScatter = plt.axes(rect_scatter)
    axHistx = plt.axes(rect_histx)
    axHisty = plt.axes(rect_histy)

    # no labels
    axHistx.xaxis.set_major_formatter(nullfmt)
    axHisty.yaxis.set_major_formatter(nullfmt)

    # now determine nice limits by hand:
    #binwidth = .25
    binwidth = 1
    highx = int(max(velo))+1+binwidth
    highy = max(dist)+1+binwidth
    lowx = int(min(velo))-binwidth
    lowy = int(min(dist))-binwidth

    axScatter.set_xlim((lowx, highx))
    axScatter.set_ylim((lowy, highy))

    binsx = np.arange(lowx, highx+binwidth, binwidth)
    binsy = np.arange(lowy, highy+binwidth, binwidth)

    # setup colorcoding
    hist, xedges, yedges = np.histogram2d(velo, dist, (binsx, binsy))
    xidx = np.clip(np.digitize(velo, binsx), 0, hist.shape[0]-1)
    yidx = np.clip(np.digitize(dist, binsy), 0, hist.shape[1]-1)
    colors = hist[xidx-1, yidx-1]
    # the scatter plot:
    axScatter.scatter(velo, dist,c=colors)
    #axScatter.scatter(velo, dist)

    #setup gridspacing

    from matplotlib.ticker import MultipleLocator
    spacing = .25
    minorLocator = MultipleLocator(spacing)
    axScatter.yaxis.set_minor_locator(minorLocator)
    axScatter.xaxis.set_minor_locator(minorLocator)

    #axScatter.grid(color='r', linestyle='--', linewidth=.5, which = 'minor')
    axScatter.grid(color='r', linestyle='-', linewidth=.5)
    axHistx.hist(velo, bins=binsx)
    axHisty.hist(dist, bins=binsy, orientation='horizontal')

    axHistx.set_xlim(axScatter.get_xlim())
    axHisty.set_ylim(axScatter.get_ylim())

    axScatter.set_xlabel("distance in km")
    axScatter.set_ylabel("velocity in km/h")
    axHistx.set_ylabel("#entries")
    axHisty.set_xlabel("#entries")
    SavePlot(day,year,"kmh",savepng=savepng,tight=False)
    if show==True: plt.show()

def MakeBPMPlots(day,bpm,option="avg",year=2016,show=False):

    plt.figure(figsize=(10,10))
    plt.plot(day,bpm,linestyle="",marker="x")
    adder=""
    if option=="avg":
        pass
    elif option=="max":
        adder="max. "
    else: print "this option is not supported"
    plt.title(adder+"Herzfrequenz")
    plt.xlabel("Nummer des Tag")
    plt.ylabel(adder+ "Herzfrequenz in bpm")
    SavePlot(day,year,adder.split(".")[0]+"bpm")
    if show==True: plt.show()

def MakeDeltaPlots(day,month,weight,year=2016,show=False,savepng=False):

    binNumbers=dayAndMonthToBin(day,month,year)
    nWeeks=int(ceil(int(binNumbers[-1]/7)))
    x= np.ones(nWeeks)
    deltaWeightMinMax = np.ones(nWeeks)
    deltaWeight0m1 = np.ones(nWeeks)
    WeightAvg = np.ones(nWeeks)
    WeightAvgError = np.ones(nWeeks)
    lastIndex=0
    for i in range(nWeeks):
        x[i]=i+1
        lowBorder=i*7
        upBorder=(i+1)*7
        tmpArray=np.array([],'d')
        while lastIndex<len(binNumbers) and int(binNumbers[lastIndex])>lowBorder and int(binNumbers[lastIndex])<=upBorder:
            tmpArray=np.append(tmpArray,weight[lastIndex])
            #~ print binNumbers[lastIndex],lowBorder,upBorder,lastIndex
            lastIndex+=1
        deltaWeightMinMax[i]=max(tmpArray)-min(tmpArray)
        deltaWeight0m1[i]=tmpArray[0]-tmpArray[-1]
        arrayMean=mean(tmpArray)
        WeightAvg[i]=arrayMean
        WeightAvgError[i]=var(tmpArray)

    plt.figure(figsize=(10,10))
    plt.plot(x,deltaWeightMinMax,linestyle="",marker="x")
    plt.title("$\Delta$ weight (max-min)")
    plt.xlabel("Nummer des Tag")
    plt.ylabel("$\Delta$ weight in kg")
    SavePlot(binNumbers,year,"deltaweightMinMax",savepng)
    if show==True: plt.show()
    plt.figure(figsize=(10,10))
    plt.plot(x,deltaWeight0m1,linestyle="",marker="x")
    plt.title("$\Delta$ weight (first minus last day of the week)")
    plt.xlabel("Nummer des Tag")
    plt.ylabel("$\Delta$ weight in kg")
    SavePlot(binNumbers,year,"deltaweightFirstLast",savepng)
    if show==True: plt.show()
    plt.figure(figsize=(10,10))
    plt.plot(x,WeightAvgError,linestyle="",marker="x")
    plt.title("variance of weight")
    plt.xlabel("Nummer des Tag")
    plt.ylabel("weight variance in kg")
    SavePlot(binNumbers,year,"weightVar",savepng)
    if show==True: plt.show()
    plt.figure(figsize=(10,10))
    plt.errorbar(x,WeightAvg,xerr=0,yerr=WeightAvgError,linestyle="",marker="x")
    plt.title("average weight")
    plt.xlabel("Nummer des Tag")
    plt.ylabel("average weight in kg")
    SavePlot(binNumbers,year,"avgWeight",savepng)
    if show==True: plt.show()

def MakeDeltaPlot(day,month,weight,year=2016,show=False,savepng=False):

    x=dayAndMonthToBin(day,month,year)
    weightDelta = delta(weight)
    weightDelta = np.append(weightDelta,0)
    nWeeks=int(ceil(int(x[-1]/7)))
    weightDeltaRebin = np.zeros(nWeeks)
    xRebin = np.ones(nWeeks)
    lastIndex=0
    for i in range(nWeeks):
        xRebin[i]=i+1
        lowBorder=i*7
        upBorder=(i+1)*7
        tmpArray=np.array([],'d')
        while lastIndex<len(x) and int(x[lastIndex])>lowBorder and int(x[lastIndex])<=upBorder:
            weightDeltaRebin[i]+=weightDelta[lastIndex]
            lastIndex+=1

    plt.figure(figsize=(10,10))
    plt.plot(x,weightDelta,linestyle="",marker="x")
    plt.title("$\Delta$ weight")
    plt.xlabel("Nummer der Woche")
    plt.ylabel("$\Delta$ weight in kg")
    plt.grid(True)
    SavePlot(x,year,"deltaweight")
    plt.figure(figsize=(10,10))
    plt.plot(xRebin,weightDeltaRebin,linestyle="",marker="o")
    plt.title("$\Delta$ weight")
    plt.xlabel("Nummer der Woche")
    plt.ylabel("$\Delta$ weight in kg")
    plt.grid(True)
    SavePlot(x,year,"deltaweightRebin",savepng)
    if show==True: plt.show()

def MakeComposition(day,month,fett,wasser,muskel,knochen,year,show=False,savepng=True):

    x=dayAndMonthToBin(day,month,year)

    plt.figure(figsize=(10,10))
    plt.plot(x,fett,linestyle="",marker="x")
    plt.xlabel("Nummer des Tages")
    plt.ylabel("Fett in %")
    SavePlot(x,year,"body1_",savepng)
    plt.figure(figsize=(10,10))
    plt.plot(x,wasser,linestyle="",marker="x")
    plt.xlabel("Nummer des Tages")
    plt.ylabel("Wasser in %")
    SavePlot(x,year,"body2_",savepng)
    plt.figure(figsize=(10,10))
    plt.plot(x,muskel,linestyle="",marker="x")
    plt.xlabel("Nummer des Tages")
    plt.ylabel("Muskel in %")
    SavePlot(x,year,"body3_",savepng)
    plt.figure(figsize=(10,10))
    plt.plot(x,knochen,linestyle="",marker="x")
    plt.xlabel("Nummer des Tages")
    plt.ylabel("Knochen in %")
    SavePlot(x,year,"body4_",savepng)
    labels = 'Fett', 'Wasser', 'Muskel', 'Knochen'
    sizes = [fett[-1], wasser[-1], muskel[-1], knochen[-1]]
    total = sum(sizes)
    plt.figure(figsize=(10,10))
    plt.pie(sizes, labels=labels, autopct=lambda(p): '{:.1f}'.format(p * total / 100), startangle=90)
    SavePlot(x,year,"body5_",savepng)
    plt.figure(figsize=(10,10))
    plt.pie(sizes, labels=labels, autopct="%1.1f%%", startangle=90)
    SavePlot(x,year,"body6_",savepng)
    if show==True: plt.show()


def SavePlot(x,year,title,savepng=False,tight=True,noAdd=True):
    today=dayToMonth(x[-1],year)
    adder=str(today[0])+"_"+str(today[1])+"_"+str(year)
    if noAdd:
        adder=""
        title=title.replace("_","")
    if tight: plt.tight_layout()
    plt.savefig("../../plots/"+title+adder+".pdf")
    if savepng: plt.savefig("../../plots/"+title+adder+".png")

if __name__=="__main__":
    pass
