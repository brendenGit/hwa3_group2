import pandas as pd                                                     # import libs

#### #### #### #### #### ####   start marriage cleaning   #### #### #### #### #### #### ####
marriage = pd.read_excel('data no meta/state-marriage-rates-90-95-99-17_no_meta.xlsx',  # read in the data to pandas dataframe, ready file
                         header=[0, 1],  # set header
                         na_values='---',  # null values in excel file
                         index_col=[0])  # set index column
marriage = marriage.stack([0,1]).reset_index()                          # reshape data by stacking to long, then reset index to new index

marriage.rename(columns={marriage.columns[0]: 'State',                  # rename columns, first column past index renamed to State
                         marriage.columns[1]: 'left',                   # second column renamed to left, for leftovers, column is dropped
                         marriage.columns[2]: 'Year',                   # third column renamed to Year
                         marriage.columns[3]: 'Marriage Rate'}          # fourth column set to Marriage Rate
                , inplace=True)                                         # true so that we don't have to set school = (copy we are returning)

marriage.drop(columns=['left'] ,inplace=True)                           # column is dropped, not needed

marriage.to_excel(excel_writer='cleaned data/marriage_cleaned_in_python.xls',   # read dataframe to excel, set file name
                sheet_name='marriage rates',                            # sheet named 'marriage rates'
                na_rep='null',                                          # treat n/a as null
                index=False)                                            # don't include pandas index


#### #### #### #### #### #### start divorce cleaning #### #### #### #### #### ####
divorce = pd.read_excel('data no meta\state-divorce-rates-90-95-99-17_no_meta.xlsx',  # read in the data to pandas dataframe, ready file
                         header=[0, 1],  # set header
                         na_values='---',  # null values in excel file
                         index_col=[0])  # set index column
divorce = divorce.stack([0,1]).reset_index()                          # reshape data by stacking to long, then reset index to new index

divorce.rename(columns={divorce.columns[0]: 'State',                  # rename columns, first column past index renamed to State
                         divorce.columns[1]: 'left',                   # second column renamed to left, for leftovers, column is dropped
                         divorce.columns[2]: 'Year',                   # third column renamed to Year
                         divorce.columns[3]: 'Divorce Rate'}          # fourth column set to Divorce Rate
                , inplace=True)                                         # true so that we don't have to set school = (copy we are returning)

divorce.drop(columns=['left'] ,inplace=True)                           # column is dropped, not needed

divorce.to_excel(excel_writer='cleaned data/divorce_cleaned_in_python.xls',   # read dataframe to excel, set file name
                sheet_name='divorce rates',                            # sheet named 'divorce rates'
                na_rep='null',                                          # treat n/a as null
                index=False)                                            # don't include pandas index

#### #### #### #### #### #### start unemployment cleaning #### #### #### #### #### ####
unemployment = pd.read_excel('data no meta\Unemployment rate by state 2000-2017_no_meta.xls',  # read in the data to pandas dataframe, ready file
                         header=[0],  # set header
                         na_values='N/A',  # null values in excel file
                         index_col=[1])  # set index column

unemployment.drop(columns=['Fips'] ,inplace=True)
unemployment.drop(columns=['MOE'] ,inplace=True)
unemployment = unemployment.reset_index()

unemployment.to_excel(excel_writer='cleaned data/unemployment_cleaned_in_python.xls',   # read dataframe to excel, set file name
                sheet_name='unemployment rates',                            # sheet named 'divorce rates'
                na_rep='null',
                index=False)                                          # treat n/a as null
