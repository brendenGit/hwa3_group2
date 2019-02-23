import pandas as pd
import glob
import os

#### #### #### #### #### ####   start marriage cleaning   #### #### #### #### #### #### ####1

marriage = pd.read_excel('data no meta/state-marriage-rates-90-95-99-17_no_meta.xlsx',
                         # read in the data to pandas dataframe, ready file
                         header=[0, 1],  # set header
                         na_values='---',  # null values in excel file
                         index_col=[0])  # set index column
marriage = marriage.stack([0, 1]).reset_index()  # reshape data by stacking to long, then reset index to new index

marriage.rename(columns={marriage.columns[0]: 'State',  # rename columns, first column past index renamed to State
                         marriage.columns[1]: 'left',  # second column renamed to left, for leftovers, column is dropped
                         marriage.columns[2]: 'Year',  # third column renamed to Year
                         marriage.columns[3]: 'Marriage Rate'}  # fourth column set to Marriage Rate
                , inplace=True)  # true so that we don't have to set school = (copy we are returning)

marriage.drop(columns=['left'], inplace=True)  # column is dropped, not needed

marriage.to_excel(excel_writer='cleaned data/marriage_cleaned_in_python.xls',  # read dataframe to excel, set file name
                  sheet_name='marriage rates',  # sheet named 'marriage rates'
                  na_rep='null',  # treat n/a as null
                  index=False)  # don't include pandas index




#### #### #### #### #### #### start divorce cleaning #### #### #### #### #### ####2

divorce = pd.read_excel('data no meta\state-divorce-rates-90-95-99-17_no_meta.xlsx',
                        # read in the data to pandas dataframe, ready file
                        header=[0, 1],  # set header
                        na_values='---',  # null values in excel file
                        index_col=[0])  # set index column
divorce = divorce.stack([0, 1]).reset_index()  # reshape data by stacking to long, then reset index to new index

divorce.rename(columns={divorce.columns[0]: 'State',  # rename columns, first column past index renamed to State
                        divorce.columns[1]: 'left',  # second column renamed to left, for leftovers, column is dropped
                        divorce.columns[2]: 'Year',  # third column renamed to Year
                        divorce.columns[3]: 'Divorce Rate'}  # fourth column set to Divorce Rate
               , inplace=True)  # true so that we don't have to set school = (copy we are returning)

divorce.drop(columns=['left'], inplace=True)  # column is dropped, not needed

divorce.to_excel(excel_writer='cleaned data/divorce_cleaned_in_python.xls',  # read dataframe to excel, set file name
                 sheet_name='divorce rates',  # sheet named 'divorce rates'
                 na_rep='null',  # treat n/a as null
                 index=False)  # don't include pandas index




#### #### #### #### #### #### start unemployment cleaning #### #### #### #### #### ####3
unemployment = pd.read_excel('data no meta\Unemployment rate by state 2000-2017_no_meta.xls',
                             # read in the data to pandas dataframe, ready file
                             header=[0],  # set header
                             na_values='N/A',  # null values in excel file
                             index_col=[1])  # set index column

unemployment.drop(columns=['Fips'], inplace=True)
unemployment.drop(columns=['MOE'], inplace=True)
unemployment = unemployment.reset_index()

unemployment.to_excel(excel_writer='cleaned data/unemployment_cleaned_in_python.xls',
                      # read dataframe to excel, set file name
                      sheet_name='unemployment rates',  # sheet named 'divorce rates'
                      na_rep='null',
                      index=False)  # treat n/a as null


#### #### #### #### #### #### start party affiliation cleaning #### #### #### #### #### ####4

partyAffiliation = pd.read_excel('data no meta/Party_ID_1939-2014_no_meta.xlsx',
                             # read in the data to pandas dataframe, ready file
                             header=[0],  # set header
                             na_values=' ',  # null values in excel file
                             index_col=[0])  # set index column

partyAffiliation = partyAffiliation.reset_index()

partyAffiliation.to_excel(excel_writer='cleaned data/party_ID_cleaned_in_python.xls',
                      # read dataframe to excel, set file name
                      sheet_name='US party affiliation',  # sheet named 'US party affiliation'
                      na_rep='null',
                      index=False)  # treat n/a as null




#### #### #### #### #### ####   start income cleaning   #### #### #### #### #### #### ####5

incomeCur = pd.read_excel("data no meta\h08_no_meta.xlsx",
                       skiprows=1,
                       header = [0,1],
                       skipfooter=54,
                       index_col=[0])

incomeCur = incomeCur.stack([0]).reset_index()

incomeCur.rename(columns={incomeCur.columns[0] : 'State',
                       incomeCur.columns[1] : 'Year',
                       incomeCur.columns[2] : 'Current Median Income',
                       incomeCur.columns[3] : 'Current Standard Error'}
            , inplace=True)

incomeCur['Year'].replace(regex=True,inplace=True,to_replace=r'\([0-9]*\)|\([^)]*\)',value=r'')
incomeCur['Year'] = incomeCur.Year.astype(int)

income = pd.read_excel("data no meta\h08_no_meta.xlsx",
                       skiprows=56,
                       header = [0,1],
                       index_col=[0])

income = income.stack([0]).reset_index()

income.rename(columns={income.columns[1] : 'drop',
                       income.columns[2] : '2017 Median Income',
                       income.columns[3] : '2017 Standard Error'}
            , inplace=True)

income.drop(columns=['drop','level_0'], axis=1, inplace=True)

totalIncomes = pd.concat([incomeCur, income], axis=1, sort=False)

totalIncomes.to_excel(excel_writer='cleaned data/total_income_cleaned_in_python.xls',  # read dataframe to excel, set file name
                   sheet_name='2017 median income rates',  # sheet named 'median income rates'
                   index=False)  # don't include pandas index

#### #### #### #### #### ####   start birthrate cleaning   #### #### #### #### #### #### ####6

df = pd.read_csv("data no meta\NCHS_-_Births_and_General_Fertility_Rates__United_States_no_meta.csv",
                         # read in the data to pandas dataframe, ready file
                         header=[0],  # set header
                         na_values=' ',)  # null values in excel file

df.to_excel(excel_writer='cleaned data/birthrate_cleaned_in_python.xls',  # read dataframe to excel, set file name
                  sheet_name='birth rates',  # name sheet
                  index=False)  # don't include pandas index



########################cleaning Migration/Mobility#########################7

# Read in .xlsx file
df = pd.read_excel("data no meta\migration.xlsx",  # Read in file
                   header=[0, 1])  # Moves the headers to the top left corner

df = df.dropna(how='all')
df.columns = df.columns.get_level_values(0)
df = df.dropna(how='any')
df = df.reset_index()

df.drop(columns=['index'], axis=1, inplace=True)


# Write to .xls file
df.to_excel(excel_writer='cleaned data/Migration_cleaned_in_python.xlsx',  # name output
            sheet_name='test1',  # name sheet
            na_rep='null',  # how to represent null values
            index=False)  # Do not keep the index


#############################Cleaning Health Insurance##########################
df = pd.read_excel('data no meta\Health Insurance Coverage Type by Family Income and Age 2008-2017_no_meta.xlsx',#Read in file
                   usecols=9,#Use all 9 columns for dataframe
                   na_values = 'N/A')#Null values are labeded N/A

df['Number'] = df['Data']#Make new column from moving number of people value

df.Number = df.Number.shift(-1)#Shift Number column up by one position

df = df.iloc[::2]#Remove every other row
#Drop Data Type column, redundant with new column
df = df.drop(['Data Type'], axis = 1)
df.rename(index= str, columns = {'Data':'Percent'}, inplace=True)#Rename column

#Write to .xls file
df.to_excel(excel_writer='cleaned data/Health_Insurance_cleaned_by_python.xlsx', #name output
                sheet_name='HealthInsuranceRates',#name sheet
                na_rep='null', #how to represent null values
                index=False) # Do not keep the index



#################################Clean State Crimes###############################
# get data file names
path =r'CrimesByState'
filenames = glob.glob(path + "/*.csv")

dfs = []
for filename in filenames:
    df = pd.read_csv(filename,error_bad_lines=False,
                       skiprows=9, #Skips metadata in rows 1-0
                       skipfooter=18) # Skips metadata on the bottom
    df = df.drop(columns = ['Revised rape rate /2','Unnamed: 12'], axis = 1) #Drop Rows
    df['State'] = os.path.basename(filename)#Make state column
    df['State'] = df['State'].map(lambda x: x.rstrip('.csv'))#remove csv
    dfs.append(df)
    
# Concatenate all data into one DataFrame
big_frame = pd.concat(dfs, ignore_index=True)

big_frame.to_excel(excel_writer='cleaned data/State_Crime_cleaned_by_python.xlsx', #name output
                sheet_name='test1',#name sheet
                na_rep='null', #how to represent null values
                index= False) # Do not keep the index
