import requests as r

class dotdict(dict):
    """dot.notation access to dictionary attributes"""
    __getattr__ = dict.get

#Constants
planck_constant = dotdict(r.get("http://constants.datanab.net/physics/planck_constant_json").json())
"""int: Module level variable documented inline.

The docstring may span multiple lines. The type may optionally be specified
on the first line, separated by a colon.
"""

standard_gravity = dotdict(r.get("http://constants.datanab.net/physics/standard_gravity_json").json())

electron_mass = dotdict(r.get("http://constants.datanab.net/physics/electron_mass_json").json())

vacuum_impedance = dotdict(r.get("http://constants.datanab.net/physics/characteristic_impedance_of_vacuum_json").json())

vacuum_permittivity = dotdict(r.get("http://constants.datanab.net/physics/vacuum_permittivity_json").json())

vacuum_permeability = dotdict(r.get("http://constants.datanab.net/physics/vacuum_permeability_json").json())
