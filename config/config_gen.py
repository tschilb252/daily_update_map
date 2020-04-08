# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 08:08:44 2020

@author: buriona
"""

'''
Keep in mind the top left corner of the button is the anchor point
'''

config_name = 'sj'
map_center = (37, -108.1)
initial_zoom = 9
huc_level = 4
filter_huc = 1408

regions = {
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

reservoirs = {
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
    
sj_config_name = 'sj'
sj_map_center = (37, -108.1)
sj_initial_zoom = 9
sj_huc_level = 4
sj_filter_huc = 1408

regions_sj = {
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

reservoirs_sj = {
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
 
gunn_config_name = 'gunn'
gunn_map_center = (38.5, -107.5)
gunn_initial_zoom = 9
gunn_huc_level = 6
gunn_filter_huc = 1402

reservoirs_gunn = {
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
regions_gunn = {
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

forecasts = {}

rg_config_name = 'rg'
rg_map_center = (35.3, -106)
rg_initial_zoom = 7
rg_huc_level = 2
rg_filter_huc = 13

regions_rg = {
    'Rio Grande': {
        'coords': [35.5, -107], 'huc-level': 2, 'anchor': (0,0)
    },
    'Upper Pecos': {
        'coords': [33.6, -105.3], 'huc-level': 6, 'anchor': (0,0)
    },
    'Rio Grande Headwaters': {
        'coords': [38.25, -106.65], 'huc-level': 6, 'anchor': (0,0)
    },
    'Rio Grande-Elephant Butte': {
        'coords': [34.7, -108.2], 'huc-level': 6, 'anchor': (0,0)
    },
    'Upper Rio Grande': {
        'coords': [36.9, -106.85], 'huc-level': 6, 'anchor': (0,0)
    },
    'Upper San Juan': {
        'coords': [37, -108.25], 'huc-level': 8, 'anchor': (0,0)
    },
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

uc_config_name = 'uc'
uc_map_center = (38.7, -109.3)
uc_initial_zoom = 7
uc_huc_level = 2
uc_filter_huc = 14

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
    
    config_name = 'uc'
    config = {
        config_name: {
            'huc_level': uc_huc_level,
            'filter_huc': uc_filter_huc,
            'zoom': uc_initial_zoom, 
            'center': rg_map_center, 
            'reservoirs': reservoirs_uc, 
            'regions': regions_uc, 
            'forecasts': forecasts
        }
    } 
    
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
        print(f'added {config_file_name} to all_config.json.')