# I write and run this python program that calculate the monthly average prices of Google stock from
# Jan 01, 2016 to Dec 31, 2020 and show the six highest monthly average prices and the six lowest
# monthly average prices for Google’s stock within these five years.
import pandas as pd


def get_data_list(filename):  # Read the raw .csv file and return the 2D list containing all the daily stock prices
    source_data = pd.read_csv(filename, header=None)  # Read the csv file and get the dataframe including columns' names
    dlist = source_data.values.tolist()  # Convert the dataframe to the 2D list
    return dlist


def get_monthly_average(dlist):  # Return the 2D list containing the date and the average price of every month
    length = len(dlist)  # Get the number of lines in the 2D list
    mon_and_year_list = []  # Create a list with the Month and Year
    ave_price_perm = []  # Create a list with average prices
    year = 2016  # The start year of data is 2016
    while year <= 2020:  # The end year of data is 2020
        month = 1
        while month <= 12:
            adj_close = 0
            sum_volumn = 0
            i = 1  # The first line doesn't have data.
            while i < length:
                strlist = dlist[i][0].split('/')  # Split one Date into three substrings, and the separator is ‘/’
                # The first substring is month and the third is year.
                if int(strlist[0]) == month and int(strlist[2]) == year:
                    adj_close += float(dlist[i][5]) * float(dlist[i][6])  # Calculate the sum of stock price this month
                    sum_volumn += float(dlist[i][6])  # Calculate the sum of volume this month
                i = i + 1  # Move to next line
            ave_price = adj_close / sum_volumn  # Compute the average price this month
            mon_and_year_list.append(str(month) + '/' + str(year))
            ave_price_perm.append(ave_price)  # Appending every data to the list it should be in
            month = month + 1  # Move to next month
        year = year + 1  # Move to next year
    ave_monthly_list = [list(t) for t in zip(mon_and_year_list, ave_price_perm)]
    # Aggregates two list and convert tuple into list
    # Get the 2D list with monthly average prices
    return ave_monthly_list


# Find six highest monthly average prices and the six lowest monthly average prices
def find_six_highest_lowest_monthly_average_price(ave_monthly_list):
    ave_monthly_list = sorted(ave_monthly_list, key=(lambda x: x[1]), reverse=True)
    # Sort the list according to monthly average prices from high to low
    six_highest_monthly_list = ave_monthly_list[0:6]
    # Get the six highest monthly average prices
    ave_monthly_list = sorted(ave_monthly_list, key=(lambda x: x[1]))
    # Sort the list according to monthly average prices from low to high
    six_lowest_monthly_list = ave_monthly_list[0:6]
    # Get the six lowest monthly average prices
    six_highest_lowest_monthly_list = six_highest_monthly_list + six_lowest_monthly_list
    # Get the 2D list that containing the six highest monthly average prices and six lowest monthly average prices
    return six_highest_lowest_monthly_list


# Return a new list containing six highest monthly average prices with the new date format
def reformat_max_res(six_highest_monthly_list):
    i = 0
    while i < 6:
        strlist = six_highest_monthly_list[i][0].split('/')
        if int(strlist[0]) == 1:
            six_highest_monthly_list[i][0] = 'Jan ' + strlist[1]
        elif int(strlist[0]) == 2:
            six_highest_monthly_list[i][0] = 'Feb ' + strlist[1]
        elif int(strlist[0]) == 3:
            six_highest_monthly_list[i][0] = 'Mar ' + strlist[1]
        elif int(strlist[0]) == 4:
            six_highest_monthly_list[i][0] = 'Apr ' + strlist[1]
        elif int(strlist[0]) == 5:
            six_highest_monthly_list[i][0] = 'May ' + strlist[1]
        elif int(strlist[0]) == 6:
            six_highest_monthly_list[i][0] = 'Jun ' + strlist[1]
        elif int(strlist[0]) == 7:
            six_highest_monthly_list[i][0] = 'Jul ' + strlist[1]
        elif int(strlist[0]) == 8:
            six_highest_monthly_list[i][0] = 'Aug ' + strlist[1]
        elif int(strlist[0]) == 9:
            six_highest_monthly_list[i][0] = 'Sep ' + strlist[1]
        elif int(strlist[0]) == 10:
            six_highest_monthly_list[i][0] = 'Oct ' + strlist[1]
        elif int(strlist[0]) == 11:
            six_highest_monthly_list[i][0] = 'Nov ' + strlist[1]
        elif int(strlist[0]) == 12:
            six_highest_monthly_list[i][0] = 'Dec ' + strlist[1]
        # Reformat the months from number to letter
        i = i + 1  # Move to next line
    return six_highest_monthly_list


# Return a new list containing six lowest monthly average prices with the new date format
def reformat_min_res(six_lowest_monthly_list):
    i = 0
    while i < 6:
        strlist = six_lowest_monthly_list[i][0].split('/')
        if int(strlist[0]) == 1:
            six_lowest_monthly_list[i][0] = 'Jan ' + strlist[1]
        elif int(strlist[0]) == 2:
            six_lowest_monthly_list[i][0] = 'Feb ' + strlist[1]
        elif int(strlist[0]) == 3:
            six_lowest_monthly_list[i][0] = 'Mar ' + strlist[1]
        elif int(strlist[0]) == 4:
            six_lowest_monthly_list[i][0] = 'Apr ' + strlist[1]
        elif int(strlist[0]) == 5:
            six_lowest_monthly_list[i][0] = 'May ' + strlist[1]
        elif int(strlist[0]) == 6:
            six_lowest_monthly_list[i][0] = 'Jun ' + strlist[1]
        elif int(strlist[0]) == 7:
            six_lowest_monthly_list[i][0] = 'Jul ' + strlist[1]
        elif int(strlist[0]) == 8:
            six_lowest_monthly_list[i][0] = 'Aug ' + strlist[1]
        elif int(strlist[0]) == 9:
            six_lowest_monthly_list[i][0] = 'Sep ' + strlist[1]
        elif int(strlist[0]) == 10:
            six_lowest_monthly_list[i][0] = 'Oct ' + strlist[1]
        elif int(strlist[0]) == 11:
            six_lowest_monthly_list[i][0] = 'Nov ' + strlist[1]
        elif int(strlist[0]) == 12:
            six_lowest_monthly_list[i][0] = 'Dec ' + strlist[1]
        # Reformat the months from number to letter
        i = i + 1  # Move to next line
    return six_lowest_monthly_list


# Output six highest monthly average prices and six lowest monthly average prices
def print_info(ave_monthly_list):
    six_highest_lowest_monthly_list = find_six_highest_lowest_monthly_average_price(ave_monthly_list)  # Find the six
    # highest monthly average prices and the six lowest monthly average prices for Google’s stock.
    six_highest_monthly_list = six_highest_lowest_monthly_list[0:6]  # Get the 2D list that containing the six highest
    # monthly average prices only
    six_highest_monthly_list = reformat_max_res(six_highest_monthly_list)  # Reformat the dates of list
    six_lowest_monthly_list = six_highest_lowest_monthly_list[6:12]  # Get the 2D list that containing the six lowest
    # monthly average prices only
    six_lowest_monthly_list = reformat_min_res(six_lowest_monthly_list)  # Reformat the dates of list
    print("Google Stock Prices Between Jan 01, 2016 and Dec 31, 2020")
    print()
    print("Six Highest Monthly Average Prices:")
    for e in six_highest_monthly_list:
        print(e[0] + ': ' + '%.2f' % e[1])  # Print each stock price to two decimal places
    print()
    print("Six Lowest Monthly Average Prices")
    for e in six_lowest_monthly_list:
        print(e[0] + ': ' + '%.2f' % e[1])  # Print each stock price to two decimal places
    print()


def main():
    name_file = input("Please enter the name of your csv file: ")  # Ask for the input file name
    list_data = get_data_list(name_file)  # Read the file and get list containing all data
    print(list_data)  # Print the list with all data
    print()
    aveprice_monthly_list = get_monthly_average(list_data)  # Compute the monthly average prices in each year
    print(aveprice_monthly_list)  # Print the list with monthly average prices
    print()
    print_info(aveprice_monthly_list)  # Print six highest monthly average prices and six lowest monthly average prices


if __name__ == "__main__":
    main()
