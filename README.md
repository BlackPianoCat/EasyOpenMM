# EasyOpenMM
An easy openMM example.

## Description
In this repo you can see an easy example code of OpenMM. To run this code you need to have installed OpenMM library https://openmm.org/ in your python environment. In `sim.py` you can see the main file for our simulation framework. In this simulation there are two basic forces that connect adjacent beads: a harmonic bond force that connects beads $i$ with $i+1$ and a harmonic angle force that is applied in the pairs of atoms $i-1$ with $i$ and $i$ with $i+1$. We use langevin integrator to minimize the energy, which means that we assume that our polymer is inside a viscous fluid. Additionally, there is a molecular dynamics part where we set a random velocity field to the atoms of the polymer and we can see how the function changes over time.

An easy way to vizualize the results of the simulation is by the software UCSF Chimera: https://www.cgl.ucsf.edu/chimera/download.html.

## Tasks
In this section I will write the tasks that you will have to do every week, and it will be updated each week.

1. Run the script and load `.cif` files with in UCSF Chimera. Additionally, find out how you can vizualize the video of MD simulation with the pair of `.psf` and `.dcd` file in UCSF Chimera. What is the difference between minimizing the initial structure in respect to a forcefield and running molecular dynamics simulation?
2. Play with the temperature, drug coefficient and step of your integrator. Can you summarize the conclusions of your results?
3. What other integrators exist in OpenMM? Implement some of them and try to understand the differences in their implementation and how affect the results?
4. Implement some additional initial structures: circle, helix, random walk, self avoiding random walk polymer, or any other geometrical structure you like. Implement it in the `utils.py` file in a similar way as it is implemented the `line()` function which draws a linear polymer.
