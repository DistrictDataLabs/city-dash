# city-dash
City Intelligence Dashboard Project

Source:  U.S. Census Bureau, 2012-2016 American Community Survey 5-Year Estimates

The files containing the data are the ones whose filenames end with “ann.csv.” Each file has a different set of metrics by zip code (demographic, economic, housing, etc.). The rest of the files contain either metadata or other info about the data in the files.

The main goal here is to be able to aggregate to a city level and display a mix of interactive visualizations and natural language descriptions on a dashboard.


### To open dash app:

- install requirements.txt
or
- run ```conda env create -f environment.yml```
- run ```python run.py```
- in browser open http://127.0.0.1:8050/
