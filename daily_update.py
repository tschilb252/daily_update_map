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
import pandas as pd
from folium.plugins import FloatImage, MousePosition, MiniMap
from folium.features import DivIcon
# import geopandas as gpd
# from shapely.geometry import Point
# from shapely.ops import cascaded_union
from daily_update_utils import get_season
from daily_update_utils import add_optional_tilesets, add_huc_layer
from daily_update_utils import get_favicon, get_bor_seal
from daily_update_utils import get_bor_js, get_bor_css
from daily_update_utils import get_default_js, get_default_css
from daily_update_utils import add_huc_chropleth, get_colormap
from daily_update_utils import NRCS_CHARTS_URL
from config.config_gen import forecasts, reservoirs, regions
from browser_print import BrowserPrint

bor_js = get_bor_js()
bor_css = get_bor_css()

default_js = get_default_js()
default_css = get_default_css()

folium.folium._default_js = default_js
folium.folium._default_css = default_css
# folium.folium._default_js = bor_js
# folium.folium._default_css = bor_css

def get_expand_button(title=''):
    return f'''
    <div class="buton" style="position: fixed; top: 10px; left: 55px; z-index:9999;">
      <button type="button" class="btn btn-light btn-lg" role="button" style="opacity: 0.8;">
        <a class="dropdown-item" href="#" target="_blank" style="padding: 0;">
          <span><i class="fa fa-external-link"></i>&nbsp {title}
        </a>
      </button>
    </div>
    '''
      

def get_legend():
    update_date = dt.now().strftime('%B %d, %Y %H:%M')
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
        Updated: {update_date}<br>
      </a>
    '''
    legend_dd = f'''
    <div class="dropdup" style="position: fixed; top: 60px; left: 55px; z-index:9999; opacity: 0.8;">
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

def add_region_markers(basin_map, regions, nrcs_url=NRCS_CHARTS_URL, map_date=None):
    huc_levels = {v['huc-level']:k for k, v in regions.items()}
    lowest_huc = min(huc_levels.keys())

    for region, region_meta in regions.items():
        print(f'    Adding {region} to the map...')
        huc_level = region_meta['huc-level']
        region_alias = region
        if region_meta['alias']:
            region_alias = region_meta['alias']
        btn_size = 'btn-sm'
        region_suffix = ''
        button_color = 'btn-info'
        if huc_level == lowest_huc:
            btn_size = 'btn-md'
            button_color = 'btn-primary'
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
            f'Go to {region_alias} {other_chart_type} Chart...</button></a></div>'
            f'<div class="row justify-content-center">{get_embed(seasonal_url)}</div>'
            f'</div></div>'
        )
        popup = folium.map.Popup(html=popup_html)
            
        marker_label = f'''
        <button type="button" class="btn {button_color} {btn_size}">
          <span style="white-space: nowrap;">{region_alias}</span><br>
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

def add_res_markers(basin_map, reservoirs, map_date=None):
    prefix = 'https://www.usbr.gov/uc/water/hydrodata/RESERVOIR_DATA'
    for res_name, res_meta in reservoirs.items():
        print(f'    Adding {res_name} to map...')
        try:
            if res_meta['region'] == 'uc':
                current_storage = get_uc_data(res_meta['sdis']['storage'], map_date=map_date)
                current_date = current_storage['dt']
                current_storage = current_storage['data']
                current_elev = get_uc_data(res_meta['sdis']['elev'], map_date=map_date)['data']
                if res_meta['sdis']['inflow']:
                    current_inflow = get_uc_data(res_meta['sdis']['inflow'], map_date=map_date)['data']
                else:
                    current_inflow = None
                current_release = get_uc_data(res_meta['sdis']['release'], map_date=map_date)['data']
            elif res_meta['region'] == 'lc':
                current_storage = get_lc_data(res_meta['sdis']['storage'], map_date=map_date)['data']
                current_elev = get_lc_data(res_meta['sdis']['elev'], map_date=map_date)['data']
                if res_meta['sdis']['inflow']:
                    current_inflow = get_lc_data(res_meta['sdis']['inflow'], map_date=map_date)['data']
                else:
                    current_inflow = None
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
            url_storage = f"{prefix}/{res_meta['id']}/dashboard.html#storage"
            url_elev = f"{prefix}/{res_meta['id']}/dashboard.html#pool_elevation"
            url_inflow = f"{prefix}/{res_meta['id']}/dashboard.html#inflow"
            url_release = f"{prefix}/{res_meta['id']}/dashboard.html#total_release"
            current_storage = f'{current_storage/1000:,.1f}'
            current_elev = f'{current_elev:,.1f}'
            if current_inflow:
                current_inflow = f'{current_inflow:,.0f}'
            else:
                current_inflow = 'N/A'
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
        
        # if current_storage and res_meta['region'].lower() == 'uc':
        #     bar = {
        #       "data": {
        #         "values": [
        #           {"%": int(percent_cap)}
        #         ]
        #       },
        #       "mark": {"type": "bar"},
        #       "encoding": {
        #         "y": {
        #           "field": "%",
        #           "type": "quantitative",
        #           "axis": {"title": "% Capacity"}
        #         }
        #       }
        #     }
        #     vega = folium.features.VegaLite(
        #         bar,
        #         width='100%',
        #         height='100%',
        #     )
            
        #     div_icon.add_to(vega)
        
        folium.Marker(
            location=res_meta['coords'],
            # popup=popup,
            tooltip=tooltip,
            icon=div_icon
        ).add_to(basin_map)

def add_frcst_markers(basin_map, forecasts, map_date=None):
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
    
    import sys
    import argparse
    cli_desc = 'Creates Upper Colorado Daily Summary map for USBR.'
    parser = argparse.ArgumentParser(description=cli_desc)
    parser.add_argument("-V", "--version", help="show program version", action="store_true")
    parser.add_argument("-c", "--config", help="name of config file to use in local config folder, pass keyword 'all' for all_config.json", required=True)
    parser.add_argument("-d", "--date", help="run for specific date (YYYY-MM-DD), currently no support for region prec/swe data, only res/frcst data")
    parser.add_argument("-o", "--output", help="set output folder")
    parser.add_argument("-n", "--name", help="use alternate name *.html, only works for configs with one entry")
    parser.add_argument("-m", "--makedir", help="create output folder if it doesn't exist", action='store_true')
    parser.add_argument("-g", "--gis", help="pass path for alt gis folder.")
    
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
    config_dir = path.join(this_dir, 'config')
    if args.config.lower() == 'all':
        config_path = path.join(config_dir, 'all_config.json')
    else:
        config_path = path.join(config_dir, args.config)
    if path.exists(config_path):
        with open(config_path, 'r') as cfg:
            config = json.load(cfg)
        print(f'Creating map(s) for config: {config_path}...\n')
    else:
        print(f'Invalid config path - {config_path} - please try again.')
        sys.exit(0)
        
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
    print(f'Creating map(s) here: {map_dir}\n')
    
    gis_dir = path.join(this_dir, 'gis')
    if path.isdir(str(args.gis)):
        print(f'Using alt gis dir: {args.gis}\n')
        gis_dir = args.gis
        
    for map_name, map_config in config.items():
        if args.name:
            map_path = path.join(map_dir, f'{args.name}.html')
        else:
            map_path = path.join(map_dir, f'{map_name}_status.html')
        
        print(f'Creating map for config item: {map_name}_status.html')
        
        print('  Adding layers and controls...')
        map_center = map_config.get('center', (40, 106))
        map_zoom = map_config.get('zoom', 6)
        map_huc_level = map_config.get('huc_level', 2)
        zoom_start = map_zoom
        if not str(map_zoom).isnumeric():
            zoom_start = 6
        
        huc_filter = map_config.get('huc_filter', [''])
        if type(huc_filter) == list:
            huc_filter = tuple([str(i) for i in huc_filter])
        elif type(huc_filter) == str or type(huc_filter) == int:
            huc_filter = tuple([str(huc_filter)])
        
        reservoirs = map_config.get('reservoirs', reservoirs)
        regions = map_config.get('regions', regions)
        forecasts = map_config.get('forecasts', forecasts)
        basin_map = folium.Map(
            tiles=None, 
            location=map_center, 
            zoom_start=zoom_start, 
            control_scale=True
        )
        
        huc_levels = ['2', '4', '6', '8']
        huc_levels[:] = [i for i in huc_levels if int(i) >= int(map_huc_level)]
        for huc_level in huc_levels:
            # huc_filter = tuple(set(i[:len(huc_level)] for i in huc_filter))
            print(f'    Adding HUC{huc_level} boundary...')
            
            huc_layer = add_huc_layer(
                level=int(huc_level), 
                gis_path=gis_dir,
                show=True, 
                embed=False, 
                huc_filter=huc_filter
            )
            if huc_layer:
                huc_layer.add_to(basin_map)

        for huc_level in huc_levels:
            print(f'    Adding HUC{huc_level} SWE/PREC layers...')
            huc_filter = tuple(set(i[:len(huc_level)] for i in huc_filter))
            show_prec = True if get_season() =='summer' and huc_level == '8' else False
            show_swe = True if not show_prec and huc_level == '8' else False
            
            for data_type in ['swe', 'prec']:
                show_dict = {'swe': show_swe, 'prec': show_prec}
                show = show_dict[data_type]
                chropleth = add_huc_chropleth(
                    gis_path=gis_dir,
                    data_type=data_type, 
                    show=show_dict[data_type], 
                    huc_level=huc_level, 
                    huc_filter=huc_filter
                )
                if chropleth:
                    chropleth.add_to(basin_map)
                    
        print('    Adding tilesets, legend, and controls...')
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
        # add_frcst_markers(basin_map, forecasts, map_date=map_date)
        print('  Adding Reservoir markers...')
        add_res_markers(basin_map, reservoirs, map_date=map_date)
        print('  Adding PREC/SWE markers...')
        add_region_markers(basin_map, regions, map_date=map_date)
        
        if not str(map_zoom).isnumeric():
            all_coords = [i['coords'] for i in reservoirs.values()]
            all_coords = all_coords + [i['coords'] for i in forecasts.values()]
            all_coords = all_coords + [i['coords'] for i in regions.values()]
            basin_map.fit_bounds(all_coords)
        
        print('  Adding legend/plugins...')
        legend = folium.Element(get_legend())
        basin_map.get_root().html.add_child(legend)
        BrowserPrint().add_to(basin_map)
        map_title = map_config.get('title', '')
        expand_btn = folium.Element(get_expand_button(map_title))
        basin_map.get_root().html.add_child(expand_btn)
        MiniMap().add_to(basin_map)
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
            find_str = ('.attr("id", ' + "'legend')"
                )
            replace_str = (
                    '''.attr("id", "legend")
        .attr("style", "background-color:rgba(255,255,255,0.75);border-radius: 10px;")'''
                )
            chart_file_str = chart_file_str.replace(find_str, replace_str)
            html_file.write(chart_file_str)
        print(f'\nCreated map here: {map_path}\n\n')