import requests as r

class dotdict(dict):
    __getattr__ = dict.get

    def __repr__(self):
        return "{} {} \n ".format(self['value'],self['units'])

#Constants
planck_constant = dotdict(r.get("http://constants.datanab.net/physics/planck_constant_json").json())
"""Planck's constant."""

standard_gravity = dotdict(r.get("http://constants.datanab.net/physics/standard_gravity_json").json())
"""Earth's gravity at the surface."""

electron_mass = dotdict(r.get("http://constants.datanab.net/physics/electron_mass_json").json())
"""The mass of the electron."""

vacuum_impedance = dotdict(r.get("http://constants.datanab.net/physics/characteristic_impedance_of_vacuum_json").json())
"""The impedance of a perfect vacuum."""

vacuum_permittivity = dotdict(r.get("http://constants.datanab.net/physics/vacuum_permittivity_json").json())
"""The permittivity of a perfect vacuum."""

vacuum_permeability = dotdict(r.get("http://constants.datanab.net/physics/vacuum_permeability_json").json())
"""The permeability of a perfect vacuum."""
