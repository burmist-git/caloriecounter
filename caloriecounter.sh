#!/bin/bash

########################################################################
# Date        : Thu Nov 26 18:04:31 CET 2020                           #
# Autor       : Leonid Burmistrov                                      #
# Description :                                                        #
########################################################################

LC_TIME=en_US.UTF-8
LANG=en_US.UTF-8

source /home/burmist/root_v6.14.00/root-6.14.00-install/bin/thisroot.sh

function push_sh {
    vecparID=0
    $sourceHome/push 0 $outRootFile $vecparID 1 $1
}

function plot_sh {
    $sourceHome/plot 0 $inRootFile $vecNamesFile
    evince $inRootFile".pdf" &
}

function ldd_info_sh {
    echo "Info --> ldd push"
    ldd push
    echo "Info --> ldd plot"
    ldd plot
}

function printHelp {
    echo " --> ERROR in input arguments "
    echo " [0] -push   : example of the push "
    echo " [1]         : weight "
    echo " [2]         : size "
    echo " [0] -plot   : example of the plot "
    echo " [0] -ldd    : print ldd info "
    echo " [0] -h      : print help"
}

sourceHome=$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )
dataFolder=$sourceHome'/data/'
outRootFile=$dataFolder'caloriecounter.root'
inRootFile=$outRootFile
vecNamesFile=$sourceHome'/vectorOfinDataValuesNames.dat'

mkdir -p $dataFolder

if [ $# -eq 0 ]; then    
    printHelp
else
    if [ "$1" = "-push" ]; then
	if [ $# -eq 2 ]; then
	    calories=$2
	    push_sh $calories
	else
            printHelp
        fi
    elif [ "$1" = "-plot" ]; then
	plot_sh
    elif [ "$1" = "-ldd" ]; then
	ldd_info_sh
    elif [ "$1" = "-h" ]; then
        printHelp
    else
        printHelp
    fi
fi
#espeak "I have done"
