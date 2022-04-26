def v1_alt(c1,m1,rho,beta,r,Delta,v2_interp):
    
    # a. expected v2 value
    Ra = (1+r)*(m1-c1)
    v2 = 0
    y2s = [1-np.sqrt(Delta),1-Delta,1+Delta,1+np.sqrt(Delta)]
    probs = [0.1,0.4,0.4,0.1]
    for y2,prob in zip(y2s,probs):
        m2 = Ra + y2
        v2 += prob*v2_interp([m2])[0]
        
    # b. total value
    return utility(c1,rho) + beta*v2

m1_vec_alt,c1_vec_alt = solve(rho,beta,r,Delta,nu,kappa,v1_alt)

# plot
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.plot(m1_vec,c1_vec,label='original')
ax.plot(m1_vec_alt,c1_vec_alt,label='new')
ax.legend(loc='upper left')
ax.set_xlabel('$m_1$')
ax.set_ylabel('$c_1$')
ax.set_title('consumption function in periode 1')
ax.set_xlim([0,4])
ax.set_ylim([0,2.5]);