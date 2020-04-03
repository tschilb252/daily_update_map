# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 08:08:44 2020

@author: buriona
"""

regions = {
    'Rio Grande': {
        'coords': [34.5, -106.5], 'huc-level': 2, 'anchor': (0,0)
    },
    'Upper Pecos': {
        'coords': [33, -105], 'huc-level': 6, 'anchor': (0,0)
    },
    'Rio Grande Headwaters': {
        'coords': [38, -106.5], 'huc-level': 6, 'anchor': (0,0)
    },
    'Rio Grande-Elephant Butte': {
        'coords': [35.3, -107.5], 'huc-level': 6, 'anchor': (0,0)
    }
}

reservoirs = {
    'Elephant Butte': {
        'coords': [33.15, -107.2], 'region': 'uc', 'anno': '', 'cap': 2010.9, 
        'id': 1119, 'anchor': (0,0), 'pop_dir': 'left',
        'sdis': 
            {'storage': 2684, 'elev': 2685, 'inflow': 2686, 'release': 2688}
    },
}

forecasts = {}
  
regions_rg = {
    'Rio Grande': {
        'coords': [34.5, -106.5], 'huc-level': 2, 'anchor': (0,0)
    },
    'Upper Pecos': {
        'coords': [33, -105], 'huc-level': 6, 'anchor': (0,0)
    },
    'Rio Grande Headwaters': {
        'coords': [38, -106.5], 'huc-level': 6, 'anchor': (0,0)
    },
    'Rio Grande-Elephant Butte': {
        'coords': [35.3, -107.5], 'huc-level': 6, 'anchor': (0,0)
    }
}

reservoirs_rg = {
    'Elephant Butte': {
        'coords': [33.15, -107.2], 'region': 'uc', 'anno': '', 'cap': 2010.9, 
        'id': 1119, 'anchor': (0,0), 'pop_dir': 'left',
        'sdis': 
            {'storage': 2684, 'elev': 2685, 'inflow': 2686, 'release': 2688}
    },
}
regions_uc = {
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

reservoirs_uc = {
    'Fontenelle': {
        'coords': [42.026, -110.068], 'region': 'uc', 'anno': '', 'cap': 344.8, 
        'id': 916, 'anchor': (0,0), 'pop_dir': 'left',
        'sdis': 
            {'storage': 1717, 'elev': 1926, 'inflow': 1790, 'release': 1870}
    },
    'Flaming Gorge': {
        'coords': [41.0934, -109.5406], 'region': 'uc', 'anno': '', 'cap': 3749,
        'id': 917, 'anchor': (0,0), 'pop_dir': 'right',
        'sdis': 
            {'storage': 1718, 'elev': 1927, 'inflow': 1791, 'release': 1871}
    },
    'Blue Mesa': {
        'coords': [38.453, -107.337], 'region': 'uc', 'anno': '', 'cap': 829.5,
        'id': 913, 'anchor': (-110,25), 'pop_dir': 'right',
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
        'id': 915, 'anchor': (105,-25), 'pop_dir': 'left',
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

if __name__ == '__main__':

    import json
    
    config_name = 'rg'
    map_center = (35.1, -106)
    initial_zoom = 7
    huc_level = 2
    filter_huc = 13
    config = {
        config_name: {
            'huc_level': huc_level,
            'filter_huc': filter_huc,
            'zoom': initial_zoom, 
            'center': map_center, 
            'reservoirs': reservoirs, 
            'regions': regions, 
            'forecasts': forecasts
        }
    } 
    
    config_file_name = f'{config_name}_config.json'
    
    with open(config_file_name, 'w') as j:
        json.dump(config, j, indent=4, sort_keys=True)
