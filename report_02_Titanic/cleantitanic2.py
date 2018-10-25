# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
from scipy.stats import mode
import string

def substrings_in_string(big_string, substrings):
    for substring in substrings:
        if string.find(big_string, substring) != -1:
            return substring
    print big_string
    return np.nan


def phase1clean(df):
    #setting silly values to nan
    df.Fare = df.Fare.map(lambda x: np.nan if x==0 else x)
    
    #Special case for cabins as nan may be signal
    df.Cabin = df.Cabin.fillna('Unknown')    

    #creating a title column from name
    title_list=['Mrs', 'Mr', 'Master', 'Miss', 'Major', 'Rev',
                'Dr', 'Ms', 'Mlle','Col', 'Capt', 'Mme', 'Countess',
                'Don', 'Jonkheer']

    df['Title']=df['Name'].map(lambda x: substrings_in_string(x, title_list))
    
    #replacing all titles with mr, mrs, miss, master
    def replace_titles(x):
        title=x['Title']
        if title in ['Don', 'Major', 'Capt', 'Jonkheer', 'Rev', 'Col']:
            return 'Mr'
        elif title in ['Countess', 'Mme']:
            return 'Mrs'
        elif title in ['Mlle', 'Ms']:
            return 'Miss'
        elif title =='Dr':
            if x['Sex']=='Male':
                return 'Mr'
            else:
                return 'Mrs'
        else:
            return title
    df['Title']=df.apply(replace_titles, axis=1)

    #Turning cabin number into Deck
    cabin_list = ['A', 'B', 'C', 'D', 'E', 'F', 'T', 'G', 'Unknown']
    df['Deck']=df['Cabin'].map(lambda x: substrings_in_string(x, cabin_list))
        
    #Creating new family_size column
    df['Family_Size']=df['SibSp']+df['Parch']
    
    return df
    
def phase2clean(train, test):
    #data type dictionary
    data_type_dict={'Pclass':'ordinal', 'Sex':'nominal', 
                    'Age':'numeric', 
                    'Fare':'numeric', 'Embarked':'nominal', 'Title':'nominal',
                    'Deck':'nominal', 'Family_Size':'ordinal'}      

    #imputing nan values
    for df in [train, test]:
        classmeans = df.pivot_table('Fare', rows='Pclass', aggfunc='mean')
        df.Fare = df[['Fare', 'Pclass']].apply(lambda x: classmeans[x['Pclass']] if pd.isnull(x['Fare']) else x['Fare'], axis=1 )
        meanAge=np.mean(df.Age)
        df.Age=df.Age.fillna(meanAge)
        modeEmbarked = mode(df.Embarked)[0][0]
        df.Embarked = df.Embarked.fillna(modeEmbarked)


#    Fare per person
    for df in [train, test]:
        df['Fare_Per_Person']=df['Fare']/(df['Family_Size']+1)
    
    #Age times class
    for df in [train, test]:
        df['Age*Class']=df['Age']*df['Pclass']
    
    data_type_dict['Fare_Per_Person']='numeric'
    data_type_dict['Age*Class']='numeric'
    
    return [train,test, data_type_dict]
    
def discretise_numeric(train, test, data_type_dict, no_bins=10):
    N=len(train)
    M=len(test)
    test=test.rename(lambda x: x+N)
    joint_df=train.append(test)
    for column in data_type_dict:
        if data_type_dict[column]=='numeric':
            joint_df[column]=pd.qcut(joint_df[column], 10)
            data_type_dict[column]='ordinal'
    train=joint_df.ix[range(N)]
    test=joint_df.ix[range(N,N+M)]
    return train, test, data_type_dict

def clean(no_bins=0):
    #you'll want to tweak this to conform with your computer's file system
    trainpath = 'C:/Documents and Settings/DIGIT/My Documents/Google Drive/Blogs/triangleinequality/Titanic/rawtrain.csv'
    testpath = 'C:/Documents and Settings/DIGIT/My Documents/Google Drive/Blogs/triangleinequality/Titanic/rawtest.csv'
    traindf = pd.read_csv(trainpath)
    testdf = pd.read_csv(testpath)

    traindf=phase1clean(traindf)
    testdf=phase1clean(testdf)
    
    traindf, testdf, data_type_dict=phase2clean(traindf, testdf)
    
    traindf, testdf, data_type_dict=discretise_numeric(traindf, testdf, data_type_dict)

    
    #create a submission file for kaggle
    predictiondf = pd.DataFrame(testdf['PassengerId'])
    predictiondf['Survived']=[0 for x in range(len(testdf))]
    predictiondf.to_csv('C:/Documents and Settings/DIGIT/My Documents/Google Drive/Blogs/triangleinequality/Titanic/prediction.csv',
                  index=False)
    return [traindf, testdf, data_type_dict]
