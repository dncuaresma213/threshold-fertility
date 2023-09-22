#------------------------------------------------------------------------------
# This python code was used to generate Figure 1 (a) to (d).
# This figure shows the dependence of the extinction probability P 
# to different parameters: fertility rate b, sex ratio r, mortality rates mm, mf.
# P[t] is a backward recurrence equation. Please refer to supplemenatary materials.
#------------------------------------------------------------------------------

# Importing libraries
import math as m
import matplotlib.pyplot as plt
import numpy as np

# Declaring variables common to all 4 panels
itr = 100                                           #maximum number of generations
P = []                                              #list for extinction probability per generation P[t]  

#------------------------------------------------------------------------------
# Figure 1 (a)
# This panel shows the dependence of probability P on fertility rate b
#------------------------------------------------------------------------------

# Equal number of females and males are assumed
r=.5

# Initializing the probability P[t] for generations t=0 to itr. 
# This is a necesary step to prevent index errors, since we work backward from P[itr] 
for j in range(0,itr+1): P.append(10)       
P[itr]=0                                

#Simulating P for mm,mf=0,1 and b=2 to 4
for mf in [0,.1]:                                   #mortality of females
    for mm in [0,.1]:                               #mortality of males
        P0=[]                                       #list for extinction probability per combination of mm,mf 
        for b in np.arange(2,4.1,.05):              #fertility rate
            for t in range(itr-1,-1,-1) :
                if m.exp(-b*r*(1-mm))+m.exp(b*(1-r)*((1-mf)*P[t+1]+mf))*(m.exp(-b*(1-r))-m.exp(-b*(1-mm*r))) < 0 : P[t] = 0
                elif m.exp(-b*r*(1-mm))+m.exp(b*(1-r)*((1-mf)*P[t+1]+mf))*(m.exp(-b*(1-r))-m.exp(-b*(1-mm*r))) > 1 : P[t] = 1 
                else: P[t] = m.exp(-b*r*(1-mm))+m.exp(b*(1-r)*((1-mf)*P[t+1]+mf))*(m.exp(-b*(1-r))-m.exp(-b*(1-mm*r)))
            P0.append(P[0])

#Plotting P against b
        bb=np.arange(2,4.1,.05)
        plt.subplot(2,2,1)
        plt.plot(bb, P0, linestyle="-", linewidth=2.6, label="{0:#.1f}".format(mm)+", ""{0:#.1f}".format(mf))
        plt.xlabel("Fertility rate, $b$", fontsize=18)
        plt.ylabel("Probability of extinction", fontsize=18)
        plt.ylim(.4,1.01)
        plt.xlim(1.99,4.01)
        plt.xticks(fontsize=12)
        plt.yticks(fontsize=12)
        plt.text(2,1.02,'(a)',fontsize=23)
        plt.legend(title_fontsize=16, title='$m_m$, $m_f$', prop={'size': 13}, loc="upper right")
        

#------------------------------------------------------------------------------
# Figure 1 (b)
# This panel shows the dependence of probability P on sex ratio r
#------------------------------------------------------------------------------

#Assuming no mortalities
mf=0; mm=0            

#Initializing P[t]
for j in range(0,itr+1): P.append(10)       
P[itr]=0                                    

for b in [2.1,2.6,3,4]:                             #fertility rate
    P0=[]
    for r in np.arange(0,1,.01):                    #sex ratio
        for t in range(itr-1,-1,-1) :
            if m.exp(-b*r*(1-mm))+m.exp(b*(1-r)*((1-mf)*P[t+1]+mf))*(m.exp(-b*(1-r))-m.exp(-b*(1-mm*r))) < 0 : P[t] = 0
            elif m.exp(-b*r*(1-mm))+m.exp(b*(1-r)*((1-mf)*P[t+1]+mf))*(m.exp(-b*(1-r))-m.exp(-b*(1-mm*r))) > 1 : P[t] = 1 
            else: P[t] = m.exp(-b*r*(1-mm))+m.exp(b*(1-r)*((1-mf)*P[t+1]+mf))*(m.exp(-b*(1-r))-m.exp(-b*(1-mm*r)))
        P0.append(P[0])
    
    rr=np.arange(0,1,.01)    
    plt.subplot(2,2,2)
    plt.plot(rr, P0, linestyle="-", linewidth=2.6, label="{0:#.1f}".format(b))
    plt.xlabel("Sex ratio at birth, $r$", fontsize=18)
    plt.ylabel("Probability of extinction", fontsize=18)
    plt.ylim(0.3,1.01)
    plt.xlim(-.01,1.01)
    plt.xticks(np.arange(0,1.1,.1),fontsize=12)
    plt.yticks(fontsize=12)
    plt.text(0,1.02,'(b)',fontsize=23)
    plt.legend(title_fontsize=16, title='$b$', prop={'size': 13}, loc="upper right")
    

#------------------------------------------------------------------------------
# Figure 1 (c)
# This panel shows the optimal r per fertility rate b
#------------------------------------------------------------------------------

# Assuming no mortalities
mf=0; mm=0

# List of optimal r per b
R=[]                                            

# List of r's and b's 
rr=np.arange(.38,.51,.0005)
bb=np.arange(2.7,9.1,.001)    

#Initializing P[t]
for j in range(0,itr+1): P.append(10)       
P[itr]=0                                    

for b in np.arange(2.7,9.1,.001):               #fertility rate
    P0=[]
    for r in np.arange(.38,.51,.0005):           #sex ratio at birth                  
        for t in range(itr-1,-1,-1) :
            if m.exp(-b*r*(1-mm))+m.exp(b*(1-r)*((1-mf)*P[t+1]+mf))*(m.exp(-b*(1-r))-m.exp(-b*(1-mm*r))) < 0 : P[t] = 0
            elif m.exp(-b*r*(1-mm))+m.exp(b*(1-r)*((1-mf)*P[t+1]+mf))*(m.exp(-b*(1-r))-m.exp(-b*(1-mm*r))) > 1 : P[t] = 1 
            else: P[t] = m.exp(-b*r*(1-mm))+m.exp(b*(1-r)*((1-mf)*P[t+1]+mf))*(m.exp(-b*(1-r))-m.exp(-b*(1-mm*r)))
        P0.append(P[0])
    
#Taking note the r that gives the minimum probability P per fertility rate b, i.e., optimal r    
    for i in range(0,len(rr)):                           
        if P0[i] == min(P0) : R.append(rr[i])

plt.subplot(2,2,3)
plt.plot(bb, R, linestyle="-", linewidth=2.6)
plt.xlabel("Fertility rate, $b$", fontsize=18)
plt.ylabel("Optimal sex ratio at birth, $r$", fontsize=18)
plt.ylim(0.379,0.501)
plt.xlim(2.69,9.1)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.text(2.7,0.5015,'(c)',fontsize=23)


#------------------------------------------------------------------------------
# Figure 1 (d)
# This panel shows the critical fertility rate b_(cr) per sex ratio r 
#------------------------------------------------------------------------------

# Initializing P[t] 
for j in range(0,itr+1): P.append(10)       
P[itr]=0                                    

for mf in [0,.1]:                               #mortality of females
    for mm in [0,.1]:                           #mortality of males
        bb=[]; rr=[]                            #list for critical fertility rate b_(cr) and corresponding sex ratio r
        for r in np.arange(0,1,.001):           #sex ratio
            for b in np.arange(2,4.1,.001):     #fertility rate
                if b*(1-r)*(1-mf)*(1-m.exp(-b*r*(1-mm))) > 1 : 
                    bb.append(b); rr.append(r)
                    break
        
        plt.subplot(2,2,4)
        plt.plot(rr,bb, linestyle="-", linewidth=2.6, label="{0:#.1f}".format(mm)+", ""{0:#.1f}".format(mf))
        plt.ylabel("Crtical fertility rate, $b_{cr}$", fontsize=18)
        plt.xlabel("Sex ratio at birth, $r$", fontsize=18)
        plt.xlim(.39,1.01)
        plt.ylim(2.4,4.01)
        plt.xticks(np.arange(.4,1.1,.1),fontsize=12)
        plt.yticks(fontsize=12)
        plt.text(0.45,3.6,'$P<1$',fontsize=20)
        plt.text(0.75,3,'$P=1$',fontsize=20)
        plt.text(0.4,4.02,'(d)',fontsize=23)
        plt.legend(title_fontsize=16, title='$m_m$, $m_f$', prop={'size': 13}, loc="upper right")

#------------------------------------------------------------------------------
#plt.suptitle('')   
plt.rcParams["figure.figsize"] = (10,10)
plt.tight_layout() 
plt.savefig("Fig1_aug24.png",dpi=1000,bbox_inches='tight')
plt.show()
