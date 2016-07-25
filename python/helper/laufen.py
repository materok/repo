import numpy as np
from ROOT import *

def moment(array, mu, sigma, n):

    nom=0.
    for item in array:
        nom += ( (item-mu) / sigma )**n
    return nom/len(array)

def mean(array):

    res=moment(array,0,1,1)
    return res

def var(array):

    res=moment(array,moment(array,0,1,1),1,2)
    return res

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

def SetDayAxis(histo,day,year):

    j=0
    k=1
    first=True
    Labels=["January","February","March","April","May","June","July","August","Oktober","September","November","Dezember"]
    for i in range(1,367):
        if i < min(day):
            continue
        elif i > max(day):
            break
        if first==True:
            if dayToMonth(i,year)[1]!=j+1:
                j=dayToMonth(i,year)[1]-1
                k=int(min(day)/20)+1
            first=False
        if dayToMonth(i,year)==(1,j+1):
            histo.GetXaxis().SetBinLabel(histo.GetXaxis().FindBin(i),Labels[j])
            j+=1
        elif i==20*k:
            histo.GetXaxis().SetBinLabel(histo.GetXaxis().FindBin(i),str(i))
            k+=1
            if k==6 or k==9:
                k+=1


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

def new_arr(arr):

    arr_new=np.array([],'d')
    for val in arr:
        arr_new=np.append(arr_new,val)
    return arr_new

def diff(y,x,f): #f is a function

    y_new=np.array([],'d')
    for i in range(0,len(y)):
        y_new= np.append(y_new, y[i]-f(x[i]) )
    return y_new

def delta(arr):

    arr_new=np.array([],'d')
    for i in range(1,len(arr)):
        arr_new= np.append(arr_new, arr[i]-arr[i-1] )
    return arr_new

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

def Markers(graph,Color=1,Style=21):
    graph.SetMarkerColor(Color) ##1: black, 2:red, 3:green, 4:blue,5: yellow, 6: magenta, 7:cyan
    graph.SetMarkerStyle(Style)  ##1: Dot, 2: cross, 3: Star, 4: circle, 5: x, 8: big point, 21:boxes
    #https://root.cern.ch/doc/v606/classTAttMarker.html

def CheckDay(day):

    test=day+3
    test=test%7
    return test

def SavePlotPDF(Canvas,Title,Path="../plots/"):
    Canvas.SaveAs(Path+Title+".pdf")

def SavePlotJPG(Canvas,Title,Path="../plots/"):
    Canvas.SaveAs(Path+Title+".jpg")

def SavePlotPNG(Canvas,Title,Path="../plots/"):
    Canvas.SaveAs(Path+Title+".png")

def MakeBPMPlots(canvas,day,bpm,option="avg",year=2016):

    graph = TGraph(len(day),day,bpm)
    graph = TGraph(len(day),day,bpm)
    if option=="avg":
        graph.SetTitle("Herzfrequenz;Tag;Herzfrequenz im bpm")
    elif option=="max":
        graph.SetTitle("max. Herzfrequenz;Tag;max. Herzfrequenz im bpm")
    Markers(graph,4,21)
    graph.Draw("AP")
    SetDayAxis(graph,day,year)
    canvas.Update()
    SavePlotPNG(canvas,canvas.GetTitle())
    SavePlotPDF(canvas,canvas.GetTitle())

def MakeFourPlots(canvas,day,time,velo,year=2016):

    gr1 = TGraphErrors(len(time),day,time,np.zeros(len(day)),TimeError(time))
    gr1.SetTitle("Laufzeiten;Tag;Zeit in min")
    f1 = TF1("f1","[0]+[1]*x", 0, 500)
    f1.SetParameters(34,-0.5)
    #~ gr1.Fit("f1", "R")
    gStyle.SetOptFit(1111)

    gr2 = TGraphErrors(len(day),day,velo,np.zeros(len(day)),VelError(velo))
    gr2.SetTitle("Geschwindigkeiten Laufzeiten 2015;Tag;Geschwindigkeit in #frac{km}{h}")
    f3 = TF1("f3","[0]+[1]*x", 0, 500)
    f3.SetParameters(34,-0.5)
    gr2.Fit("f3", "R")

    resVel=diff(velo,day,f3)
    gr3 = TGraph(len(day),day,resVel)
    gr3.SetTitle("Abweichung von Fit;Tag;Abweichung der Geschwindigkeit")
    f2 = TF1("f1","0", 0, 500)

    deltaVel=delta(velo)
    gr4 = TGraph(len(deltaVel),day,deltaVel)
    gr4.SetTitle("Differenz von Geschwindigkeiten von aufeinanderfolgenden Laeufen;Tag;Differenz")

    Graphs=[gr1,gr2,gr3,gr4]
    for graph in Graphs:
        Markers(graph,1,8)

    canvas.Divide(2,2)
    canvas.cd(1)
    canvas.cd(1).SetGrid()
    gr1.Draw("AP")
    canvas.cd(2)
    canvas.cd(2).SetGrid()
    gr3.Draw("AP")
    f2.Draw("SAME")
    canvas.cd(3)
    canvas.cd(3).SetGrid()
    gr2.Draw("AP")
    canvas.Update()
    canvas.cd(4)
    canvas.cd(4).SetGrid()
    gr4.Draw("AP")
    f2.Draw("SAME")
    for graph in Graphs:
        SetDayAxis(graph,day,year)
    canvas.Update()
    SavePlotPNG(canvas,canvas.GetTitle())
    SavePlotPDF(canvas,canvas.GetTitle())

def MakeCumulPlot(canvas,day,distance,year=2016):

    func = TF1("f2","[0]+[1]*x", 0, 500)
    func.SetParameters((int(day[-1]/7)+1)*20,0)
    canvas.SetGrid()
    cumulDist= makeCumul(distance)
    graph = TGraph(len(day),day,cumulDist)
    graph.SetTitle("Laufstrecke;Nummer des Tages;Strecke gelaufen")
    Markers(graph)
    graph.Draw("AP")
    func.Draw("same")
    string="gelaufene Strecke: " + str(cumulDist[-1]) + " km"
    tex=TLatex(0.5,0.5,"u")
    tex.SetNDC()
    tex.SetTextAlign(11)
    tex.SetTextSize(0.05)
    tex.DrawLatex(0.44,0.1,string)
    SetDayAxis(graph,day,year)
    canvas.Update()
    SavePlotPNG(canvas,canvas.GetTitle())
    SavePlotPDF(canvas,canvas.GetTitle())
    print "ich bin schon ", cumulDist[-1]," km gelaufen"
    print "ich haette ", func.GetParameter(0)," km laufen sollen"

def MakePercPlot(canvas,day,year=2016):

    perc=percentage(day)
    graph = TGraph(len(day),day,perc)
    graph.SetTitle("Lauf Prozent;Nummer des Tages; Prozent")
    Markers(graph,1,8)
    graph.Draw("AP")
    SetDayAxis(graph,day,year)
    canvas.Update()
    SavePlotPNG(canvas,canvas.GetTitle())
    SavePlotPDF(canvas,canvas.GetTitle())

def Make2DPlot(canvas,time,distance):

    ROOT.gStyle.SetOptStat(0)
    minX = int(distance.min())
    maxX = int(distance.max()+1)
    y=time/distance
    minY = int(y.min())
    if y.min()-int(y.min())>0.5:
        minY+=0.5
    maxY = int(y.max())+0.5
    if y.max()-int(y.max())>0.5:
        maxY+=0.5
    binX = (maxX-minX)
    binY = (maxY-minY)*12  # 60s/12bins = 5s/bin
    histogram = TH2F("h", "", int(binX), minX, maxX, int(binY), minY, maxY)
    for i in range(0,len(distance)):
        histogram.Fill(distance[i],y[i])
    histogram.SetTitle(";Strecke in km;Zeit in min/km")
    histogram.SetMarkerColor(kBlue+1)
    histogram.Draw("colz2")
    canvas.Update()
    SavePlotPNG(canvas,canvas.GetTitle())
    SavePlotPDF(canvas,canvas.GetTitle())


def MakeOld2DPlot(canvas,time,distance):

    ROOT.gStyle.SetOptStat(0)
    minX = int(distance.min()-1)
    maxX = int(distance.max()+1)
    minY = time.min()-0.2
    maxY = time.max()+0.2
    binX = (maxX-minX)
    binY = ((maxY-minY))
    histogram = TH2F("h", "", int(binX), minX, maxX, int(binY), minY, maxY)
    for i in range(0,len(distance)):
        histogram.Fill(distance[i],time[i])
    histogram.SetTitle(";Strecke in km;Zeit in min")
    histogram.SetMarkerColor(kBlue+1)
    histogram.Draw("colz2")
    canvas.Update()
    SavePlotPNG(canvas,canvas.GetTitle())
    SavePlotPDF(canvas,canvas.GetTitle())

def MakeDayPlot(canvas,day):

    histogram = TH1D("h", "", 7, 0, 7)
    histogram.SetTitle(";Tag;Eintraege")
    for entry in day:
        histogram.Fill(CheckDay(entry))
    Labels=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
    n_bin=1
    for label in Labels:
        histogram.GetXaxis().SetBinLabel(n_bin,label)
        n_bin+=1
    histogram.Draw()
    SavePlotPNG(canvas,canvas.GetTitle())
    SavePlotPDF(canvas,canvas.GetTitle())

def MakeMonthPlot(canvas,day,year):


    Labels=["January","February","March","April","May","June","July","August","Oktober","September","November","Dezember"]
    histogram = TH1D("h", "", len(Labels), 0, len(Labels))
    histogram.SetTitle(";Monat;Eintraege")
    for entry in day:
        histogram.Fill(dayToMonth(entry,year)[1]-1)
    n_bin=1
    for label in Labels:
        histogram.GetXaxis().SetBinLabel(n_bin,label)
        n_bin+=1
    histogram.Draw()
    SavePlotPNG(canvas,canvas.GetTitle())
    SavePlotPDF(canvas,canvas.GetTitle())

def MakeMonthKMPlot(canvas,day,year,dist):


    ROOT.gStyle.SetOptStat(0)
    Labels=["January","February","March","April","May","June","July","August","Oktober","September","November","Dezember"]
    histogram = TH1D("h", "", len(Labels), 0, len(Labels))
    histogram1 = TH1D("h1", "", len(Labels), 0, len(Labels))
    histogram.SetTitle(";Monat;km gelaufen")
    for i in range(0,len(day)):
        histogram.Fill(dayToMonth(day[i],year)[1]-1,dist[i])
    n_bin=1
    i=1
    for label in Labels:
        histogram.GetXaxis().SetBinLabel(n_bin,label)
        n_bin+=1
        if histogram.GetBinContent(n_bin)>0.:
            i+=1
    multi=dayToMonth(day[-1],year)[0]
    if i in [1,3,5,7,8,10,12]:
        multi/=31.
    elif i in [4,6,9,11]:
        multi/=30.
    elif i in [2]:
        multi/=28.
    else:
        print "something strange is going on, could not find case"
    multi=1/multi
    histogram1.Fill(dayToMonth(day[-1],year)[1]-1,histogram.GetBinContent(i)*multi)
    leg=TLegend(0.7,0.8,0.9,0.9)
    leg.AddEntry(histogram,"data","l")
    leg.AddEntry(histogram1,"prognosis","l")

    histogram.Draw()
    histogram.Draw("same text")
    histogram1.SetLineColor(kRed)
    histogram1.Draw("same")
    histogram1.Draw("same text")
    leg.Draw("same")
    SavePlotPNG(canvas,canvas.GetTitle())
    SavePlotPDF(canvas,canvas.GetTitle())


def MakeLBLPlot(canvas,day,velo,year=2016):

    length=5.555
    const=50./2100.
    time_trans=length/velo*60.
    #~ time_trans=length/VelError(velo)*60.
    time_err=np.sqrt(const**2+(VelError(velo)/velo)**2)*time_trans
    graph = TGraphErrors(len(velo),day,time_trans,np.zeros(len(day)),time_err)
    graph.SetTitle("auf LBL umgerechnete Zeit;Nummer des Tages; Zeit in Min")
    graph.SetMarkerStyle(21)
    graph.Draw("AP")
    SetDayAxis(graph,day,year)
    SavePlotPNG(canvas,canvas.GetTitle())
    SavePlotPDF(canvas,canvas.GetTitle())



def MakeStats(canvas,day,stats,day_run,height=1.70,height_err=0.01,year=2016):

    x_run=np.zeros(len(day))
    xerr=np.zeros(len(day))
    xerr_run=np.zeros(len(day))
    yerr=np.zeros(len(stats))
    y_run=np.zeros(len(stats))
    yerr_run=np.zeros(len(stats))
    y_bmi=np.zeros(len(stats))
    yerr_bmi=np.zeros(len(stats))
    for i in range(0,len(stats)):
        if i < 5:
            yerr[i]=var(stats[:5])**.5
        else:
            yerr[i]=var(stats[i-5:i])**.5
        if day[i] in day_run:
            x_run[i]=day[i]
            y_run[i]=stats[i]
            yerr_run[i]=yerr[i]
        y_bmi[i]=stats[i]/(height**2)
        yerr_bmi[i]=y_bmi[i]*np.sqrt((yerr[i]/stats[i])**2+(2*height_err/height)**2)
        #~ yerr_bmi[i]=y_bmi[i]*np.sqrt((yerr[i]/stats[i])**2)
    canvas.Divide(2)
    canvas.cd(1)
    graph = TGraphErrors(len(day),day,stats,xerr,yerr)
    graph.SetTitle(";Nummer des Tages; Gewicht in kg")
    Markers(graph,1,8)
    graph.Draw("AP")
    graph_run = TGraphErrors(len(day_run),x_run,y_run,xerr,yerr_run)
    Markers(graph_run,3,8)
    graph_run.Draw("same P")
    canvas.Update()
    canvas.cd(2)
    bmi_graph = TGraphErrors(len(day),day,y_bmi,xerr,yerr_bmi)
    bmi_graph.SetTitle(";Nummer des Tages; BMI in #frac{kg}{m^{2}}")
    Markers(bmi_graph,1,8)
    bmi_graph.Draw("AP")
    for graphs in [graph,bmi_graph]:
        SetDayAxis(graphs,day,year)
    canvas.Update()
    SavePlotPNG(canvas,canvas.GetTitle())
    SavePlotPDF(canvas,canvas.GetTitle())


    lowBound=19.
    if 19 > min(y_bmi):
        lowBound=min(y_bmi)/0.99
    bmi_graph.GetYaxis().SetRangeUser(lowBound,max(y_bmi)*1.01)
    func=TF1("f1","[0]",0,365)
    func.SetParameter(0,20)
    func.Draw("SAME")
    canvas.cd(1)
    lowBound=19.*height**2
    if 19*height**2 > min(stats):
        lowBound=min(stats)/0.99
    graph.GetYaxis().SetRangeUser(lowBound,max(stats)*1.01)
    func1=TF1("f2","[0]",0,365)
    func1.SetParameter(0,20.*height**2)
    func1.Draw("SAME")
    canvas.Update()
    SavePlotPNG(canvas,"wunsch"+canvas.GetTitle())
    SavePlotPDF(canvas,"wunsch"+canvas.GetTitle())

def MakeMPKPlot(canvas,velo):

    ROOT.gStyle.SetOptStat(1111)
    xmax=int(60./min(velo))+1
    if abs(xmax-60./min(velo))>0.5:
        xmax-=0.5
    xmin=int(60./max(velo))
    if abs(xmin-60./max(velo))>0.5:
        xmin+=0.5
    temp=xmax-xmin
    multi=12
    binx=int((temp)*multi)
    histogram = TH1D("h", "", binx, xmin, xmax)
    histogram.SetTitle(";Zeit pro KM;Eintraege")
    for item in velo:
        histogram.Fill(60./item)
    histogram.Draw()
    canvas.Update()
    SavePlotPNG(canvas,canvas.GetTitle())
    SavePlotPDF(canvas,canvas.GetTitle())
    ROOT.gStyle.SetOptStat(0)
