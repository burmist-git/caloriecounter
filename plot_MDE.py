#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Date        : Tue Dec 29 14:22:36 CET 2020
Autor       : Leonid Burmistrov
Description : Simple reminder-training example.
'''

import numpy as np
import matplotlib.pyplot as plt
from optparse import OptionParser

def getHistBins(nBins,xMin,xMax):
    binW = (xMax - xMin)/nBins
    return [xMin + binW*i for i in range(nBins+1)]

def plot(dataM,dataD,dataE,dataT):
    #
    nBins = 50
    xMin = 0
    xMax = 5000
    bins = getHistBins(nBins,xMin,xMax)
    #
    print('Morning : {:,.2f} +/- {:,.2f}'.format(np.mean(dataM),np.std(dataM)))
    print('Day     : {:,.2f} +/- {:,.2f}'.format(np.mean(dataD),np.std(dataD)))
    print('Evening : {:,.2f} +/- {:,.2f}'.format(np.mean(dataE),np.std(dataE)))
    print('Total   : {:,.2f} +/- {:,.2f}'.format(np.mean(dataT),np.std(dataT)))
    #
    fig, axs = plt.subplots( nrows=1, ncols=2,
                             sharex=False, sharey=False,
                             squeeze=True, subplot_kw=None,
                             gridspec_kw=None,
                             figsize=(12,6))
    plt.tight_layout()
    axs[0].hist(dataM, bins=bins, alpha=0.5)
    axs[0].hist(dataD, bins=bins, alpha=0.5)
    axs[0].hist(dataE, bins=bins, alpha=0.5)
    axs[1].hist(dataT, bins=bins)        
    #
    fig2, axs2 = plt.subplots( nrows=1, ncols=3,
                               sharex=False, sharey=False,
                               squeeze=True, subplot_kw=None,
                               gridspec_kw=None,
                               figsize=(18,6))
    plt.tight_layout()
    axs2[0].hist(dataM, bins=bins)
    axs2[1].hist(dataD, bins=bins)
    axs2[2].hist(dataE, bins=bins)    
    #
    plt.show()
    
def main():
    if (len(args) < 1) :
        parser.print_help()
    elif (len(args) != (options.morning + options.day + options.evening + options.total)):
        print('ERROR in input format :')
        parser.print_help()
    else:
        data=np.array(list(map(int,np.array(args))))
        #print(options)
        #print(data)
        dataM=data[0:options.morning]
        dataD=data[options.morning:(options.morning + options.day)]
        dataE=data[(options.morning + options.day):(options.morning + options.day + options.evening)]
        dataT=data[(options.morning + options.day + options.evening):]
        plot(dataM,dataD,dataE,dataT)
        
parser = OptionParser()
parser.add_option('-m', '--morning',
                  dest='morning', type="int",default=30,
                  help="number of entries for morning calories")
parser.add_option('-d', '--day',
                  dest='day', type="int",default=30,
                  help="number of entries for day calories")
parser.add_option('-e', '--evening',
                  dest='evening', type="int",default=30,
                  help="number of entries for evening calories")
parser.add_option('-t', '--total',
                  dest='total', type="int",default=30,
                  help="number of entries for total calories")
(options, args) = parser.parse_args()
    
if __name__ == "__main__":
    main()
