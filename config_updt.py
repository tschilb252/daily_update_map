# -*- coding: utf-8 -*-
"""
Created on Tue Dec 15 09:24:28 2020

@author: buriona
"""

import json
import sys
import os
huc_id = 14
config_list = os.walk('./config')
config_list = [i for i in config_list]
config_list = config_list[0]
config_list = config_list[2]

for curr_config in [i for i in config_list if i.endswith('.json')]:
    with open(f'./config/{curr_config}', 'r') as f:
        c = json.load(f)
    with open(f'./config/{curr_config}', 'r') as f:    
        new_c = json.load(f)
        
    for k, v in c.items():
        for region, region_config in v['regions'].items():
            if not region_config['alias']:
                new_c[k]['regions'][region]['alias'] = region
    
        for region, region_config in v['regions'].items():
            huc_level = region_config['huc-level']
            region_str = region
            if huc_level == 2:
                region_str = region_str + ' Region'
            name_key = 'Name'
            if huc_level == 4:
                name_key = 'NAME'
            huc_level_key = f'HUC{huc_level}'
            with open(f'./gis/HUC{huc_level}.topojson', 'r') as g:
                gis = json.load(g)
            geos = gis['objects'][huc_level_key]['geometries']
            huc_meta = [i for i in geos if i['properties'].get(name_key,'not right') == region_str]
            if len(huc_meta) == 1:
                huc_meta = huc_meta[0]
                huc_id = huc_meta["properties"][huc_level_key]
                huc_name = huc_meta["properties"][name_key]
                new_region = f'{huc_id}_{huc_name}'
                new_region = new_region.replace(" ", "_").replace("'", "")
                print(new_region)
                new_c[k]['regions'][new_region] = new_c[k]['regions'].pop(region)
            elif len(huc_meta) == 0:
                print(f'could not find huc meta for {region_str} in {huc_level_key}')
            else:
                huc2 = str(huc_id)[:2]
                huc_meta = [i for i in huc_meta if i['properties'].get(huc_level_key,'not right')[:2] == huc2]
                if len(huc_meta) == 1:
                    huc_meta = huc_meta[0]
                    huc_id = huc_meta["properties"][huc_level_key]
                    huc_name = huc_meta["properties"][name_key]
                    new_region = f'{huc_id}_{huc_name}'
                    new_region = new_region.replace(" ", "_").replace("'", "")
                    print(new_region)
                    new_c[k]['regions'][new_region] = new_c[k]['regions'][region]
                    del new_c[k]['regions'][region]
                elif 'muddy' in region.lower():
                    huc_meta = huc_meta[0]
                    huc_id = '14070002'
                    huc_name = huc_meta["properties"][name_key]
                    new_region = f'{huc_id}_{huc_name}'
                    new_region = new_region.replace(" ", "_").replace("'", "")
                    print(new_region)
                    new_c[k]['regions'][new_region] = new_c[k]['regions'].pop(region)
                else:
                    print(f'multiple hucs found for {region_str} error!!!!!!!!!!!!!!!!!!')
                    
    with open(f'./new_config/{curr_config}', 'w') as f:
        json.dump(new_c, f, sort_keys=True, indent=2)
                
