void u8()
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
//	float z[nrEvents];
	float xmin = -.25;
	float xmax = .25;
	float ymin = -.25;
	float ymax = .25;
	float zmin = -1;
	float zmax = 1;
	float b = 0;
	float r = .05;
	float ab=.1;
	float l = .3;
	float c = TMath::ATan(r/ab);
	float d = TMath::ATan(-r/ab);
	const int k= 10;
	float z[k];
	float a[nrEvents];
	float abs[nrEvents];
	float crit[nrEvents];
	float exp[nrEvents];
	float phi[nrEvents];
	float o=0;
	TH2F *hit[k];
	TH2F *miss[k];
	char *hitname = new char[10];
	char *missname = new char[10];

	
	
	for (int j = 0; j<1; j++){
		sprintf(hitname,"hit%d",j);
		hit[j] = new TH2F(hitname,"",400,xmin,xmax,400,ymin,ymax);
		hit[j]->SetMarkerColor(kRed);
		sprintf(missname,"miss%d",j);
		miss[j] = new TH2F(missname,"",400,xmin,xmax,400,ymin,ymax);
		miss[j]->SetMarkerColor(kBlue);
		
	for (Int_t i=0; i<nrEvents; i++) { 
		x[i]=x1->Uniform(xmin,xmax); //(xmin,xmax);
		y[i]=y1->Uniform(ymin,ymax); //(ymin,ymax);
		abs[i] = sqrt( y[i]**2 + x[i]**2);
		crit[i] = z1->Uniform(0,1);
		
//		if (x>0 && y<0)
			phi[i]=TMath::ATan(y[i]/x[i]);
//		else (x>0 && y>0)
	//		phi[i]=TMath::ATan(y[i]/x[i]);
		a[i]=  abs[i] -r/TMath::ASin(phi[i]);
		exp[i] = .5**(-a[i]/.1);
		//cout << exp[i] << " "<<   crit[i]<< endl;
		o= r/TMath::ASin(phi[i]) - d/TMath::ACos(phi[i]) ;
	//	b=TMath::ATan(x[i]/y[i]);
	//	if (x[i]>=0.1 && x[i] <= 0.3 && y[i] < 0.05 && y [i] > -0.05 && a>=d && a <=c)  // produziert den kasten
	//	if (x[i]>=0.1 && phi[i]>=d && phi[i] <=c && r/TMath::Sin(phi[i]) >abs[i] )
			hit[j]->Fill(x[i],y[i]);
		else if (x[i]>=0.1 && phi[i]>=d && phi[i] <=c && r/sin(phi[i]) >abs[i] )
			hit[j]->Fill(x[i],y[i]);
		else
		miss[j]->Fill(x[i],y[i]);
		}
		z[j]=hit[j]->GetEntries()/nrEvents;
		//cout << sin(phi)*r << " " << abs << endl;
	}
	
	float zmean[k+1];
	zmean[0] =0;
	float var[k+1];
	var[0]=0;

	for (int i = 0; i<k; i++)
		zmean[i+1]=zmean[i]+z[i];
	float zmean1 = zmean[k]/k;
	
	for (int i=0;i<k;i++)
		var[i+1]=(z[i]-zmean1)**2+var[i];
	
	float abw = sqrt(var[k]/(k-1));
//	cout << zmean1 <<"+- " << abw << endl;
//	cout << "#Entries = 10 hoch " << log10(nrEvents) << endl;
//	cout << "Pi ist ungefaehr " <<  pi<< endl ;

	
	gStyle->SetOptStat(000);
	c = new TCanvas("c","c",200,9,700,700);
	hit[0]->Draw();
	miss[0]->Draw("SAME");
}


/*
c: 50% teilchen nach 10cm im zählrohr ~> WK: 0.5 ** (strecke / 10 cm)



*/