#------------------------------------------------------------------------------
# This python code was used to generate Figure 3.
# This figure shows the ratio of extinct population (simulated) per generation. 
#------------------------------------------------------------------------------

# Importing libraries
import matplotlib.pyplot as plt
import numpy as np

# Declaring variables 
itr = 10                                        #max number of generations
rep = 10000                                     #number of replications
maxP= 10000                                     #max population
Pop = []                                        #list for population
Tex = []                                        #list for time to extinction
N = []                                          #number of offspring per female per generation
M = []                                          #number of male offpsring per female
F = []                                          #number of female offspring

# Assuming no mortalities
mm=0; mf=0

Gen = []                                        #number of generations
for t in range(0,itr+1):
    Gen.append(t)

#------------------------------------------------------------------------------
# Figure 3 (a)
# This panel shows the extinction ratio per generation for different values of b. 
#------------------------------------------------------------------------------

# Assuming equal number of males and females
r=.5

# Markers for the plot
m = ['o','v','s','p']
clr = ['sienna','green','red','orange']
mi =0 

# Simulating the population for different fertility rates
for b in [1.7, 1.9, 2.1, 2.3]:                  #fertility rates
    Ex = []                                     #extinction ratio
    A = []                                      #simulated population

# Simulating the population, s replications
    for s in range(0,rep) :                     
        Pop.clear()
        Pop.append(1)                   
        for t in range(1,itr+2) :
            if Pop[t-1] == 0 : N.append(0), M.append(0), F.append(0)
            else:
                for i in range(0,Pop[t-1]):
                    N.append(np.random.poisson(lam=b))                         #number of offspring per female
                    dMi = N[i]
                    Mb = np.random.binomial(n=dMi,p=r)
                    Fb = N[i]-Mb
                    M.append(Mb*(1-mm))                                        #surviving number of males
                    F.append(Fb*(1-mf))                                        #surviving number of females
            if sum(M) == 0 : Pop.append(0)
            else: Pop.append(min(maxP,sum(F))) 
            N.clear(), M.clear(), F.clear()
        if s == 0 : A=np.array([Pop])
        else : A=np.vstack([A,Pop])                                            #A is a repXitr array, containing counts of population per run

# Counting the number of extinct population per generation
    for co in range(0,itr+1):
        ext=0
        for ro in range(0,rep):
            if A[ro,co] == 0 : ext=ext+1
        Ex.append(ext/rep)

    plt.subplot(2,2,1)
    plt.scatter(Gen, Ex, alpha=1, marker=m[mi], color=clr[mi], label="{0:#.2f}".format(b))
    plt.ylim(0.5,1)
    plt.xticks(np.arange(0,itr+1,step=2))
    plt.legend(title_fontsize=16, title='$b$', prop={'size': 13}, loc="lower right")
    plt.ylabel("Extinction ratio", fontsize=18)
    plt.xlabel("Generation, $t$", fontsize=18)
    plt.text(0,1.01,'(a)',fontsize=23)
    mi=mi+1

#------------------------------------------------------------------------------
# Figure 3 (a)
# This panel shows the extinction ratio per generation for different values of b=2.1
# but with r=0.4, 0.5. 
#------------------------------------------------------------------------------r=.4

# Assuming fertility rate b=2.1 (RRF)
b=2.1

# Markers, colors for the plot
m = ['P','s']
clr = ['blue','red']
mi =0 

for r in [.4,.5] :                          
    Ex = []
    A = []
    for s in range(0,rep) :                         #number of replications
        Pop.clear()
        Pop.append(1)                   #single female at generation 0
        for t in range(1,itr+2) :
            if Pop[t-1] == 0 : N.append(0), M.append(0), F.append(0)
            else:
                for i in range(0,Pop[t-1]):
                    N.append(np.random.poisson(lam=b))                         #number of offspring per female
                    dMi = N[i]
                    Mb = np.random.binomial(n=dMi,p=r)
                    Fb = N[i]-Mb
                    M.append(Mb*(1-mm))                                        #surviving number of males
                    F.append(Fb*(1-mf))                                        #surviving number of females
            if sum(M) == 0 : Pop.append(0)
            else: Pop.append(min(maxP,sum(F))) 
            N.clear(), M.clear(), F.clear()
        if s == 0 : A=np.array([Pop])
        else : A=np.vstack([A,Pop])                                            #A is a repXitr array, containing counts of population per run

    for co in range(0,itr+1):
        ext=0
        for ro in range(0,rep):
            if A[ro,co] == 0 : ext=ext+1
        Ex.append(ext/rep)

    plt.subplot(2,2,2)
    plt.scatter(Gen, Ex, alpha=1, marker=m[mi], color=clr[mi], label="{0:#.2f}".format(r))
    plt.ylim(0.5,1)
    plt.xticks(np.arange(0,itr+1,step=2))
    plt.legend(title_fontsize=16, title='$r$', prop={'size': 13}, loc="lower right")
    plt.ylabel("Extinction ratio", fontsize=18)
    plt.xlabel("Generation, $t$", fontsize=18)
    plt.text(0,1.01,'(b)',fontsize=23)
    mi=mi+1
    
plt.rcParams["figure.figsize"] = (10,9)
plt.tight_layout() 
plt.savefig("Fig3_sept19.png",dpi=1000,bbox_inches='tight')
plt.show()
