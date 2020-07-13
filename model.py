

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from model_helpers import plot_volumes, volume_to_area


def read_dataset(filepath):
    """
    Reads a csv file from filepath, stores as pandas dataframe and imputes any missing and inconsistent data
    Parameters
    ----------
    filepath : [str]
        path of csv file to read data
    Returns
    -------
        data frame is returned after imputing missing and inconsistent data
    """
    data_frame = pd.read_csv(filepath, dtype={'date': str})
    # checks for inconsistent or missing data and imputes it
    data_frame = check_data_validity(data_frame)
    return data_frame


def largest_area(data):
    """
    Computes largest value of area column in data
    Parameters
    ----------
    data : [pandas DataFrame]
        dataframe consisting all data from csv file
    Returns
    -------
    float largest value of area column in dataframe
    """
    return max(data.area)


def average_volume(data):
    """
    Computes average of volume column in dataframe
    Parameters
    ----------
    data : [pandas DataFrame]
        dataframe consisting all data from csv file
    Returns
    -------
    float round to 2 decimals - average of volume column in dataframe
    """
    average_volume = np.mean(data.volume)
    return round(average_volume, 2)


def most_average_rainfall(data):
    """
    Computes average of rainfall column and finds value in column closest to average rainfall
    Parameters
    ----------
    data : [pandas DataFrame]
        dataframe consisting all data from csv file
    Returns
    -------
    Month and year (str) whose rainfall value is closest to average rainfall
    """
    min_difference = max(data.rainfall)
    round_average_rainfall = round(np.mean(data.rainfall), 2)
    for i in range(len(data.index)):
        current_difference = abs(data.rainfall[i] - round_average_rainfall)
        # computes min_difference from average to current rainfall
        if current_difference < min_difference:
            min_difference = current_difference
            req_month_index = i
    # computes month, year of month, year index provided.
    return index_to_name_month(int(data.date[req_month_index][4:]) - 1) + ", " + data.date[req_month_index][:4]


def hottest_month(data):
    """
    Computes sum of max_temperature of each month for all data and retrieves max of that values
    Parameters
    ----------
    data : [pandas DataFrame]
        dataframe consisting all data from csv file
    Returns
    -------
    hottest month name like 'January', 'February' ...
    """
    month_temp_sum = [0 for x in range(12)]
    month_added = [0 for x in range(12)]
    month_temp_average =[0 for x in range(12)]
    for i in range(len(data.index)):
        # list of each month's individual sum of max_temperatures
        month_temp_sum[int(data.date[i][4:]) - 1] += data.max_temperature[i]
        # No of times each month's max_temp is added seperate for 12 months
        month_added[int(data.date[i][4:]) - 1] += 1
    # Denominator may  be different for each month in avg calculation
    for i in range(12):
        #Average calculated if only atleast that month is added atleast once
        if month_added[i] !=0:
            month_temp_average[i] = (month_temp_sum[i] / month_added[i])
    hot_month_index = month_temp_average.index(max(month_temp_average))
    hot_month_name = index_to_name_month(hot_month_index)
    return hot_month_name


def area_vs_volume(data):
    """
    Plots 2 graphs based on areas, volumes of lake George over the months from 1990 to 2018
    1. plots % change in areas, volumes compared to initial areas, volumes(1990 Jan)
    2.Plots % change in areas, volumes comapred to previous month's areas, volumes
    Parameters
    ----------
    data : [pandas DataFrame]
        dataframe consisting all data from csv file
    """
    volumes = [0]
    areas = [0]
    areas2 = areas[:]
    volumes2 = volumes[:]
    index_list = data.index
    for i in range(1, len(data.index)):
        # change % of areas compared to initial
        areas.append(((data.area[i] / data.area[0]) - 1) * 100)
        # change % of volume compared to initial
        volumes.append(((data.volume[i] / data.volume[0]) - 1) * 100)
        # change % of areas compared to previous month's area
        areas2.append(((data.area[i] / data.area[i - 1]) - 1) * 100)
        # change % of volume compared to previous month's volume
        volumes2.append(((data.volume[i] / data.volume[i - 1]) - 1) * 100)
    y_label_1 = '% change from the initial value'
    y_label_2 = '% change from the previous month'
    image_name = 'Area_vs_volume_initial'
    image_name_2 = 'Area_vs_volume_previous'
    # plot initial difference
    plot_graph(index_list, areas, volumes, y_label_1, image_name)
    # plot previous month's difference
    plot_graph(index_list, areas2, volumes2, y_label_2, image_name_2)


def plot_graph(index_list, areas, volumes, y_label, image_name):
    """
    Plots a graph for areas list, volumes list against index_list , y_label
    Parameters
    ----------
    index_list : [int] - list of indices representing number of months from 199001 to plot n x-axis
    areas : [float] - list of area values to plot on y-axis
    volumes : [float] - list of volume values to plot on y-axis
    y_label : [str] - label for y-axis
    image_name : [str]- name to save the plot(fig)

    """
    a = plt.plot(index_list, areas, 1, color='b')
    b = plt.plot(index_list, volumes, 1, color='orange')
    plt.savefig(image_name, format="svg")
    # For identification of area, volume in the plot
    plt.legend((a[0], b[0]), ("areas", "volumes"))
    plt.xlabel('Time(months) from Jan 1990 to Dec 2018')
    plt.ylabel(y_label)
    plt.title('% changes in areas, volumes of Lake George over time')
    plt.show()


def lake_george_simple_model(data, evaporation_rate):
    """
    Predicts volumes for evry month based on its rainfall, constant evaporation rate (simple model)
    (current volume = previous volume + rainfall received - evaporated)
    Parameters
    ----------
    data : [pandas DataFrame]
        dataframe consisting all data from csv file
    evaporation_rate : [int or float]
        rate for calculating water(in litres) evaporating per square meter
    Returns
    -------
    volumes [float]
    list of volumes predicted for every month using a simple model
    """
    # Considering max area of lake as catchment area
    catchment_area = largest_area(data)
    rainfall_received = [data.rainfall[0] * catchment_area]
    evaporated = [data.area[0] * evaporation_rate]
    volumes_list = [data.volume[0]]
    # considering current area as surface area, is used for next month's prediction
    surface_area = [data.area[0]]
    for i in range(1, len(data.index)):
        # total rainfall received for the entire month
        rainfall_received.append(data.rainfall[i] * catchment_area)
        #total evaporated water for entire month
        evaporated.append(evaporation_rate * surface_area[i - 1])
        # Predicted volume for ith month - simple model
        volumes_list.append(volumes_list[i - 1] + rainfall_received[i] - evaporated[i])
        # Surface area updating for next month's prediction usage
        surface_area.append(volume_to_area(volumes_list[i]))
    return volumes_list


def lake_george_complex_model(data):
    """
    Predicts volumes for evry month based on its rainfall, changing evaporation rate depending on temperatures,
    windspeed, solar exposure and humidity (Complex model)
    (current volume = previous volume + rainfall received - evaporated) but evaporation rate changes every month
    Parameters
    ----------
    data : [pandas DataFrame]
        dataframe consisting all data from csv file
    Returns
    -------
    volumes [float]
    list of volumes predicted for every month using complex model
    """
    # Considering max area of lake as catchment area
    catchment_area = largest_area(data)
    rainfall_received = [data.rainfall[0] * catchment_area]
    evaporated = [data.area[0] * (
            (1.6 * data.max_temperature[0]) - (3 * data.min_temperature[0]) - (2.5 * data.wind_speed[0]) + (
            4.5 * data.solar_exposure[0]) - (0.4 * data.humidity[0]))]
    volumes_list = [data.volume[0]]
    surface_area = [data.area[0]]
    for i in range(1, len(data.index)):
        #Evaporation rate changes every month unlike simple model
        evaporation_rate = (1.6 * data.max_temperature[i]) - (3 * data.min_temperature[i]) - (
                2.5 * data.wind_speed[i]) + (4.5 * data.solar_exposure[i]) - (0.4 * data.humidity[i])
        #total rainfall received for the entire month
        rainfall_received.append(data.rainfall[i] * catchment_area)
        # total evaporated water for entire month
        evaporated.append(evaporation_rate * surface_area[i - 1])
        #Predicted volume for ith month - complex model
        volumes_list.append(volumes_list[i - 1] + rainfall_received[i] - evaporated[i])
        #surface area computed to be used in next month's prediction
        surface_area.append(volume_to_area(volumes_list[i]))
    return volumes_list


def evaluate_model(data, volumes):
    """
    Calculates mean absolute error for volume in dataframe(expected) and volumes(predicted)
    Parameters
    ----------
    data : [pandas DataFrame]
        dataframe consisting all data from csv file
    volumes : [float]
        List of volumes, in litres, like output by lake_george_simple_model
    Returns
    -------
    mean_absolute_error [float] litres - mean error in volumes compared to (data.volumes)
    """
    #calculates absolute volume changes of expected and predicted volumes of model
    errors = [np.abs(data.volume[i] - volumes[i]) for i in range(len(data.volume))]
    #plots a histogram for these errors with frequency
# =============================================================================
#     plt.hist(errors)
#     plt.xlabel("Error")
#     plt.ylabel("Frequency")
#     plt.title("Mean Absolute Error")
#     plt.show()
# =============================================================================
    #calculates average of these errors list - mean_absolute error
    mean_absolute_error = np.mean(errors)
    return mean_absolute_error


def index_to_name_month(month_index):
    """
    Converts month index(int) 0-11 to respective months
    Parameters
    ----------
    month_index : [int]
        integer to convert to month name from 0-11
    Returns
    Month name(str) to corresponding month_index (0-11)0- January...11-December
    if index not in between 0-11, returns None

    """
    if month_index == 0:
        return 'January'
    elif month_index == 1:
        return 'February'
    elif month_index == 2:
        return 'March'
    elif month_index == 3:
        return 'April'
    elif month_index == 4:
        return 'May'
    elif month_index == 5:
        return 'June'
    elif month_index == 6:
        return 'July'
    elif month_index == 7:
        return 'August'
    elif month_index == 8:
        return 'September'
    elif month_index == 9:
        return 'October'
    elif month_index == 10:
        return 'November'
    elif month_index == 11:
        return 'December'
    else:
        return None


def check_data_validity(data):
    """
    Performs validation checks on all columns of dataframe, imputes if necessary
    Parameters
    ----------
    data : [pandas DataFrame]
        dataframe consisting all data from csv file
    Returns
    Data frame with imputations if they were detected.

    """
    for i in range(len(data.index)):
        # swap min, max temp if max<min
        if data.max_temperature[i] < data.min_temperature[i]:
            temp = data.max_temperature[i]
            data.loc[i, 'max_temperature'] = data.min_temperature[i]
            data.loc[i, 'min_temperature'] = temp
        # impute with mean if null
        if pd.isnull(data.loc[i, 'max_temperature']) is True:
            data.loc[i, 'max_temperature'] = np.mean(data.max_temperature)
        # impute with mean if null
        if pd.isnull(data.loc[i, 'min_temperature']) is True:
            data.loc[i, 'min_temperature'] = np.mean(data.min_temperature)
        # impute with 000001 if null
        if pd.isnull(data.loc[i, 'date']) is True or len(data.date[i]) < 5:
            data.loc[i, 'date'] = '000001'
        # Add extra 0 as month is missing 0
        if (len(data.date[i]) == 5):
            data.loc[i, 'date'] = data.date[i][:4] + '0' + data.date[i][4:]
        # impute with mean if null or <0
        if data.volume[i] < 0 or pd.isnull(data.loc[i, 'volume']) is True:
            data.loc[i, 'volume'] = np.mean(data.volume)
        # impute with mean if null or <0
        if data.area[i] < 0 or pd.isnull(data.loc[i, 'area']) is True:
            data.loc[i, 'area'] = np.mean(data.area)
        # impute with mean if null or <0
        if data.humidity[i] < 0 or pd.isnull(data.loc[i, 'humidity']) is True:
            data.loc[i, 'humidity'] = np.mean(data.humidity)
        # impute with mean if null or <0
        if data.wind_speed[i] < 0 or pd.isnull(data.loc[i, 'wind_speed']) is True:
            data.loc[i, 'wind_speed'] = np.mean(data.wind_speed)
        # impute with mean if null or <0
        if data.solar_exposure[i] < 0 or pd.isnull(data.loc[i, 'solar_exposure']) is True:
            data.loc[i, 'solar_exposure'] = np.mean(data.solar_exposure)
        # impute with mean if null or <0
        if data.rainfall[i] < 0 or pd.isnull(data.loc[i, 'rainfall']) is True:
            data.loc[i, 'rainfall'] = np.mean(data.rainfall)
    return data


if __name__ == '__main__':
    data = read_dataset("lake_george_data.csv")

    large_area = largest_area(data)
    print("Largest area of lake is : ", large_area)

    avg_volume = average_volume(data)
    print("Average volume of lake is : ", avg_volume)

    avg_rainfall = most_average_rainfall(data)
    print("Month closest to average rainfall is : ", avg_rainfall)

    hot_month = hottest_month(data)
    print("Hottest month on average is : ", hot_month)

    area_vs_volume(data)

    predicted_volume_simple = lake_george_simple_model(data, 55)
    predicted_volume_complex = lake_george_complex_model(data)

    plot_volumes(predicted_volume_simple)
    plot_volumes(predicted_volume_complex)

    print("Error using simple model is ", evaluate_model(data, predicted_volume_simple))
    print("Error using complex model is ", evaluate_model(data, predicted_volume_complex))
