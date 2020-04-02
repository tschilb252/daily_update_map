# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 06:55:24 2020

@author: buriona
"""

import re
import json
from io import StringIO
from datetime import datetime as dt
from os import path, makedirs
from requests import get as r_get
import folium
import branca
import pandas as pd
from folium.plugins import FloatImage, MousePosition
from folium.features import DivIcon
# import geopandas as gpd
# from shapely.geometry import Point
# from shapely.ops import cascaded_union
from uc_update_utils import get_fa_icon, get_icon_color, get_season
from uc_update_utils import add_optional_tilesets, add_huc_layer, get_huc
from uc_update_utils import get_favicon, get_bor_seal
from uc_update_utils import get_bor_js, get_bor_css
from uc_update_utils import get_default_js, get_default_css

bor_js = get_bor_js()
bor_css = get_bor_css()

default_js = get_default_js()
default_css = get_default_css()

folium.folium._default_js = default_js
folium.folium._default_css = default_css
# folium.folium._default_js = bor_js
# folium.folium._default_css = bor_css

nrcs_url = 'https://www.nrcs.usda.gov/Internet/WCIS/basinCharts/POR'
NRCS_CHARTS_URL = 'https://www.nrcs.usda.gov/Internet/WCIS/basinCharts/POR'

regions = {
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

forecasts = {}

reservoirs = {
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

    
# uc_config = dict(regions=regions, forecasts=forecasts, reservoirs=reservoirs)

# with open(path.join('config', 'uc_config.json'), 'w') as j:
#     json.dump(uc_config, j, indent=4, sort_keys=True)
# import sys
# sys.exit(0)
# colormap = branca.colormap.LinearColormap(['red', 'yellow', 'green', 'blue'], index=[50, 70, 100, 150])
def get_huc_nrcs_stats(huc_level='6', try_all=False):
    print(f'  Getting NRCS stats for HUC{huc_level}...')
    data_types = ['prec', 'wteq']
    index_pg_urls = [f'{NRCS_CHARTS_URL}/{i.upper()}/assocHUC{huc_level}' 
                     for i in data_types]
    index_pg_resps = [r_get(i) for i in index_pg_urls]
    index_pg_codes = [i.status_code for i in index_pg_resps]
    if not set(index_pg_codes) == set([200]):
        print(
            index_pg_urls, 
            f'  Could not download index file, trying all basins...'
        )
        try_all = True
        index_page_strs = ['' for i in index_pg_resps]
    else:
        index_page_strs = [i.text for i in index_pg_resps]
    topo_json_path = f'./gis/HUC{huc_level}.topojson'
    with open(topo_json_path, 'r') as tj:
        topo_json = json.load(tj)
    huc_str = f'HUC{huc_level}'
    attrs = topo_json['objects'][huc_str]['geometries']
    for attr in attrs:
        props = attr['properties']
        huc_name = props['Name']
        file_name = f'href="{huc_name.replace(" ", "%20")}.html"'
        if not try_all and file_name in index_page_strs[0]:
            print(f'  Getting NRCS PREC stats for {huc_name}...')
            props['prec_percent'] = get_nrcs_basin_stat(
                huc_name, huc_level=huc_level, data_type='prec'
            )
        else:
            props['prec_percent'] = "N/A"
        if not try_all and file_name in index_page_strs[1]:
            print(f'  Getting NRCS WTEQ stats for {huc_name}...')
            props['swe_percent'] = get_nrcs_basin_stat(
                huc_name, huc_level=huc_level, data_type='wteq'
            )
        else:
            props['swe_percent'] = "N/A"
    topo_json['objects'][huc_str]['geometries'] = attrs
    with open(topo_json_path, 'w') as tj:
        json.dump(topo_json, tj)
    
def get_nrcs_basin_stat(basin_name, huc_level='2', data_type='wteq'):
    stat_type_dict = {'wteq': 'Median', 'prec': 'Average'}
    url = f'{NRCS_CHARTS_URL}/{data_type.upper()}/assocHUC{huc_level}/{basin_name}.html'
    try:
        response = r_get(url)
        if not response.status_code == 200:
            print(f'      Skipping {basin_name} {data_type.upper()}, NRCS does not publish stats.')
            return 'N/A'
        html_txt = response.text
        stat_type = stat_type_dict.get(data_type, 'Median')
        regex = f"(?<=% of {stat_type} - )(.*)(?=%<br>%)"
        swe_re = re.search(regex, html_txt, re.MULTILINE)
        stat = html_txt[swe_re.start():swe_re.end()]
    except Exception as err:
        print(f'      Error gathering data for {basin_name} - {err}')
        stat = 'N/A'
    return stat

def add_huc_chropleth(m, data_type='swe', show=True, huc_level='6', 
                      gis_path='gis', filter_str=None):
    huc_str = f'HUC{huc_level}'
    topo_json_path = path.join(gis_path, f'{huc_str}.topojson')
    stat_type_dict = {'swe': 'Median', 'prec': 'Avg.'}
    stat_type = stat_type_dict.get(data_type, '')
    layer_name = f'{huc_str} % {stat_type} {data_type.upper()}'
    with open(topo_json_path, 'r') as tj:
        topo_json = json.load(tj)
    if filter_str:
        topo_json = filter_topo_json(
            topo_json, huc_level=huc_level, filter_str=filter_str
        )
    style_chropleth_dict = {
        'swe': style_swe_chropleth, 'prec': style_prec_chropleth
    }
    folium.TopoJson(
        topo_json,
        f'objects.{huc_str}',
        name=layer_name,
        show=show,
        style_function=style_chropleth_dict[data_type],
        tooltip=folium.features.GeoJsonTooltip(
            ['Name', f'{data_type}_percent'],
            aliases=['Basin Name:', f'{layer_name}:'])
    ).add_to(m)

def style_swe_chropleth(feature):
    colormap = get_colormap()
    stat_value = feature['properties'].get('swe_percent', 'N/A')
    if stat_value == 'N/A':
        fill_opacity = 0
    else:
        stat_value = float(stat_value)
        fill_opacity = (abs(stat_value - 100)) / 100
    return {
        'fillOpacity': 0 if stat_value == 'N/A' else 0.5,#0.75 if fill_opacity > 0.75 else fill_opacity,
        'weight': 0,
        'fillColor': '#00000000' if stat_value == 'N/A' else colormap(stat_value)
    }

def style_prec_chropleth(feature):
    colormap = get_colormap()
    stat_value = feature['properties'].get('swe_percent', 'N/A')
    if stat_value == 'N/A':
        fill_opacity = 0
    else:
        stat_value = float(stat_value)
        fill_opacity = (abs(stat_value - 100)) / 100
    return {
        'fillOpacity': 0 if stat_value == 'N/A' else 0.5,#0.75 if fill_opacity > 0.75 else fill_opacity,
        'weight': 0,
        'fillColor': '#00FFFFFF' if stat_value == 'N/A' else colormap(stat_value)
    }

def filter_geo_json(geo_json_path, filter_attr='HUC2', filter_str='14'):
    f_geo_json = {'type': 'FeatureCollection'}
    with open(geo_json_path, 'r') as gj:
        geo_json = json.load(gj)
    features = [i for i in geo_json['features'] if 
                i['properties'][filter_attr][:2] == filter_str]
    f_geo_json['features'] = features
    
    return f_geo_json

def filter_topo_json(topo_json, huc_level=2, filter_str='14'):
    geometries = topo_json['objects'][f'HUC{huc_level}']['geometries']
    geometries[:] = [i for i in geometries if 
                i['properties'][f'HUC{huc_level}'][:len(filter_str)] == filter_str]
    topo_json['geometries'] = geometries
    return topo_json

def get_colormap(low=50, high=150):
    colormap = branca.colormap.linear.RdYlBu_09.scale(low, high)
    colormap.caption = '% of Average/Median Precip./SWE'
    return colormap

def get_legend():
    update_date = dt.now().strftime('%B %d, %Y')
    legend_items = f'''
      <a class="dropdown-item" href="#">
        <b>Basin Data</b>
      </a>
      <a class="dropdown-item" href="https://www.wcc.nrcs.usda.gov/" target="_blank">
        <span><i class="fa fa-umbrella"></i>&nbsp % Avg. Precipitation
      </a>
      <a class="dropdown-item" href="https://www.wcc.nrcs.usda.gov/" target="_blank">
        <span><i class="fa fa-snowflake-o"></i>&nbsp % Median SWE
      </a>
      <div class="dropdown-divider"></div>
      <a class="dropdown-item" href="#">
        <b>Reservoir Data</b>
      </a>
      <a class="dropdown-item" href="https://www.usbr.gov/library/glossary/#S" target="_blank">
        <i class="fa fa-tint"></i>&nbsp Storage
      </a>
      <a class="dropdown-item" href="https://www.usbr.gov/library/glossary/#P" target="_blank">
        <span><i class="fa fa-caret-down"></i>&nbsp Pool Elevation
      </a>
      <a class="dropdown-item" href="https://www.usbr.gov/library/glossary/#I" target="_blank">
        <i class="fa fa-sign-in"></i>&nbsp Inflow
      </a>
      <a class="dropdown-item" href="https://www.usbr.gov/library/glossary/#R" target="_blank">
        <i class="fa fa-external-link"></i>&nbsp Release
      </a>
      <div class="dropdown-divider"></div>
      <a class="dropdown-item" href="#">
        <sup>1</sup>Sensitive to seasonal flows<br>
      </a>
      <a class="dropdown-item" href="#">
        <sup>2</sup>Less sensitive to seasonal flows<br>
      </a>
      <div class="dropdown-divider"></div>
      <a class="dropdown-item" href="#">
        Updated: {update_date}<br>
      </a>
    '''
    legend_dd = f'''
    <div class="dropdup" style="position: fixed; top: 10px; left: 50px; z-index:9999;">
      <button type="button" class="btn btn-warning btn-lg dropdown-toggle" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
        Legend
      </button>
      <div class="dropdown-menu" aria-labelledby="dropdownMenuLink">
{legend_items}   
      </div>   
    </div>
  
  '''
    return legend_dd

def get_uc_data(sdi, map_date=dt.now()):
    base_url = 'https://www.usbr.gov/pn-bin/hdb/hdb.pl?svr=uchdb2'
    sdi = f'&sdi={sdi}'
    tstp = '&tstp=DY'
    now = map_date
    dt_t1 = dt(now.year - 1, now.month, now.day).strftime('%Y-%m-%dT00:00')
    t1 = f'&t1={dt_t1}'
    dt_t2 = dt(now.year, now.month, now.day).strftime('%Y-%m-%dT00:00')
    t2 = f'&t2={dt_t2}'
    suffix= '&table=R&mrid=0&format=88'
    request_url = f'{base_url}{sdi}{tstp}{t1}{t2}{suffix}'
    response = StringIO(r_get(request_url).text)
    df = pd.read_csv(
        response, index_col='Date', parse_dates=True
    )
    df = df.astype(float)
    df.dropna(inplace=True)
    return {
        'data': df.iloc[-1,0], 
        'dt': df.index[-1].to_pydatetime(),
        'url': request_url.replace('format=88', 'format=html')
    }

def get_lc_data(sdi, map_date=dt.now()):
    base_url = 'https://www.usbr.gov/pn-bin/hdb/hdb.pl?svr=lchdb2'
    sdi = f'&sdi={sdi}'
    tstp = '&tstp=DY'
    now = map_date
    dt_t1 = dt(now.year - 1, now.month, now.day).strftime('%Y-%m-%dT00:00')
    t1 = f'&t1={dt_t1}'
    dt_t2 = dt(now.year, now.month, now.day).strftime('%Y-%m-%dT00:00')
    t2 = f'&t2={dt_t2}'
    suffix= '&table=R&mrid=0&format=88'
    request_url = f'{base_url}{sdi}{tstp}{t1}{t2}{suffix}'
    response = StringIO(r_get(request_url).text)
    df = pd.read_csv(
        response, index_col='Date', parse_dates=True
    )
    df = df.astype(float)
    df.dropna(inplace=True)
    return {
        'data': df.iloc[-1,0], 
        'dt': df.index[-1].to_pydatetime(),
        'url': request_url.replace('format=88', 'format=html')
    }

def get_frcst_data(site_id, map_date=dt.now()):
    base_url = 'https://www.nwrfc.noaa.gov/water_supply/ws_text.cgi'
    station = f'?id={site_id.upper()}'
    now = map_date
    wy = now.year
    if now.month > 9:
        wy += 1
    wy_str = f'&wy={wy}'
    period = '&per=APR-AUG'
    frcst_type = '&type=ESP10'
    prob = '&prob=0'
    request_url = f'{base_url}{station}{wy_str}{period}{frcst_type}{prob}'
    request_txt = r_get(request_url).text
    request_txt = request_txt.replace('<br>', '\n')
    request_txt = request_txt.replace('</pre></body>', '')
    request_io = StringIO()
    request_io.write(request_txt)
    request_io.seek(0)
    df_all = pd.read_csv(
        request_io, skiprows=4, index_col='Issuance Date', 
        parse_dates=True, na_values=''
    )
    df = df_all[['50% FCST']].copy()
    df = df.astype(float)
    df.dropna(inplace=True)
    df.index = pd.to_datetime(df.index)
    df.sort_index(inplace=True)
    return {
        'data': df.iloc[-1,0], 
        'dt': df.index[-1].to_pydatetime(),
        'url': request_url
    }

def get_embed(href):
    embed = (
        f'<div class="container embed-responsive embed-responsive-4by3" style="overflow: hidden; height: 650px; width: 720px;">'
        f'  <iframe class="embed-responsive-item" src="{href}" scrolling="no" frameborder="0" allowfullscreen></iframe>'
        f'</div>'
    )   
    return embed

def add_region_markers(basin_map, regions=regions, nrcs_url=nrcs_url, map_date=None):
    for region, region_meta in regions.items():
        print(f'    Adding {region} to the map...')
        huc_level = region_meta['huc-level']
        btn_size = ''
        region_suffix = ' Region'
        if huc_level > 2:
            btn_size = 'btn-sm'
            region_suffix = ''
        swe_url = f'{nrcs_url}/WTEQ/assocHUC{huc_level}/{region}{region_suffix}.html'
        prec_url = f'{nrcs_url}/PREC/assocHUC{huc_level}/{region}{region_suffix}.html'
        try:
            swe_txt = r_get(swe_url).text
            prec_txt = r_get(prec_url).text
            swe_regex = r"(?<=% of Median - )(.*)(?=%<br>%)"
            prec_regex = r"(?<=% of Average - )(.*)(?=%<br>%)"
        
            swe_re = re.search(swe_regex, swe_txt, re.MULTILINE)
            prec_re = re.search(prec_regex, prec_txt, re.MULTILINE)
            swe_percent = swe_txt[swe_re.start():swe_re.end()]
            prec_percent = prec_txt[prec_re.start():prec_re.end()]
        except Exception as err:
            print(f'      Error gathering data for {region} - {err}')
            swe_percent = 'N/A'
            prec_percent = 'N/A'
            
        seasonal_url = swe_url
        other_season_url = prec_url
        other_chart_type = 'Precip.'
        if get_season() == 'summer':
            seasonal_url = prec_url
            other_season_url = swe_url
            other_chart_type = 'Snow'
            
        popup_html = (
            f'<div class="container">'
            f'<div class="row justify-content-center">'
            f'<div class="col">'
            f'<a href="{other_season_url}" target="_blank">'
            f'<button class="btn btn-primary btn-sm btn-block">'
            f'Go to {region} {other_chart_type} Chart...</button></a></div>'
            f'<div class="row justify-content-center">{get_embed(seasonal_url)}</div>'
            f'</div></div>'
        )
        popup = folium.map.Popup(html=popup_html)
            
        marker_label = f'''
        <button type="button" class="btn btn-primary {btn_size}">
          <span style="white-space: nowrap;">{region}</span><br>
          <span style="white-space: nowrap;">
            {prec_percent}% <i class="fa fa-umbrella"></i>
            {swe_percent}% <i class="fa fa-snowflake-o"></i>
          </span>
        </button>
        '''
        
        div_icon = DivIcon(
            icon_anchor=(0,0),
            html=marker_label,
        )
        folium.Marker(
            location=region_meta['coords'],
            popup=popup,
            tooltip='Click for chart.',
            icon=div_icon
        ).add_to(basin_map)

def add_res_markers(basin_map, reservoirs=reservoirs, map_date=None):
    prefix = 'https://www.usbr.gov/uc/water/hydrodata/RESERVOIR_DATA'
    for res_name, res_meta in reservoirs.items():
        print(f'    Adding {res_name} to map...')
        try:
            if res_meta['region'] == 'uc':
                current_storage = get_uc_data(res_meta['sdis']['storage'], map_date=map_date)
                current_date = current_storage['dt']
                current_storage = current_storage['data']
                current_elev = get_uc_data(res_meta['sdis']['elev'], map_date=map_date)['data']
                current_inflow = get_uc_data(res_meta['sdis']['inflow'], map_date=map_date)['data']
                current_release = get_uc_data(res_meta['sdis']['release'], map_date=map_date)['data']
            elif res_meta['region'] == 'lc':
                current_storage = get_lc_data(res_meta['sdis']['storage'], map_date=map_date)['data']
                current_elev = get_lc_data(res_meta['sdis']['elev'], map_date=map_date)['data']
                current_inflow = get_lc_data(res_meta['sdis']['inflow'], map_date=map_date)['data']
                current_release = get_lc_data(res_meta['sdis']['release'], map_date=map_date)['data']
            else:
                current_storage = None
                current_elev = None
                current_inflow = None
                current_release = None
                
        except Exception as err:
            print(f'      Error gathering data for {res_name} - {err}')
            current_storage = None
            current_elev = None
            current_inflow = None
            current_release = None
                
        if current_storage and res_meta['region'].lower() == 'uc':
            percent_cap = 100 * round(current_storage / (1000 * res_meta['cap']), 2)
            percent_cap = f'{percent_cap:0.0f}'
            tooltip = f"As of: {current_date.strftime('%x')}"
            anno = res_meta['anno']
            url_storage = f"{prefix}/{res_meta['id']}/dashboard.html#inflow"
            url_elev = f"{prefix}/{res_meta['id']}/dashboard.html#pool_elevation"
            url_inflow = f"{prefix}/{res_meta['id']}/dashboard.html#inflow"
            url_release = f"{prefix}/{res_meta['id']}/dashboard.html#total_release"
            current_storage = f'{current_storage/1000:,.1f}'
            current_elev = f'{current_elev:,.1f}'
            current_inflow = f'{current_inflow:,.0f}'
            current_release = f'{current_release:,.0f}'
        else:
            current_storage = 'N/A'
            current_elev = 'N/A'
            current_inflow = 'N/A'
            current_release = 'N/A'
            percent_cap = 'N/A'
            tooltip = 'Error retrieving data!'
            anno = ''
            url_storage = ''
            url_elev = ''
            url_inflow = ''
            url_release = ''
        
        marker_label = f'''
        <div class="drop{res_meta['pop_dir']}">
          <button type="button" class="btn btn-secondary btn-sm dropdown-toggle" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
            <span style="white-space: nowrap;">
                <b>{res_name}</b><br>{percent_cap}% capacity<sup>{anno}</sup>
            </span>
          </button>
          <div class="dropdown-menu" aria-labelledby="dropdownMenuLink">
            <a class="dropdown-item" href="{url_storage}" target="_blank">
              <i class="fa fa-tint"></i> &nbsp; {current_storage} kaf
            </a>
            <a class="dropdown-item" href="{url_elev}" target="_blank">
              <i class="fa fa-caret-down"></i>  &nbsp; {current_elev}' 
            </a>  
            <a class="dropdown-item" href="{url_inflow}" target="_blank">
              <i class="fa fa-sign-in"></i> &nbsp; {current_inflow} cfs 
            </a>  
            <a class="dropdown-item" href="{url_release}" target="_blank">
              <i class="fa fa-external-link"></i> &nbsp; {current_release} cfs
            </a>
          </div>
        </div>
          
        '''
        
        icon_anchor = res_meta['anchor']
            
        div_icon = DivIcon(
            # icon_size=(120,40),
            icon_anchor=icon_anchor,
            html=marker_label,
        )
        
        bar = {
          "data": {
            "values": [
              {"%": int(percent_cap)}
            ]
          },
          "mark": {"type": "bar"},
          "encoding": {
            "y": {
              "field": "%",
              "type": "quantitative",
              "axis": {"title": "% Capacity"}
            }
          }
        }
        vega = folium.features.VegaLite(
            bar,
            width='100%',
            height='100%',
        )
        
        div_icon.add_to(vega)
        
        folium.Marker(
            location=res_meta['coords'],
            # popup=popup,
            tooltip=tooltip,
            icon=div_icon
        ).add_to(basin_map)

def add_frcst_markers(basin_map, forecasts=forecasts, map_date=None):
    for frcst_name, frcst_meta in forecasts.items():
        print(f'    Adding {frcst_name} to map...')
        
        try:
            if frcst_meta['region'] == 'pn':
                current_data = get_frcst_data(frcst_meta['id'], map_date=map_date)
            else:
                current_data = None
        except Exception as err:
            print(f'      Error gathering data for {frcst_name} - {err}')
            current_data = None
                
        if current_data:
            percent_cap = 100 * round(current_data['data'] / (frcst_meta['avg']), 2)
            percent_cap = f'{percent_cap:0.0f}'
            tooltip = f"As of: {current_data['dt'].strftime('%x')}"
            anno = frcst_meta['anno']    
            url = current_data['url']
        else:
            percent_cap = 'N/A'
            tooltip = 'Error retrieving data!'         
            anno = ''
            url = ''
            
        marker_label = f'''
        <a href="{url}" target="_blank">
          <button type="button" class="btn btn-sm btn-info">
            <span style="white-space: nowrap;">{frcst_name}</span><br>
            <span style="white-space: nowrap;">
              Apr-Aug Forecast
            </span>
            <span style="white-space: nowrap;">
              {percent_cap}%<sup>{anno}</sup> <i class="fa fa-tachometer"></i>
            </span>
          </button>
        </a>
        '''

        div_icon = DivIcon(
            icon_anchor=(0,0),
            html=marker_label,
        )
        
        folium.Marker(
            location=frcst_meta['coords'],
            # popup=popup,
            tooltip=tooltip,
            icon=div_icon
        ).add_to(basin_map)
        
if __name__ == '__main__':
    import argparse
    cli_desc = 'Creates Upper Colorado Daily Summary map for USBR.'
    parser = argparse.ArgumentParser(description=cli_desc)
    parser.add_argument("-V", "--version", help="show program version", action="store_true")
    parser.add_argument("-d", "--date", help="run for specific date (YYYY-MM-DD), currently no support for region prec/swe data, only res/frcst data")
    parser.add_argument("-o", "--output", help="set output folder")
    parser.add_argument("-n", "--name", help="use alternate name *.html")
    parser.add_argument("-m", "--makedir", help="create output folder if it doesn't exist", action='store_true')
    parser.add_argument("-g", "--gis", help="update local gis files with current NRCS data, or pass path for alt gis folder.", const=True, nargs='?')
    
    args = parser.parse_args()
    
    if args.version:
        print('region_status.py v1.0')
    map_date = dt.now()
    if args.date:
        try:
            map_date = dt.strptime(args.date, "%Y-%m-%d")
        except ValueError as err:
            print(f'Could not parse {args.date}, using current date instead. - {err}')    
    
    this_dir = path.dirname(path.realpath(__file__))
    map_dir = path.join(this_dir, 'maps')
    makedirs(map_dir, exist_ok=True)
    if args.output:
        if path.exists(args.output):
            map_dir = args.output
        else:
            if args.makedir:
                try:
                    map_dir = args.output
                    makedirs(map_dir, exist_ok=True)
                except Exception as err:
                    print(f'Cannot create {args.output}, using {map_dir} instead. - {err}')
            else:
                print(f'{args.output} does not exist, using {map_dir} instead.')  
    if args.name:
        map_path = path.join(map_dir, f'{args.name}.html')
    else:
        map_path = path.join(map_dir, 'uc_status.html')
    
    gis_dir = path.join(this_dir, 'gis')
    if path.isdir(str(args.gis)):
        gis_dir = args.gis
    if args.gis == True:
        for huc_level in ['2', '6', '8']:
            get_huc_nrcs_stats(huc_level)
        
    print(f'Creating map here: {map_dir}')
    print(f'  Adding layers and controls...')
    
    basin_map = folium.Map(
        tiles=None, location=(39.0, -108.6), zoom_start=7, control_scale=True
    )
    
    for huc_level in ['6', '8']:
        show_prec = False
        show_swe = False
        if huc_level == '8':
            show_swe = True
            if get_season() =='summer':
                show_prec = True
                show_swe = False
        add_huc_chropleth(
            basin_map, 
            data_type='swe', 
            show=show_swe, 
            huc_level=huc_level, 
            gis_path='gis', 
            filter_str='14'
        )
        add_huc_chropleth(
            basin_map, 
            data_type='prec', 
            show=show_prec, 
            huc_level=huc_level, 
            gis_path='gis', 
            filter_str='14'
        )
    add_huc_layer(basin_map, level=6, show=True, embed=False, filter_on='14')
    add_huc_layer(basin_map, level=8, show=False, embed=False, filter_on='14')
    add_huc_layer(basin_map, level=2, show=False, embed=False,  filter_on='14')
    
    add_optional_tilesets(basin_map)
    folium.LayerControl('topleft', collapsed=True).add_to(basin_map)
    FloatImage(
        get_bor_seal(orient='horz'),
        bottom=5,
        left=1
    ).add_to(basin_map)
    MousePosition(prefix="Location: ").add_to(basin_map)
    get_colormap().add_to(basin_map)
    # print('  Adding Regional Forecast markers...')
    # add_frcst_markers(basin_map, map_date=map_date)
    print('  Adding Reservoir markers...')
    add_res_markers(basin_map, map_date=map_date)
    print('  Adding PREC/SWE markers...')
    add_region_markers(basin_map, map_date=map_date)
    
    all_coords = [i['coords'] for i in reservoirs.values()]
    all_coords = all_coords + [i['coords'] for i in forecasts.values()]
    all_coords = all_coords + [i['coords'] for i in regions.values()]
    # basin_map.fit_bounds(all_coords)

    legend = folium.Element(get_legend())
    basin_map.get_root().html.add_child(legend)
    basin_map.save(map_path)
    flavicon = (
        f'<link rel="shortcut icon" '
        f'href="{get_favicon()}"></head>'
    )
    with open(map_path, 'r') as html_file:
        chart_file_str = html_file.read()

    with open(map_path, 'w') as html_file:
        chart_file_str = chart_file_str.replace(r'</head>', flavicon)
        replace_str = (
            '''left:1%;
                    max-width:15%;
                    max-height:15%;
                    background-color:rgba(255,255,255,0.5);
                    border-radius: 10px;
                    padding: 10px;'''
        )
        chart_file_str = chart_file_str.replace(r'left:1%;', replace_str)
        find_str = (
                """.append("svg")
        .attr("id", 'legend')"""
            )
        replace_str = (
                '''.append("svg")
                     .attr("id", "legend")
                     .attr("style", "background-color:rgba(255,255,255,0.75);border-radius: 10px;")'''
            )
        chart_file_str = chart_file_str.replace(find_str, replace_str)
        html_file.write(chart_file_str)
    print(f'\nCreated map here: {map_path}')