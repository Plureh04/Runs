Project README
Getting Started with Google Colab

To run this project, please follow these steps to set up your environment in Google Colab:
1. Copy the Code to Google Colab

    Open Google Colab

    Click on "File" > "New Notebook" to create a new Colab notebook

    Copy and paste the provided Python code into the notebook cells

2. Download the Required CSV File

    Download the dataset CSV file provided with this project to your local machine

3. Upload the CSV File to Google Colab

In your Colab notebook:
python:

    from google.colab import files
    uploaded = files.upload()

Click the "Choose Files" button that appears when you run this cell

Select the CSV file you downloaded

Wait for the upload to complete

4. Verify the File is in Colab's Content

After uploading, verify the file is available by running:
python

    import pandas as pd
    import os

# List files in the content directory
print(os.listdir())

# Verify your CSV file is present
# If your file is named 'data.csv', for example:
if 'data.csv' in os.listdir():
    print("File successfully uploaded!")
    df = pd.read_csv('data.csv')
    print(df.head())
else:
    print("File not found - please upload again")

5. Run the Project

    You can now execute the rest of the code cells in order

    Make sure to update any file paths in the code to match your CSV filename
