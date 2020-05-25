#!/usr/bin/env bash

grep 192.168.1.100 deconz_buttons.log > deconz_buttons_filtered.log
./deconz-analyze-button-events.py deconz_buttons_filtered.log > deconz_buttons.csv
./deconz-rename-devices.py lqi-names.csv deconz_buttons.csv > deconz_buttons_renamed.csv
