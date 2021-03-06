import numpy as np
import sys

sys.path.append( '../../pkg' )
import pymod_indx, pymod_data, pymod_plot

# dat_idx = [ pymod_indx.idx_ppar( pymod_indx.directions_3, 
#                                 [-1, 1, 1], "z" ) ]

dat_idx = [[4, '[-1, 1, 1] in z-axis']]
fun_idx = [ lambda x: np.imag(x) ]

t = np.loadtxt( "../../res/time.dat" )
data = np.loadtxt( "res/ppar_1d_1_0.dat" )

handle, legend = [], []
ax = pymod_plot.plot_1d_init()

pymod_data.plot_signal_1d( t, data, dat_idx, fun_idx, handle, 
                         legend, ax, t0=-80, lim=[-50.0, 392], 
                         lbl="", padding=.0 )

pymod_plot.plot_draw( handle, legend, ax, 
                      xlabel=r"Freq. (cm$^{-1}$)",
                      ylabel=r"Signal (arb.)", 
                      title=r"Spectrum" )#,
#xlim=[-80000, 8000] )
