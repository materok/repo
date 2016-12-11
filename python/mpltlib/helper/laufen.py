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

def dayToMonth(day,year):
    #~ [january,febuary,march,april,may,june,july,august,september,oktober,november,december]
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

def makeStats(x,y,year,runX,height=1.70,height_err=0.01):

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
    for i in range(len(x)):
        j,k= dayToMonth(x[i],year)
        if j==1:
            labels.append(possibleLabels[k-1])
            x_ticks.append(x[i])
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
    plt.savefig("../../plots/stats"+str(year)+".pdf")
    plt.show()


if __name__=="__main__":
    main()
