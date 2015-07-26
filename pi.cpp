void pi()
{
	const int nrEvents=100000;
	
	TRandom3 *r3=new TRandom3();
	TRandom3 *x1=new TRandom3();
	x1->SetSeed(0);
	TRandom3 *y1=new TRandom3();
	y1->SetSeed(0);
	float x[nrEvents];
	float y[nrEvents];
	float z[nrEvents];
	int xmin = 0;
	int xmax = 1;
	int ymin = 0;
	int ymax = 1;
	float a = 0;
	float b = 0;

	TH2F *h3=new TH2F("h3","TRandom3",400,xmin,xmax,400,ymin,ymax); 
	h3->SetMarkerColor(kRed);
	TH2F *h4=new TH2F("h4","TRandom3",400,xmin,xmax,400,ymin,ymax); 
	h4->SetMarkerColor(kBlue);
	TStopwatch *st=new TStopwatch();
	st->Start();
	for (Int_t i=0; i<nrEvents; i++) { 
		x[i]=x1->Rndm(); //(xmin,xmax);
		y[i]=y1->Rndm(); //(ymin,ymax);
		z[i]=x[i]**2+y[i]**2;
		
		a=TMath::ATan(y[i]/x[i]);
		b=TMath::Sin(a);
	//	if (z[i]<1)
		if (y[i] <b)
		h3->Fill(x[i],y[i]);
		else
		h4->Fill(x[i],y[i]);
		
	}
	st->Stop();
	float pi=4*h3->GetEntries()/nrEvents;

	cout << "Berechnung dauerte " << st->CpuTime()<<  " Sekunden"  << endl;
	cout << "#Entries = 10 hoch " << log10(nrEvents) << endl;
	cout << "Pi ist ungefähr " <<  pi<< endl ;

	gStyle->SetOptStat(000);
	c = new TCanvas("c","c",200,9,700,700);
	h3->Draw();
	h4->Draw("SAME");
}