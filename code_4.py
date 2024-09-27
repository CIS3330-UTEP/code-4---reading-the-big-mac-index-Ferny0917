import csv
import pandas as pd
big_mac_file = './big-mac-full-index.csv'

df = pd.read_csv('./big-mac-full-index.csv')



def get_big_mac_price_by_year(year,country_code):
    # code to get the year simpler because it woudn't read it from the string
    query_dt = f"(date >= '{year}-01-01' and date <= '{year}-12-31')"
    df_result = df.query(query_dt)
    #get the country code even if its lower case
    query_cc = f"(iso_a3 == '{country_code.upper()}')"
    sub_df = df_result.query(query_cc)
    #get the dollar amount from the column and get the mean value
    mean_price = sub_df['dollar_price'].mean()
    #answer in two values
    return round (mean_price,2)

def get_big_mac_price_by_country(country_code):
    #I just copy this line from the first code that focus on the country code
    query_cc = f"(iso_a3 == '{country_code.upper()}')"
    #query from country that we remove result cause we dont need date
    sub_df = df.query(query_cc)
    # mean of price 
    mean_price = sub_df['dollar_price'].mean()
    return round (mean_price,2)



def get_the_cheapest_big_mac_price_by_year(year):
    #copy the line for checking the years
    query_dt = f"(date >= '{year}-01-01' and date <= '{year}-12-31')"
    df_result = df.query(query_dt)
    #df_result['dollar_price'] is selecting the column with that name. .loc lcoating the row by and index and idxmin check for the lowest vaule from the row and columns
    mini = df_result.loc[df_result['dollar_price'].idxmin()]
    #Here the code is getting the information from mini and looks for country name
    country_name = mini['name']
    #Here the code is getting the information from mini and looks for country code
    country_cc = mini['iso_a3']
    #Here the code is also getting information from mini and getting the value from dollar price and rounds into 2 decimal place
    price = round(mini['dollar_price'],2)
    return  f"{country_name}({country_cc}): ${price}"

def get_the_most_expensive_big_mac_price_by_year(year):
    query_dt = f"(date >= '{year}-01-01' and date <= '{year}-12-31')"
    df_result = df.query(query_dt)
    #df_result['dollar_price'] is selecting the column with that name. .loc lcoating the row by and index and idxmax check for the highest vaule from the row and columns
    maxi = df_result.loc[df_result['dollar_price'].idxmax()]
    #Here the code is getting the information from mini and looks for country name
    country_name = maxi['name']
    #Here the code is getting the information from mini and looks for country code
    country_cc = maxi['iso_a3']
    #Here the code is also getting information from mini and getting the value from dollar price and rounds into 2 decimal place
    price = round(maxi['dollar_price'],2)
    return  f"{country_name}({country_cc}): ${price}"

if __name__ == "__main__":
    result_a = get_big_mac_price_by_year(2012,'jpn')
    print(result_a)
    result_b = get_big_mac_price_by_country('mex')
    print(result_b)
    result_c = get_the_cheapest_big_mac_price_by_year(2008)
    print(result_c)
    result_d = get_the_most_expensive_big_mac_price_by_year(2003)
    print(result_d)