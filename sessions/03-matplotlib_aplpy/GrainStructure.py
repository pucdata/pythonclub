class Grain_Structure:
    """Class which contains the grains structure that will be analyzed"""
    def __init__(self):
        self.grains = None
        self.grains_reverse = None
        self.areas = None
        self.grains_ids = None
        self.num_grains = None
        self.num_junctions = None
        self.num_boundaries = None
        self.B = None
        self.Bref = None
        self.xi = None
        self.l_cheb = None
        self.dl_cheb = None
        self.N_gauss = None
        self.AL = None
        self.coordinates = None
        self.interior_points_coordinates = None
        self.neighbors = None
        self.shifts = None
        self.junctions_ids = None
        self.interior_points_ids = None
        self.nint = None
        self.num_ip = None
        self.F = None
        self.used_junctions = None


class Boundary_Data:
    """Class which cointains boundary interpolators and related"""
    def __init__(self):
        self.x = None
        self.y = None
        self.lx = None
        self.ly = None
        self.dlx = None
        self.dly = None
