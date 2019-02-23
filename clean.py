import pandas as pd
import glob
import os


### This python script will clean every file in our No Meta Data folder. This folder can be found on GitHub
### as well as our ICON submission. There are 9 chunks of code, each created for the different types of data
### files that need to be cleaned. each chunk of code is indicated with 12 sets of ####


#### #### #### #### #### ####   start marriage cleaning   #### #### #### #### #### ####

marriage = pd.read_excel('data no meta/state-marriage-rates-90-95-99-17_no_meta.xlsx',  # read in the data to pandas dataframe, ready file
                         header=[0, 1],                                                 # set header
                         na_values='---',                                               # null values in excel file
                         index_col=[0])                                                 # set index column
marriage = marriage.stack([0, 1]).reset_index()                                         # reshape data

marriage.rename(columns={marriage.columns[0]: 'State',                                  # rename columns, first column past index renamed to State
                         marriage.columns[1]: 'left',                                   # second column renamed to left, for leftovers, column is dropped
                         marriage.columns[2]: 'Year',                                   # third column renamed to Year
                         marriage.columns[3]: 'Marriage Rate'}                          # fourth column set to Marriage Rate
                , inplace=True)

marriage.drop(columns=['left'], inplace=True)                                           # column is dropped, not needed

marriage.to_excel(excel_writer='cleaned data/marriage_cleaned_in_python.xls',           # read dataframe to excel, set file name
                  sheet_name='marriage rates',                                          # sheet named 'marriage rates'
                  na_rep='null',                                                        # treat n/a as null
                  index=False)                                                          # don't include pandas index




#### #### #### #### #### ####   start divorce cleaning   #### #### #### #### #### ####

divorce = pd.read_excel('data no meta\state-divorce-rates-90-95-99-17_no_meta.xlsx',    # read in the data to pandas dataframe, ready file
                        header=[0, 1],                                                  # set header
                        na_values='---',                                                # null values in excel file
                        index_col=[0])                                                  # set index column
divorce = divorce.stack([0, 1]).reset_index()                                           # reshape data

divorce.rename(columns={divorce.columns[0]: 'State',                                    # rename columns, first column past index renamed to State
                        divorce.columns[1]: 'left',                                     # second column renamed to left, for leftovers, column is dropped
                        divorce.columns[2]: 'Year',                                     # third column renamed to Year
                        divorce.columns[3]: 'Divorce Rate'}                             # fourth column set to Divorce Rate
               , inplace=True)

divorce.drop(columns=['left'], inplace=True)                                            # column is dropped, not needed

divorce.to_excel(excel_writer='cleaned data/divorce_cleaned_in_python.xls',             # read dataframe to excel, set file name
                 sheet_name='divorce rates',                                            # sheet named 'divorce rates'
                 na_rep='null',                                                         # treat n/a as null
                 index=False)                                                           # don't include pandas index




#### #### #### #### #### ####   start unemployment cleaning   #### #### #### #### #### ####

unemployment = pd.read_excel('data no meta\Unemployment rate by state 2000-2017_no_meta.xls',
                             header=[0],                                                # set header
                             na_values='N/A',                                           # null values in excel file
                             index_col=[1])                                             # set index column

unemployment.drop(columns=['Fips'], inplace=True)                                       #dropping columns of unneeded data
unemployment.drop(columns=['MOE'], inplace=True)                                        #dropping columns of unneeded data
unemployment = unemployment.reset_index()

unemployment.to_excel(excel_writer='cleaned data/unemployment_cleaned_in_python.xls',   # read dataframe to excel, set file name
                      sheet_name='unemployment rates',                                  # sheet named 'unemployment rates'
                      na_rep='null',
                      index=False)                                                      # treat n/a as null


#### #### #### #### #### ####   start party affiliation cleaning   #### #### #### #### #### ####

partyAffiliation = pd.read_excel('data no meta/Party_ID_1939-2014_no_meta.xlsx',        # read in the data to pandas dataframe, ready file
                             header=[0],                                                # set header
                             na_values=' ',                                             # null values in excel file
                             index_col=[0])                                             # set index column

partyAffiliation = partyAffiliation.reset_index()

partyAffiliation.to_excel(excel_writer='cleaned data/party_ID_cleaned_in_python.xls',   # read dataframe to excel, set file name
                      sheet_name='US party affiliation',                                # sheet named 'US party affiliation'
                      na_rep='null',
                      index=False)                                                      # treat n/a as null




#### #### #### #### #### ####   start income cleaning   #### #### #### #### #### ####

incomeCur = pd.read_excel("data no meta\h08_no_meta.xlsx",                              # read in the data to pandas dataframe, ready file
                       skiprows=1,                                                      # skipping meta data
                       header = [0,1],                                                  # set header
                       skipfooter=54,                                                   # we skip the bottom table here so that we can create to dataframes
                       index_col=[0])                                                   # set index

incomeCur = incomeCur.stack([0]).reset_index()                                          # reshaping data

incomeCur.rename(columns={incomeCur.columns[0] : 'State',                               # rename columns after reshape
                       incomeCur.columns[1] : 'Year',
                       incomeCur.columns[2] : 'Current Median Income',
                       incomeCur.columns[3] : 'Current Standard Error'}
            , inplace=True)

incomeCur['Year'].replace(regex=True,inplace=True,to_replace=r'\([0-9]*\)|\([^)]*\)',value=r'')
incomeCur['Year'] = incomeCur.Year.astype(int)                                          # line 110 and 109 are house keeping, tidying up data types
                                                                                        # and adding a regular expression to remove meta data
income = pd.read_excel("data no meta\h08_no_meta.xlsx",                                 # we now read in the file again to create the second
                       skiprows=56,                                                     # dataframe, we do this by now skipping the first table
                       header = [0,1],                                                  # with skiprows, and set the header
                       index_col=[0])                                                   # set index

income = income.stack([0]).reset_index()                                                # reshape data

income.rename(columns={income.columns[1] : 'drop',                                      # rename column to drop to mark for later to discard
                       income.columns[2] : '2017 Median Income',                        # renaming columns
                       income.columns[3] : '2017 Standard Error'}
            , inplace=True)

income.drop(columns=['drop','level_0'], axis=1, inplace=True)                           # dropping unneeded columns

totalIncomes = pd.concat([incomeCur, income], axis=1, sort=False)                       # creating one large dataframe concatonating the
                                                                                        # 2 dataframes we created
totalIncomes.to_excel(excel_writer='cleaned data/total_income_cleaned_in_python.xls',   # read dataframe to excel, set file name
                   sheet_name='median income rates',                                    # sheet named 'median income rates'
                   index=False)                                                         # don't include pandas index




#### #### #### #### #### ####   start birthrate cleaning   #### #### #### #### #### ####

df = pd.read_csv("data no meta\NCHS_-_Births_and_General_Fertility_Rates__United_States_no_meta.csv",
                         header=[0],                                                    # set header
                         na_values=' ',)                                                # null values in excel file

df.to_excel(excel_writer='cleaned data/birthrate_cleaned_in_python.xls',                # read dataframe to excel, set file name
                  sheet_name='birth rates',                                             # name sheet
                  index=False)                                                          # don't include pandas index




#### #### #### #### #### #### ####   cleaning Migration/Mobility #### #### #### #### #### #### ####

df = pd.read_excel("data no meta\migration.xlsx",                                       # Read in file
                   header=[0, 1])                                                       # Moves the headers to the top left corner

df = df.dropna(how='all')                                                               # dropping null values
df.columns = df.columns.get_level_values(0)                                             # reshaping data
df = df.dropna(how='any')                                                               # dropping null values
df = df.reset_index()                                                                   # reshaping data

df.drop(columns=['index'], axis=1, inplace=True)

df.to_excel(excel_writer='cleaned data/Migration_cleaned_in_python.xlsx',               # Write to .xls file
            sheet_name='migration rates',                                               # name sheet
            na_rep='null',                                                              # how to represent null values
            index=False)                                                                # Do not keep the index




#### #### #### #### #### #### ####   Cleaning Health Insurance   #### #### #### #### #### #### ####

df = pd.read_excel('data no meta\Health Insurance Coverage Type by Family Income and Age 2008-2017_no_meta.xlsx',
                   usecols=9,                                                           # Use all 9 columns for dataframe
                   na_values = 'N/A')                                                   # Null values are labeded N/A

df['Number'] = df['Data']                                                               # Make new column from moving number of people value

df.Number = df.Number.shift(-1)                                                         # Shift Number column up by one position

df = df.iloc[::2]                                                                       # Remove every other row
df = df.drop(['Data Type'], axis = 1)                                                   # Drop Data Type column, redundant with new column
df.rename(index= str, columns = {'Data':'Percent'}, inplace=True)                       # Rename column

#Write to .xls file
df.to_excel(excel_writer='cleaned data/Health_Insurance_cleaned_by_python.xlsx',        # name output
                sheet_name='HealthInsuranceRates',                                      # name sheet
                na_rep='null',                                                          # how to represent null values
                index=False)                                                            # Do not keep the index




#### #### #### #### #### #### ####   Clean State Crimes   #### #### #### #### #### #### ####
                                                                                        # we cleaned our crime by state data by downloading individual state
                                                                                        # data files, placing them in a folder, looping through that folder,
                                                                                        # and running each data set through the code below. We then concatonate
                                                                                        # all of the dataframes into one large dataframe
path =r'CrimesByState'                                                                  # get data file names, setting path to our Crime by State Data folder
filenames = glob.glob(path + "/*.csv")                                                  # set filenames to select all files that are of type .csv

dfs = []                                                                                # creating dictionary for our dataframes
for filename in filenames:                                                              # looping through our data folder
    df = pd.read_csv(filename,error_bad_lines=False,
                       skiprows=9,                                                      # Skips metadata in rows 1-0
                       skipfooter=18)                                                   # Skips metadata on the bottom
    df = df.drop(columns = ['Revised rape rate /2','Unnamed: 12'], axis = 1)            # Drop Rows
    df['State'] = os.path.basename(filename)                                            # Make state column
    df['State'] = df['State'].map(lambda x: x.rstrip('.csv'))                           # remove csv
    dfs.append(df)                                                                      # append dataframe to dataframe dictionary

big_frame = pd.concat(dfs, ignore_index=True)                                           # Concatenate all data into one DataFrame

big_frame.to_excel(excel_writer='cleaned data/State_Crime_cleaned_by_python.xlsx',      # name output
                sheet_name='crime rates by state',                                      # name sheet
                na_rep='null',                                                          # how to represent null values
                index= False)                                                           # Do not keep the index