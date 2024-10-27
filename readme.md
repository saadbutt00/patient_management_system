                                                                      Patient Management System
Overview
The Patient Management System is a simple web application built using Streamlit. It allows users to manage patient information in a hospital or clinic environment. 
The application uses a linked list data structure to manage the list of patients, where each patient has a unique ID, name, age, medical condition, urgency level, 
and admission time.

Users can:

Add new patients.
Update patient information.
Remove patients from the system.
Display the list of patients, sorted either by admission time or urgency level.
Features
Add Patient:

Users can add a patient by providing basic details such as ID, name, age, medical condition, urgency level, and admission time.
Admission time is automatically captured as the current date and time when the patient is added.
Update Patient:

Users can update the details of a patient by specifying the patient ID and the new details (name, age, medical condition, urgency level).
Remove Patient:

Users can remove a patient from the system by entering the patient ID.
Display Patients:

Users can display the list of patients sorted by either admission time or urgency level.
The list is displayed with all details such as patient ID, name, age, medical condition, urgency level, and admission time.
Data Structure
The application uses a Linked List to store and manage patient records. Each patient is an instance of the Patient class, 
which contains attributes like patient ID, name, age, medical condition, urgency level, admission time, and a pointer to the next patient.

How to Use
1. Add a Patient
Fill in the form for adding a patient by providing their ID, name, age, and medical condition.
Select an urgency level from 1 to 5 (1 being the lowest and 5 being the highest).
Click "Add Patient" to add the patient to the list.
2. Update a Patient
To update a patient's information, enter the patient ID of the patient to be updated.
Fill in the updated information (name, age, medical condition, urgency level).
Click "Update Patient" to update the patient's details.
3. Remove a Patient
Enter the patient ID of the patient you want to remove.
Click "Remove Patient" to remove the patient from the list.
4. Display Patients
Choose how you want to sort the list of patients (either by admission time or urgency level).
Click "Show Patients" to display the list of patients.

App Link: https://patientmanagementsystem.streamlit.app/
