import pandas as pd

data = pd.read_csv("D:/VSC/Python/python/Python/Pre-Processing/final.csv")
del data['hyperlink']
del data['temp_discovery_date']
del data['temp_mass']
del data['pl_name']
del data['default_flag']
del data['sy_snum']
del data['sy_pnum']
del data['discoverymethod']
del data['disc_year']
del data['disc_facility']
del data['soltype']
del data['pl_controv_flag']
del data['pl_refname']
del data['pl_orbper']
del data['pl_orbpererr1']
del data['pl_orbpererr2']
del data['pl_orbperlim']
del data['pl_orbsmax']
del data['pl_orbsmaxerr1']
del data['pl_orbsmaxerr2']
del data['pl_orbsmaxlim']
del data['pl_rade']
del data['pl_radeerr1']
del data['pl_radeerr2']
del data['pl_radelim']
del data['pl_radj']
del data['pl_radjerr1']
del data['pl_radjerr2']
del data['pl_radjlim']
del data['pl_bmasse']

print(data.shape)

data = data.rename({
    'host_name':'solar_system'
})
