#include <vector>
#include <fstream>
#include <iostream>
#include <string>
using namespace std;

#define SPLIT " "
#define NEXTT(vec) ((vec).push_back(atof(pch = strtok(NULL, SPLIT))))

void laufkumul() {
	string inp_filename = "C:/Users/Marcel/Documents/laufen/kumul.txt";
	vector <float> strecke, tag, anzahl;
	int n = 0;

	string line;
	ifstream inFile(inp_filename.c_str());
	if (inFile.is_open()) {
		while (getline(inFile, line)) {
            char* pch = strtok(line.c_str(), SPLIT);
			strecke.push_back(atof(pch));
			NEXTT(tag);
	//		NEXTT(anzahl);
			n++;
		}
	}
	inFile.close();
	
	float* x  = &tag[0];
	float* y  = &strecke[0];
	//float* z  = &anzahl[0];



	const int k=n;
	float y1[k];
	float proc[k];
	float z[k];
	for (int i=0;i<k; i++){
		if(i==0) {y1[i]=y[i];}
		else	{y1[i]= y[i]+y1[i-1];}
		z[i]=i+1;
		proc[i]=z[i]/tag[i];
	}

	c1 = new TCanvas("laufkumul","laufkumul",200,9,700,500);
	c1->SetGrid();
	gr = new TGraph(n,x,y1);
	gr2 = new TGraph(n,z,y1);
	gr->SetTitle("Laufstrecke");
	gr->GetXaxis()->SetTitle("Nummer des tages");
	gr->GetYaxis()->SetTitle("Strecke gelaufen");
	gr->SetMarkerColor(kBlack);
	gr2->SetMarkerColor(kRed);
	gr->SetMarkerStyle(8);
	gr2->SetMarkerStyle(8);
	gr->Draw("AP");
//	gr2->Draw("SAME");
	c1->Update();

	c2 = new TCanvas("Prozentanteil","anteil",915,9,700,500);
	gr1 = new TGraph(n,x,proc);
	gr1->SetTitle("Lauf Prozent");
	gr1->GetXaxis()->SetTitle("Nummer des Tages");
	gr1->GetYaxis()->SetTitle("Prozent");
	gr1->SetMarkerStyle(8);
	gr1->Draw("AP");
	c2->Update();


	float sum[0];
	sum[0]= 0;
	int k1=k-1;
	int k2=k-1;
	for (int i=x[k-1]; i>=x[k-1]-6; i--){
		if(i==x[k2]){
			sum[0]+=y[k1];
			//sum+=y[i]
			k1--;
			k2--;
		}
	}
	cout << "Gesamtstrecke ist:" << y1[k-1] << " und in den letzten 7 Tagen, bin ich " << sum[0] << " gelaufen." << endl;
	
//	strecke.clear();
//	delete tag;
//	delete anzahl;
	}

#undef SPLIT
#undef NEXTT
