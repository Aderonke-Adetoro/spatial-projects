### This script will be divided into three parts. Read the code comments for understanding of each step
#### before execution, be sure your filepath is correct and you have tthe necessary modules intalled on your notebook/code terminal

#CLEANING/FILTERING THE WORLD ENERGY DATA

import pandas as pd      # pandas for data manipulation
import numpy as np       # numpy for handling numerical operations

#Add file path, header/rows, footers to skip, columns to use/skip
energy = pd.read_excel("Energy Indicators.xls",
                       skiprows=17,
                       skipfooter=38,
                       usecols=[2, 3, 4, 5])  

#Assign required column names
energy.columns = ["Country", 
                      "Energy Supply", 
                      "Energy Supply per Capita", 
                      "% Renewable"
]                                          

# Convert 'Energy Supply' to numeric and multiply by 1,000,000
energy["Energy Supply"] = pd.to_numeric(energy["Energy Supply"], errors='coerce') #convert 'Energy Supply' column datatype to numeric before value conversion
energy["Energy Supply"] = energy["Energy Supply"] * 1000000.0  # convert 'Energy Supply' values from petajoules to gigajoules

# Replace specific values with NaN
pd.set_option('future.no_silent_downcasting', True) #to stop getting the 'replace to not be deprecated/removed in future version' error/notification(i used jupyter notebook, hence this)
energy = energy.replace(["...", "--", ""], np.NaN) #replace missing values with NaN
energy = energy.dropna(subset=["Country"]) #this drops any part f the column country with Nan as value

#employing dictionary usage for Country elements update
energy["Country"] = energy["Country"].replace({"United States of America":"United States", 
                                              "United Kingdom of Great Britain and Northern Ireland": "United Kingdom",
                                              "China, Hong Kong Special Administrative Region":"Hong Kong"
})                                      #proper country name formatting

#number and/or parenthesis removal from country names
energy["Country"] = energy["Country"].str.replace(r'\d+', '', regex = True) #numbers stripping
energy["Country"] = energy["Country"].str.replace(r'\(.*\)', '', regex = True).str.strip() #parenthesis and whitespace stripping


### IMPORTING AND CLEANING THE GDP DATASET

import pandas as pd

#Dataframe creation
GDP = pd.read_csv ("world_bank.csv",
      skiprows= 4
      )       

#Proper country name formatting
GDP["Country Name"] = GDP["Country Name"].replace({"Korea, Rep.":"South Korea",
                                                  "Iran, Islamic Rep.":"Iran",
                                                  "Hong Kong SAR, China":"Hong Kong"
                                                  })                

#column name update to avoid future inconsistency
GDP.rename(columns = {'Country Name': 'Country'}, inplace=True)


### READING THE SCIMAGO DATASET

import pandas as pd

#Dataframe creation
scimEn = pd.read_excel("scimagojr-3.xlsx")


### DATA MERGING; SCIEMN, GDP AND ENERGY ACCORDING TO RANK, YEAR AND OTHERS
#NOW LETS COMBINE/MERGE THE FILTERED OUTPUT OF EACH DATASET

import pandas as pd

# Filter the GDP data for the years 2006-2015(country column was added because it's needed for merge)
GDP_filter = GDP[["Country","2006", "2007", "2008", "2009", "2010", "2011", "2012", "2013", "2014", "2015"]] # i used double square brackets since i accessed multiple columns that i still needed to output as dataframe

# Filter ScimEn data for the top 15 countries by their Rank
scimEn_filter = scimEn[scimEn['Rank'] <= 15] 

# Merge datasets based on 'Country'
merged_df = pd.merge(scimEn_filter, energy, how="left", on="Country")
final_df = pd.merge(merged_df, GDP_filter, how="left", on="Country")

# Set the index to 'Country' and sort by 'Rank'
final_df.set_index("Country", inplace=True) #index setting
final_df.sort_values(by="Rank", inplace=True)   #rank sorting

# Reorder columns to match the required order
columns_order = ['Rank', 'Documents', 'Citable documents', 'Citations', 'Self-citations',
                 'Citations per document', 'H index', 'Energy Supply', 'Energy Supply per Capita', '% Renewable',
                 '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015']
final_df = final_df[columns_order] 

### We have a new output that can be exported as a new csv file using the syntax below

final_df.to_csv("Country_Ranking_by_Energy_and_GDP.csv", index = False) #this will save your merged filtered data as a csv file on your PC