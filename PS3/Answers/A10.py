def assets_row_by_row(x,R,Y):
    return R*(x['inc']-x['con'])+Y
    
def assets_all_at_once(income,consumption,R,Y):
    return R*(income-consumption)+Y

def assets_adj(assets,R,Y):
    assets *= R
    assets += Y

R = 1.2 # return rate
Y = 1 # income
dt_true['assets_1'] = R*(dt_true['inc']-dt_true['con'])+Y
dt_true['assets_2'] = dt_true.apply(assets_row_by_row,axis=1,args=(R,Y))
dt_true['assets_3'] = assets_all_at_once(dt_true['inc'].values,dt_true['con'].values,R,Y)
dt_true['assets_4'] = dt_true['inc']-dt_true['con']
assets_adj(dt_true['assets_4'],R,Y)

dt_true.head()