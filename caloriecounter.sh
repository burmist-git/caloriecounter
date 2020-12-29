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

#|  Fri Nov 27 11:25:26 CET 2020  |  M: 120 kCal                                        |
#|                                |  D: 1041 kCal                                       |
#|                                |  E: 1096 kCal                                       |
#|                                |                                                     |
#|                                |  TOTAL: 2257 kCal                                   |
function plot_py_sh {
    wcl=$(conda env list | grep $condaEvnName | wc -l)
    if [ $wcl = 0 ]; then
	create_conda_env_sh
    else
	consumption_Morning=$(grep M: $consumptionLog | awk {'print $10'} | grep -v kCal | xargs)
	conM_n=$(grep M: $consumptionLog | awk {'print $10'} | grep -v kCal | wc -w)
	consumption_Day=$(grep D: $consumptionLog | awk {'print $4'} | grep -v kCal | xargs)
	conD_n=$(grep D: $consumptionLog | awk {'print $4'} | grep -v kCal | wc -w)
	consumption_Evening=$(grep E: $consumptionLog | awk {'print $4'} | grep -v kCal | xargs)
	conE_n=$(grep E: $consumptionLog | awk {'print $4'} | grep -v kCal | wc -w)
	consumption_Total=$(grep TOTAL: $consumptionLog | awk {'print $4'} | grep -v kCal | xargs)
	conT_n=$(grep TOTAL: $consumptionLog | awk {'print $4'} | grep -v kCal | wc -w)
	#echo $consumption_Morning
	#echo $consumption_Day
	#echo $consumption_Evening
	#echo $consumption_Total
	#echo $conM_n
	#echo $conD_n
	#echo $conE_n
	#echo $conT_n
	python plot_MDE.py -m $conM_n -d $conD_n -e $conE_n -t $conT_n $consumption_Morning $consumption_Day $consumption_Evening $consumption_Total	
    fi
}

function ldd_info_sh {
    echo "Info --> ldd push"
    ldd push
    echo "Info --> ldd plot"
    ldd plot
}

function create_conda_env_sh {
    wcl=$(conda env list | grep $condaEvnName | wc -l)
    if [ $wcl = 0 ]; then
	conda create --name $condaEvnName -y numpy matplotlib
	conda env list | grep $condaEvnName
	echo "> conda activate $condaEvnName"
    else
	conda env list | grep $condaEvnName
	echo "> conda activate $condaEvnName"
    fi
}

function printHelp {
    echo " --> ERROR in input arguments "
    echo " [0] -push   : example of the push "
    echo " [1]         : weight "
    echo " [2]         : size "
    echo " [0] -plot   : example of the plot "
    echo " [0] -plotpy : plots consumption info histograms with python  "
    echo " [0] -create : create conda env "
    echo " [0] -ldd    : print ldd info "
    echo " [0] -h      : print help"
}

sourceHome=$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )
dataFolder=$sourceHome'/data/'
outRootFile=$dataFolder'caloriecounter.root'
inRootFile=$outRootFile
vecNamesFile=$sourceHome'/vectorOfinDataValuesNames.dat'
consumptionLog=$sourceHome'/consumption.md'
condaEvnName='calories'


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
    elif [ "$1" = "-plotpy" ]; then
	plot_py_sh
    elif [ "$1" = "-create" ]; then
	create_conda_env_sh
    elif [ "$1" = "-ldd" ]; then
	ldd_info_sh
    elif [ "$1" = "-h" ]; then
        printHelp
    else
        printHelp
    fi
fi
#espeak "I have done"
