# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 08:08:44 2020

@author: buriona
"""

'''
Keep in mind the top left corner of the button is the anchor point
'''

forecasts = {}

config_name = 'ug'
map_center = (41.4, -109.85)
initial_zoom = 9
huc_level = 4
huc_filter = [1404]

regions = {
    'Upper Green': {
        'coords': [41.6, -110.1], 'huc-level': 6, 'anchor': (0,0)
    },

}

reservoirs = {
    'Flaming Gorge': {
        'coords': [40.91474, -109.42185], 'region': 'uc', 'anno': '', 'cap': 3749.0, 
        'id': 917, 'anchor': (0,-15), 'pop_dir': 'up',
        'sdis': 
            {'storage': 1718, 'elev': 1927, 'inflow': 1791, 'release': 1871}
    },

}
    

ug_config_name = 'ug'
ug_map_center = (41.6, -109.85)
ug_initial_zoom = 9
ug_huc_level = 4
ug_huc_filter = [1404, 140500]

ug_regions = {
    'Upper Green': {
        'coords': [41.6, -110.1], 'huc-level': 6, 'anchor': (0,0)
    },
    'Blacks Fork': {
        'coords': [41.3, -110.4], 'huc-level': 8, 'anchor': (0,0)
    },
    'Big Sandy': {
        'coords': [42.06, -109.64], 'huc-level': 8, 'anchor': (0,0)
    },
    'New Fork': {
        'coords': [42.9, -109.8], 'huc-level': 8, 'anchor': (0,0)
    },
    'Upper Green-Flaming Gorge Reservoir': {
        'coords': [41.12, -109.92], 'huc-level': 8, 'anchor': (0,0)
    },
    'Little Snake': {
        'coords': [41.05, -108.08], 'huc-level': 8, 'anchor': (0,0)
    },
    'Upper Yampa': {
        'coords': [40.53, -107.35], 'huc-level': 8, 'anchor': (0,0)
    },
    'Upper White': {
        'coords': [40.02, -107.85], 'huc-level': 8, 'anchor': (0,0)
    },
    
}

ug_reservoirs = {
    'Flaming Gorge': {
        'coords': [40.91474, -109.42185], 'region': 'uc', 'anno': '', 'cap': 3749.0, 
        'id': 917, 'anchor': (50,30), 'pop_dir': 'up',
        'sdis': 
            {'storage': 1718, 'elev': 1927, 'inflow': 1791, 'release': 1871}
    },
    'Fontenelle': {
        'coords': [42.02617, -110.06816], 'region': 'uc', 'anno': '', 'cap': 344.8, 
        'id': 916, 'anchor': (0,0), 'pop_dir': 'up',
        'sdis': 
            {'storage': 1717, 'elev': 1926, 'inflow': 1790, 'release': 1870}
    },
    'Eden': {
        'coords': [42.21665, -109.37087], 'region': 'uc', 'anno': '', 'cap': 13.164, 
        'id': 954, 'anchor': (0,-20), 'pop_dir': 'up',
        'sdis': 
            {'storage': 1752, 'elev': 1959, 'inflow': 1823, 'release': 1903}
    },
    'Big Sandy': {
        'coords': [42.24993, -109.42803], 'region': 'uc', 'anno': '', 'cap': 36.688, 
        'id': 936, 'anchor': (0,20), 'pop_dir': 'up',
        'sdis': 
            {'storage': 1734, 'elev': 1941, 'inflow': 1805, 'release': 1885}
    },
    'Meeks Cabin': {
        'coords': [41.01664, -110.58344], 'region': 'uc', 'anno': '', 'cap': 29.87, 
        'id': 944, 'anchor': (25,0), 'pop_dir': 'up',
        'sdis': 
            {'storage': 1742, 'elev': 1949, 'inflow': 1813, 'release': 1893}
    },
    'Stateline': {
        'coords': [40.98291, -110.39038], 'region': 'uc', 'anno': '', 'cap': 13.88, 
        'id': 949, 'anchor': (-25,0), 'pop_dir': 'up',
        'sdis': 
            {'storage': 1747, 'elev': 1954, 'inflow': 1818, 'release': 1898}
    }
}

ug_config = {
    ug_config_name: {
        'huc_level': ug_huc_level,
        'huc_filter': ug_huc_filter,
        'zoom': ug_initial_zoom, 
        'center': ug_map_center, 
        'reservoirs': ug_reservoirs, 
        'regions': ug_regions, 
        'forecasts': forecasts
    }
}     

pb_config_name = 'pb'
pb_map_center = (39.03, -110.83)
pb_initial_zoom = 9
pb_huc_level = 6
pb_huc_filter = [14060007, 14060009, 14070002, 14070003]

pb_regions = {
    'Lower Green': {
        'coords': [39.67, -111.53], 'huc-level': 6, 'anchor': (0,0)
    },
    'Upper Colorado-Dirty Devil': {
        'coords': [38.72, -111.86], 'huc-level': 6, 'anchor': (0,0)
    },
    'Price': {
        'coords': [39.57, -110.85], 'huc-level': 8, 'anchor': (0,0)
    },
    'San Rafael': {
        'coords': [39.06, -110.9], 'huc-level': 8, 'anchor': (0,0)
    },
    'Muddy': {
        'coords': [38.75, -111.2], 'huc-level': 8, 'anchor': (0,0)
    },
    'Fremont': {
        'coords': [38.45, -111.76], 'huc-level': 8, 'anchor': (0,0)
    }
}

pb_reservoirs = {
    'Huntington North': {
        'coords': [39.38458, -111.09082], 'region': 'uc', 'anno': '', 'cap': 1105.91, 
        'id': 956, 'anchor': (0,10), 'pop_dir': 'up',
        'sdis': 
            {'storage': 1754, 'elev': 1961, 'inflow': 1825, 'release': 1905}
    },
    'Joes Valley': {
        'coords': [39.2901, -111.27888], 'region': 'uc', 'anno': '', 'cap': 61.59, 
        'id': 932, 'anchor': (0,0), 'pop_dir': 'up',
        'sdis': 
            {'storage': 1730, 'elev': 1937, 'inflow': 1801, 'release': 1881}
    },
    'Scofield': {
        'coords': [39.77656, -111.05074], 'region': 'uc', 'anno': '', 'cap': 65.8, 
        'id': 931, 'anchor': (0,-10), 'pop_dir': 'up',
        'sdis': 
            {'storage': 1729, 'elev': 1936, 'inflow': 1800, 'release': 1880}
    }
}    

pb_config = {
    pb_config_name: {
        'huc_level': pb_huc_level,
        'huc_filter': pb_huc_filter,
        'zoom': pb_initial_zoom, 
        'center': pb_map_center, 
        'reservoirs': pb_reservoirs, 
        'regions': pb_regions, 
        'forecasts': forecasts
    }
} 
    
ub_config_name = 'ub'
ub_map_center = (40.2, -110.3)
ub_initial_zoom = 9
ub_huc_level = 6
ub_huc_filter = [14060003, 14060004, 14060005, 14060010]

ub_regions = {
    'Lower Green': {
        'coords': [40.4, -110.23], 'huc-level': 6, 'anchor': (0,0)
    },
    'Duchesne': {
        'coords': [40.42, -110.65], 'huc-level': 8, 'anchor': (0,0)
    },
    'Lower Green-Diamond': {
        'coords': [40.35, -109.56], 'huc-level': 8, 'anchor': (0,0)
    },
    'Strawberry': {
        'coords': [40.2, -110.815], 'huc-level': 8, 'anchor': (0,0)
    },
    'Lower Green-Desolation Canyon': {
        'coords': [39.86, -110.5], 'huc-level': 8, 'anchor': (0,0)
    },
}

ub_reservoirs = {
    'Soldier Creek': {
        'coords': [40.13564, -111.02659], 'region': 'uc', 'anno': '', 'cap': 1105.91, 
        'id': 962, 'anchor': (55,0), 'pop_dir': 'up',
        'sdis': 
            {'storage': 1760, 'elev': 1967, 'inflow': 1831, 'release': 1911}
    },
    'Starvation': {
        'coords': [40.19324, -110.44722], 'region': 'uc', 'anno': '', 'cap': 162.279, 
        'id': 928, 'anchor': (0,0), 'pop_dir': 'up',
        'sdis': 
            {'storage': 1726, 'elev': 1934, 'inflow': 1798, 'release': 1878}
    },
    'Steinaker': {
        'coords': [40.51456, -109.53275], 'region': 'uc', 'anno': '', 'cap': 36.148, 
        'id': 927, 'anchor': (0,-14), 'pop_dir': 'up',
        'sdis': 
            {'storage': 1725, 'elev': 1933, 'inflow': 1797, 'release': 1877}
    },
    'Red Fleet': {
        'coords': [40.57543, -109.42052], 'region': 'uc', 'anno': '', 'cap': 25.7, 
        'id': 960, 'anchor': (0,12), 'pop_dir': 'up',
        'sdis': 
            {'storage': 1758, 'elev': 1965, 'inflow': 1829, 'release': 1909}
    },
    'Moon Lake': {
        'coords': [40.57445, -110.50665], 'region': 'uc', 'anno': '', 'cap': 37.848, 
        'id': 930, 'anchor': (-30,0), 'pop_dir': 'up',
        'sdis': 
            {'storage': 1728, 'elev': 1935, 'inflow': 1799, 'release': 1879}
    },
    'Upper Stillwater': {
        'coords': [40.56565, -110.70044], 'region': 'uc', 'anno': '', 'cap': 31.382, 
        'id': 963, 'anchor': (30,0), 'pop_dir': 'up',
        'sdis': 
            {'storage': 1761, 'elev': 1968, 'inflow': 1832, 'release': 1912}
    },
    'Currant Creek': {
        'coords': [40.33841, -111.05821], 'region': 'uc', 'anno': '', 'cap': 15.464, 
        'id': 952, 'anchor': (0,0), 'pop_dir': 'up',
        'sdis': 
            {'storage': 1750, 'elev': 1957, 'inflow': 1821, 'release': 1901}
    }
}
  
ub_config = {
    ub_config_name: {
        'huc_level': ub_huc_level,
        'huc_filter': ub_huc_filter,
        'zoom': ub_initial_zoom, 
        'center': ub_map_center, 
        'reservoirs': ub_reservoirs, 
        'regions': ub_regions, 
        'forecasts': forecasts
    }
} 

gb_config_name = 'gb'
gb_map_center = (41.05, -112.1)
gb_initial_zoom = 9
gb_huc_level = 4
gb_huc_filter = [1601,160201,160202]

gb_regions = {
    'Bear': {
        'coords': [41.6, -112.75], 'huc-level': 4, 'anchor': (0,0)
    },
    'Upper Bear': {
        'coords': [41.66, -111.21], 'huc-level': 6, 'anchor': (0,0)
    },
    'Lower Bear': {
        'coords': [41.6, -112.31], 'huc-level': 6, 'anchor': (0,0)
    },
    'Provo': {
        'coords': [40.54, -111.75], 'huc-level': 8, 'anchor': (0,0)
    },
    'Jordan': {
        'coords': [40.7, -111.98], 'huc-level': 8, 'anchor': (0,0)
    },
    'Spanish Fork': {
        'coords': [40.1, -111.58], 'huc-level': 8, 'anchor': (0,0)
    },
    'Weber': {
        'coords': [41.1, -111.85], 'huc-level': 6, 'anchor': (0,0)
    },
    'Great Salt Lake': {
        'coords': [40.77, -112.5], 'huc-level': 4, 'anchor': (0,0)
    },
    
}

gb_reservoirs = {
    'Willard Bay': {
        'coords': [41.37738, -112.08339], 'region': 'uc', 'anno': '', 'cap': 222.273, 
        'id': 925, 'anchor': (0,0), 'pop_dir': 'up',
        'sdis': 
            {'storage': 1723, 'elev': 1932, 'inflow': 1796, 'release': 1876}
    },
    'Jordanelle': {
        'coords': [40.59833, -111.42304], 'region': 'uc', 'anno': '', 'cap': 311.0, 
        'id': 964, 'anchor': (0,0), 'pop_dir': 'up',
        'sdis': 
            {'storage': 1762, 'elev': 1969, 'inflow': 1833, 'release': 1913}
    },
    'Deer Creek': {
        'coords': [40.40837, -111.52908], 'region': 'uc', 'anno': '', 'cap': 150.161, 
        'id': 953, 'anchor': (0,0), 'pop_dir': 'up',
        'sdis': 
            {'storage': 1751, 'elev': 1958, 'inflow': 1822, 'release': 1902}
    },
    'Causey': {
        'coords': [41.29828, -111.58591], 'region': 'uc', 'anno': '', 'cap': 7.07, 
        'id': 938, 'anchor': (0,0), 'pop_dir': 'up',
        'sdis': 
            {'storage': 1736, 'elev': 1943, 'inflow': 1807, 'release': 1887}
    },
    'Lost Creek': {
        'coords': [41.18318, -111.39905], 'region': 'uc', 'anno': '', 'cap': 22.501, 
        'id': 942, 'anchor': (0,0), 'pop_dir': 'up',
        'sdis': 
            {'storage': 1740, 'elev': 1947, 'inflow': 1811, 'release': 1891}
    },
    'Echo': {
        'coords': [40.96412, -111.43239], 'region': 'uc', 'anno': '', 'cap': 73.94, 
        'id': 941, 'anchor': (-28,0), 'pop_dir': 'up',
        'sdis': 
            {'storage': 1739, 'elev': 1946, 'inflow': 1810, 'release': 1890}
    },
    'East Canyon': {
        'coords': [40.92027, -111.60099], 'region': 'uc', 'anno': '', 'cap': 49.510, 
        'id': 940, 'anchor': (28,0), 'pop_dir': 'up',
        'sdis': 
            {'storage': 1738, 'elev': 1945, 'inflow': 1809, 'release': 1889}
    },
    'Rockport': {
        'coords': [40.78944, -111.40263], 'region': 'uc', 'anno': '', 'cap': 115.075, 
        'id': 947, 'anchor': (0,0), 'pop_dir': 'up',
        'sdis': 
            {'storage': 1745, 'elev': 1952, 'inflow': 1816, 'release': 1896}
    },
    'Hyrum': {
        'coords': [41.62117, -111.86099], 'region': 'uc', 'anno': '', 'cap': 14.734, 
        'id': 957, 'anchor': (0,0), 'pop_dir': 'up',
        'sdis': 
            {'storage': 1755, 'elev': 1962, 'inflow': 1826, 'release': 1906}
    },
    'Newton': {
        'coords': [41.8998, -111.97562], 'region': 'uc', 'anno': '', 'cap': 5.374, 
        'id': 959, 'anchor': (0,0), 'pop_dir': 'up',
        'sdis': 
            {'storage': 1757, 'elev': 1964, 'inflow': 1828, 'release': 1908}
    },
}    
 
gb_config = {
    gb_config_name: {
        'huc_level': gb_huc_level,
        'huc_filter': gb_huc_filter,
        'zoom': gb_initial_zoom, 
        'center': gb_map_center, 
        'reservoirs': gb_reservoirs, 
        'regions': gb_regions, 
        'forecasts': forecasts
    }
} 

sj_config_name = 'sj'
sj_map_center = (37, -108.1)
sj_initial_zoom = 9
sj_huc_level = 4
sj_huc_filter = 1408

sj_regions = {
    'San Juan': {
        'coords': [37, -108.26], 'huc-level': 4, 'anchor': (0,0)
    },
    'Upper San Juan': {
        'coords': [37, -107], 'huc-level': 8, 'anchor': (0,0)
    },
    'Piedra': {
        'coords': [37.53, -107.34], 'huc-level': 8, 'anchor': (0,0)
    },
    # 'Blanco': {
    #     'coords': [38.7, -107.6], 'huc-level': 8, 'anchor': (0,0)
    # },
    'Animas': {
        'coords': [37.65, -107.8], 'huc-level': 8, 'anchor': (0,0)
    },
    'Middle San Juan': {
        'coords': [36.9, -109], 'huc-level': 8, 'anchor': (0,0)
    },
    'Chaco': {
        'coords': [36.45, -108.84], 'huc-level': 8, 'anchor': (0,0)
    },
    'Mancos': {
        'coords': [37.2, -108.7], 'huc-level': 8, 'anchor': (0,0)
    },
    'Montezuma': {
        'coords': [37.7, -109.28], 'huc-level': 8, 'anchor': (0,0)
    },
    'Chinle': {
        'coords': [36.8, -109.8], 'huc-level': 8, 'anchor': (0,0)
    },
    
}

sj_reservoirs = {
    'Navajo': {
        'coords': [36.80063, -107.61203], 'region': 'uc', 'anno': '', 'cap': 1701.3, 
        'id': 920, 'anchor': (0,0), 'pop_dir': 'up',
        'sdis': 
            {'storage': 1720, 'elev': 1929, 'inflow': 1793, 'release': 1873}
    },
    'Vallecito': {
        'coords': [37.37834, -107.57486], 'region': 'uc', 'anno': '', 'cap': 125.442, 
        'id': 933, 'anchor': (-85,-40), 'pop_dir': 'up',
        'sdis': 
            {'storage': 1731, 'elev': 1938, 'inflow': 1802, 'release': 1882}
    },
    'Lemon': {
        'coords': [37.39538, -107.66269], 'region': 'uc', 'anno': '', 'cap': 39.792, 
        'id': 934, 'anchor': (0,0), 'pop_dir': 'up',
        'sdis': 
            {'storage': 1732, 'elev': 1939, 'inflow': 1803, 'release': 1883}
    },
    'McPhee': {
        'coords': [37.57588, -108.57307], 'region': 'uc', 'anno': '', 'cap': 381.0, 
        'id': 958, 'anchor': (0,0), 'pop_dir': 'up',
        'sdis': 
            {'storage': 1756, 'elev': 1963, 'inflow': 1827, 'release': 1907}
    },
    'Nighthorse': {
        'coords': [37.22392, -107.91694], 'region': 'uc', 'anno': '', 'cap': 115.075, 
        'id': 3083, 'anchor': (0,0), 'pop_dir': 'up',
        'sdis': 
            {'storage': 14623, 'elev': 14621, 'inflow': 14617, 'release': 14620}
    },
    'Jackson': {
        'coords': [37.40186, -108.27342], 'region': 'uc', 'anno': '', 'cap': 115.075, 
        'id': 935, 'anchor': (0,0), 'pop_dir': 'up',
        'sdis': 
            {'storage': 1733, 'elev': 1940, 'inflow': 1804, 'release': 1884}
    },
}
 
sj_config = {
    sj_config_name: {
        'huc_level': sj_huc_level,
        'huc_filter': sj_huc_filter,
        'zoom': sj_initial_zoom, 
        'center': sj_map_center, 
        'reservoirs': sj_reservoirs, 
        'regions': sj_regions, 
        'forecasts': forecasts
    }
} 
    
gunn_config_name = 'gunn'
gunn_map_center = (38.5, -107.5)
gunn_initial_zoom = 9
gunn_huc_level = 6
gunn_huc_filter = 1402

gunn_reservoirs = {
    'Paonia': {
        'coords': [38.94919, -107.34347], 'region': 'uc', 'anno': '', 'cap': 15.522, 
        'id': 945, 'anchor': (-10,0), 'pop_dir': 'up',
        'sdis': 
            {'storage': 1743, 'elev': 1950, 'inflow': 1814, 'release': 1894}
    },
    'Ridgway': {
        'coords': [38.23636, -107.75914], 'region': 'uc', 'anno': '', 'cap': 82.98, 
        'id': 912, 'anchor': (20,0), 'pop_dir': 'up',
        'sdis': 
            {'storage': 1713, 'elev': 1922, 'inflow': 1786, 'release': 1860}
    },
    'Silver Jack': {
        'coords': [38.22692, -107.54041], 'region': 'uc', 'anno': '', 'cap': 13.0, 
        'id': 939, 'anchor': (-20,0), 'pop_dir': 'up',
        'sdis': 
            {'storage': 1737, 'elev': 1944, 'inflow': 1808, 'release': 1888}
    },
    'Taylor Park': {
        'coords': [38.81844, -106.60592], 'region': 'uc', 'anno': '', 'cap': 106.21, 
        'id': 948, 'anchor': (0,0), 'pop_dir': 'up',
        'sdis': 
            {'storage': 1746, 'elev': 1953, 'inflow': 1817, 'release': 1897}
    },
    'Blue Mesa': {
        'coords': [38.45305, -107.33677], 'region': 'uc', 'anno': '', 'cap': 829.5, 
        'id': 913, 'anchor': (-40,35), 'pop_dir': 'up',
        'sdis': 
            {'storage': 1714, 'elev': 1923, 'inflow': 1787, 'release': 1867}
    },
    'Morrow Point': {
        'coords': [38.45191, -107.53791], 'region': 'uc', 'anno': '', 'cap': 117.025, 
        'id': 914, 'anchor': (-10,-25), 'pop_dir': 'up',
        'sdis': 
            {'storage': 1715, 'elev': 1924, 'inflow': 1788, 'release': 1868}
    },
    'Crystal': {
        'coords': [38.51046, -107.62374], 'region': 'uc', 'anno': '', 'cap': 17.536, 
        'id': 915, 'anchor': (-10,10), 'pop_dir': 'up',
        'sdis': 
            {'storage': 1716, 'elev': 1925, 'inflow': 1789, 'release': 1869}
    },
}
    
gunn_regions = {
    'Gunnison': {
        'coords': [38.7, -107.6], 'huc-level': 4, 'anchor': (0,0)
    },
    'East-Taylor': {
        'coords': [39, -106.9], 'huc-level': 8, 'anchor': (0,0)
    },
    'Tomichi': {
        'coords': [38.5, -106.7], 'huc-level': 8, 'anchor': (0,0)
    },
    'Uncompahgre': {
        'coords': [38.5, -108.1], 'huc-level': 8, 'anchor': (0,0)
    },
    'Lower Gunnison': {
        'coords': [38.7, -108.5], 'huc-level': 8, 'anchor': (0,0)
    },
    'Pecos Headwaters': {
        'coords': [33, -105], 'huc-level': 8, 'anchor': (0,0)
    },
    'North Fork Gunnison': {
        'coords': [39.04, -107.74], 'huc-level': 8, 'anchor': (0,0)
    },
   
}

gunn_config = {
    gunn_config_name: {
        'huc_level': gunn_huc_level,
        'huc_filter': gunn_huc_filter,
        'zoom': gunn_initial_zoom, 
        'center': gunn_map_center, 
        'reservoirs': gunn_reservoirs, 
        'regions': gunn_regions, 
        'forecasts': forecasts
    }
} 

rg_config_name = 'rg'
rg_map_center = (35, -106)
rg_initial_zoom = 7
rg_huc_level = 2
rg_huc_filter = [1301, 1302, 1303, 1305, 1306, 140801, 140801]

rg_regions = {
    'Rio Grande': {
        'coords': [35.35, -107], 'huc-level': 2, 'anchor': (0,0)
    },
    'Upper Pecos': {
        'coords': [33.6, -105.3], 'huc-level': 6, 'anchor': (0,0)
    },
    'Rio Grande Headwaters': {
        'coords': [37.9, -106.65], 'huc-level': 6, 'anchor': (0,0)
    },
    'Rio Grande-Elephant Butte': {
        'coords': [34.7, -108.2], 'huc-level': 6, 'anchor': (0,0)
    },
    'Upper Rio Grande': {
        'coords': [36.9, -106.85], 'huc-level': 6, 'anchor': (0,0)
    },
    'Upper San Juan': {
        'coords': [37, -108.55], 'huc-level': 8, 'anchor': (0,0)
    },
}

rg_reservoirs = {
    'Elephant Butte': {
        'coords': [33.15, -107.2], 'region': 'uc', 'anno': '', 'cap': 2010.900, 
        'id': 1119, 'anchor': (0,0), 'pop_dir': 'up',
        'sdis': 
            {'storage': 2684, 'elev': 2685, 'inflow': 2686, 'release': 2688}
    },
    'Heron': {
        'coords': [36.6973, -106.6992], 'region': 'uc', 'anno': '', 'cap': 401.662, 
        'id': 2686, 'anchor': (-60,-30), 'pop_dir': 'up',
        'sdis': 
            {'storage': 19176, 'elev': 19175, 'inflow': None, 'release': 19609}
    },
    'El Vado': {
        'coords': [36.5948, -106.7366], 'region': 'uc', 'anno': '', 'cap': 114.202, 
        'id': 2685, 'anchor': (60,-30), 'pop_dir': 'up',
        'sdis': 
            {'storage': 19548, 'elev': 19547, 'inflow': None, 'release': 19626}
    },
    'Abiquiu': {
        'coords': [36.2686, -106.4551], 'region': 'uc', 'anno': '', 'cap': 186.820, 
        'id': 2729, 'anchor': (0,-48), 'pop_dir': 'up',
        'sdis': 
            {'storage': 19127, 'elev': 19126, 'inflow': None, 'release': 20055}
    },
    'Caballo': {
        'coords': [32.89646, -107.29219], 'region': 'uc', 'anno': '', 'cap': 224.464, 
        'id': 1094, 'anchor': (0,-35), 'pop_dir': 'up',
        'sdis': 
            {'storage': 2678, 'elev': 2679, 'inflow': 2680, 'release': 2682}
    },
    'Sumner': {
        'coords': [34.62884, -104.3924], 'region': 'uc', 'anno': '', 'cap': 35.917, 
        'id': 943, 'anchor': (0,0), 'pop_dir': 'up',
        'sdis': 
            {'storage': 1741, 'elev': 1948, 'inflow': 1812, 'release': 1892}
    },
    'Brantley': {
        'coords': [32.5442, -104.3814], 'region': 'uc', 'anno': '', 'cap': 42.602, 
        'id': 937, 'anchor': (75,10), 'pop_dir': 'up',
        'sdis': 
            {'storage': 1735, 'elev': 1942, 'inflow': 1812, 'release': 1892}
    },
    'Avalon': {
        'coords': [32.4908, -104.2522], 'region': 'uc', 'anno': '', 'cap': 4.466, 
        'id': 2684, 'anchor': (-35,-10), 'pop_dir': 'up',
        'sdis': 
            {'storage': 19172, 'elev': 19171, 'inflow': None, 'release': 20821}
    }
}

rg_config = {
    rg_config_name: {
        'hrg_level': rg_huc_level,
        'huc_filter': rg_huc_filter,
        'zoom': rg_initial_zoom, 
        'center': rg_map_center, 
        'reservoirs': rg_reservoirs, 
        'regions': rg_regions, 
        'forecasts': forecasts
    }
}    

uc_config_name = 'uc'
uc_map_center = (39.3, -109.1)
uc_initial_zoom = 7
uc_huc_level = 2
uc_huc_filter = 14

uc_regions = {
    'Upper Colorado': {
        'coords': [39.8, -110.7], 'huc-level': 2, 'anchor': (0,0)
    },
    'Gunnison': {
        'coords': [39.0, -108.3], 'huc-level': 6, 'anchor': (0,0)
    },
    'Colorado Headwaters': {
        'coords': [40, -107.1], 'huc-level': 6, 'anchor': (0,0)
    },
    'White-Yampa': {
        'coords': [40.9, -107.9], 'huc-level': 6, 'anchor': (0,0)
    },
    'Upper Green': {
        'coords': [42.9, -110.5], 'huc-level': 6, 'anchor': (0,0)
    },
    'Lower Green': {
        'coords': [40.5, -110.8], 'huc-level': 6, 'anchor': (0,0)
    },
    'Upper Colorado-Dirty Devil': {
        'coords': [38.2, -112.25], 'huc-level': 6, 'anchor': (0,0)
    },
    'Upper Colorado-Dolores': {
        'coords': [37.7, -108.2], 'huc-level': 6, 'anchor': (0,0)
    },
    'Lower San Juan': {
        'coords': [37.7, -110.2], 'huc-level': 6, 'anchor': (0,0)
    },
    'Upper San Juan': {
        'coords': [36.3, -108.5], 'huc-level': 6, 'anchor': (0,0)
    },
}

uc_reservoirs = {
    'Fontenelle': {
        'coords': [42.026, -110.068], 'region': 'uc', 'anno': '', 'cap': 344.8, 
        'id': 916, 'anchor': (0,0), 'pop_dir': 'up',
        'sdis': 
            {'storage': 1717, 'elev': 1926, 'inflow': 1790, 'release': 1870}
    },
    'Flaming Gorge': {
        'coords': [41.0934, -109.5406], 'region': 'uc', 'anno': '', 'cap': 3749,
        'id': 917, 'anchor': (0,0), 'pop_dir': 'up',
        'sdis': 
            {'storage': 1718, 'elev': 1927, 'inflow': 1791, 'release': 1871}
    },
    'Blue Mesa': {
        'coords': [38.453, -107.337], 'region': 'uc', 'anno': '', 'cap': 829.5,
        'id': 913, 'anchor': (-110,25), 'pop_dir': 'up',
        'sdis': 
            {'storage': 1714, 'elev': 1923, 'inflow': 1787, 'release': 1867}
    },
    'Morrow Point': {
        'coords': [38.452, -107.538], 'region': 'uc', 'anno': '', 'cap': 117.25,
        'id': 914, 'anchor': (0,0), 'pop_dir': 'up',
        'sdis': 
            {'storage': 1715, 'elev': 1924, 'inflow': 1843, 'release': 1868}
    },
    'Crystal': {
        'coords': [38.51, -107.624], 'region': 'uc', 'anno': '', 'cap': 17.536,
        'id': 915, 'anchor': (105,-25), 'pop_dir': 'up',
        'sdis': 
            {'storage': 1716, 'elev': 1925, 'inflow': 1844, 'release': 1869}
    },
    'Navajo': {
        'coords': [36.801, -107.612], 'region': 'uc', 'anno': '', 'cap': 1696,
        'id': 920, 'anchor': (0,0), 'pop_dir': 'up',
        'sdis': 
            {'storage': 1720, 'elev': 1929, 'inflow': 1793, 'release': 1873}
    },
    'Lake Powell': {
        'coords': [37.0688, -111.2439], 'region': 'uc', 'anno': '', 'cap': 24322,
        'id': 919, 'anchor': (0,0), 'pop_dir': 'up',
        'sdis': 
            {'storage': 1719, 'elev': 1928, 'inflow': 1792, 'release': 1872}
    }
} 

uc_config = {
    uc_config_name: {
        'huc_level': uc_huc_level,
        'huc_filter': uc_huc_filter,
        'zoom': uc_initial_zoom, 
        'center': uc_map_center, 
        'reservoirs': uc_reservoirs, 
        'regions': uc_regions, 
        'forecasts': forecasts
    }
}

all_configs = {
    'uc': uc_config,
    'gunn': gunn_config,
    'gb': gb_config,
    'pb': pb_config,
    'rg': rg_config,
    'sj': sj_config,
    'ub': ub_config,
    'ug': ug_config
}

if __name__ == '__main__':

    import json
    import sys
    from os import path
    import argparse
    cli_desc = 'Creates Upper Colorado Daily Summary map for USBR.'
    parser = argparse.ArgumentParser(description=cli_desc)
    parser.add_argument("-V", "--version", help="show program version", action="store_true")
    parser.add_argument("-A", "--add", help="adds current config to all_config.json", action="store_true")   
    parser.add_argument("-r", "--remove", help="removes a config from all_config.json")   
    args = parser.parse_args()
    
    if args.version:
        print('region_status.py v1.0')
        
    this_dir = path.dirname(path.realpath(__file__))
    
    if args.remove:
        print(f'Removing {args.remove} from all_config.json if present.')
        all_config_file_name = f'all_config.json'
        with open(all_config_file_name, 'r') as j:
            all_config = json.load(j)
        all_config.pop(args.remove, None)
        with open(all_config_file_name, 'w') as j:
            json.dump(all_config, j, indent=4, sort_keys=True)
        sys.exit(0)

    for config_name, config in all_configs.items():
        config_file_name = f'{config_name}_config.json'
        with open(config_file_name, 'w') as j:
            json.dump(config, j, indent=4, sort_keys=True)
        print(f'Created {config_file_name}.')
        if args.add:
            all_config_file_name = f'all_config.json'
            with open(all_config_file_name, 'r') as j:
                all_config = json.load(j)
            all_config[config_name] = config[config_name]
            with open(all_config_file_name, 'w') as j:
                json.dump(all_config, j, indent=4, sort_keys=True)
            print(f'  added {config_file_name} to all_config.json.')