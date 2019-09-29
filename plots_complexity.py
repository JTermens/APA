#--------------------------------------------------------------------
# COMPUTATIONAL COMPLEXITY PLOTS
#
# This code plots six different complexity bounds, O(f(n)), for the
# inputs [1,10,50,100]. Complexity bounds are computed with NumPy
# and plots are generated using MatPlotLib.
#
# Joan Térmens Cascalló,                  Last revision: Sep 29, 2019
#--------------------------------------------------------------------


import math
import numpy as np
import matplotlib.pyplot as plt

def plot_complexity(n):

    # Compute complexity functions

    fun_fact=[np.math.factorial(k) for k in n]
    fun_exp2=np.power(2,n)
    fun_sq=np.power(n,2)
    fun_lin=n
    fun_sqrt=np.sqrt(n)
    fun_log=np.log(n)

    # Use matplotlib to plot the previous fun_

    plt.figure(figsize=(8, 8), dpi=100) # Define size and definition
    plt.title('Complexity by outcome size', fontsize=15) # Title

    plt.xlim(0, max(n)) # X axis specifications:
    plt.xlabel('Outcome size, $n$',fontsize=12) # títol de l'eix x

    plt.ylim(0,2*max(n)) # Define Y axis analogously
    plt.ylabel('Complexity, $O(n)$',fontsize=12)

    # Plots

    plt.plot(n,fun_fact, label=r'$n!$', color='#e41a1c')
    plt.plot(n,fun_exp2, label=r'$2^n$', color='#377eb8')
    plt.plot(n,fun_sq, label=r'$n^2$', color='#4daf4a')
    plt.plot(n,fun_lin, label=r'$n$', color='#984ea3')
    plt.plot(n,fun_sqrt, label=r'$\sqrt{n}$', color='#ff7f00')
    plt.plot(n,fun_log, label=r'$\log{(n)}$', color='#ffff33')

    plt.legend(loc='upper right') # Legend location
    plt.show()

n=[1,10,50,100] # Input
plot_complexity(n)
