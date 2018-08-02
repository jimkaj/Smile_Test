# -*- coding: utf-8 -*-
"""
Created on Thu Aug  2 00:42:50 2018

This file inputs one of the dataframes created by virtual_groups.py and graphs
the results.

On Q01 accuracy rate for individuals was 61.6 %  
On Q02 accuracy rate for individuals was 88.88 %
On Q03 accuracy rate for individuals was 58.22 %
On Q04 accuracy rate for individuals was 57.08 %
On Q05 accuracy rate for individuals was 74.3 %
On Q06 accuracy rate for individuals was 78.62 %
On Q07 accuracy rate for individuals was 79.36 %
On Q08 accuracy rate for individuals was 81.12 %
On Q09 accuracy rate for individuals was 76.23 %
On Q10 accuracy rate for individuals was 76.8 %
On Q11 accuracy rate for individuals was 72.54 %
On Q12 accuracy rate for individuals was 75.24 % **plot this
On Q13 accuracy rate for individuals was 81.23 %
On Q14 accuracy rate for individuals was 71.68 %
On Q15 accuracy rate for individuals was 78.0 %
On Q16 accuracy rate for individuals was 77.23 %
On Q17 accuracy rate for individuals was 55.82 % **plot this
On Q18 accuracy rate for individuals was 93.81 % **plot this
On Q19 accuracy rate for individuals was 85.41 % **plot this
On Q20 accuracy rate for individuals was 63.47 % **plot this

@author: James Kajdasz
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#lets open up our dataframe
df = pd.read_csv('Nominal_Group_Data_s30_g30.csv', low_memory=False)

# There are 20 different lines we could plot. Let's pull out 5 good ones
# duplicating _group_size column so we can use it later
df['size'] = df['group_size'] 

# On Q17 accuracy rate for individuals was 55.82 %
Q17_check = df['difficulty'] == 55.82 
df_Q17 = df[Q17_check] 
means_Q17 = df_Q17.groupby('group_size').mean()
Q17_size = means_Q17['size']
Q17_perf = means_Q17['sample_performance']

# On Q01 accuracy rate for individuals was 61.6 %
#Q01_check = df['difficulty'] == 61.60 
#df_Q01 = df[Q01_check] 
#means_Q01 = df_Q01.groupby('group_size').mean()
#Q01_size = means_Q01['size']
#Q01_perf = means_Q01['sample_performance']

# On Q20 accuracy rate for individuals was 63.47 % **plot this
Q20_check = df['difficulty'] == 63.47 
df_Q20 = df[Q20_check] 
means_Q20 = df_Q20.groupby('group_size').mean()
Q20_size = means_Q20['size']
Q20_perf = means_Q20['sample_performance']

# On Q12 accuracy rate for individuals was 75.24 %
Q12_check = df['difficulty'] == 75.24 
df_Q12 = df[Q12_check] 
means_Q12 = df_Q12.groupby('group_size').mean()
Q12_size = means_Q12['size']
Q12_perf = means_Q12['sample_performance']

# On Q19 accuracy rate for individuals was 85.41 %
Q19_check = df['difficulty'] == 85.41 
df_Q19 = df[Q19_check] 
means_Q19 = df_Q19.groupby('group_size').mean()
Q19_size = means_Q19['size']
Q19_perf = means_Q19['sample_performance']

# On Q18 accuracy rate for individuals was 93.81 %
Q18_check = df['difficulty'] == 93.81 
df_Q18 = df[Q18_check] 
means_Q18 = df_Q18.groupby('group_size').mean()
Q18_size = means_Q18['size']
Q18_perf = means_Q18['sample_performance']


# Let's plot our lines
plt.plot(Q17_size, Q17_perf, Q20_size, Q20_perf, Q12_size, Q12_perf, 
         Q19_size, Q19_perf, Q18_size, Q18_perf)

plt.xlabel('Group Size')
plt.ylabel('Mean Group Performance')
plt.title('Performance vs. Group Size for Tasks of Varying Difficulty')
plt.show()

