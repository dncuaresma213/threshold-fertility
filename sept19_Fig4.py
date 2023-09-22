#------------------------------------------------------------------------------
# This python code was used to generate Figure 4.
# This figure shows histogram of the number of generations lived of simulated population.  
#------------------------------------------------------------------------------

# Imporating libraries
import matplotlib.pyplot as plt
import numpy as np
import statistics as st

# Declaring variables
gen = 50                            #max number of generations
rep = 10000                         #number of replications
maxP= 10000                         #max population
Pop = []                            #list for population
N = []                              #number of offspring per female per generation
M = []                              #number of male offpsring per female
F = []                              #number of female offspring

# Assuming no mortalities, and equal number of females and males
mm=0; mf=0; r=0.5

# Number of bins
B= range(0,gen+1,5)


#------------------------------------------------------------------------------
# Figure 4 (a)
# This panel shows the histogram for b=1.5.   
#------------------------------------------------------------------------------

b=1.5
Tex = []                            #list for time to extinction

for s in range(0,rep) :             #number of replications
    Pop.clear()
    Pop.append(1)                   #single female at generation 0
    for t in range(1,gen+2) :
        if Pop[t-1] == 0 : N.append(0), M.append(0), F.append(0)
        else:
            for i in range(0,Pop[t-1]):
                N.append(np.random.poisson(lam=b))                             #number of offspring per female
                dMi = N[i]
                Mb = np.random.binomial(n=dMi,p=r)
                Fb = N[i]-Mb
                M.append(Mb*(1-mm))                                            #surviving number of males
                F.append(Fb*(1-mf))                                            #surviving number of females                F.append(np.random.binomial(n=Fb,p=1-mf))                      #surviving number of females
        if sum(M) == 0 : Pop.append(0)
        else: Pop.append(min(maxP,sum(F))) 
        N.clear(), M.clear(), F.clear()
        if Pop[t] == 0 and Pop[t-1] > 0 : Tex.append(t)

plt.subplot(2,1,1)
plt.hist(Tex,bins=B)
plt.xlim(0,50)
plt.xticks(range(0,55,5))
plt.yscale('log')
plt.ylim(1,10**4)
plt.ylabel("Frequency")
plt.xlabel("Generations lived")
plt.text(0,10**4+100,'(a)',fontsize=20)
plt.text(42,10**3+3000,'$b=1.5$',fontsize=15)


#------------------------------------------------------------------------------
# Figure 4 (b)
# This panel shows the histogram for b=2.1.   
#------------------------------------------------------------------------------

b=2.1
Tex = []                            

for s in range(0,rep) :             
    Pop.clear()
    Pop.append(1)                   
    for t in range(1,gen+2) :
        if Pop[t-1] == 0 : N.append(0), M.append(0), F.append(0)
        else:
            for i in range(0,Pop[t-1]):
                N.append(np.random.poisson(lam=b))                             
                dMi = N[i]
                Mb = np.random.binomial(n=dMi,p=r)
                Fb = N[i]-Mb
                M.append(Mb*(1-mm))                                            #surviving number of males
                F.append(Fb*(1-mf))                                            #surviving number of females                F.append(np.random.binomial(n=Fb,p=1-mf))                      #surviving number of females
        if sum(M) == 0 : Pop.append(0)
        else: Pop.append(min(maxP,sum(F))) 
        N.clear(), M.clear(), F.clear()
        if Pop[t] == 0 and Pop[t-1] > 0 : Tex.append(t)

plt.subplot(2,1,2)
plt.hist(Tex,bins=B)
plt.xlim(0,50)
plt.xticks(range(0,55,5))
plt.yscale('log')
plt.ylim(1,10**4)
plt.ylabel("Frequency")
plt.xlabel("Generations lived")
plt.text(0,10**4+100,'(b)',fontsize=20)
plt.text(42,10**3+3000,'$b=2.1$',fontsize=15)

plt.rcParams["figure.figsize"] = (7,7)
plt.tight_layout() 
plt.savefig("Fig4_sept19.png",dpi=1000,bbox_inches='tight')
plt.show()
