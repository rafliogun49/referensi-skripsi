import os
import json
# Specify the directory path where your PDF files are located

# Get all the files in the directory
file_list = os.listdir("./")

# Filter the PDF files
pdf_files = [file for file in file_list if file.endswith('.pdf')]

pdf_file_names = []

# Append the PDF file names to the list
for pdf_file in pdf_files:
    name_file = {
        'name': pdf_file
    }
    pdf_file_names.append(name_file)

# Convert the list to JSON format
json_data = json.dumps(pdf_file_names)

# Print the JSON data
print(json_data)

# Write the JSON data to a file
with open('pdf_files.json', 'w') as json_file:
    json_file.write(json_data)
