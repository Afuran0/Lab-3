import pandas as pd
# csv file data 
data= pd.read_csv("budget_data.csv")

#priting the first couple of rows from the csv file 

print ("Data preview:")
print(data.head())
print("\nColumn Names:")
print(data.columns)

data.columns =  data.columns.str.strip()
#rename the columns
data.rename(columns={"Date":"date","Profit/Losses":"rofit_loss"},inplace=True)

#print data values 
print("\nunique Date Values:")
print(data["date"].unique())

data["date"]= pd.to_datetime(data["date"],format="%Y-%m-%d",errors="coerce")

print("\nRows with unparseable dates:")
print(data[data['date'].isna()])

def serial_search(data, target_date):
    """Perform a serial (linear) search for the profit/loss on a given date."""
    for index, row in data.iterrows():
        if row['date'] == target_date:
            return row['profit_loss']
    return None

def binary_search(data, target_date):
    """ peform a binary search for the profit/loss on a given date."""
    low=0
    high=len(data)-1
    while low <=high:
        mid=(low+high)//2
        mid_date=data.iloc[mid]["date"]

    if mid_date==target_date:
        return data.iloc[mid]["profit_loss"]
    elif mid_date <target_date:
        low=mid+1
    else:
        high = mid - 1
    return None
#search for date 

test_date = pd.to_datetime("2023-01-02")

#serial search

serial_result = serial_search(data, test_date)
print(f"\nSerial Search Result for {test_date.date()}: {serial_result}")

#binary search
sorted_data = data.sort_values(by='date').reset_index(drop=True)
binary_result = binary_search(sorted_data, test_date)
print(f"Binary Search Result for {test_date.date()}: {binary_result}")
