#include <vector>
#include <fstream>
#include <iostream>
#include <string>
#include <algorithm> // std::min_element
using namespace std;

#define SPLIT " "
#define NEXTT(vec) ((vec).push_back(atof(pch = strtok(NULL, SPLIT))))

void kmZeit() {
	string inp_filename = "C:/Users/Marcel/Documents/laufen/kmZeit.txt";
	vector <float> zeit, km;
	int n = 0;

	string line;
	ifstream inFile(inp_filename.c_str());
	if (inFile.is_open()) {
		while (getline(inFile, line)) {
            char* pch = strtok(line.c_str(), SPLIT);
			zeit.push_back(atof(pch));
			NEXTT(km);
			n++;
		}
	}
	inFile.close();
	
	float* x  = &km[0];
	float* y  = &zeit[0];
	const int k=n;
	float minX = *min_element(km.begin(),km.end())-1;
	float maxX = *max_element(km.begin(),km.end())+1;
	float minY = *min_element(zeit.begin(),zeit.end() )-0.2;
	float maxY = *max_element(zeit.begin(),zeit.end() )+0.2;
	const int binX = (maxX-minX)+1;
	const int binY = ((maxY-minY))*10;
	c1= new TCanvas("2dhist","2dhist", 915,567,700,500);
	TH2F* histogram = new TH2F("h", "", binX, minX, maxX, binY, minY, maxY);
	for (int i=0; i<k; i++)
		histogram->Fill(x[i],y[i]);
	histogram->GetXaxis()->SetTitle("Strecke in km");
	histogram->GetYaxis()->SetTitle("Zeit pro km");
//	histogram->SetLineWidth(2);
	histogram->SetMarkerColor(kBlue+1);
	histogram->Draw("lego2");
}

#undef SPLIT
#undef NEXTT
