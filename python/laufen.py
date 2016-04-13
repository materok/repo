import numpy as np
from ROOT import *
#from helper.helper import tConvert,calcVelo,makeCumul,percentage,new_arr,diff,delta
from helper.helper import *
#import os
#import time
#from datetime import date
def main():
    
    #base=os.getcwd()
    #date=time.strftime("%Y-%m-%d")
    #os.mkdir(date)
    #km5,t5,bpm,day,km1,t1,km2,t2,km3,t3,km4,t4= np.genfromtxt('data.txt', unpack=True)
    km5,t5,bpm,bpm_max,day= np.genfromtxt('../dataLight.txt', unpack=True)
    #km5 and t5 are complete distance traveled and time needed
    bpm=new_arr(bpm)
    bpm_max=new_arr(bpm_max)    
    day=new_arr(day)
 #   t1,t1min = tConvert(t1)
 #   vel1=calcVelo(km5,t5)
 #   t2,t2min = tConvert(t2)
 #   vel2=calcVelo(km5,t5)
 #   t3,t3min = tConvert(t3)
 #   vel3=calcVelo(km5,t5)
 #   t4,t4min = tConvert(t4)
 #   vel4=calcVelo(km5,t5)
    t5,t5min = tConvert(t5)
    vel5=calcVelo(km5,t5)
    cumulDist= makeCumul(km5)
    perc=percentage(day)
    
    c1 = TCanvas("laufkumul","laufkumul",200,9,700,500)
    c1.SetGrid()
    gr = TGraph(len(t5),day,cumulDist)
    gr.SetTitle("Laufstrecke;Nummer des Tages;Strecke gelaufen")
    Markers(gr)
    gr.Draw("AP")
    c1.Update()
    c1.SaveAs("../plots/test.png")
    
    c2 = TCanvas("Prozentanteil","anteil",915,9,700,500)

    gr1 = TGraph(len(day),day,perc)
    gr1.SetTitle("Lauf Prozent;Nummer des Tages; Prozent")
#    gr1.GetXaxis().SetTitle("Nummer des Tages")
#    gr1.GetYaxis().SetTitle("Prozent")
    #gr1.SetMarkerStyle(8)
    Markers(gr1,1,8)
    gr1.Draw("AP")
    c2.Update()
    c2.SaveAs("../plots/test1.png")

    c6 = TCanvas("laufen2016","laufen",1200,1000)
    
    gr2 = TGraph(len(t5),day,t5min)
    gr2.SetTitle("Laufzeiten;Tag;Zeit in min")
#    Markers(gr2,kBlue,8)
#    gr2.SetMarkerColor(kBlack)
#    gr2.SetMarkerStyle(8)
    f1 = TF1("f1","[0]+[1]*x", 0, 500)
    f1.SetParameters(34,-0.5)
    gr2.Fit("f1", "R")
    gStyle.SetOptFit(1111)
	
    gr4 = TGraph(len(day),day,vel5)
    gr4.SetTitle("Geschwindigkeiten Laufzeiten 2015;Tag;Geschwindigkeit in #frac{km}{h}")
#    Markers(gr4,1,8)
    f3 = TF1("f3","[0]+[1]*x", 0, 500)
    f3.SetParameters(34,-0.5)
    gr4.Fit("f3", "R")
    
    resVel=diff(vel5,day,f3)
    gr3 = TGraph(len(day),day,resVel)
    gr3.SetTitle("Abweichung von Fit;Tag;Abweichung der Geschwindigkeit")
#    Markers(gr3,1,8)
    f2 = TF1("f1","0", 0, 500)

    deltaVel=delta(vel5)
    gr5 = TGraph(len(day),day,deltaVel)
    gr5.SetTitle("Differenz von Geschwindigkeiten von aufeinanderfolgenden Laeufen;Tag;Differenz")
#    Markers(gr5,1,8)

    Graphs=[gr2,gr3,gr4,gr5]
    for graph in Graphs:
        Markers(graph,1,8)

    c6.Divide(2,2)
    c6.cd(1)
    c6.cd(1).SetGrid()
    gr2.Draw("AP")
    c6.cd(2)
    c6.cd(2).SetGrid()
    gr3.Draw("AP")
    #f2.Draw("SAME")
    c6.Update()
    c6.cd(3)
    c6.cd(3).SetGrid()
    gr4.Draw("AP")
    c6.cd(4)
    c6.cd(4).SetGrid()
    gr5.Draw("AP")
    #f2.Draw("SAME")
    c6.Update()
    c6.SaveAs("../plots/test2.png")
    c6.SaveAs("../plots/test2.pdf")
  #  raw_input("")

    c3 = TCanvas("bpm","bpm",200,9,700,500)
    gr6 = TGraph(len(day),day,bpm)
    gr6.SetTitle("Herzfrequenz;Tag;Herzfrequenz im bpm")
    Markers(gr6,4,21)
    gr6.Draw("AP")
    c3.Update()
    c3.SaveAs("../plots/test3.png")

    c5 = TCanvas("bpm_max","bpm_max",200,9,700,500)
    gr7 = TGraph(len(day),day,bpm_max)
    gr7.SetTitle("max. Herzfrequenz;Tag;max. Herzfrequenz im bpm")
    Markers(gr7,4,21)
    gr7.Draw("AP")
    c5.Update()
    c5.SaveAs("../plots/test5.png")

    minX = km5.min()
    maxX = km5.max()
    minY = t5min.min()-0.2;
    maxY = t5min.max()+0.2;
    binX = (maxX-minX)+1;
    binY = ((maxY-minY))*10;
    c4= TCanvas("2dhist","2dhist", 915,567,700,500);
    histogram = TH2F("h", "", int(binX), minX, maxX, int(binY), minY, maxY);
    for i in range(0,len(km5)):
        histogram.Fill(km5[i],t5min[i]);
    histogram.SetTitle(";Strecke in km;Zeit pro km");
    histogram.SetMarkerColor(kBlue+1);
    histogram.Draw("lego2");
    c4.SaveAs("../plots/test4.png");
    

if __name__=="__main__":
    main()