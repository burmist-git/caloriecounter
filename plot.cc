/***********************************************************************
* Date        : Thu Nov 26 18:04:31 CET 2020                           *
* Autor       : Leonid Burmistrov                                      *
* Description :                                                        *
***********************************************************************/

//my
#include "libpushVectorInRoot.h"

//root
#include "TROOT.h"
#include "TStyle.h"
#include "TString.h"
#include "TH1D.h"
#include "TH2D.h"
#include "TFile.h"
#include "TRandom3.h"
#include "TGraph.h"
#include "TCanvas.h"
#include "TMultiGraph.h"
#include "TGaxis.h"

//C, C++
#include <iostream>
#include <stdlib.h>
#include <assert.h>
#include <fstream>
#include <iomanip>
#include <time.h>

using namespace std;

int main(int argc, char *argv[]){
  if(argc == 4 && atoi(argv[1])==0){
    TString rootFileIn = argv[2];
    TString vecNamesFile = argv[3];
    Int_t saveKey = 1;
    Double_t timeAxisLabelOffset = 0.02;
    std::vector<TGraph*> gr_v = getGraphsVector (rootFileIn, vecNamesFile, saveKey);
    //
    Double_t v_min = 0;
    Double_t v_max = 5000;
    TCanvas *c1 = new TCanvas("c1","c1",10,10,1200,800);
    gStyle->SetPalette(1);
    gStyle->SetFrameBorderMode(0);
    gROOT->ForceStyle();
    gStyle->SetStatColor(kWhite);
    c1->SetRightMargin(0.12);
    c1->SetLeftMargin(0.12);
    c1->SetTopMargin(0.1);
    c1->SetBottomMargin(0.15);
    c1->SetGrid();
    //
    gr_v.at(0)->SetTitle("Calories counter");
    gr_v.at(0)->SetLineColor(kRed);
    gr_v.at(0)->SetMarkerColor(kRed);
    gr_v.at(0)->SetMarkerStyle(20);
    gr_v.at(0)->SetLineStyle(kSolid);
    gr_v.at(0)->SetMinimum(v_min);
    gr_v.at(0)->SetMaximum(v_max);
    gr_v.at(0)->Draw("APL");
    gr_v.at(0)->GetYaxis()->SetTitle("Calories, kCal");  
    gr_v.at(0)->GetXaxis()->SetTimeDisplay(1);
    gr_v.at(0)->GetXaxis()->SetTimeFormat("#splitline{%m/%d}{%H:%M}%F1970-01-01 00:00:00");
    gr_v.at(0)->GetXaxis()->SetLabelOffset(timeAxisLabelOffset);
    //
    TString pdfOutFile = rootFileIn;
    pdfOutFile += ".pdf";
    c1->SaveAs(pdfOutFile.Data());
  }
  else{
    cout<<" --> ERROR in input arguments "<<endl
	<<" runID [1] = 0 (execution ID number)"<<endl
      	<<"       [2] - rootFileIn"<<endl
	<<"       [3] - vecNamesFile"<<endl;
  }
  return 0;
}
