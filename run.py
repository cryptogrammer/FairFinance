import os, sys
import pickle, itertools

os.system("python stockPerformance.py 2014 1 1 2015 1 1 AAPL ADP MSFT FB > test.txt")
print("STOCK PERFORMANCE DONE")
ls_safe_stocks = []
f = open('numOptimal', 'r')
k = int(f.readline())
f.close()
f = open('optimalStocks','r')
for i in range(k):
	ls_safe_stocks.append((f.readline()).replace("\n",""))
f.close()
NUMSTOCKSINAPORTFOLIO = 4
#possibleCombinations = list(itertools.combinations(ls_safe_stocks,NUMSTOCKSINAPORTFOLIO))
#uniqueCombinations = []
#for comb in possibleCombinations:
#         uniqueCombinations.append(comb)
print("COMBINATION DONE")
## Allocations
f = open('allocationNumbers', 'w')
f.write('')
f.close()
#for perm in uniqueCombinations:
perm = ls_safe_stocks
temp = ""
temp  = temp + str(perm) + " "
temp = temp[0:len(temp)-1]
temp = temp.replace("(","")
temp = temp.replace("\'","")
temp = temp.replace(",","")
temp = temp.replace(")","")
temp = temp.replace("]","")
temp = temp.replace("[","")
os.system("python allocation.py 2014 1 1 2015 1 1 " + str(temp))
print("ALLOCATION DONE")

## 2 Year Sharpe

f = open('two_year_sharpe', 'w')
f.write('')
f.close()

f = open('allocationNumbers', 'r')
#for k in range(len(uniqueCombinations)):
tempData = f.readline()
print tempData
stocks = tempData[0:tempData.index('(')-1]
allocations = tempData[tempData.index('(')+1:tempData.index(')')]
allocations = allocations.replace(",","")
os.system("python twoYearSharpe.py 2013 1 1 2015 1 1 " + stocks + " " + allocations)
print("2 DONE")


## 3 Month Sharpe and Volatility

f = open('three_month_analysis', 'w')
f.write('')
f.close()

f = open('allocationNumbers', 'r')
#for k in range(len(uniqueCombinations)):
tempData = f.readline()
stocks = tempData[0:tempData.index('(')-1]
allocations = tempData[tempData.index('(')+1:tempData.index(')')]
allocations = allocations.replace(",","")
os.system("python threeMonthAnalysis.py 2014 9 1 2015 1 1 " + stocks + " " + allocations)
print("3 DONE")

twoYearSharpe = []

f = open('two_year_sharpe', 'r')
#for k in range(len(uniqueCombinations)):
temp = f.readline()
twoYearSharpe.append(float(temp))
f.close()

threeMonthSharpe = []
threeMonthVolatility = []

f = open('three_month_analysis', 'r')
#for k in range(len(uniqueCombinations)):
temp = f.readline()
sharpe = temp[0:temp.index(',')]
volatility = temp[temp.index(',')+1:]
threeMonthSharpe.append(float(sharpe))
threeMonthVolatility.append(float(volatility))
f.close()

print("TWO YEAR SHARPE")
print twoYearSharpe
print("\n\nTHREE MONTH SHARPE")
print threeMonthSharpe
print("Volatility")
print threeMonthVolatility
