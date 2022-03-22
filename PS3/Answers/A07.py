# Q7
I = (dt_true['income'] < 0.5)
dt_true.loc[I, ['consumption']] = dt_true.loc[I, ['income']].values
dt_true['consumption'].mean()