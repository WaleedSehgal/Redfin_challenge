# San Francisco Food Trucks data

This repositiory contains a command-line python program that prints out list of open food trucks in the city of San Francisco. The program queries the Mobile Food Schedule API to get food truck data. 

## Prerequisites to run the program

To run the program, make sure you full fill the requirements below:

* The minimum python version required to run this program is python 3.5.2. If you already have python installed, check your python version by running the following command in your terminal.

    ```
    python --version
    ```

    If you do not have python installed, download and install the latest python version [here](https://www.python.org/downloads/)


* Install the following two required libraries using [**pip**](https://pip.pypa.io/en/stable/) the de facto python package installer:
    
    * Install the [**requests**](http://docs.python-requests.org/en/master/) library to make HTTP requests to external APIs. Run the following command in the terminal to install requests.
        ```
        pip install request
        ```

    * Install the **pandas** library to tabulate and view data, for more information on pandas, see [pandas documentation](https://pandas.pydata.org/pandas-docs/stable/). Run the following command in the terminal to install pandas.
        ```
        pip install pandas
        ```
    
    
    >**Note:**
    >If you are calling this API within an application and feel like your application might call it quite extensively, please follow the instuctions in the [Mobile Food Schedule API documentation](https://dev.socrata.com/docs/app-tokens.html) to get an application token. The API requests that can be made without using an application token are limited. Request with application tokens have a higher limit, but might be throtteled if abused.

## Run the program

To run this program from a command-line terminal follow the steps below:

1. [Clone](https://help.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository) this repository from github.

2. Navigate to the repository folder in your terminal.

3. Run the program using the following command:

    ```
    python show_open_food_trucks.py
    ```

    On a successful execution, the program will display maximum 10 results at a time, it will prompt you to input 'y' to view next results or 'n' to quit.




