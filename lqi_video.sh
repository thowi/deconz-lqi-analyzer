#!/bin/bash
ffmpeg -r 30 -pattern_type glob -i 'lqi-*.png' -vf scale='min(1280\,iw):trunc(ow/a/2)*2' -vcodec h264 -preset ultrafast -r 30 lqi.mp4
