dt_alt = dt_true.copy()

print(f'before: {dt_true.shape[0]} observations, {dt_true.shape[1]} variables')
dt_true.drop('ratio',axis=1,inplace=True)
I = dt_true['income'] > 1.5
dt_true.drop(dt_true[I].index,inplace=True)
dt_true.drop(dt_true.loc[:5].index,inplace=True)
print(f'after: {dt_true.shape[0]} observations, {dt_true.shape[1]} variables')

# alternative: keep where I is false
del dt_alt['ratio']
I = dt_alt['income'] > 1.5
dt_alt = dt_alt[~I]
dt_alt = dt_alt.iloc[5:,:]
print(f'after (alt): {dt_alt.shape[0]} observations, {dt_alt.shape[1]} variables')