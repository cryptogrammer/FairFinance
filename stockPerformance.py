''' Code template from QSTK tutorial used.'''

import QSTK.qstkutil.qsdateutil as du
import QSTK.qstkutil.tsutil as tsu
import QSTK.qstkutil.DataAccess as da
import datetime as dt
import matplotlib.pyplot as plt
import pandas as pd
import sys
import numpy as np
import math
import itertools
import pickle

def simulate(dt_start, dt_end, ls_symbols, alloc):
    print ("VERY IMPORTANT")
    dt_timeofday = dt.timedelta(hours=16)
    ldt_timestamps = du.getNYSEdays(dt_start, dt_end, dt_timeofday)
    c_dataobj = da.DataAccess('Yahoo')
    ls_keys = ['open', 'high', 'low', 'close', 'volume', 'actual_close']
    ldf_data = c_dataobj.get_data(ldt_timestamps, ls_symbols, ls_keys)
    d_data = dict(zip(ls_keys, ldf_data))
    d_data = d_data['actual_close']
    print d_data
    d_data = d_data.fillna(method='ffill')
    d_data = d_data.fillna(method='bfill')
    d_data = d_data.fillna(1.0)
    temp_data = d_data.values

    print temp_data
    normalized = temp_data/temp_data[0, :]
    for allocIndex in range(len(ls_symbols)):
        normalized[:, allocIndex] = normalized[:, allocIndex]*alloc[allocIndex]
    cumulative_return = normalized.sum(axis = 1)
    returns = [0]
    for i in range(1, len(cumulative_return)):
        returns.append(cumulative_return[i]/cumulative_return[i-1] - 1)
    daily_return = np.mean(returns)
    std_dev = np.std(returns)
    sharpe = 1.0*math.sqrt(252)*daily_return/std_dev
    final_cumulative_return = cumulative_return[-1]
    return std_dev, daily_return ,sharpe, final_cumulative_return


def main():
    ls_symbols = []
    ls_performance = {}
    ls_final_performance = {}
    ls_sorted = {}
    for i in range(7,len(sys.argv)):    
	ls_symbols.append(sys.argv[i])
    dt_start = dt.datetime(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]))
    dt_end = dt.datetime(int(sys.argv[4]), int(sys.argv[5]), int(sys.argv[6]))
        
    alloc = [1.0]
    print("IN MAIN")
    for k in ls_symbols: 
    	max_sharpe, final_std_dev, final_daily_return, final_cumulative_return = 0,0,0,0
   	std_dev, daily_return, sharpe, cumulative_return = simulate(dt_start, dt_end, [k], alloc)
        ls_performance[k] = [sharpe, std_dev, cumulative_return, daily_return]
	print("OIE")
	print sharpe
	ls_sorted[sharpe] = k
    keylist = ls_sorted.keys()
    keylist.sort()
    newKeyList = []
    for i in range(1,len(keylist)+1):
	newKeyList.append(keylist[len(keylist) -i])
    print newKeyList
    maxNumStocks = 10
    numStocks = maxNumStocks
    f = open('optimalStocks', 'w')
    for m in newKeyList:
	if(numStocks > 0 and  m > 1):
		ls_final_performance[ls_sorted[m]] = [ls_performance[ls_sorted[m]]]
        	numStocks = numStocks -1
	f.write(str(ls_sorted[m]) + '\n')
    f.close()
    print ls_final_performance
    fk = open('numOptimal', 'w')
    x = maxNumStocks-numStocks
    fk.write(str(x))
    fk.close()
    print("FINAL CUMULATIVE RETURN")
    print(cumulative_return)
if __name__ == '__main__':
    main()
