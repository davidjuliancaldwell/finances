import numpy as np
import matplotlib.pylab as plt
import seaborn as sns
sns.set()

pv=1000
r=0.08
n=20

t=np.linspace(0,n-1,n)
fv_1=np.ones(len(t))*pv
fv_2=pv*(1+r*t) #simple interest
fv_3=pv*(1+r)**t


fv_1plot = plt.plot(t,fv_1,'b-',label='Under your pillow')
fv_2plot = plt.plot(t,fv_2,'g-',label='Simple Interest')
fv_3plot = plt.plot(t,fv_3,'r-',label='Compound Interest')
#plt.plot(t,examp4,'m-')
plt.title("One time investment of $1000 \n Simple vs. Compounded Interest Rate, 8%")
plt.xlabel("Number of Years, t")
plt.ylabel("US Dollars")
plt.xlim(0,21)
plt.ylim(0,5000)
plt.legend()
#plt.show()
plt.savefig('finance_int_compound.png', dpi=600)


pmt = -1000
fv = -1000
pv=1000
r=0.08
n=20
rate1 = 0.001
rate2 = 0.08
nper = np.arange(0,n)
examp4 = np.fv(0, nper, pmt, fv, when = 'begin')
examp5 = np.fv(rate1,nper,pmt,fv,when='begin')
examp6 =  np.fv(rate2, nper, pmt, fv, when = 'begin')
examp4plot = plt.plot(t,examp4,'b-',label='Under your pillow')
examp5plot = plt.plot(t,examp5,'g-',label='Money into bank and bank return rate')
examp6plot = plt.plot(t,examp6,'r-',label='Annual investment and compound interest')

plt.title("Compound Interest on Yearly Investment 8% return \n  vs. Placed in Bank 0.1%")
plt.xlabel("Number of Years, t")
plt.ylabel("US Dollars")
plt.xlim(0,21)
plt.ylim(0,60000)
plt.legend()
#plt.show()
plt.savefig('finance_yearly_invest.png', dpi=600)
