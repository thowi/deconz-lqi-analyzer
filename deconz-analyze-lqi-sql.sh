#!/usr/bin/env bash

./deconz-analyze-lqi-sql.py deconz_lqi.log > deconz_lqi.csv
./deconz-rename-devices.py lqi-names.csv deconz_lqi.csv > deconz_lqi_renamed.csv
