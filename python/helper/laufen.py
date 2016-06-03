import numpy as np
from ROOT import *

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

def MakeBPMPlots(canvas,day,bpm,option="avg"):
    
    graph = TGraph(len(day),day,bpm)
    graph = TGraph(len(day),day,bpm)
    if option=="avg":
        graph.SetTitle("Herzfrequenz;Tag;Herzfrequenz im bpm")
    elif option=="max":
        graph.SetTitle("max. Herzfrequenz;Tag;max. Herzfrequenz im bpm")
    Markers(graph,4,21)
    graph.Draw("AP")
    canvas.Update()
    SavePlotPNG(canvas,canvas.GetTitle())
    SavePlotPDF(canvas,canvas.GetTitle())
    
def MakeFourPlots(canvas,day,time,velo):    
    
    gr1 = TGraphErrors(len(time),day,time,np.zeros(len(day)),TimeError(time))
    gr1.SetTitle("Laufzeiten;Tag;Zeit in min")
    f1 = TF1("f1","[0]+[1]*x", 0, 500)
    f1.SetParameters(34,-0.5)
    gr1.Fit("f1", "R")
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
    canvas.Update()
    SavePlotPNG(canvas,canvas.GetTitle())
    SavePlotPDF(canvas,canvas.GetTitle())
    
def MakeCumulPlot(canvas,day,distance):

    func = TF1("f2","[0]+[1]*x", 0, 500)    
    func.SetParameters((int(day[-1]/7)+1)*20,0)
    canvas.SetGrid()
    cumulDist= makeCumul(distance)
    graph = TGraph(len(day),day,cumulDist)
    graph.SetTitle("Laufstrecke;Nummer des Tages;Strecke gelaufen")
    Markers(graph)
    graph.Draw("AP")
    func.Draw("same")
    canvas.Update()
    SavePlotPNG(canvas,canvas.GetTitle())
    SavePlotPDF(canvas,canvas.GetTitle())

def MakePercPlot(canvas,day):
  
    perc=percentage(day)
    graph = TGraph(len(day),day,perc)
    graph.SetTitle("Lauf Prozent;Nummer des Tages; Prozent")
    Markers(graph,1,8)
    graph.Draw("AP")
    canvas.Update()
    SavePlotPNG(canvas,canvas.GetTitle())
    SavePlotPDF(canvas,canvas.GetTitle())
    
def Make2DPlot(canvas,time,distance):
    
    minX = distance.min()
    maxX = distance.max()
    minY = time.min()-0.2
    maxY = time.max()+0.2
    binX = (maxX-minX)+1
    binY = ((maxY-minY))*10
    histogram = TH2F("h", "", int(binX), minX, maxX, int(binY), minY, maxY)
    for i in range(0,len(distance)):
        histogram.Fill(distance[i],time[i])
    histogram.SetTitle(";Strecke in km;Zeit pro km")
    histogram.SetMarkerColor(kBlue+1)
    histogram.Draw("lego2")
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
    
def MakeStats(canvas,day,stats):
  
    graph = TGraph(len(day),day,stats)
    graph.SetTitle(";Nummer des Tages; Gewicht in kg")
    Markers(graph,1,8)
    graph.Draw("AP")
    canvas.Update()
    SavePlotPNG(canvas,canvas.GetTitle())
    SavePlotPDF(canvas,canvas.GetTitle())
