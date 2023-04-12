import copy
import numpy as np
import time
from utils import *
import openmm as mm
import openmm.unit as u
from tqdm import tqdm
from sys import stdout
from mdtraj.reporters import HDF5Reporter
from openmm.app import PDBFile, PDBxFile, ForceField, Simulation, PDBReporter, PDBxReporter, DCDReporter, StateDataReporter, CharmmPsfFile

# 0. Generate some initial structure
N_beads=100
points = line(N_beads)
write_mmcif(points,'init_struct.cif')
generate_psf(N_beads,'LE_init_struct.psf')

# 1. Define System
pdb = PDBxFile('init_struct.cif')
forcefield = ForceField('forcefields/classic_sm_ff.xml')
system = forcefield.createSystem(pdb.topology, nonbondedCutoff=1*u.nanometer)
integrator = mm.LangevinIntegrator(310, 0.05, 100 * mm.unit.femtosecond)

# 2. Define the forcefield
# 2.1. Harmonic bond borce between succesive beads
bond_force = mm.HarmonicBondForce()
system.addForce(bond_force)
for i in range(system.getNumParticles() - 1):
    bond_force.addBond(i, i + 1, 0.1, 300000.0)
bond_force.addBond(10, 70, 0.1, 300000.0) # connect bead 10 with bead 70

# 2.2. Harmonic angle force between successive beads so as to make chromatin rigid
angle_force = mm.HarmonicAngleForce()
system.addForce(angle_force)
for i in range(system.getNumParticles() - 2):
    angle_force.addAngle(i, i + 1, i + 2, np.pi, 500)

# 3. Minimize energy
simulation = Simulation(pdb.topology, system, integrator)
simulation.reporters.append(StateDataReporter(stdout, 10, step=True, totalEnergy=True, potentialEnergy=True, temperature=True))
simulation.reporters.append(DCDReporter('stochastic_LE.dcd', 10))
simulation.context.setPositions(pdb.positions)
simulation.minimizeEnergy(tolerance=0.001)
state = simulation.context.getState(getPositions=True)
PDBxFile.writeFile(pdb.topology, state.getPositions(), open('minimized.cif', 'w')) # save minimized file

# 4. Run md simulation
simulation.context.setVelocitiesToTemperature(310, 0)
simulation.step(10000)
state = simulation.context.getState(getPositions=True)
PDBxFile.writeFile(pdb.topology, state.getPositions(), open('after_sim.cif', 'w')) # save minimized file
