Loads the CSV output of
[deconz-lqi-plugin](https://github.com/ma-ca/deconz-lqi-plugin) and generates a
timeline of the LQI.

# Setup

1. Install [deconz-lqi-plugin](https://github.com/ma-ca/deconz-lqi-plugin) on
your server where deCONZ is runnning.
1. Create a cronjob to run `gviz_crt.py` every minute and copy the CSV to a
timestamped file. You can adapt my `lqi-cron.sh` script.

# Usage

1. Pass the generated `lqi-names.csv` and `lqi-$DATE.csv` files to
`deconz-lqi-analyzer.py`.
1. Open the generated CSV file in a spreadsheet and create a graph for it.
1. Profit.
