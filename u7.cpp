//import time

/*
def func_test(x):
    return x**2
	*/
void u7(){
  //  #start runtime measurement
   // start = time.time()


//	TH1->SetDefaultSumw2(True);
//	gStyle->SetOptStat(000);

//	c = new TCanvas("c","c",200,9,700,500);
	
//	gROOT->SetBatch();
	/*

  //  # Define 2D histograms for hit and miss and use different colors
  //  borders = [[0.,1.],[0.,1.]];
    histtitle = "A meaningful title";
    hithist = TH2F("hist_hit", histtitle, 1000,//borders[0][0],borders[0][1],
                      1000
          //            borders[1][0],
         //             borders[1][1])
		 );
    hithist.SetMarkerColor(kGreen)

    misshist =TH2F("hist_miss",
                       histtitle,
                       1000,
             //          borders[0][0],
           //            borders[0][1],
                       1000);
         //              borders[1][0],
       //                borders[1][1])
    misshist.SetMarkerColor(kRed)
	/*
   // # Create random number generator with seed 123
    rand = TRandom3(123)

   // # Dice a pair of uniform distributed random numbers between 0 and 1.
 //   x = rand.Rndm(); // # Zufallszahl
//	cout << x << endl;
  //  y = rand; //# Zufallszahl
//	cout << x << " " << y<< endl;
   // # Fill the random numbers in hithist if condition is true or in
   // # misshist otherwise
    if func_test(#Argument) #Bedingung:
        hithist.Fill( x, y )
    else:
        misshist.Fill( x, y )

   // # Draw both hists in same canvas
    hithist.Draw()
    misshist.Draw("same")
	*/
   // #save the canvas to a pdf file
    /*
	const int n = 10;
	const int k = n;
	float x[k];
	float y[k];
	x[0]=0;
	y[0]=1/2f;


	for (int i=1; i<k; i++){
		x[i]=i;
		y[i]=y[i-1]+1/2f;
	}
	
		gr = new TGraph(n,x,y);
		gr->Draw("AP");*/
    //end = time.time()
    //print "Runtime %.2fs" %(end - start)

	TRandom3 rdm(111);
	r.Rndm();

	cout << r << endl;


}
