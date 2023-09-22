#------------------------------------------------------------------------------
# This python code was used to generate Figure 2.
# This figure shows the dynamics of the population starting with a single female
# in generation 0 with subcritical fertility rates.
#------------------------------------------------------------------------------

# Importing libraries
import math as m
import matplotlib.pyplot as plt
import numpy as np

# Assuming no mortalities
mm=0; mf=0

# Declaring variables common to all panels
rep = 100                           #number of replications
maxP= 10000                         #max population
Pop = []                            #list for population
Tex = []                            #list for time to extinction
N = []                              #number of offspring per female per generation
M = []                              #number of male offpsring per female
F = []                              #number of female offspring

# Counting the number of extinct populations
count21a=0; count21b=0              #panel (a,b)
count205a=0; count205b=0            #panel (c,d)

#------------------------------------------------------------------------------
# Figure 2 (a) lin-lin scale, (b) log-lin scale.
#------------------------------------------------------------------------------

# Assumptions
r=.5                                #sex ratio
b=2.1                               #fertility rate
itr21 = 100                         #max number of generations

# Simulating the population for t generations, s replications
for s in range(0,rep) :             
    Pop.clear()
    Pop.append(1)                   
    for t in range(1,itr21+1) :
        if Pop[t-1] == 0 : N.append(0), M.append(0), F.append(0)
        else:
            for i in range(0,Pop[t-1]):
                N.append(np.random.poisson(lam=b))                             #number of offspring per female
                dMi = N[i]
                Mb = np.random.binomial(n=dMi,p=r)
                Fb = N[i]-Mb
                M.append(Mb*(1-mm))                                            #surviving number of males
                F.append(Fb*(1-mf))                                            #surviving number of females
        if sum(M) == 0 : Pop.append(0)
        else: Pop.append(min(maxP,sum(F))) 
        N.clear(), M.clear(), F.clear()

#Counting the number of populations that went extinct    
    if Pop[100] == 0 : count21a=1+count21a
    if Pop[itr21] == 0 : count21b=1+count21b

#Plotting the dynamics of the population in lin-lin scale    
    plt.subplot(2,2,1)
    plt.plot(Pop, linestyle="-", color="blue")
    plt.ylabel("Population", fontsize=18)
    plt.xlabel("Generation, $t$", fontsize=18)
    plt.ylim(0,100)
    plt.text(0,100,'(a)',fontsize=23)

#Plotting the dynamics of the population in log-lin scale
    plt.subplot(2,2,2)
    plt.plot(Pop, linestyle="-", color="blue")
    plt.ylabel("Population", fontsize=18)
    plt.xlabel("Generation, $t$", fontsize=18)
    plt.yscale('log',base=10)
    plt.ylim((10**0,10**4))
    plt.text(0,10**4+500,'(b)',fontsize=23)


#------------------------------------------------------------------------------
# Figure 2 (b) lin-lin scale, (b) log-lin scale.
#------------------------------------------------------------------------------

# Assumptions
r=.5
b=2.05
itr = 200                           

for s in range(0,rep) :             
    Pop.clear()
    Pop.append(1)                   
    for t in range(1,itr+1) :
        if Pop[t-1] == 0 : N.append(0), M.append(0), F.append(0)
        else:
            for i in range(0,Pop[t-1]):
                N.append(np.random.poisson(lam=b))                             #number of offspring per female
                dMi = N[i]
                Mb = np.random.binomial(n=dMi,p=r)
                Fb = N[i]-Mb
                M.append(Mb*(1-mm))                                            #surviving number of males
                F.append(Fb*(1-mf))                                            #surviving number of females
        if sum(M) == 0 : Pop.append(0)
        else: Pop.append(min(maxP,sum(F))) 
        N.clear(), M.clear(), F.clear()
    
    if Pop[100] == 0 : count205a=1+count205a
    if Pop[itr] == 0 : count205b=1+count205b
    
    plt.subplot(2,2,3)
    plt.plot(Pop, linestyle="-", color="blue")
    plt.ylabel("Population", fontsize=18)
    plt.xlabel("Generation, $t$", fontsize=18)
    plt.ylim(0,100)
    plt.text(0,100,'(c)',fontsize=23)

    plt.subplot(2,2,4)
    plt.plot(Pop, linestyle="-", color="blue")
    plt.ylabel("Population", fontsize=18)
    plt.xlabel("Generation, $t$", fontsize=18)
    plt.yscale('log',base=10)
    plt.ylim((10**0,10**4))
    plt.text(0,10**4+500,'(d)',fontsize=23)

#------------------------------------------------------------------------------
plt.rcParams["figure.figsize"] = (10,10)
plt.tight_layout() 
plt.savefig("Fig2_sept19.png",dpi=1000,bbox_inches='tight')
plt.show()
