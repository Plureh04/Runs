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

Click the "Choose Files" button that appears when you run this cell

Select the CSV file you downloaded

Wait for the upload to complete

4. Verify the File is in Colab's Content

After uploading, verify the file is available by running:
python

    import pandas as pd

    # Read the CSV file into a pandas DataFrame
    df = pd.read_csv('Golden.csv')

    filtered = df[df['Adittional comment'] == 'good']

    print(filtered)

5. Run the Project

    You can now execute the rest of the code cells in order

    Make sure to update any file paths in the code to match your CSV filename
