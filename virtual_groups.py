# -*- coding: utf-8 -*-
"""
Created on Mon Jul 30 23:35:20 2018

This program combines individuals to generate random virtual groups from a 
dataset of a desired size. It can be used to demosntrate the "Wisdom of the 
crowd" This program inputs the file Clean_Smile_Data.csv.  The user designates
1) What question do you want to use (there are 20 smile videos to choose from) 
2) How big do you want to make your simulated virtual group?
3) How many groups do you want to generate?
It outputs the accuracy rates of the groups generated. It saves this data to 
a .csv file titled 'Nominal_Group_Data.csv' The file contains 3 variables:
  sample_performance: each data point is a sample of groups. The sample
    performance is the average performance of all the groups in that sample.
  difficulty: This is the difficulty of the individual video, defined as 
    the average individual accuracy for the entire 60,000+ responses.
  group_size: number of individuals randoly put into a given group   

@author: James Kajdasz
"""
import numpy as np
import pandas as pd

def individual_answer(q):
    '''This function returns the overall mean accuracy for a particular 
    smile video Q.'''
    accuracy = df[q].count() / len(df) * 100
    return round(accuracy, 2)     

def group_answer(q, group_size):
    '''This function takes the smile video (q) and generates a simulated random
    group of size (group_size). It returns the group's collective answer 
    of the video. Returns 0 if group was incorrect, 1 if group was correct
    ''' 
    # find end of list
    end = int(len(df)-1)
    # create a random group of size (group_size)
    group = df.iloc[np.random.randint(0, end, group_size), :]    
    
    # did majority of group get video correct?
    vote = group[q].count()
    if vote > (len(group)/2):
        # the group got the right answer
        return 1
    elif vote == (len(group)/2):
        # the group is tied
        return 0.5
    else:
        # the group got the wrong answer
        return 0    

def sample_answer(q, group_size, sample_size):
    '''This function takes the smile video 'q', the group size (group_size), 
    and generates (sample_size) number of groups. It returns the average accuracy 
    rate of the groups in the sample
    '''    
    i = sample_size
    group_answers = []
    while i > 0:
        answer = group_answer(q, group_size)
        group_answers.append(answer)
        i -= 1
    return (100*np.mean(group_answers)) 

def repeat_samples(q, group_size, sample_size, num_samples):
    ''' This procedure will repeat the sampling process (sample_answer) for 
    a desired number of times (num_samples). It returns a list of how each 
    sample performed on the task.
    '''
    j = num_samples
    accuracy_samples = []
    while j > 0:
        sample = sample_answer(q, group_size, sample_size)
        accuracy_samples.append(sample)
        j -= 1
    np_accuracy_samples = np.array(accuracy_samples)
    return np_accuracy_samples

def col_nam(n):
    '''This function takes an integer n and out puts the appropriate name of 
    one of the smile_video columns. Ex: in 3. Out: 'Q03'
    '''
    n = int(n)
    if n < 10:
        n = '0' + str(n)
    else:
        n = str(n)
    q = 'Q'+ n
    return q

      
# Let's open our data file
df = pd.read_csv('Clean_Smile_Data.csv', low_memory=False)

# Let's figure out what the user wants to do
# There are 20 different videos of people smiling. What video to start?
inp = int(input('Which video do you want to start with? (enter 1-20): '))
# Some formatting of the input helps us turn it into the appropriate column name
q = col_nam(inp)

# Individuals are put together to form a virtual group. Group is any size 
group_size = int(input('What is the starting size of the virtual groups? (enter integer): '))  
# How many groups will be created for the sample?
sample_size = int(input('How many groups do you want to make? (enter integer): ')) 
# how many times do you want to repeat this sampling process?
num_samples = int(input('How many times do you want to repeat this sampling method? (enter integer): '))


df_samples = pd.DataFrame()


''' The main script below will create a DataFrame consisting of simulation data
of every possible group size, starting with 'group_size' and going up to 99.
It will do this for every video, starting with 'inp' and going up to 20.
'''

#let's do this for every video from inp to 20
while inp <= 20:
    q = col_nam(inp)
    print('On',q, 'accuracy rate for individuals was', individual_answer(q),'%')
    #Let's do this for every sized group, up to 100
    while group_size < 100:
        #print('I am generating', sample_size, 'groups of', group_size, '...')
        # get group performance metrics 
        samples = repeat_samples(q, group_size, sample_size, num_samples)
        
        # make sample data frame   
        d = {'sample_performance':samples}
        df_sampleA = pd.DataFrame(data=d)  
        df_sampleA['difficulty'] = individual_answer(q)
        df_sampleA['group_size'] = group_size
    
        # concatenate the dataframes
        frames = [df_sampleA, df_samples]
        df_samples = pd.concat(frames)
        
        #step up all the iterators
        group_size += 2
        samples = []
    
    # iterate to the next smile video
    inp += 1
    group_size = 1

#let's save our new data frame
df_samples.to_csv('Nominal_Group_Data.csv')    





