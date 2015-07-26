void u8b1()
{
	const int nrEvents=100000;
	
	TRandom3 *x1=new TRandom3();
	x1->SetSeed(0);
	TRandom3 *y1=new TRandom3();
	y1->SetSeed(0);
	float x[nrEvents];
	float y[nrEvents];
	float z[nrEvents];
	float xmin = -1;
	float xmax = 1;
	float ymin = -1;
	float ymax = 1;
	float a = 0;
	float c = TMath::ATan(0.05/0.10);
	float d = TMath::ATan(-0.05/0.10);
	const int k= 10;
	float z[k];
	TH2F *hit[k];
	TH2F *miss[k];
	char *hitname = new char[10];
	char *missname = new char[10];

	
	
	for (int j = 0; j<k; j++){
		sprintf(hitname,"hit%d",j);
		hit[j] = new TH2F(hitname,"",400,xmin,xmax,400,ymin,ymax);
		hit[j]->SetMarkerColor(kRed);
		sprintf(missname,"miss%d",j);
		miss[j] = new TH2F(missname,"",400,xmin,xmax,400,ymin,ymax);
		miss[j]->SetMarkerColor(kBlue);
		
	for (Int_t i=0; i<nrEvents; i++) { 
		x[i]=x1->Uniform(xmin,xmax); //(xmin,xmax);
		y[i]=y1->Uniform(ymin,ymax); //(ymin,ymax);
	
		
		a=TMath::ATan(y[i]/x[i]);
		if (x[i]>=0.1 && a>=d && a <=c)
		hit[j]->Fill(x[i],y[i]);
		else
		miss[j]->Fill(x[i],y[i]);
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
	hit[1]->Draw();
	miss[1]->Draw("SAME");
}

