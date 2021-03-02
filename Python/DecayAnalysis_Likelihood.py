import numpy as np
import matplotlib.pyplot as plt
import math

#Define the parameters and alpha
alpha=0.05

Lambda_null=50
Lambda_alter=70

#open the output files
f1 = open("Decayoutput_null.txt", "r")
f2 = open("Decayoutput_alter.txt", "r")

array_null=[]
array_alter=[]


#import data and convert it to numpy arrays
for line in f1:
    array_null.append(int(line))

for line in f2:
    array_alter.append(int(line))    

#sort the arrays
array_alter.sort()
array_null.sort()

#list has to be converted to an array to work with it
array_alter=np.array(array_alter)



lambda_crit = array_null[min(int((1-alpha)*len(array_null)), len(array_null)-1)]
first_leftover = np.where( array_alter > lambda_crit )[0][0]
beta = first_leftover/len(array_alter)





#Calculating the Likelyhood 

i=0
Likelihood_H0=[]
Likelihood_H1=[]
LH0=0
LH1=0
for i in range(0,len(array_null)):
    LH0=np.exp(-Lambda_null)*Lambda_null**array_null[i]/np.math.factorial(array_null[i])
    LH1=np.exp(-Lambda_alter)*Lambda_alter**array_null[i]/np.math.factorial(array_null[i])
    Likelihood_H0.append((LH0))
    Likelihood_H1.append((LH1))

    



array_null.sort()






#Plotting Likelyhood Ratio
fig,ax=plt.subplots()

ax.plot(array_null,Likelihood_H0, label='L(H0)')
ax.plot(array_null,Likelihood_H1,label='L(H1)')
plt.axvline(lambda_crit, color='k')

plt.title("Likelihood plots for Null and Alternative Hypothesis")
plt.xlabel("Parameter(Lambda)")
plt.ylabel("Likelihood ")
plt.grid(True)
plt.plot([],[], '', label='$\lambda_{crit} = $' + '${:.3f}$'.format(lambda_crit))
plt.plot([],[], '', label='$\\alpha = {:.3f}$'.format(alpha))
plt.plot([],[], '', label='$\\beta = {:.3f}$'.format(beta))
ax.fill_between(array_null,0,Likelihood_H0, alpha=0.5)
ax.fill_between(array_null,0,Likelihood_H1, alpha=0.5)
plt.grid()
plt.legend()
plt.savefig('Likelihood_plot.pdf')



plt.show()
