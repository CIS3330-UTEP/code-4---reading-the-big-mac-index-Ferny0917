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
    pass # Remove this line and code your function

def get_the_most_expensive_big_mac_price_by_year(year):
    pass # Remove this line and code your function

if __name__ == "__main__":
    result_a = get_big_mac_price_by_year(2012,'jpn')
    print(result_a)
    result_b = get_big_mac_price_by_country('mex')
    print(result_b)