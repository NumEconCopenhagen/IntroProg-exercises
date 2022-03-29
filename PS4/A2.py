merged_true = pd.merge(nah1_true,pop,how='left',on=['year'])
merged_true.sample(10)