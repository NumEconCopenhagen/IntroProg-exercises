# Q5
I = (dt_true['income'] > 1) & (dt_true['ratio'] > 0.7)
dt_true.loc[I].head()