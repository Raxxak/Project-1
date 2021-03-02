#This is the DECAY SIMULATOR (The second code will involve analysis and hypothesis testing) This simulates a radioactive decay

from scipy.stats import poisson
import numpy as np
import matplotlib.pyplot as plt


###DEFINE VARIABLES###########
Lambda_null=50
Lambda_alter=70#Average counts per hour
NumberofEvents=1000000
####################################

#CREATES THE DISTRIBUTION
datanull = np.random.poisson(Lambda_null, NumberofEvents)
dataalter = np.random.poisson(Lambda_alter, NumberofEvents)


#WRITES THE OUTPUT IN A TEXTFILE

np.savetxt("Decayoutput_null.txt", datanull,fmt='%u')
np.savetxt("Decayoutput_alter.txt",  dataalter,fmt='%u')



#PLOTS THE DISTRIBUTION

plt.hist(datanull,alpha=0.6, bins=Lambda_null+15,label='H0, Lambda= '+str(Lambda_null), density=True)
plt.hist(dataalter,alpha=0.6, bins=Lambda_alter+15,label='H1, Lambda= '+str(Lambda_alter), density=True)

plt.title('Distribution of the Count')
plt.ylabel('Probability')
plt.xlabel('Counts in  seconds')
plt.grid()
plt.legend(loc='upper right')
plt.savefig('Normalized_Distribution.pdf')

plt.show()


