#!/bin/bash
cd && cd lqi/deconz-lqi-plugin && ./gviz_crt.py && cp lqi.csv lqi-`date +%Y-%m-%d-%H-%M-%S`.csv
find . -mmin +59 -and -name "lqi-*.png" -delete
find . -mtime +7 -and -name "lqi-*.csv" -delete
