# EasyOpenMM
An easy openMM example.

Please focus your attention on `utils.py` file.

## Description
In this repo you can see an easy example code of OpenMM. To run this code you need to have installed OpenMM library https://openmm.org/ in your python environment. In `sim.py` you can see the main file for our simulation framework. In this simulation there are two basic forces that connect adjacent beads: a harmonic bond force that connects beads $i$ with $i+1$ and a harmonic angle force that is applied in the pairs of atoms $i-1$ with $i$ and $i$ with $i+1$. We use langevin integrator to minimize the energy, which means that we assume that our polymer is inside a viscous fluid. Additionally, there is a molecular dynamics part where we set a random velocity field to the atoms of the polymer and we can see how the function changes over time.

An easy way to vizualize the results of the simulation is by the software UCSF Chimera: https://www.cgl.ucsf.edu/chimera/download.html.

## Tasks
In this section I will write the tasks that you will have to do every week, and it will be updated each week.

Having this repository as template:

1. Run the script and load `.cif` files with in UCSF Chimera. Additionally, find out how you can vizualize the video of MD simulation with the pair of `.psf` and `.dcd` file in UCSF Chimera. What is the difference between minimizing the initial structure in respect to a forcefield and running molecular dynamics simulation?
2. Play with the temperature, drug coefficient and step of your integrator. Can you summarize the conclusions of your results?
3. What other integrators exist in OpenMM? Implement some of them and try to understand the differences in their implementation and how affect the results?
4. Implement some additional initial structures: circle, helix, random walk, self avoiding random walk polymer, or any other geometrical structure you like. Implement it in the `utils.py` file in a similar way as it is implemented the `line()` function which draws a linear polymer.
5. What happens if you change the temperature $T$ of the simulation? Note that there are two temperatures in the simulation: in langevin integrator, and in random velocity field. Keep both of them equal during the simulation.
6. Let's focus on the loop force that connects atom 10 with atom 70. Implement a separate force `loop_force()` responsible for long range bonds that will be a separate class from `bond_force()` that connects adjacent beads. Can you implement a script where this force will change during the simulation? Try to make it change like (10,70),(11,69),(12,68),(13,67),(14,66),.... To achieve this goal, define a molecular simulation step (i.e. step=100) and try to change the parameters of loop extrusion force during  each step of the molecular simulation. How the resulting video depends on the simulation step?
7. Implement Leaonard-Jones potential. To do that use custom non bonded force of OpenMM http://docs.openmm.org/latest/api-python/generated/openmm.openmm.CustomNonbondedForce.html. Try to tune the parameters of Leonard-Jones potential so as to make the simulation not to blow up. (note: take care of what integration step you use, it can be that the simulation would blow up if the step is too big).
8. Now keep `loop_force()` fixed over time, and try to see what happens if you add three fixed loops implemented as harmonic bonds (i.e. (10,70),(20,30),(80,90)). Generalize it for $N$ loops.
9. Comment the previously defined Leonard-Jones potential, and let's try an easier case. Let's define Leonard_Jones potential as, $$V_{LJ}=\epsilon \left(\frac{\sigma_{1}\sigma_{2}}{r}\right)^{\alpha}$$. This means that for now we are focusing in the repelling part of the Leonard-Jones potential. Play with the different values of $\alpha$.
10. Now do the following two plots, which will help you to do some diagnostics so as to understand if your simulation works well.

    a. Plot the distance between $i$ and $j$ as a function of time. Where $i$ and $j$ are the beads which are connected by the loop force.
    
    b. Use the function `distance.cdist()`  of `scipy.spatial`, so as to create a matrix $N\times N$ with the all versus all distances between atoms of your polymer. First plot the matrix as a heatmap for the minimized structure, and then try to create a video, which will show how the all versus all distance heatmap changes over time.
    
    c. Plot the average (over simulation time) distance heatmap, and the variance (over simulatiomn time) of distance heatmaps.
    
11. Write the algorithm the as a class. This class should have an `init` function where the most important parameters of the simulation are determined. It should have a function where the forces are determined, and another one class for energy minimization or molecular simulation.
12. Find the `.bedpe` file in the github repository and create a function that reads it as a pandas dataframe and it reades the anchors. This function should read the loops for a paricular chromosome and region, and downgrade them into appropriate resolution so as to fit the dimension of the polymer. The output of this function should be a numpy array with left and right side anchors.
13. Modify your simulation class, so as to take these loops as input and run a simulation for the loops specified from the experiment.
14. Download the `.hic` data and `.bedpe` for CTCF ChIA-PET for GM12878 from ENCODE https://www.encodeproject.org/. Keep the anchors with the higher PET-count. Moreover download Hi-C data (like the ones in the repository) for the same cell-line GM12878. Check the differences between them and try to create models for both kinds of data.
15. Install Juicerbox and vizualize the `.hic` heatmaps and the loops to have better idea what is going on: https://github.com/aidenlab/Juicebox.

New tasks:
16. Try to make loop extrusion force dependent on the value of the PET-count, so as to have closer distance when the PET-count is higher and bigger distance when the PET-count is lower. Experiment and implement your own function for that. 
