import numpy as np
import matplotlib.pyplot as plt
import math
# Define the parameters and alpha

alpha=0.05    
Lambda_null=50
Lambda_alter=70

#open the output files
f1 = open("Decayoutput_null.txt", "r")
f2 = open("Decayoutput_alter.txt", "r")



array_alter=[]
array_null=[]



#import data and convert it to numpy arrays
for line in f1:
    array_null.append(int(line))
for line in f2:
    array_alter.append(int(line))    
    


#sort the arrays
array_null.sort()
array_alter.sort()





array_alter=np.array(array_alter)




#Calculating the Likelyhood 

i=0
p0=[]
p1=[]
L_Ratio_H0=[]
L_Ratio_H1=[]
LH0=0
LH1=0
for i in range(0,len(array_null)):
    LH0=(np.exp(-Lambda_null))*(Lambda_null**array_null[i])/np.math.factorial(array_null[i])
    LH1=(np.exp(-Lambda_alter))*(Lambda_alter**array_null[i])/np.math.factorial(array_null[i])
    p0.append(LH0)
    p1.append(LH1)
    L_Ratio_H0.append(np.log10(LH0/LH1))
    L_Ratio_H1.append(np.log10(LH1/LH0))




lambda_crit = array_null[min(int((1-alpha)*len(array_null)), len(array_null)-1)]
first_leftover = np.where( array_alter > lambda_crit )[0][0]
beta = first_leftover/len(array_alter)
#plotting
weights0 = np.ones_like(L_Ratio_H0) / len(L_Ratio_H0)
weights1 = np.ones_like(L_Ratio_H1) / len(L_Ratio_H1)


fig,ax=plt.subplots()
plt.hist(L_Ratio_H0,65,weights=weights0,alpha=0.5,label="assuming $\\mathbb{H}_0$")
plt.hist(L_Ratio_H1,65,weights=weights1, alpha=0.5,label="assuming $\\mathbb{H}_1$")
plt.axvline(alpha, color='r', linewidth=1, label='$\\lambda_\\alpha$')
ax.plot([], [], ' ', label="$\\alpha = 0.05$")
ax.plot([], [], ' ', label="$\\beta = $"+str(beta) ) 
plt.legend()
plt.title('Log-Likelihood Ratio Plot')
plt.xlabel('$\\lambda = \\log({\\cal L}_{\\mathbb{H}_{1}}/{\\cal L}_{\\mathbb{H}_{0}})$')
plt.ylabel('Probability')
plt.grid(True)
plt.savefig('Log_Likelihood_Ratio.pdf')
plt.show()
