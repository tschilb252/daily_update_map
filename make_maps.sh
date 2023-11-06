#!/bin/bash

source /wrg/hdb/apps/python/hdb_env/bin/activate

cd /wrg/hdb/apps/python/daily_update_map

python /wrg/hdb/apps/python/daily_update_map/daily_update.py -o /wrg/exec/pub/flat_files/status_maps -g /wrg/exec/pub/flat_files/assets/gis -c all_config.json
