import batman
import numpy as np
import matplotlib.pyplot as plt
from pylab import *
from matplotlib import rc

rc('font',**{'family':'sans-serif','sans-serif':['Arial']})
matplotlib.rcParams.update({'font.size':14})

params = batman.TransitParams()
params.t0 = 0
params.per = 4.3050011
params.rp = 0.86
params.a = 0.0531
params.inc = 87.9
params.ecc = 0
params.w = 0
params.u = [0.1, 0.3]
params.limb_dark = "quadratic"
   
t = np.linspace(-0.025, 0.025, 1000)  	#times at which to calculate light curve	
m = batman.TransitModel(params, t)      #initializes model

flux = m.light_curve(params)		#calculates light curve
plt.plot(t, flux)


plt.xlabel("Time from central transit (days)")
plt.ylabel("Relative flux")
#plt.ylim((0.975, 1.001))

plt.savefig("WASP_60_b_assignment1_taskF.png")

plt.show()
