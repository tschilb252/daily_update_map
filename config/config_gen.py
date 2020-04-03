# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 08:08:44 2020

@author: buriona
"""

'''
1) HUC Level 6 - Gunnison Basin (140200)

2) HUC Level 8 -  East-Taylor (140200XX)
    HUC Level 8 -  Tomichi (140200XX)
    HUC Level 8 -  Upper Gunnison (140200XX)
    HUC Level 8 -  Uncompahgre (140200XX)
    HUC Level 8 -  Lower Gunnison (140200XX)
    HUC Level 8 -  North Fork Gunnison (140200XX)

3) I would like the following reservoirs included with info provided in this order:
site_name (site_id, inflowSDI, elevationSDI, storageSDI, releaseSDI, lat, long)

Crystal (915, 1789, 1925, 1716, 1869, 38.51046, -107.62374)
Morrow Point (914, 1788, 1924, 1715, 1868, 38.45191, -107.53791)
Blue Mesa (913, 1787, 1923, 1714, 1867, 38.45305, -107.33677)
Taylor Park (948, 1817, 1953, 1746, 1897, 38.81844, -106.60592)
Silver Jack (939, 1808, 1944, 1737, 1888, 38.22692, -107.54041)
Ridgway (912, 1786, 1922, 1713, 1860, 38.23636, -107.75914)
Paonia (945, 1814, 1950, 1743, 1894, 38.94919, -107.34347)
'''

reservoirs = {
    'Paonia': {
        'coords': [38.94919, -107.34347], 'region': 'uc', 'anno': '', 'cap': 15.522, 
        'id': 945, 'anchor': (0,0), 'pop_dir': 'up',
        'sdis': 
            {'storage': 1743, 'elev': 1950, 'inflow': 1814, 'release': 1894}
    },
    'Ridgway': {
        'coords': [38.23636, -107.75914], 'region': 'uc', 'anno': '', 'cap': 82.98, 
        'id': 912, 'anchor': (0,0), 'pop_dir': 'up',
        'sdis': 
            {'storage': 1713, 'elev': 1922, 'inflow': 1786, 'release': 1860}
    },
    'Silver Jack': {
        'coords': [38.22692, -107.54041], 'region': 'uc', 'anno': '', 'cap': 13.0, 
        'id': 939, 'anchor': (0,0), 'pop_dir': 'up',
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
        'id': 913, 'anchor': (0,0), 'pop_dir': 'up',
        'sdis': 
            {'storage': 1714, 'elev': 1923, 'inflow': 1787, 'release': 1867}
    },
    'Morrow Point': {
        'coords': [38.45191, -107.53791], 'region': 'uc', 'anno': '', 'cap': 117.025, 
        'id': 914, 'anchor': (0,0), 'pop_dir': 'up',
        'sdis': 
            {'storage': 1715, 'elev': 1924, 'inflow': 1788, 'release': 1868}
    },
    'Crystal': {
        'coords': [38.51046, -107.62374], 'region': 'uc', 'anno': '', 'cap': 17.536, 
        'id': 915, 'anchor': (0,0), 'pop_dir': 'up',
        'sdis': 
            {'storage': 1716, 'elev': 1925, 'inflow': 1789, 'release': 1869}
    },
}
regions = {
    'Gunnison': {
        'coords': [38.7, -107.6], 'huc-level': 4, 'anchor': (0,0)
    },
    'East-Taylor': {
        'coords': [39, -106.9], 'huc-level': 8, 'anchor': (0,0)
    },
    'Tomichi': {
        'coords': [38.5, -106.5], 'huc-level': 8, 'anchor': (0,0)
    },
    'Uncompahgre': {
        'coords': [38.5, -108.1], 'huc-level': 8, 'anchor': (0,0)
    },
    'Lower Gunnison': {
        'coords': [39, -108.5], 'huc-level': 8, 'anchor': (0,0)
    },
    'Pecos Headwaters': {
        'coords': [33, -105], 'huc-level': 8, 'anchor': (0,0)
    },
    'North Fork Gunnison': {
        'coords': [39, -107.7], 'huc-level': 8, 'anchor': (0,0)
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
    from os import path
    import argparse
    cli_desc = 'Creates Upper Colorado Daily Summary map for USBR.'
    parser = argparse.ArgumentParser(description=cli_desc)
    parser.add_argument("-V", "--version", help="show program version", action="store_true")
    parser.add_argument("-A", "--add", help="adds current config to all_config.json", action="store_true")   
    
    args = parser.parse_args()
    
    if args.version:
        print('region_status.py v1.0')
        
    this_dir = path.dirname(path.realpath(__file__))
    
    config_name = 'gunn'
    map_center = (38.5, -107.5)
    initial_zoom = 9
    huc_level = 6
    filter_huc = 140200
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
        
    if args.add:
        all_config_file_name = f'all_config.json'
        with open(all_config_file_name, 'r') as j:
            all_config = json.load(j)
        all_config[config_name] = config
        with open(all_config_file_name, 'w') as j:
            json.dump(all_config, j, indent=4, sort_keys=True)