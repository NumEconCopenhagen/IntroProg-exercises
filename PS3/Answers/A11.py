# a. load data set
nah1 = pd.read_excel('data/NAH1_pivoted.xlsx',skiprows=2)

# b. rename variables
rename_dict['Unnamed: 0'] = 'year'
nah1.rename(columns=rename_dict,inplace=True)

# c. remove rows where Y is nan
I = nah1['Y'].notna()
nah1 = nah1[I]

# d. correct year column data
I = nah1['year'].notna()
J = nah1['year'].isna()
nah1.loc[J,['year']] = nah1.loc[I,['year']].values

# e. only keep rows with '2010-prices, chained values'
I = nah1['Unnamed: 1'] == '2010-prices, chained values'
nah1 = nah1[I]

# f. only keep renamed variables
nah1 = nah1.loc[:,['year','Y','C','G','I','X','M']]
nah1