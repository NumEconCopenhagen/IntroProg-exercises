# Q6
I = (dt_true['income'] < 0.5)
dt_true.loc[I, ['consumption']] = 0.5
dt_true['consumption'].mean()