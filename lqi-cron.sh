#!/bin/bash
cd /home/$USER/lqi/deconz-lqi-plugin && /home/$USER/lqi/deconz-lqi-plugin/gviz_crt.py && cp lqi.csv lqi-`date +%Y-%m-%d-%H-%M-%S`.csv
find /home/$USER/lqi/deconz-lqi-plugin -mtime +1 -and -name "lqi-*.png" -delete
