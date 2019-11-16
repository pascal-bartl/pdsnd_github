import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')

    while True:
        city = input('Would you like to see data for Chicago, New York, or Washington: ')
        if city not in ('Washington', 'Chicago', 'New York'):
            print("Not an appropriate choice. This Input Function is case sensitive.")
        else:
            break

    while True:
        case_m = input('Would you like to filter the data by month, day, both or not at all? Type "none" for no time filter: ')
        if case_m not in ('month', 'day', 'both', 'none'):
            print("Not an appropriate choice. This Input Function is case sensitive.")
        else:
            break

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        Month_Temp = input('[If you entered "day" or "none" before just enter a random month now, it will not affect the analysis] Which month? All, January, February, March, April, May, or June?: ')
        if Month_Temp not in ('All', 'January', 'February', 'March', 'April', 'May', 'June'):
            print("Not an appropriate choice. This Input Function is case sensitive.")
        else:
            break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        try:
            while True:
                Day_Temp = input('[If you entered "month" or "none" before just enter a random day now, it will not affect the analysis] Which day? All, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday: ')
                if Day_Temp not in ('All', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'):
                    print("Not an appropriate choice. This Input Function is case sensitive.")
                else:
                    break
            break
        except ValueError:
            print("Not an appropriate choice. This Input Function is case sensitive.")

    if case_m in ('both'):
        month = Month_Temp
        day = Day_Temp
    elif case_m in ('month'):
        month = Month_Temp
        day = 'All'
    elif case_m in ('day'):
        month = 'All'
        day = Day_Temp
    else:
        month = 'All'
        day = 'All'



    print('-'*40)
    return city, case_m, month, day


##########################################################################

def load_data(city, case_m, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    monthh = month
    dayy = day
    city = city

    #city, month, day = get_filters()
    #df = pd.DataFrame(CITY_DATA)
    df_w = pd.read_csv('./washington.csv')
    df_w['City'] = 'Washington'
    df_n = pd.read_csv('./new_york_city.csv')
    df_n['City'] = 'New York'
    df_c = pd.read_csv('./chicago.csv')
    df_c['City'] = 'Chicago'

    df_temp = df_w
    df_temp = df_temp.append(df_n)
    df_temp = df_temp.append(df_c)

    # convert the Start Time column to datetime
    df_temp['Start Time'] = pd.to_datetime(df_temp['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df_temp['month'] = df_temp['Start Time'].dt.month
    df_temp['day_of_week'] = df_temp['Start Time'].dt.weekday_name
    df_temp['hour'] = df_temp['Start Time'].dt.hour
    df_temp['Start End Combination'] = df_temp['Start Station'] + df_temp['End Station']
    df_temp['Trip Duration Hour'] = df_temp['Trip Duration'] / 3600

    # filter by month if applicable
    monthhh = monthh.lower()
    if monthhh != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        monthhh = months.index(monthhh) + 1

        # filter by month to create the new dataframe
        df_temp = df_temp[df_temp['month'] == monthhh]

    #filter by day of week if applicable
    dayyy = dayy.lower()
    if dayyy != 'all':
        #filter bypyt day of week to create the new dataframe
        df_temp = df_temp[df_temp['day_of_week'] == dayyy.title()]


    ## city filtern
    is_city =  df_temp['City']==city
    df = df_temp[is_city]

    return df

#################################################################################

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print('most common month [output as an integer (e.g., 1=Januray)]:', df['month'].mode()[0])

    # TO DO: display the most common day of week
    print('most common day of week:', df['day_of_week'].mode()[0])

    # TO DO: display the most common start hour
    print('most common start hour:', df['hour'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


#################################################################################

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print('most commonly used start station:', df['Start Station'].mode()[0])

    # TO DO: display most commonly used end station
    print('most commonly used end station:', df['End Station'].mode()[0])

    # TO DO: display most frequent combination of start station and end station trip
    print('most frequent combination of start station and end station trip:', df['Start End Combination'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

#################################################################################

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print('total travel time [Hours]:', df['Trip Duration Hour'].sum())

    # TO DO: display mean travel time
    print('mean travel time [Hours]:', df['Trip Duration Hour'].mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

#################################################################################

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()



    # TO DO: Display counts of user types
    print('counts of user types:', df['User Type'].value_counts())


    while True:
        try:
            print('counts of gender:', df['Gender'].value_counts())

            # TO DO: Display earliest, most recent, and most common year of birth
            print('earliest year of birth:', int(df['Birth Year'].min()))
            print('most recent year of birth:', int(df['Birth Year'].max()))
            print('most common year of birth:', int(df['Birth Year'].mode()[0]))
            #while True:
                #day_temp = input('[If you entered "month" or "none" before just enter a random day now, it will not affect the analysis] Which day? All, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday: ')
                #if day_temp not in ('All', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'):
                    #print("Not an appropriate choice. This Input Function is case sensitive.")
                #else:
                    #break
            break
        except ValueError:
            print("THERE ARE NO USER FURTHER GENDER AND BIRTH YEAR STATISTICS FOR CITY: WASHINGTON")
            break


    #print('counts of gender:', df['Gender'].value_counts())

    # TO DO: Display earliest, most recent, and most common year of birth
    #print('earliest year of birth:', int(df['Birth Year'].min()))
    #print('most recent year of birth:', int(df['Birth Year'].max()))
    #print('most common year of birth:', int(df['Birth Year'].mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


#################################################################################

def main():
    while True:
        city, case_m, month, day = get_filters()

        #city = 'Washington'
        #case_m = 'both'
        #month = 'All'
        #day = 'All'

        df = load_data(city, case_m, month, day)


        #print(city)
        #print(case_m)
        #print(month)
        #print(day)
        #print(df)
        #df.to_csv(r'.\File Name.csv')

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        count = -5
        #print(count)

        while True:

            while True:
                answ = input('Would you like to view indivual trip data? Type "yes" or "no".: ')
                if answ not in ('yes', 'no'):
                    print("Not an appropriate choice. This Input Function is case sensitive.")
                else:
                    break


            if answ.lower() != 'no':
                count = count + 5
                #print(count)
                print(df.iloc[count])
                print(df.iloc[count+1])
                print(df.iloc[count+2])
                print(df.iloc[count+3])
                print(df.iloc[count+4])

                #answ = input('Would you like to view indivual trip data? Type "yes" or "no".: ')
            else:
                break

        while True:
            restart = input('\nWould you like to restart? Enter yes or no.\n')
            if restart not in ('yes', 'no'):
                print("Not an appropriate choice. This Input Function is case sensitive.")
            else:
                break

        if restart.lower() != 'yes':
                break


if __name__ == "__main__":
    main()
