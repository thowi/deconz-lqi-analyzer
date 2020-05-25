#!/usr/bin/env bash

# If pyenv is installed, load pyenv and activate the environment.
if command -v pyenv 1>/dev/null 2>&1; then
  eval "$(pyenv init -)"
  eval "$(pyenv virtualenv-init -)"
  pyenv activate deconz-lqi-analyzer
fi

./deconz-lqi-analyzer.py lqi-names.csv lqi-2020-05-21*.csv > lqi_timeline.csv

if command -v pyenv 1>/dev/null 2>&1; then
  pyenv deactivate
fi