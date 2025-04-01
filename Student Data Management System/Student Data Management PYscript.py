#!/usr/bin/env python
# coding: utf-8

# ### Creating a Student Grade Management System

# ### This program will create a student management system that allows users to enter student data, display student data, export the data into a csv file and exit the system using Menu Driven Interface.

# In[1]:


#COLLECTING THE STUDENT DATA AND STORING IT IN A NESTED DICTIONARY

def collect_student_data(): #student data function creation/definition
    students = {} # initialising a dictionary to store collected student data
    
### collecting student data using while loop and user input
    while True:
        print (f"Hello student, your Name and selected subject scores will be requested for and recorded")
        student_name = input("Enter your Surname and First name (or type DONE to finish): ")
        if student_name.lower() == "done": # initialising an exit for the input function
            break

        try: # getting subject scores with validation
            math_score = float(input("Enter your Math score: "))
            science_score = float(input("Enter your Science score: "))
            english_score = float(input("Enter your English score: "))

        except: # invalid input error handling
            print(f"Invalid input, please enter numerical values only for your subject scores")
            continue

### calculating student average score across the three subjects using mathematical operators
        total_score = (math_score + science_score + english_score)
        average_score = total_score / 3

### grade assignment based on student average score using conditional statement

        if average_score >= 85:
            grade = "A"
        elif average_score >= 75:
            grade = "B"
        elif average_score >= 65:
            grade = "C"
        elif average_score >= 55:
            grade = "D"
        else:
            grade = "F"

### creating Student Data using a Dictionary
        student_data = {"Math" : math_score,
                        "Science" : science_score, 
                        "English" : english_score,
                        "Average Score" : average_score,
                        "Final Grade": grade,
            
                       }
        students[student_name] = student_data  #updating the dictionary witha nested dictionary

    return students


# In[3]:


### DISPLAY STUDENT DATA STAGE
### displaying student data using function, and looping through student dictionary

def display_data(students):
    print ("\nDISPLAYING STUDENT DATA: ")
    for student_name, data in students.items():
        print (f"{student_name}'s grade is: ")
        for key, value in data.items():
            print (f"\n\t{key}: {value}")


# In[5]:


### Creating a Menu driven interface for data collection and retrieval based on user's input/choice
#First we import the necessary modules
import builtins #builtins.open to bypass ipython restriction(this is due to using jupyter notebook not .py) 
import csv #to handle csv files
import os #to read the csv fiepath and check if it exists;needed for data appending

def menu_interface():  # function created
    students = {}       # initialising student dictionary
    while True:   # initialsing condition
        
        ### displaying messages to assist user's choice
        print("\n STUDENT DATA MANAGEMENT SYSTEM ")
        print ("Enter 1 to enter Student Data ")
        print ("\n Enter 2 to display Student Data ")
        print ("\n Enter 3 to export to csv")
        print ("\n Enter 4 to exit the system ")
        user_choice = input("Enter your choice between 1-4: ")

        if user_choice == "1":
            student_data = collect_student_data()  # function call
            students.update(student_data)  # data updating in the student dictionary
        elif user_choice == "2":
            display_data(students)  # function call
        elif user_choice == "3":
            filename = "StudentData.csv"
            file_exists = os.path.isfile(filename) #create a csv file to hold your data
            #Using the with statement for file handling and "a" to append data written into the file
            with builtins.open(filename, mode = "a", newline = "") as file: #with statement for file handling
                student_csv_writer = csv.DictWriter(file, fieldnames = ["student_name", "Math", "Science", "English", 
                                                                        "Average Score", "Final Grade"])
                if not file_exists: #if the file doesn't exist already, do syntax below
                    student_csv_writer.writeheader()
                #converting a nested dictionary to a list of dictionaries, which is the only format that the\ 
                #csv.DictWriter can handle
                csv_data = []      #An empty list to collect a list of dictionary values
                for student_name, data in students.items(): #iterating through the main dictionary with student data
                    row = {"student_name": student_name} #creating a new dictionary with student_name as stand-alone\
                    #key:value pair
                    row.update(data) #updating the dictionary row with other students' data like math, science scores etc
                    csv_data.append(row) #adding the values from the dictionary row to the list csv_data
                student_csv_writer.writerows(csv_data) #write rows value from the csv_data to the created csv sheet\ 
                #that is to be exported 
                print (f"Student data has been saved to {filename}.") #successful output statement!

        elif user_choice == "4":
            print ("Exiting the Student Data Management System, Goodbye!!") #program exit condition message
            break
        else:
            print ("Invalid choice, please enter a number between 1-4. ")
        
if __name__ == "__main__":       ### for direct script execution
    menu_interface()       ###calling the function
    


# In[ ]:




