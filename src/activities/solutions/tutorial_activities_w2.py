### WEEK 2 - TUTORIAL SOLUTIONS
# 02-01 - Python Structure
from pathlib import Path
from importlib.resources import files

# Using pathlib.Path - WORKS
#folder name, file name
# QUESTIONN - why dont you need 3 .parents for actvities, src and the working file?
def activity_02_01_pathlib():
    csv_file = Path(__file__).parent.parent.joinpath("data", "paralympics_raw.csv")
    if csv_file.exists():
        print(f"CSV file found: {csv_file}")
    else:
        print("CSV file not found.") 

# Using importlib.resources - WORKS
def activity_02_01_importlib():
    # big folder.small folder, file name.csv
    csv_file= files("activities.data").joinpath("paralympics_raw.csv")

    if csv_file.exists():
        print(f"CSV file found: {csv_file}")
    else:
        print("CSV file not found.")

# QUESTION - Can you automate the csv read if its in a folder of multiple
# 02-02 - Python Structure
import pandas as pd
def activity_02_02():
    xlsx_file = Path(__file__).parent.parent.joinpath("data","paralympics_all_raw.xlsx")
    csv_file = Path(__file__).parent.parent.joinpath("data", "paralympics_raw.csv")

    csv_df = pd.read_csv(csv_file)
    first_sheet_df = pd.read_excel(xlsx_file) #reads sheet 1 
    second_sheet_df = pd.read_excel(xlsx_file, sheet_name=1) #reads sheet 2 (counts from 0)
    return csv_df, first_sheet_df, second_sheet_df 

# 02-03 - Pandas Describe
# Pandas imported as pd earlier
def activity_02_03_describe(my_dataframe):
    """ Prints description of the dataframe including: number of columns,
        number of rows, first and last 5 rows, data types and statistcial 
        summaries

        Parameters:  
        dataframe (df): dataframe of the read relevant files

        Returns:
        statement (str): qualitative description of the dataframe

    """
    print(my_dataframe.shape)
    print(my_dataframe.head())
    print(my_dataframe.tail())
    print(my_dataframe.columns)
    print(my_dataframe.dtypes)
    print(my_dataframe.info())
    print(my_dataframe.describe())
    
    # the events ones are not the same - 32 vs 35

# 02-04 - Missing Values
# Explores data quality
def activity_02_04_missing(dataframe):
    num_null = dataframe.isna().sum()
    print(num_null)

    missing_rows = dataframe[dataframe.isna().any(axis=1)]
    return missing_rows

# 02-05 - Plot Overview
import matplotlib.pyplot as plt
#No activity code - justread text on styling and creating plots

# 02-06 - Plot Distribution
def activity_02_06_histogram(dataframe):
    columns = ['participants_m']
    dataframe[columns].hist()
    plt.show()

def activity_02_06_boxplot(dataframe):
    columns = ['participants_m']
    dataframe[columns].boxplot()
    plt.show()

# 02-07 - Plot Timeseries
def activity_02_07_plot_tsreies(dataframe):
    fig, ax = plt.subplots()
    #cleaning
    dataframe["type"].str.strip().str.lower()
    dataframe["start"] = pd.to_datetime(dataframe["start"])

    summer_df = dataframe[dataframe["type"] == "summer"]
    winter_df = dataframe[dataframe["type"] == "winter"]
    
    #Summer Plot
    summer_df.plot(x="start", y = "participants_m", ax=ax)
    summer_df.plot(x="start", y = "participants_f", ax=ax)

    #Winter Plot
    winter_df.plot(x="start", y = "participants_m", ax=ax)
    winter_df.plot(x="start", y = "participants_f", ax=ax)
    
    ax.set_xlabel("Year")
    ax.set_ylabel("Number of Participants")
    ax.grid(True)
    ax.legend()
    plt.show()

# 02-08 - Categorical Data
def activity_02_08_categorical(dataframe):
    type_count = dataframe["type"].value_counts()
    print(type_count)

    dis_count = dataframe["disabilities_included"].value_counts()
    print(dis_count)

# 02-09 - Data Prep
def activity_02_09_prep(dataframe):

    #Information studens want by column: country, host, start, end, events, sports, participants_m, participants_f, participants
    columns_needed = ["country", "host", "start", "end", "events", "sports", "participants_m", "participants_f", "participants"]

    # Removing columns not needed
    dataframe = dataframe[columns_needed].copy() # making a new df not changing og

    # Fixign missing info in columns
    for col in ["country", "start"]: #removing becuase it either hasnt been decided or taken place
        data_frame = dataframe.dropna(subset=[col], inplace=True)

    for col in ["participants_m", "participants_f", "participants", "events", "sports"]: 
        dataframe[col] = dataframe[col].fillna(0) #filling with 0

    # Changing datatypes
    dataframe["start"] = pd.to_datetime(dataframe["start"], dayfirst=True) #dayfirst because its dd/mm/yyyy
    dataframe["end"] = pd.to_datetime(dataframe["end"], dayfirst=True)
    for col in ["events", "sports", "participants_m", "participants_f", "participants"]:
        dataframe[col] = dataframe[col].astype(int)

    # Categorical data cleaning
    for col in ["country", "host"]:
        dataframe[col] = dataframe[col].str.strip().str.lower()

    for col in ["events", "sports", "participants_m", "participants_f", "participants"]:
        dataframe[col] = dataframe[col].apply(lambda x: max(x, 0)) #making sure no negative values

    #new columns: duration? days?
    return dataframe

# 02-10 - Locating Rows and Columns
# No activity code - just read text on finding rows and columns

# 02-11 - Removing Columns
def activity_02_11_remove(dataframe):
    columns_to_remove = ["disabilities_included", "URL", "highlights"]
    dataframe.drop(columns=columns_to_remove, inplace=True)

    return dataframe
   
# 02-12 - Resolve Missing/Incorrect Values
def activity_02_12_resolve(dataframe):
    column_check  = ["participants_m", "participants_f"]

    dataframe = dataframe.dropna(subset=column_check)
    dataframe = dataframe.reset_index(drop=True)
    print(dataframe.head(3))
    print(dataframe["type"].value_counts())
    return dataframe

def activity_02_12_replace(dataframe):
    dataframe["type"] = dataframe["type"].str.strip().str.lower()
    print(dataframe["type"].value_counts())
    return dataframe

# 02-13 - Change Datatypes
def activity_02_13_change(dataframe):

    #int
    columns_to_change = ["countries","events", "participants_m", "participants_f", "participants"]

    for col in columns_to_change:
        dataframe[col] = dataframe[col].fillna(0)
        dataframe[col] = dataframe[col].astype(int)

    #datetime
    dates_to_change = ["start", "end"]
    for col in dates_to_change:
        dataframe[col] = pd.to_datetime(dataframe[col], dayfirst=True)
        dataframe[col] = dataframe[col].dt.tz_localize("Europe/London")

    #str 
    str_to_change = ["type","country", "host","disabilities_included", "URL", "highlights"]
    for col in str_to_change:
        dataframe[col] = dataframe[col].str.strip().str.lower()
        dataframe[col] = dataframe[col].astype("string")

    print(dataframe.dtypes)
    return dataframe

# 02-14 - New Column
def activity_02_14_newcolumn(dataframe):
    dataframe["start"] = pd.to_datetime(dataframe["start"], dayfirst=True)
    dataframe["end"] = pd.to_datetime(dataframe["end"], dayfirst=True)
    duration_values = (dataframe["end"] - dataframe["start"]).dt.days.astype(int)

    dataframe.insert(dataframe.columns.get_loc("end")+1, "duration", duration_values)
    print(dataframe["duration"].head(3))

# 02-15 to 02-18 Joining & Saving Dataframes
#Just read texts on when to use merge, join and how to save dataframes

#MAIN
def main():
    # Returns all three dataframes (for each sheet)
    csv_df, first_sheet_df, second_sheet_df = activity_02_02() 
       
    # Call the function named 'describe_dataframe' - you may have a different name for your function
    #activity_02_03_describe(csv_df)
    #activity_02_03_describe(first_sheet_df)
    #activity_02_03_describe(second_sheet_df)

    #Investigating Data Quality 
    #activity_02_04_missing(csv_df)

    #Plotting Distribution
    #activity_02_06_histogram(csv_df)
    #activity_02_06_boxplot(csv_df)

    #activity_02_07_plot_tsreies(csv_df)

    #activity_02_08_categorical(csv_df)

    #activity_02_09_prep(csv_df)

    #activity_02_11_remove(csv_df)

    #Change input if you want to clean the resolved dataframe
    #activity_02_12_resolve(csv_df)
    #activity_02_12_replace(csv_df)
  
    #activity_02_13_change(csv_df)

    activity_02_14_newcolumn(csv_df)

if __name__ == "__main__":
    main()

