# a. merge
full = pd.merge(pop, prices_long, on=['date','municipality'], how='left')
full.sort_values(['municipality','date'], inplace=True)

# b. take logs
full['log_population'] =  np.log(full['population'])
full['log_price'] =  np.log(full['price'])

full[['d_log_population','d_log_price']] = full.groupby('municipality')[['log_population','log_price']].diff(1)

# c. figur 1: log differences
ax = full.plot(x = 'd_log_population', y = 'd_log_price', kind = 'scatter',
               c='log_population',cmap='Blues',alpha=0.5); 

ax.set_xlabel('log difference in population') 
ax.set_ylabel('log difference in price');