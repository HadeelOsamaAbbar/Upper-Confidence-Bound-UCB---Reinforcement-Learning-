

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import math

# Importing the dataset
dataset = pd.read_csv('Ads_CTR_Optimisation.csv')
d=10
num_selection=[0]*d
sum_rewards=[0]*d
adsSellect=[]
N=10000
total=0
for n in range(N):
    maxUpperBound=0
    ad=0
    for i in range(d):
        if num_selection[i]>0:
           avg=sum_rewards[i]/num_selection[i]
           dlta=math.sqrt(1.5*math.log(n+1)/num_selection[i])
           upper_bound=dlta+avg
        else:
            upper_bound=1e400
        if maxUpperBound<upper_bound:
           maxUpperBound =upper_bound
           ad=i
    adsSellect.append(ad) 
    num_selection[ad]=num_selection[ad]+1
    rew=dataset.values[n,ad]
    sum_rewards[ad]=sum_rewards[ad]+rew
    total=total+rew



plt.hist(adsSellect)   