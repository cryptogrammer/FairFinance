import os, sys
import pickle, itertools

os.system("python stockPerformance.py 2014 1 1 2015 1 1 A AA AAPL ABBV ABC ABT ACE ACN ACT ADBE ADI ADM ADP ADS ADSK ADT AEE AEP AES AET AFL AGN AIG AIV AIZ AKAM ALL ALLE ALTR ALXN AMAT AME AMG AMGN AMP AMT AMZN AN ANTM AON APA APC APD APH ARG ATI AVB AVGO AVP AVY AXP AZO BA BAC BAX BBBY BBT BBY BCR BDX BEN BF/B BHI BIIB BK BLK BLL BMY BRCM BRK/B BSX BWA BXP C CA CAG CAH CAM CAT CB CBG CBS CCE CCI CCL CELG CERN CF CFN CHK CHRW CI CINF CL CLX CMA CMCSA CME CMG CMI CMS CNP CNX COF COG COH COL COP COST COV CPB CRM CSC CSCO CSX CTAS CTL CTSH CTXS CVC CVS CVX D DAL DD DE DFS DG DGX DHI DHR DIS DISCA DISCK DLPH DLTR DNB DNR DO DOV DOW DPS DRI DTE DTV DUK DVA DVN EA EBAY ECL ED EFX EIX EL EMC EMN EMR EOG EQR EQT ESRX ESS ESV ETFC ETN ETR EW EXC EXPD EXPE F FAST FB FCX FDO FDX FE FFIV FIS FISV FITB FLIR FLR FLS FMC FOSL FOXA FSLR FTI FTR GAS GCI GD GE GGP GILD GIS GLW GM GMCR GME GNW GOOG GOOGL GPC GPS GRMN GS GT GWW HAL HAR HAS HBAN HCBK HCN HCP HD HES HIG HOG HON HOT HP HPQ HRB HRL HRS HSP HST HSY HUM IBM ICE IFF INTC INTU IP IPG IR IRM ISRG ITW IVZ JCI JEC JNJ JNPR JOY JPM JWN K KEY KIM KLAC KMB KMI KMX KO KORS KR KRFT KSS KSU L LB LEG LEN LH LLL LLTC LLY LM LMT LNC LO LOW LRCX LUK LUV LVLT LYB M MA MAC MAR MAS MAT MCD MCHP MCK MCO MDLZ MDT MET MHFI MHK MJN MKC MLM MMC MMM MNK MNST MO MON MOS MPC MRK MRO MS MSFT MSI MTB MU MUR MWV MYL NAVI NBL NBR NDAQ NE NEE NEM NFLX NFX NI NKE NLSN NOC NOV NRG NSC NTAP NTRS NU NUE NVDA NWL NWSA OI OKE OMC ORCL ORLY OXY PAYX PBCT PBI PCAR PCG PCL PCLN PCP PDCO PEG PEP PETM PFE PFG PG PGR PH PHM PKI PLD PLL PM PNC PNR PNW POM PPG PPL PRGO PRU PSA PSX PVH PWR PX PXD QCOM QEP R RAI RCL REGN RF RHI RHT RIG RL ROK ROP ROST RRC RSG RTN SBUX SCG SCHW SE SEE SHW SIAL SJM SLB SNA SNDK SNI SO SPG SPLS SRCL SRE STI STJ STT STX STZ SWK SWN SWY SYK SYMC SYY T TAP TDC TE TEG TEL TGT THC TIF TJX TMK TMO TRIP TROW TRV TSCO TSN TSO TSS TWC TWX TXN TXT TYC UA UHS UNH UNM UNP UPS URBN URI USB UTX V VAR VFC VIAB VLO VMC VNO VRSN VRTX VTR VZ WAT WBA WDC WEC WFC WFM WHR WIN WM WMB WMT WU WY WYN WYNN XEC XEL XL XLNX XOM XRAY XRX XYL YHOO YUM ZION ZMH ZTS > test.txt")
print("STOCK PERFORMANCE DONE")
ls_safe_stocks = []
f = open('numOptimal', 'r')
k = int(f.readline())
f.close()
f = open('optimalStocks','r')
for i in range(k):
	ls_safe_stocks.append((f.readline()).replace("\n",""))
f.close()
print ls_safe_stocks
print len(ls_safe_stocks)
NUMSTOCKSINAPORTFOLIO = 4
possibleCombinations = list(itertools.combinations(ls_safe_stocks,NUMSTOCKSINAPORTFOLIO))
uniqueCombinations = []
for comb in possibleCombinations:
         uniqueCombinations.append(comb)
print("COMBINATION DONE")
## Allocations
f = open('allocationNumbers', 'w')
f.write('')
f.close()
for perm in uniqueCombinations:
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
for k in range(len(uniqueCombinations)):
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
for k in range(len(uniqueCombinations)):
	tempData = f.readline()
	stocks = tempData[0:tempData.index('(')-1]
	allocations = tempData[tempData.index('(')+1:tempData.index(')')]
	allocations = allocations.replace(",","")
	os.system("python threeMonthAnalysis.py 2014 9 1 2015 1 1 " + stocks + " " + allocations)
print("3 DONE")

twoYearSharpe = []

f = open('two_year_sharpe', 'r')
for k in range(len(uniqueCombinations)):
	temp = f.readline()
	print temp
	twoYearSharpe.append(float(temp))
f.close()

threeMonthSharpe = []
threeMonthVolatility = []

f = open('three_month_analysis', 'r')
for k in range(len(uniqueCombinations)):
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
print("STOCK PORTFOLIOS")
print uniqueCombinations
