# -*- coding: utf-8 -*-
"""
Created on Mon Jul 30 11:19:20 2018

This program inputs the raw data file "Spot_the_Fake_Smile_v.3.csv".
-It selects only key variables(columns) of data
-It eliminates rows where the survey was not completed.
-It renames the columns
-It saves this data as "Clean_Smile_Data.csv"

Variable Description for Output File 'Clean_Smile_Data.csv':
Subject:  Individual Subject ID number. Used as index.
Confidence: How many out of 20 smile videos do you think you'll get?
Is_Femane: 'Female' if selected. 'NaN' if Male or no choice entered
Is_Male: 'Male' if selected. 'NaN' if Female or no choice entered     
Age: Age entered. NaN if not entered.
Children: # of children reported by participant. NaN if not entered.
Career: Reported years in a career that 'required you read people'
Q01-Q20: If answered correctly, it will say 'Genuine' or 'Fake' (which
is the correct answer for the given question). If answered incorrectly,
it will say NaN. All non-answers are filtered out of cleaned data.

@author: James Kajdasz
"""
import pandas as pd

# Let's open the file
df_input = pd.read_csv('Spot the Fake Smile v.3.csv', header=None, 
    skiprows=(0,1), 
    usecols=[0,9,10,11,12,28,29,30,33,35,37,38,40,43,44,47,48,50,53,55,57,58,60,62,65,66,68,69],
        low_memory=False)
df_input.columns=['Subject','Confidence','Is_Female','Is_Male','Age','Children',
                  'Career','Q01','Q02','Q03','Q04','Q05','Q06','Q07','Q08','Q09',
                  'Q10','Q11','Q12','Q13','Q14','Q15','Q16','Q17','Q18',
                  'Q19','Q20_wrong','Q20']
df_input.set_index('Subject', inplace=True)
df_input.head()

#Let's filter out people who didn't finish the whole survey
# Mark people who didn't answer last question (True: Finished survey)
finish = (df_input.iloc[:,25]=='Genuine')|(df_input.iloc[:,26]=='Fake')
# Create a new dataframe containing only people who answerd last question
df_clean = df_input[finish]
# Now we don't need the 'Q20_wrong' variable anymore.
# (we just used it to filter out those who didn't answer the last question)
df_clean = df_clean.drop(columns=['Q20_wrong'])

# Now let's save the cleaned data
df_clean.to_csv('Clean_Smile_Data.csv')




