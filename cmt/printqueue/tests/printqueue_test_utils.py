#! /usr/bin/env python

import os
import numpy as np


def assert_isfile_and_remove(filename):
    if os.path.isfile(filename):
        os.remove(filename)
    else:
        raise AssertionError('%s is not a file' % filename)


class UniformRectilinearGridPort(object):
    def __init__(self):
        self._shape = (4, 5)
        self._spacing = (1., 2.)
        self._origin = (0., 1.)
        self._values = {
            'landscape_surface__elevation': np.ones(self._shape),
            'sea_surface__temperature': np.zeros(self._shape),
            'sea_floor_surface_sediment__mean_of_grain_size':
                np.zeros(self._shape),
            'air__density': np.zeros(self._shape),
            'glacier_top_surface__slope': np.zeros(self._shape),
        }

    def get_grid_shape(self, var_name):
        return self._shape

    def get_grid_spacing(self, var_name):
        return self._spacing

    def get_grid_origin(self, var_name):
        return self._origin

    def get_grid_values(self, var_name):
        return self._values[var_name]


