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
    
def plot_errorbar():
    fig = plt.figure()
    x = np.arange(10)
    y = 2.5 * np.sin(x / 20 * np.pi)
    yerr = np.linspace(0.05, 0.2, 10)
    
    plt.errorbar(x, y + 3, yerr=yerr, label='both limits (default)')
    
    plt.errorbar(x, y + 2, yerr=yerr, uplims=True, label='uplims=True')
    
    plt.errorbar(x, y + 1, yerr=yerr, uplims=True, lolims=True,
                 label='uplims=True, lolims=True')
    
    upperlimits = [True, False] * 5
    lowerlimits = [False, True] * 5
    plt.errorbar(x, y, yerr=yerr, uplims=upperlimits, lolims=lowerlimits,
                 label='subsets of uplims and lolims')
    
    plt.legend(loc='lower right')    
    
    plt.show()

def plot_scatter():
    
    np.random.seed(19680801)
    x = np.random.random(100)*5
    y = np.random.random(100)*5

    fig = plt.figure(num=None, figsize=None, dpi=None, facecolor=None,
                     edgecolor=None, frameon=True, clear=False)
    fig.add_axes([0.1, 0.1, 0.85, 0.85])
    
    plt.scatter(x, y, s=None, c=None, marker=None, cmap=None, norm=None,
                vmin=None, vmax=None, alpha=None, linewidths=None,
                edgecolors=None, plotnonfinite=False, data=None)

    plt.title('The title')
    plt.xlim(-0.5, 5.5)
    plt.ylim(-0.5, 5.5)
    plt.xlabel('The x lable')
    plt.ylabel('The y lable')
    plt.show()

def plot_subplot01():

    np.random.seed(19680801)
    x1 = np.random.random(100)*5
    y1 = np.random.random(100)*5
    x2 = np.random.random(100)*5
    y2 = np.random.random(100)*5

    # using the variable axs for multiple Axes
    fig, axs = plt.subplots( nrows=2, ncols=1,
                             sharex=False, sharey=False,
                             squeeze=True, subplot_kw=None,
                             gridspec_kw=None,
                             figsize=(10,12))
    #plt.tight_layout()

    # 
    axs[0].plot(x1, y1)
    axs[0].set_xbound(-0.5,5.5)
    axs[0].set_ybound(-0.5,5.5)
    axs[0].set_title('The title 0')
    axs[0].set_xlabel('The x lable 0')
    axs[0].set_ylabel('The y lable 0')
    axs[0].set_position([0.05,0.55,0.9,0.40])
    #
    axs[1].scatter(x2, y2)
    axs[1].set_xbound(-0.5,5.5)
    axs[1].set_ybound(-0.5,5.5)
    axs[1].set_title('The title 1')
    axs[1].set_xlabel('The x lable 1')
    axs[1].set_ylabel('The y lable 1')
    axs[1].set_position([0.05,0.05,0.9,0.40])
    #
    print(type(axs))
    print(type(axs[0]))
    
    plt.show()    



def plot_hist():

    classType = [0,1]
    nn    = [10000,1000]
    x0    = [10,11]
    sigma = [0.1,0.1]
    
    '''
    classType = [0,1,2,3,4]
    nn    = [100,500,1000,5000,10000]
    x0    = [0,1,2,3,4]
    sigma = [0.3,0.3,0.8,0.2,10.0]
    '''
    
    nPlots=len(nn) + 2
    ncols=math.ceil(nPlots**(0.5))
    nrows=int(nPlots/ncols)+math.ceil(nPlots/ncols-int(nPlots/ncols))
    print(ncols)
    print(nrows)
    
    nBins = 300
    nSigma = 4
    xMin = int(np.array(x0).min() - math.ceil(nSigma*np.array(sigma).max()))
    xMax = int(np.array(x0).max() + math.ceil(nSigma*np.array(sigma).max()))
    #xMin = 8
    #xMax = 12
    bins = getHistBins(nBins,xMin,xMax)
    print(len(bins))
    print(xMin)
    print(xMax)
    print(nSigma*np.array(sigma).max())
    
    data = generateHistData(nn,x0,sigma)
    datay = [classType[i]*np.ones(nn[i]) for i in range(len(x0))]
    
    # using the variable axs for multiple Axes
    
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
