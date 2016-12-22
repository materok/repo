import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

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


def dayToMonth(day,year):
    # [january,febuary,march,april,may,june,july,august,september,oktober,november,december]
    month=[31,28,31,30,31,30,31,31,30,31,30,31]
    if year%4==0:
        month[1]=month[1]+1
    i=1
    counter=1
    j=0
    while i<day:
        counter+=1
        if counter==month[j]+1:
            j+=1
            counter=1
        i+=1
    return counter,j+1

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
        sec=(time_old-min)/.6
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

def makeCumul(distance): #distance is an array

    distanceCumul=np.array([],'d')
    cumul=0
    for dist in distance:
        cumul+=dist
        distanceCumul=np.append(distanceCumul,cumul)
    return distanceCumul

def percentage(day): #day is an array

    n=0.
    perc_arr=np.array([],'d')
    for run in day:
        n+=1
        perc=n/run*100
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


def makeStats(x,y,year,runX,height=1.70,height_err=0.01,show=False):

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
    #for i in range(len(x)):
        #j,k= dayToMonth(x[i],year)
        #if j==1:
            #labels.append(possibleLabels[k-1])
            #x_ticks.append(x[i])
        #else:
            #labels.append('')
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
    SavePlot(x,year,"stats")
    if show==True: plt.show()

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

    plt.plot(day,cumulDist,marker="+")
    maxVal=(int(day[-1]/7)+1)*20
    x1,x2,y1,y2 = plt.axis()
    plt.axis((x1,x2,0,maxVal+20))
    plt.axhline(maxVal, color='r')
    plt.title("gelaufene Strecke")
    plt.xlabel("Nummer des Tag")
    plt.ylabel("Strecke in km")
    SavePlot(day,year,"cumul")
    if show==True: plt.show()

def MakePercPlot(day,year=2016,show=False):

    perc=percentage(day)
    plt.plot(day,perc,marker="+")
    plt.title("Lauf Prozent")
    plt.xlabel("Nummer des Tages")
    plt.ylabel("Prozent")
    SavePlot(day,year,"perc")
    if show==True: plt.show()

def MakeBPMPlots(day,bpm,option="avg",year=2016,show=False):

    plt.plot(day,bpm,linestyle="",marker="x")
    adder=""
    if option=="avg":
        pass
    elif option=="max":
        adder="max. "
    else: print "this option is not supported"
    plt.title(adder+"Herzfrequenz")
    plt.xlabel("Nummer des Tag")
    plt.ylabel(adder+ "Herzfrequenz im bpm")
    SavePlot(day,year,adder.split(".")[0]+"bpm")
    if show==True: plt.show()

def SavePlot(x,year,title):
    today=dayToMonth(x[-1],year)
    adder=str(today[0])+"_"+str(today[1])+"_"+str(year)
    plt.savefig("../../plots/"+title+adder+".pdf")

if __name__=="__main__":
    main()
