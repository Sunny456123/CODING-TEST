#1. Write a Python program to read a CSV file and display its contents.
import csv
import os

# Define the path to your CSV file
file_path = r'C:\Users\acer\Documents\Desktop\python files\Book1.csv'

# Check if the file exists
if os.path.exists(file_path):
    # Open the CSV file
    with open(file_path, mode='r', newline='') as file:
        # Create a CSV reader object
        csv_reader = csv.reader(file)
        
        # Iterate over the rows in the CSV file
        for row in csv_reader:
            print(row)
else:
    print(f"File not found: {file_path}")
