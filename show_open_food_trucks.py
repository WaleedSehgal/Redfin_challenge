#!/usr/bin/env python

# Make sure to install requests, pandas and tabulate before running:
# > pip install requests
# > pip install pandas
# > pip install tabulate
# Documentation for the requests library can be found here: http://docs.python-requests.org/en/master/
# Documentation for pandas can be found here: https://pandas.pydata.org/pandas-docs/stable/
# Documentation for tabulate can be found here: https://pypi.org/project/tabulate/

import os
import sys
import json
import requests
import datetime
import pandas as pd
from tabulate import tabulate

class Display(object):

    def __init__(self):
        self.offset = 0

        # EOF indicates end of results
        self.EOF = False

    # Function to generate URL 
    def get_url(self):
        today = datetime.datetime.today()
        day = today.weekday()+1
        curr_time = datetime.datetime.now().time().strftime('%H:%M')

        url  = "http://data.sfgov.org/resource/bbb8-hzi6.json?dayorder={}&$select=applicant, location \
        &$where=start24 <='{}' AND end24>='{}'&$limit=10&$offset={}&$order=applicant ASC".format(day,curr_time,curr_time,self.offset)

        return url

    # Returns current open trucks
    def return_open_trucks(self):

        data = Data()
        open_trucks = data.get_parsed_truck_data()

        # Handles exception cases
        if open_trucks is None:
            print("Data request not successfull!")
            sys.exit()
        
        # If there are not trucks open
        elif len(open_trucks)==0:
            print("There are no food trucks open currently!")
            sys.exit()
        
        if len(open_trucks)<10:
            print(tabulate(open_trucks, headers='keys'))
            self.EOF = True
        
        return open_trucks

class Data(object):

    # Request current open trucks
    def get_data(self,url):
        
        try:
            response = requests.get(url, timeout=5)
        
        # If any exception occurs, return nothing
        except requests.exceptions.RequestException as e:
            return None
        
        # For status 200
        return response

        # # For status 200
        # response.encoding='utf-8'
        # data = response.json()
        # open_trucks = self.parse_truck_data(data)
        
        # return open_trucks
    
    # Parse truck data
    def get_parsed_truck_data(self):
            
            diplay = Display()
            url = display.get_url()
            response = self.get_data(url)

            data = response.json()
            df = pd.DataFrame(columns=['NAME', 'ADDRESS'])
            for truck in data:
                df = df.append({'NAME':truck['applicant'], 'ADDRESS':truck['location']}, ignore_index=True)

            return df


if __name__ == "__main__": 

    display = Display()
    
    while not display.EOF:
        
        trucks = display.return_open_trucks()
        
        if trucks is None:
            print("Request timed out!")
            sys.exit()

        if not display.EOF:
            print(tabulate(trucks, headers='keys'))
            next_results = input("Want to see more result? (y/n), and 'p' for previous results").lower()
            if next_results=="y":
                display.offset+=10
            elif next_results=="p":
                 if display.offset>=10:
                    display.offset-=10
                 else:
                     print("No more results prior to this!")
                     break
            else:
                break
        else:
            print("\n No more results to show! \n")
            break