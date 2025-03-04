
ORS_API_KEY = "please insert your OpenRouteService API KEY here"

import requests #JSON request module to access an online API url
import time   #API rate-limiting module
#define function for the distance to be calculated
def get_driving_distance(origin, destination): #function definition
    #define parameter  
    parameters = {
    "api_key": ORS_API_KEY,
    "start": f"{origin[1]},{origin[0]}",
    "end": f"{destination[1]},{destination[0]}",      
}
#create response variable with the url of the ORS direction service
    response= requests.get("https://api.openrouteservice.org/v2/directions/driving-car", params=parameters)
#conditional statement for API REQUEST STATUS
    if response.status_code == 200:
        print ("Request Successful!")
        data = response.json() #parsing the json data as python objects
        try: #Error handling 
            summary = data["features"][0]["properties"]["summary"] #extracting the distancce and duration from the data dictionary
            distance = summary["distance"]
            distance = distance/1000 #converting the distance to kilometres
            time.sleep(5) #condition to iterate through the sleep after 5seconds to beat API limit
            return distance
        except KeyError as e:
            print(f"KeyError: {e} - The key was not found in the response.")
            print("Response Content:", data)
            return None
        
    else: #condition for incorrect/expired API/URL
        print ("Request Failed!")
        return None
munich = (48.1351, 11.5820)  #origin coordinate definition in (latitude, longitude)
destinations= {"berlin":(52.5200, 13.4050),
       "Lincolnshire":(53.2179, 0.2000),
       "Nigeria":(7.3683, 4.1962),
      }    #definition of the coordinates of the destinations using dictionary
#iterating through the three destinations
for location, coordinates in destinations.items(): #condition for iteration
    distance = get_driving_distance(munich, coordinates) #Function called and assigned to variable distance
    if distance is not None:
        print(f"Distance from Munich to {location} is {distance} km") #printing result for a successful request