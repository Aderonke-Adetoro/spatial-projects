#!/usr/bin/env python
# coding: utf-8

# # Los Angeles 2020 to 2024 Crime Data Analysis; Cleaning, Filtering, Reformatting, Grouping and Exporting

# In[57]:


import pandas as pd
import numpy as np

# Function to load and filter the data
def load_data(file_path, use_columns, column_rename):
    """Load the data, filter columns, and rename the columns."""
    
    data = pd.read_csv(file_path, usecols=use_columns) #data loading and filtering
    data.rename(columns = column_rename, inplace = True) #columns renaming
    return data

# Function to clean coordinates to valid coordinates only
def clean_coordinates(data):
    """Remove rows with invalid latitude or longitude."""
    
    return data[(data["Latitude"] != 0.000) & (data["Longitude"] != 0.000)]

# Function to clean and process 'Date' column; reformating
def clean_date(data):
    """Convert the 'Date' column to datetime and remove invalid dates."""
    
    data["Date"] = pd.to_datetime(data["Date"], errors = "coerce", format = "%m/%d/%Y %I:%M:%S %p")
    data.dropna(subset = ["Date"], inplace = True)
    return data

# Function to clean and format the 'Time' column
def fix_time_format(time):
    """Fix time strings, ensuring they are in HH:MM format."""
    
    time = str(time).zfill(4)  # Ensure time has at least 4 digits
    if ":" not in time:
        time = f"{time[:2]}:{time[2:]}"  # Insert colon
    return time.split(":")[0] + ":" + time.split(":")[1]

def clean_time(data):
    """Fix the 'Time' column formatting."""
    
    data["Time"] = data["Time"].apply(fix_time_format)
    return data

# Function to handle missing values and sort data
def handle_missing_values(data):
    """Replace missing values and sort by date."""
    
    data.replace("##########", np.nan, inplace=True)
    data.sort_values(by = "Date", ascending = True, inplace = True)
    return data

# Function to calculate most common crime by location
def get_most_common_crime(data):
    """Group crimes by location and get the most common crime for each location."""
    
    crime_counts = data.groupby(["Latitude", "Longitude", "Crime Description"]).size().reset_index(name="Count")
    most_common_crime = (
        crime_counts
        .sort_values(["Latitude", "Longitude", "Count"], ascending = [True, True, False])
        .drop_duplicates(subset = ["Latitude", "Longitude"], keep = "first")
    )
    return most_common_crime

# Function to calculate hourly crime frequency
def get_hourly_crime_frequency(data):
    """Group crimes by location and hour, and get the peak crime hours."""
    
    data["Hour"] = pd.to_datetime(data["Time"], format = '%H:%M').dt.hour
    hourly_counts = data.groupby(["Latitude", "Longitude", "Hour"]).size().reset_index(name = "Crime Frequency")
    hot_times = (
        hourly_counts
        .sort_values(["Latitude", "Longitude", "Crime Frequency"], ascending = [True, True, False])
        .drop_duplicates(subset = ["Latitude", "Longitude"], keep ="first")
    )
    return hot_times

# Function to merge results; most common crime by location and peak hour
def merge_results(most_common_crime, hot_times):
    """Merge most common crime and hot times data."""
    
    results = pd.merge(most_common_crime, hot_times, on = ["Latitude", "Longitude"])
    return results

# Main execution block; defining data for each function
def main():

    #file path definition; insert the full path of the dataset on your PC to avoid erorr
    file_path = "Crime_Data_from_2020_to_Present.csv"
    
    # Column selection
    use_columns = [2, 3, 4, 5, 8, 9, 15, 26, 27]
    
    #renaming columns to simpler and descriptive names for easier access using dicttionary
    column_rename = {
        "DATE OCC": "Date",
        "TIME OCC": "Time",
        "AREA": "Area Code",
        "AREA NAME": "Location",
        "Crm Cd": "Crime Code",
        "Crm Cd Desc": "Crime Description",
        "Premis Desc": "Premise",
        "LAT": "Latitude",
        "LON": "Longitude"
    }
    
    
    # Load and preprocess data; assign data and variable name to each function
    la_crime = load_data(file_path, use_columns, column_rename)
    la_crime = clean_coordinates(la_crime)
    la_crime = clean_date(la_crime)
    la_crime = clean_time(la_crime)
    la_crime = handle_missing_values(la_crime)
    
    # Analyse data; assign data and variable name to each function
    most_common_crime = get_most_common_crime(la_crime)
    hot_times = get_hourly_crime_frequency(la_crime)
    results = merge_results(most_common_crime, hot_times)
    
    # Output results to csv and display it
    results.to_csv("Cleaned_Los_Angeles_Crime_dataset", index = False)
    print("\n The Cleaned Crime Data Successfully exported to 'Cleaned_Los_Angeles_Crime_dataset'")
    print(results)
    
# call and Run the script
if __name__ == "__main__":
    main()


# In[ ]:




