#include <vector>
#include <fstream>
#include <iostream>
#include <string>
using namespace std;

#define SPLIT " "
#define NEXTT(vec) ((vec).push_back(atof(pch = strtok(NULL, SPLIT))))

void lauf2015() {
	string inp_filename = "C:/Users/Marcel/Documents/laufen/zeit2015.txt";
	vector <float> zeit, anzahl;
	int n = 0;

	string line;
	ifstream inFile(inp_filename.c_str());
	if (inFile.is_open()) {
		while (getline(inFile, line)) {
            char* pch = strtok(line.c_str(), SPLIT);
			zeit.push_back(atof(pch));
			NEXTT(anzahl);
			n++;
		}
	}
	inFile.close();
	
	float* x  = &anzahl[0];
	float* y  = &zeit[0];
	
	c1 = new TCanvas("laufen2015","laufen",200,9,700,500);
	c1->SetGrid();
	gr = new TGraph(n,x,y);
	gr->SetTitle("Laufzeiten");
   	gr->GetXaxis()->SetTitle("Kalenderwoche");
	gr->GetYaxis()->SetTitle("Zeit in min");
	gr->SetMarkerColor(kBlack);
	gr->SetMarkerStyle(8);
	TF1 *f1 = new TF1("f1","[0]+[1]*x", 0, 50);
	f1->SetParameters(34,-0.5);
	gr->Fit("f1", "R");
	gStyle->SetOptFit(1111);
	gr->Draw("AP");
	c1->Update();

	const int k=n;
	float y1[k];

	for (int i=0;i<k; i++)
			y1[i]= y[i]-f1(x[i]);
	
	c2 = new TCanvas("laufen2015 res","laufen res",915,9,700,500);
	gr1 = new TGraph(n,x,y1);
	gr1->SetTitle("Abweichung von Fit");
	gr1->GetXaxis()->SetTitle("Kalenderwoche");
	gr1->GetYaxis()->SetTitle("Abweichung in #frac{min #upoint 100}{60}");
	gr1->SetMarkerStyle(8);
	TF1 *f2 = new TF1("f1","0", 0, 50);
	gr1->Draw("AP");
	f2->Draw("SAME");
		

//	c3= new TCanvas("laufen2015 hist res","laufen hist res", 915,567,700,500);
	TH1F* histogram = new TH1F("h", "Diff", 10, -2, 2);
	for (int i=0; i<n; i++)
		histogram->Fill(y1[i]);
	histogram->GetXaxis()->SetTitle("Differenz");
	histogram->GetYaxis()->SetTitle("Anzahl");
	histogram->SetLineWidth(2);
	histogram->SetMarkerColor(kBlue+1);
//	histogram->Draw();

	string inp_filename1 = "C:/Users/Marcel/Documents/laufen/v2015.txt";
	vector <float> v;
	int n1 = 0;

	string line;
	ifstream inFile(inp_filename1.c_str());
	if (inFile.is_open()) {
		while (getline(inFile, line)) {
            char* pch = strtok(line.c_str(), SPLIT);
			v.push_back(atof(pch));
			n1++;
		}
	}
	inFile.close();
	 
	float* y2  = &v[0];

//	c4 = new TCanvas("laufen2015 v","laufen v",200,567,700,500);
	gr2 = new TGraph(n,x,y2);
	gr2->SetTitle("Geschwindigkeiten Laufzeiten 2015");
	gr2->GetXaxis()->SetTitle("Kalenderwoche");
	gr2->GetYaxis()->SetTitle("Geschwindigkeit in #frac{km}{h}");
	gr2->SetMarkerStyle(8);
	TF1 *f3 = new TF1("f3","[0]+[1]*x", 0, 50);
	f3->SetParameters(34,-0.5);
	gr2->Fit("f3", "R");
//	gStyle->SetOptFit(1111);
//	gr2->Draw("AP");
	
	const int k1=n-1	;
	float x3[k1];
	float y3[k1];
	
	for (int i=0;i<k1; i++){
		x3[i]=x[i];
		y3[i]= y[i+1]-y[i];
	//	cout << y3[i] << " " << x3[i] << endl;
	}

/*	
	c5 = new TCanvas("laufen2015 diff","laufen diff",200,9,1400,500);

	c5->Divide(2,1);
	c5->cd(1);
	c5-> //cd(1)->
	SetGrid();*/
	gr3 = new TGraph(k1,x3,y3);
	gr3->SetTitle("Differenz von Laufzeiten 2015");
	gr3->GetXaxis()->SetTitle("Kalenderwoche");
	gr3->GetYaxis()->SetTitle("Differenz");
	gr3->SetMarkerStyle(8);
//	TF1 *f3 = new TF1("f4","[0]+[1]*x", 0, 50);
//	f4->SetParameters(34,-0.5);
//	gr3->Fit("f4", "R");
	gr3->Draw("AP");
	f2->Draw("SAME");
	/*
	c5->cd(2);
	TH1F* histogram1 = new TH1F("h", "Diff", 20, -3.5, 3);
	for (int i=0; i<k1; i++)
		histogram1->Fill(y3[i]);
	histogram1->GetXaxis()->SetTitle("Differenz");
	histogram1->GetYaxis()->SetTitle("Anzahl");
	histogram1->SetLineWidth(2);
	histogram1->SetMarkerColor(kBlue+1);
	histogram1->Draw("*H");
	*/
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
//	histogram->Draw("*H");
	
	}

#undef SPLIT
#undef NEXTT
