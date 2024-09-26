import csv
import pandas as pd
big_mac_file = './big-mac-full-index.csv'

df = pd.read_csv('./big-mac-full-index.csv')



year =  2010
query_dt = f"((date >= ' {year}-01-01' and date <= '{year}-12-31'))"
df_result = df.query(query_dt)

country_code = 'arg'
query_cc = f"(iso_a3 == '{country_code.upper()}')"
sub_df = df_result.query(query_cc)


def get_big_mac_price_by_year(year,country_code):
    query_dt = f"((date >= ' {year}-01-01' and date <= '{year}-12-31'))"
    df_result = df.query(query_dt)
    query_cc = f"(iso_a3 == '{country_code.upper()}')"
    sub_df = df_result.query(query_cc)
    return sub_df

def get_big_mac_price_by_country(country_code):
    pass # Remove this line and code your function

def get_the_cheapest_big_mac_price_by_year(year):
    pass # Remove this line and code your function

def get_the_most_expensive_big_mac_price_by_year(year):
    pass # Remove this line and code your function

if __name__ == "__main__":
    result_a = get_big_mac_price_by_year ()
    print(result_a) 