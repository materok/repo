void u8b()
{
	const int nrEvents=100000;
	
	TRandom3 *x1=new TRandom3();
	x1->SetSeed(0);
	TRandom3 *y1=new TRandom3();
	y1->SetSeed(0);
	TRandom3 *z1=new TRandom3();
	z1->SetSeed(0);
	float x[nrEvents];
	float y[nrEvents];
	float z[nrEvents];
	float xmin = -1;
	float xmax = 1;
	float ymin = -1;
	float ymax = 1;
	float zmin = -1;
	float zmax = 1;
	float a = 0;
	float b = 0;
	float c = TMath::ATan(0.05/0.10);
	float d = TMath::ATan(-0.05/0.10);
	
	TH2F *h3=new TH2F("h3","TRandom3",400,xmin,xmax,400,ymin,ymax); 
	h3->SetMarkerColor(kRed);
	TH2F *h4=new TH2F("h4","TRandom3",400,xmin,xmax,400,ymin,ymax); 
	h4->SetMarkerColor(kBlue);
	for (Int_t i=0; i<nrEvents; i++) { 
		x[i]=x1->Uniform(xmin,xmax); //(xmin,xmax);
		y[i]=y1->Uniform(ymin,ymax); //(ymin,ymax);
		z[i]=x[i]**2+y[i]**2;
		
		a=TMath::ATan(y[i]/x[i]);
	//	b=TMath::ATan(x[i]/y[i]);
	//	if (x[i]>=0.1 && x[i] <= 0.3 && y[i] < 0.05 & y [i] > -0.05 && a>=d && a <=c)  // produziert den kasten
		if (x[i]>=0.1 && a>=d && a <=c)
		h3->Fill(x[i],y[i]);
//		if ( x[i]> 0){
//		if (a <c)
//		h3->Fill(x[i],y[i]);
		else
		h4->Fill(x[i],y[i]);
//		}

	}
	float pi=h3->GetEntries()/nrEvents;

	cout << "#Entries = 10 hoch " << log10(nrEvents) << endl;
	cout << "Pi ist ungefaehr " <<  pi<< endl ;

	gStyle->SetOptStat(000);
	c = new TCanvas("c","c",200,9,700,700);
	h3->Draw();
	h4->Draw("SAME");
}