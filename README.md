# Description
Calculation of nonlinear spectroscopy from non-perturbative propagation of density matrix defined in spectral representation.

# Applications
For example, 2D third-order spectra can be obtained for photon-echo experiments.

# Reference
1. T. Mančal, A. V. Pisliakov, and G. R. Fleming, The Journal of Chemical Physics 124, 234504 (2006).
2. B. Brüggemann, P. Kjellberg, and T. Pullerits, Chemical Physics Letters 444, 192 (2007).

# Quick Startup

Before starting up, you need to set `Makefile.in` to make sure it is compilable.
The options to check are `CC`, `CFLAGS` and `LFLAGS`.
The program requires following dependencies,
* BLAS and LAPACK - Matrix inverse is used for Seidner's method
* GSL - Too lazy to write my own ODE solver
* MPICH2 - neither am I that patient to wait for results...
* libconfig - used to read `parameters.cfg` with nice format.
  But probably I will try JSON soon.

Several templates have already been there so just choose the suitable one and
comment out all the others. Then you can check it by follow the next explanations
step by step.

## 1D Nonlinear spectroscopy for single molecule (Seidner's method):
This is the option you can play on a destop machine.

* In file `src/Makefile`, set
  `SRC = seidner_main_single.cc`
* In file `parameters.cfg`, set
  `esmb.n_esmb = 1`,
  `mvar.ny = 1`,
  `pols.ppar_calc_method = "seidner"`
* Be sure you create the folder `./res` to store results
* Run `./test`
* After the main program exits, create folder `./fig` to store image files. Then run
  `python plot_ppar.py` to see nonlinear signals in different directions. The index in
  file name specified in the script `plot_ppar.py` suggest the direction of the signal,
  e.g., 37 indicates the wave vector direction of [-1, 1, 1], whose correspondence
  can be found in file `parameters.cfg`. `coo2` in the file name is for z-direction
  of the emitting field.

## 2D Nonlinear spectroscopy for single molecule (Seidner's method):
This option should be run on nodes with MPI avaiable. Something like 20 nodes are good.
You can configure the required number of nodes by just modifying
`nohup mpirun -n NUMBER ./test &` in file `./Makefile`

* In file `src/Makefile`, set
  `SRC = main_mpi.cc`
* In file `parameters.cfg`, set
  `esmb.n_esmb = 1`,
  `mvar.ny = 20`,
  `pols.ppar_calc_method = "seidner"`
* Be sure you create the folder `./res` to store results before running.
* Run `make run`
* After the main program exists, go to `ana/seidner`, `make`, then run `./test`.
  Be sure `res` is also present in this folder.
* Check result by running `python plot_ppar_2d.py`. The naming convention is simlar like
  that in 1D case. Enjoy!

# Code Specification

Array of polarization:
Generic: pol[nx][n_dpl][n_dim]
Seidner: pol[n_phase][nx][n_dpl][n_dim]
