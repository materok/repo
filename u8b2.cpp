void u8b2()
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
	float xmin = -1;
	float xmax = 1;
	float ymin = -1;
	float ymax = 1;
	float zmin = 0;
	float zmax = 1;
	float r = .05;
	float ab=.1;
	float l = .3;
	float c = TMath::ATan(r/ab);
	float d = TMath::ATan(-r/ab);
	float e = TMath::ATan(r/l);
	const int k= 10;
	float z[k];
	float a[nrEvents];
	float amax[nrEvents];
	float abs[nrEvents];
	float crit[nrEvents];
	float exp[nrEvents];
	float phi[nrEvents];
	TH2F *hit[k];
	TH2F *miss[k];
	TH2F *kasten[k];
	char *hitname = new char[10];
	char *missname = new char[10];
	char *kastenname = new char[10];

	
	
	for (int j = 0; j<k; j++){
		sprintf(hitname,"hit%d",j);
		hit[j] = new TH2F(hitname,"",400,xmin,xmax,400,ymin,ymax);
		hit[j]->SetMarkerColor(kRed);
		sprintf(missname,"miss%d",j);
		miss[j] = new TH2F(missname,"",400,xmin,xmax,400,ymin,ymax);
		miss[j]->SetMarkerColor(kBlue);
		sprintf(kastenname,"kasten%d",j);
		kasten[j] = new TH2F(kastenname,"",400,xmin,xmax,400,ymin,ymax);
		kasten[j]->SetMarkerColor(kGreen);
		
	for (Int_t i=0; i<nrEvents; i++) { 
		x[i]=x1->Uniform(xmin,xmax); //(xmin,xmax);
		y[i]=y1->Uniform(ymin,ymax); //(ymin,ymax);
		abs[i] = sqrt( y[i]**2 + x[i]**2);
		crit[i] = z1->Uniform(zmin,zmax);
		
		phi[i]=TMath::ATan(y[i]/x[i]);
		a[i]=  abs[i] -ab/TMath::Cos(phi[i]);
		if (x[i]>=0.1 && phi[i]>=d && phi[i] <=c && r/TMath::Abs( TMath::Sin(phi[i])) >=abs[i] && x[i] <l ){
			exp[i] = 1 -.5**(a[i]/.1);
			if ( exp[i] >crit[i])
				hit[j]->Fill(x[i],y[i]);
			else
				miss[j]->Fill(x[i],y[i]);
		}
		else if (x[i]>=l && phi[i]>=d && phi[i] <=c && r/TMath::Abs(TMath::Sin(phi[i])) >=abs[i] ){
		amax[i]=  (l -ab)/TMath::Cos(phi[i]);
		exp[i] = 1 -.5**(TMath::Abs(amax[i])/.1);

			if ( exp[i] >crit[i])
				hit[j]->Fill(x[i],y[i]);
			else
				miss[j]->Fill(x[i],y[i]);
		}
	else if (x[i]>=.1 && (phi[i])>=d && phi[i] <=c && r/TMath::Abs(TMath::Sin(phi[i])) <abs[i] && TMath::Abs(phi[i]) >=e){
		amax[i]=  r/TMath::Abs(TMath::Sin(phi[i])) -ab/TMath::Cos(phi[i]);
		exp[i] = 1 -.5**(TMath::Abs(amax[i])/.1);

			if ( exp[i] >crit[i])
				hit[j]->Fill(x[i],y[i]);
			else
				miss[j]->Fill(x[i],y[i]);
	}
	else if (x[i]>=.1 && (phi[i])>=d && phi[i] <=c && r/TMath::Abs(TMath::Sin(phi[i])) <abs[i] && TMath::Abs(phi[i]) <e){
		amax[i]=  (l -ab)/TMath::Cos(phi[i]);
		exp[i] = 1 -.5**(TMath::Abs(amax[i])/.1);

			if ( exp[i] >crit[i])
				hit[j]->Fill(x[i],y[i]);
			else
				miss[j]->Fill(x[i],y[i]);
	}
	else 
		miss[j]->Fill(x[i],y[i]);
	if (x[i]>=.095 && x[i] <= .1 && y[i] < .05 && y [i] > -.05 && phi[i]>=d && phi[i]<=c) 
		kasten[j]->Fill(x[i],y[i]);
	else if (x[i]>=.3 && x[i] <= .3005 && y[i] < .05 && y [i] > -.05 && phi[i]>=d && phi[i]<=c) 
		kasten[j]->Fill(x[i],y[i]);
	else if (x[i]>=.095 && x[i] <= .3005 && y[i] < .051 && y [i] > .05 && phi[i]>=d && phi[i]<=c) 
		kasten[j]->Fill(x[i],y[i]);
	else if (x[i]>=.095 && x[i] <= .3005 && y[i] < -.05 && y [i] > -.051 && phi[i]>=d && phi[i]<=c) 
		kasten[j]->Fill(x[i],y[i]);
			}
		z[j]=hit[j]->GetEntries()/nrEvents;
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
	cout << zmean1 <<"+- " << abw << endl;
	gStyle->SetOptStat(000);
	c = new TCanvas("c","c",200,9,700,700);
	hit[0]->Draw();
	miss[0]->Draw("SAME");
	kasten[0]->Draw("SAME");
}


/*
c: 50% teilchen nach 10cm im zählrohr ~> WK: 0.5 ** (strecke / 10 cm)



*/