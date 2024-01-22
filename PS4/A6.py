# c. figur 2: mean log differences
mean_diff = lambda x: np.mean(x.diff())
full_grouped = full.groupby('municipality').agg({'log_population':[mean_diff,'last'],'log_price':mean_diff})
full_grouped.columns = ['md_log_population','last_log_population','md_log_price']

ax = full_grouped.plot(x = 'md_log_population', y = 'md_log_price', kind = 'scatter',
                       c='last_log_population',cmap='Blues'); 
ax.set_xlabel('within-municipality mean log difference in population')
ax.set_ylabel('within-municipality mean log difference in price',fontsize=10); 