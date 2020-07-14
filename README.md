# Lake-George-Modelling using Python3 (May 2020)

Lake George, or Weereewa (in Ngunnawal), is an intermittent lake to the north-east of Canberra, Australia. It is well-known for having dramatic changes in water level. When full, it’s around 145 km2—20 times bigger than Lake Burley Griffin! But most of the time in contemporary history, it’s been fairly empty. This unusual
behaviour has given Lake George quite the reputation and even some persistent myths and legends, including everything from a secret underground link between Lake George and Mount Gambier, to bunyip and alien sightings. Of course, these legends are (probably) not true, and the fluctuating water levels of Lake George are explained by its unusually shallow geology, evaporation, and rainfall. This code is used to investigate the water level of Lake George and develop two models of how it fills and ebbs over time.

## Read Data

This model uses data from January 1990 to December 2018. It reads the data as a pandas dataframe object. The code also checks for any missing valuesand imputes them with values that seem relevant to them.  

## Statistics

The model data outputs the following after reading the data and performing computations:
+ Largest area covered by the lake over the years, 
+ Average Volume of the lake over the years,
+ Hottest month on average
+ The month and year whose rainfall is closest to the average rainfall

## Topography

The model plots 2 graphs based on areas, volumes of lake George over the months from 1990 to 2018. The first graph plots percentage change in areas, volumes compared to the initial area and volume of Lake ie, January 1990. The second plot is a graph showing percentage change in areas and volumes compared to its previous month's area and volume.
    


## Modelling

A simple model and a complex model of Lake George is predicted using this code.

### Simple Model

Using the monthly rainfall data to estimate the volume of Lake George for each month in the data, assuming a constant evaporation rate each month. Assumptions are made regarding the catchment area and surface area of Lake George. Use of functions from model-helpers.py is made to get a visual image to aid the modelling process. For simple model, evaporation rate is set to 55 mm/month.

### Complex Model

Same as simple model but the evaporation rate is always changing.

                    Evaporation rate = -3T(min) + 1.6T(max) - 2.5W + 4.5S - 0.4H
                    
where T is the temperature (in Celsius), S is the solar exposure (in MJ/month/m<sup>2</sup>), W is the wind speed(in m/s), and H is the humidity (as a percentage,i.e. as a number between 0 and 100). This model uses this evaporation rate instead of the constant evaporation rate to predict the volume of the model.

## Model Evaluation

Mean Abosulte Error is used to calculate the error in predicting the volumes using both simple and comlex model.
