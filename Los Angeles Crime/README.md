# **Visualising Crime Data for Public Safety and Awareness Using Geospatial Tools and Technology: A Case Study of Los Angeles, United States of America.**

## Project Overview
This project leverages advanced geospatial technology and data analysis techniques to analyse and visualise Los Angeles crime data between 2020 and 2024, focusing on identifying patterns, hotspots, and trends in crime. Using Python libraries, including Pandas, Numpy, and the datetime module, the project processed a substantial dataset of at least 110,000 crime records, transforming it into actionable intelligence. Through carefully mapping crime occurrences with geographic coordinates, descriptions, and timestamps, the project delivers meaningful insights into public safety concerns. The visualisation uses an interactive mapping platform integrated with ArcGIS technology, allowing users to dynamically explore crime statistics through visually appealing heatmaps, charts, and pop-ups.
**Los Angeles Crime Web-app Link** - [Los Angeles Crime Web-App](https://shorturl.at/uOaJb)

## Project Aim
The project aims to bridge the gap between raw crime data and meaningful interpretation, empowering the public to understand crime dynamics better, enabling proactive safety measures and fostering informed decision-making. The visualisation transforms complex and static datasets into actionable information that both policymakers and the general public can access intuitively.

## Project Objectives
•	Acquire raw Los Angeles crime data from 2020 to 2024 as a comma-delimited (CSV) file.
•	Process and read crime data using Python libraries/modules, including pandas, numpy, and datetime.
•	Extract and rename essential columns from the Los Angeles Crime data.
•	Transform crime data through cleaning, grouping, and merging operations.
•	Reduce the dataset from 110,000 rows and 27 columns to approximately 77,860 rows and 6 columns.
•	Generate a structured CSV output for visualisation purposes.
•	Construct feature layers in ArcGIS Online for spatial analysis and visualisation.
•	Deploy an interactive web application using ArcGIS Instant Apps for enhanced user experience and accessibility.

## Methodology
### **Data Preprocessing Workflow**
1. Initial data loading and inspection using Pandas library
2. Column filtering and renaming to maintain relevant attributes
3.  Rigorous data cleaning to address several quality issues: 
	- Removal of records with invalid coordinates (e.g., where latitude and longitude values were 0.000)
    - Standardization of time values to HH:MM format
	- Conversion of dates to consistent DD/MM/YYformat
    - Replacement of missing crime values with NaN to prevent analysis conflicts.
4.	Data aggregation through custom grouping operations: 
	- Location-based aggregation to identify the most occurring crime types per geographic area
    - Temporal aggregation to determine crime frequency distribution by hour
5.	Merging of grouped datasets to create a comprehensive analytical foundation containing coordinates, crime types, temporal patterns, and frequency metrics

**Link to Script**- [Los Angeles Crime Data Cleaning python script](<Los Angeles Crime Data Cleaning Script.py>)

### **Visualisation Workflow**
1.	Import of cleaned dataset (77,000 records) to ArcGIS Online as a CSV feature layer
2.	Symbology customisation to display circle icons with embedded average crime time information
3.	Creation of multiple visualisation components: 
	- Pie charts showing crime type distribution by percentage
	- Line charts illustrating crime frequency across hours of the day
	- Bar charts correlating crime types with peak occurrence times
4.	Application of hotspot analysis tools to identify statistically significant crime concentrations
5.	Configuration of interactive pop-ups to display detailed information on user interaction
6.	Integration of all components into ArcGIS Instant Apps to create a cohesive interactive experience

**Los Angeles Crime Map Visualisation**- ![Los Angeles Crime Map](<Los Angeles Crime Map.jpg>)

## **Key Findings**
 - Vehicle theft emerged as the most prevalent crime type across Los Angeles during the study period
 - Peak crime activity consistently occurs around 12:00, with approximately 6,000 incidents recorded during this hour
 - Downtown Los Angeles and surrounding neighbourhoods represent significant crime hotspots with 99% statistical confidence
 - While criminal activity is distributed throughout the city, clear concentration patterns emerged through spatial analysis

## Benefits for Public Safety and Awareness
1.	**Identifying Hotspots:**
>>> The visual representation highlights areas with a high concentration of crimes, enabling law enforcement and local authorities to allocate resources effectively. For example, specific neighbourhoods in Downtown LA with recurring vehicle thefts can be prioritised for patrols and surveillance. Targeted interventions such as watch programs and street-light improvement can be created for areas of concern. This fosters data-driven decisions to improve public safety.

2.	**Understanding Crime Patterns:**
>>> Charts showing crime types and their frequency during peak hours (notably at 12:00) provide simplified and deeper insights into temporal trends. This information is crucial for addressing crimes that occur predominantly during specific times of the day or night, allowing for strategic allocation of law enforcement resources.

3.	**Engaging the Public:**
>>> The interactive interface fosters community awareness by making crime data accessible to diverse users. Intuitive search functionality, togglable layers, and    interactive charts enable visitors, potential residents, and current community members to make informed decisions about safety precautions in different neighbourhoods of Los Angeles.

**User Experience Considerations**

The application was designed with multiple users in mind:
- Community members, visitors and tourists: Simple interface with search functionality to locate specific neighbourhoods
- Law enforcement: Detailed hotspot analysis and temporal pattern visualisation for resource allocation
- Policy makers: Comprehensive data views supporting evidence-based decision-making for public safety initiatives

**Future Enhancements**
-	Integration with demographic and socioeconomic datasets to explore potential correlations
-	Implementation of predictive modelling to forecast emerging crime hotspots
-	Development of automated alert systems for significant pattern changes
-	Expansion to include comparative analysis with other metropolitan areas
-	Incorporation of real-time data feeds for more timely insights

**Conclusion**
This project demonstrates the transformative potential of geospatial technology and data science in addressing public safety challenges. Converting raw crime data into an interactive, transparent, and engaging platform fosters informed decision-making at both institutional and individual levels. The identification of vehicle theft as the predominant crime type, the recognition of midday as peak crime time, and the mapping of Downtown LA as a significant hotspot provide actionable intelligence for targeted interventions. This approach exemplifies how data storytelling can address pressing societal concerns while respecting ethical considerations around sensitive information, ultimately contributing to safer communities and enhanced public trust.

## Reference
1 Data Source: Kaggle Dataset
2 Author: Aderonke Adetoro
3 Software used: 
   - Jupyter Notebook for scripting
   - ArcGIS Online
   - ArcGIS Instant App
   - VS Code
   - Microsoft Excel
   