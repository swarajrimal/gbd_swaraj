# About the project
This project is to create Python code snippets as requested for pre-interview by GrowByData. In this project, I have include snippets for ETL including data cleansing, usage of Lambda function for data manipulation, and visualization of data using Matplotlib/Seaborn tools. The data is present in a CSV file, and contains the time-record of the values of 4 different particulate matters in the environment pertaining to a single location - Ratnapark.

I have uploaded 3 separate Python files, and a CSV data file to the repository. I will describe the contents of each file in detail below.

1. **etl.py:**
This code snippet contains code to collect CSV data, look for data issues, clean and transform data, and store the data to a JSON file. The CSV file should be presnet in the current working directory and the JSON file will be stored in the same working directory.
2. **lambda.py:**
This code snippet contains lambda expression for data manipulation within a dataframe. 
3. **visualize.py:**
This code snippet contains code to visualize data based on the categories and attributes of the data. I have used Seaborn and Matplotlib to create Boxplot, Histogram and Time-Series Scatterplot to visualize the data.

## Running the code
Running the code is very straightforward. Clone the repository to your local directory and run each Python code separately using your favorite editor. Follow the steps:
1. First run *etl.py* file. This will read the contents of CSV, clean the data and stores the data to a JSON file named **"ratnapark.json"** within the current working directory.

2. Then run *lambda.py* file. It will read the contents from the JSON file and simply add a *'_'* character in front of the contents of *"particulate_matter"* column. It will then print out the first 5 results.

3. Lastly, run the *visualize.py* file. It will produce the Boxplot for *"values"* for each *"partuculate_matter"* category. It will also produce a Histogram of *"values"* column to examine its distribution, and will produce a Time-Series Scatterplot of *"values"* column for each *"particulate_matter"*.

## Explanation and Results
I will now describe the working of the code snippets inside each of the file. 

1. **etl.py**

We start by importing the packages of OS operation and for Pandas. We use Pandas to read and write dataframes using Python. We first make sure the current working directory is set and all the reading and writing happens in that directory. 
We then read the contents of our data from a CSV file named *"ratnapark.csv"* to a variable named *file*. The variable *file* now contains a dataframe created using the data contents of the CSV file and is ready for further analysis in Python.
Upon inspection, I found the column name *"particulate_matter"* had a trailing space, and so I removed the space by renaming the column. Next, I checked for any missing values and found that none of the attributes had any missing values.

I also checked for the data types of the columns and found them all to be of type *object*, which I felt should be converted into the actual data types. The attribute *datetime* needed to be converted to *date* type, and the attribute *value* needed to be converted to *float* type.
I converted the data type *datetime* field to *date* without any issues, but converting *value* to *float* was giving me errors. Upon inspection, I found inconsistencies in some of the rows of *value* column where there were some irrelevent data instead of floating point numbers (represented by string).
I then removed those rows with inconsistent *value* data using regex filtering and creating subset of the data. About 15 rows were removed in total. I was then able to convert the data type of *value* column to *float* in new dataset *df* without any issues.

Next, I checked the distribution of the *value* column to look for any extreme values or outliers present. The 75th percentile value and the maximum value of the column had a very large difference, suggesting presence of outliers. 
count |   59070.000000
----- | ------
mean   |     53.838407
std    |    128.955722
min    |      0.100000
25%    |     11.300000
50%    |     30.200000
75%    |     63.300000
max    |   9625.600000

I removed the outliers by filtering the data for the vlaues more than 1.5 times the inter-quartile distance from the 75th percentile value. The filtering removed 3,794 records from the dataset. The statistic of the final dataset looks like this.
count  |  55276.000000
------- | -------
mean  |      36.919034
std    |     33.027273
min     |     0.100000
25%     |    10.000000
50%     |    27.400000
75%     |    54.300000
max     |   141.200000

Now the data looked clean and transformed, and ready to be stored in JSON format to the local storage. I reset the index of the new dataset, named it as *df1*, and stored it in JSON file named **"ratnapark.json"** in the current working directory. This was done using *to_json* tool of Pandas.

2. **lambda.py**

This code snippet simply reads the content of the JSON file named **"ratnapark.json"** from the current working directory using Pandas, and applies a lambda function to append a character to the *"particulate_matter"* column.

The contents of JSON file is loaded as a dataframe in *df* variable. I then use the *apply()* function along with *lambda* function to add a *'_'* character in front of the contents of *"particulate_matter"* attribute and apply to all rows of the dataframe. The resulting sample is then printed out for users to inspect the result of the function.

3. **visualize.py**

This code snippet produces visualizations based on the data. We first load the contents of the JSON file named **"ratnapark.json"** from the current working directory using Pandas, convert it to dataframe, and load into a variable named *df*. Next, we create a visualization for the relationship of *"value"* attribute with the *"particulate_matter"* column by creating a Boxplot using Seaborn tool.


