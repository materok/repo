#include <vector>
#include <fstream>
#include <iostream>
#include <string>
#include <algorithm> // std::min_element
using namespace std;

#define SPLIT " "
#define NEXTT(vec) ((vec).push_back(atof(pch = strtok(NULL, SPLIT))))

void mash2016light() {
	
	string inp_filename = "C:/Users/Marcel/ownCloud/laufen/dataLight.txt";
	vector <float> km5,t5,bpm,bpmMax,day;
	//km5,t5,bpm,day,km1,t1,km2,t2,km3,t3,km4,t4
	int n = 0;

	string line;
	ifstream inFile(inp_filename.c_str());
	if (inFile.is_open()) {
		while (getline(inFile, line)) {
            char* pch = strtok(line.c_str(), SPLIT);
			km5.push_back(atof(pch));
			NEXTT(t5);
			NEXTT(bpm);
			NEXTT(bpmMax);
			NEXTT(day);
			n++;
		}
	}
	inFile.close();
	
	float* x  = &day[0];
	float* y  = &t5[0];
	float* length  = &km5[0];

	c1 = new TCanvas("laufen2015","laufen",200,9,700,500);
	c1->SetGrid();
	gr = new TGraph(n,x,y);
	gr->SetTitle("Laufzeiten");
   	gr->GetXaxis()->SetTitle("Tag");
	gr->GetYaxis()->SetTitle("Zeit in min");
	gr->SetMarkerColor(kBlack);
	gr->SetMarkerStyle(8);
	TF1 *f1 = new TF1("f1","[0]+[1]*x", 0, 500);
	f1->SetParameters(34,-0.5);
	gr->Fit("f1", "R");
	gStyle->SetOptFit(1111);
	gr->Draw("AP");
	c1->Update();
	c1->SaveAs("C:/Users/Marcel/ownCloud/laufen/plots/Laufzeiten.png");
	const int k=n;
	float v[k];
	for (int i=0;i<k;i++){
		v[i]=length[i]/y[i]*60;
	}
	 
	float* y2  = &v[0];

	gr2 = new TGraph(n,x,y2);
	gr2->SetTitle("Geschwindigkeiten 2016");
	gr2->GetXaxis()->SetTitle("Tag");
	gr2->GetYaxis()->SetTitle("Geschwindigkeit in #frac{km}{h}");
	gr2->SetMarkerStyle(8);
	TF1 *f3 = new TF1("f3","[0]+[1]*x", 0, 500);
	f3->SetParameters(34,-0.5);
	gr2->Fit("f3", "R");
	

	float y1[k];

	for (int i=0;i<k; i++)
			y1[i]= y2[i]-f3(x[i]);
	
	//c2 = new TCanvas("laufen2015 res","laufen res",915,9,700,500);
	gr1 = new TGraph(n,x,y1);
	gr1->SetTitle("Abweichung von v Fit");
	gr1->GetXaxis()->SetTitle("Tag");
	gr1->GetYaxis()->SetTitle("Abweichung in #frac{km}{h}");
	gr1->SetMarkerStyle(8);
	TF1 *f2 = new TF1("f1","0", 0, 500);
	//gr1->Draw("AP");
	//f2->Draw("SAME");

	const int k1=n-1;
	float x3[k1];
	float y3[k1];
	
	for (int i=0;i<k1; i++){
		x3[i]=x[i];
		y3[i]= y2[i+1]-y2[i];
	}

	gr3 = new TGraph(k1,x3,y3);
	gr3->SetTitle("Differenz von Geschwindigkeiten 2016");
	gr3->GetXaxis()->SetTitle("Tag");
	gr3->GetYaxis()->SetTitle("Differenz");
	gr3->SetMarkerStyle(8);
	gr3->Draw("AP");
	f2->Draw("SAME");

	TCanvas *c6 = new TCanvas("alle Daten2015", "alle Daten2015", 1200,1000);

	c6->Divide(2,2);
	c6->cd(1);
	c6->cd(1)->SetGrid();
	gr->Draw("AP");
	c6->cd(2);
	c6->cd(2)->SetGrid();
	gr1->Draw("AP");
	f2->Draw("SAME");
	c6->Update();
	c6->cd(3);
	c6->cd(3)->SetGrid();
	gr2->Draw("AP");
	c6->cd(4);
	c6->cd(4)->SetGrid();
	gr3->Draw("AP");
	f2->Draw("SAME");
	c6->SaveAs("C:/Users/Marcel/ownCloud/laufen/plots/allData.png");

	const int k=n;
	float* x  = &km5[0];
	float* y  = &v[0];
	float y3[k];
	float minY1 =2000;
	float maxY1 =0;
	for (int i=0;i<k; i++){
		y3[i]= 60/y[i];
		if (minY1 >y3[i]){minY1=y3[i];}
		if (maxY1 <y3[i]){maxY1=y3[i];}
		//cout << y3[i] << endl;
	}

	
	float minX = *min_element(km5.begin(),km5.end())-1;
	float maxX = *max_element(km5.begin(),km5.end())+1;
	float minY = minY1-0.2;
	float maxY = maxY1+0.2;
//	float minY = *min_element(y3[0],y3[k-1])-0.2;
//	float maxY = *max_element(y3[0],y3[k-1])+0.2;
	const int binX = ((maxX-minX)+1)*10;
	const int binY = ((maxY-minY))*10;
	c1= new TCanvas("2dhist","2dhist", 915,567,700,500);
	TH2F* histogramX = new TH2F("hX", "", binX, minX, maxX, binY, minY, maxY);
	for (int i=0; i<k; i++)
		histogramX->Fill(x[i],y3[i]);
	histogramX->GetXaxis()->SetTitle("Strecke in km");
	histogramX->GetYaxis()->SetTitle("Zeit pro km");
	histogramX->SetMarkerColor(kBlue+1);
	histogramX->Draw("lego2");

	
	float* y  = &bpm[0];
	float* x  = &day[0];

	c1 = new TCanvas("bpm","bpm",200,9,700,500);
	gr1 = new TGraph(n,x,y);
	gr1->SetTitle("Herzfrequenz");
   	gr1->GetXaxis()->SetTitle("Tag");
	gr1->GetYaxis()->SetTitle("Herzfrequenz im bpm");
	gr1->SetMarkerColor(4);
	gr1->SetMarkerStyle(21);
	gr1->Draw("ALP");
	c1->Update();
	c1->SaveAs("C:/Users/Marcel/ownCloud/laufen/plots/bpm.png");

	float* y  = &bpmMax[0];
	float* x  = &day[0];

	c1 = new TCanvas("bpm","bpm",200,9,700,500);
	gr1 = new TGraph(n,x,y);
	gr1->SetTitle("Herzfrequenz");
   	gr1->GetXaxis()->SetTitle("Tag");
	gr1->GetYaxis()->SetTitle("max Herzfrequenz im bpm");
	gr1->SetMarkerColor(4);
	gr1->SetMarkerStyle(21);
	gr1->Draw("ALP");
	c1->Update();
	c1->SaveAs("C:/Users/Marcel/ownCloud/laufen/plots/bpmMax.png");

	
	
	float* x  = &day[0];
	float* y  = &km5[0];



	const int k=n;
	float y1[k];
	float proc[k];
	float z[k];
	for (int i=0;i<k; i++){
		if(i==0) {y1[i]=y[i];}
		else	{y1[i]= y[i]+y1[i-1];}
		z[i]=i+1;
		proc[i]=z[i]/day[i];
	}

	int exp=(day[k-1]/7);
	int exp1=(exp+1)*20;
	TF1 *expFunc = new TF1("expFunc","[0]+[1]*x",0,500);
	expFunc->SetParameters(exp1,0);
	cout << exp<<endl;

	c1 = new TCanvas("laufkumul","laufkumul",200,9,700,500);
	c1->SetGrid();
	gr = new TGraph(n,x,y1);
	gr2 = new TGraph(n,z,y1);
	gr->SetTitle("Laufstrecke");
	gr->GetXaxis()->SetTitle("Nummer des Tages");
	gr->GetYaxis()->SetTitle("Strecke gelaufen");
	gr->SetMarkerColor(kBlack);
	gr2->SetMarkerColor(kRed);
	gr->SetMarkerStyle(8);
	gr2->SetMarkerStyle(8);
	gr->Draw("AP");
	expFunc->Draw("same");
	c1->Update();
	c1->SaveAs("C:/Users/Marcel/ownCloud/laufen/plots/cumul.png");

	c2 = new TCanvas("Prozentanteil","anteil",915,9,700,500);
	gr1 = new TGraph(n,x,proc);
	gr1->SetTitle("Lauf Prozent");
	gr1->GetXaxis()->SetTitle("Nummer des Tages");
	gr1->GetYaxis()->SetTitle("Prozent");
	gr1->SetMarkerStyle(8);
	gr1->Draw("AP");
	c2->Update();
	c2->SaveAs("C:/Users/Marcel/ownCloud/laufen/plots/perc.png");


	float sum[0];
	sum[0]= 0;
	int k1=k-1;
	int k2=k-1;
	for (int i=x[k-1]; i>=x[k-1]-6; i--){
		if(i==x[k2]){
			sum[0]+=y[k1];
			k1--;
			k2--;
		}
	}
	cout << "Gesamtstrecke ist:" << y1[k-1] << " und in den letzten 7 Tagen, bin ich " << sum[0] << " gelaufen." << endl;
	

	}

#undef SPLIT
#undef NEXTT

void histSetting(TH1F* histogram, char* title, char* xTitle, char* yTitle, int lw, int mc) {
		histogram->SetTitle(title);
		histogram->GetXaxis()->SetTitle(xTitle);
		histogram->GetYaxis()->SetTitle(yTitle);
		histogram->SetLineWidth(lw);
		histogram->SetLineColor(mc);
	}
