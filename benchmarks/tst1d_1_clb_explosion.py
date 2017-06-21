# ----------------------------------------------------------------------------------------
# 					SIMULATION PARAMETERS FOR THE PIC-CODE SMILEI
# ----------------------------------------------------------------------------------------

import math
# resolution
resx = 100.0
rest = 110.0
# plasma length
L = 2.0*math.pi

Main(
    geometry = "1d3v",
    interpolation_order = 2,
    
    cell_length = [L/resx],
    sim_length  = [3.0*L],
    
    number_of_patches = [ 4 ],
    
    timestep = L/rest,
    sim_time = 10.0 * math.pi,
    
    clrw = 1,
    
    EM_boundary_conditions = [ ['silver-muller'] ],
    
    random_seed = 0
)

Species(
	species_type = "charges",
	position_initialization = "random",
	momentum_initialization = "cold",
	n_part_per_cell = 100,
	mass = 1836.0,
	charge = 1.0,
	nb_density = trapezoidal(1., xvacuum=L, xplateau=L),
	boundary_conditions = [
		["stop", "stop"],
	],
)

DiagFields(
	every = int(rest/10.),
	fields = ['Ex','Rho_charges']
)

DiagScalar(
	every = 1
)


DiagParticleBinning(
	output = "density",
	every = 50,
	species = ["charges"],
	axes = [
		["p", 0., 10., 10],
	]
)

