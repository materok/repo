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

def Markers(graph,Color=1,Style=21):
    graph.SetMarkerColor(Color) ##1: black, 2:red, 3:green, 4:blue,5: yellow, 6: magenta, 7:cyan  
    graph.SetMarkerStyle(Style)  ##1: Dot, 2: cross, 3: Star, 4: circle, 5: x, 8: big point, 21:boxes 
    #https://root.cern.ch/doc/v606/classTAttMarker.html

def SavePlotPDF(Canvas,Title,Path="../plots/"):
    Canvas.SaveAs(Path+Title+".pdf")

def SavePlotJPG(Canvas,Title,Path="../plots/"):
    Canvas.SaveAs(Path+Title+".jpg")

def SavePlotPNG(Canvas,Title,Path="../plots/"):
    Canvas.SaveAs(Path+Title+".png")
    