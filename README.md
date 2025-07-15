![Static Badge](https://img.shields.io/badge/Python-python?color=grey)
![Static Badge](https://img.shields.io/badge/Jupyter-python?label=Python&color=FFA500)
![Static Badge](https://img.shields.io/badge/PySpark-Python?color=red)

### Traffic Data Analysis 
### Purpose: 

1. Determine the most congested areas within each city code. 
2. Determine if the time of day impacts the congestion. 

### Steps Taken:
1. After joning the two data sets, persist the data as a whole in the 
silver level data warehouse. 

### Analysis:

1. Plot the highest congested area for each city code on a map 

### Issues:

1. Joining the data between the two data sets (metrics and detectors)
on the detector ID (a column both datasets possessed) leaded to an issue where 
the city and citycode did not match. 
   2. City: Torino matched to 10 unique city codes. 
   3. To avoid the mismatch of data, the column city and citycode columns
   from the metrics and detectors data sets were mapped together. 
