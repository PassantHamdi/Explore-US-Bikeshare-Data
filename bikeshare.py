def main():
    import time
    import pandas as pd
    import numpy as np

    CITY_DATA = { 'Chicago': 'chicago.csv',
                  'New York': 'new_york_city.csv',
                  'Washington': 'washington.csv' }

    def get_filters(city, month, day):
        return city, month, day
        """
        Asks user to specify a city, month, and day to analyze.

        Returns:
            (str) city - name of the city to analyze
            (str) month - name of the month to filter by, or "all" to apply no month filter
            (str) day - name of the day of week to filter by, or "all" to apply no day filter
        """
    print('Hello! Let\'s explore some US bikeshare data!')
        # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input('Would you like to explore data for Chicago, New York or Washington?\n')
        if city not in('Chicago','New York', 'Washington'):
                    print('\nPlease make sure to select correct city')
        else:
            break
        # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input('Which month would you like to filter by? January, February, March, April, May, June? or type all for no filter\n')
        if month not in('January','February', 'March','April','May','June','all'):
                    print('\nPlease make sure to enter correct month')
        else:
            break

        # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input('Which day would you like to filter by? ? or type all for no filter\n')
        if day not in('Monday','Tuesday', 'Wednesday','Thursday','Friday','Saturday','Sunday','all'):
                    print('\nPlease make sure to enter correct input')
        else:
            break

    print('-'*40)

    def load_data(city, month, day):
        return df
        """
        Loads data for the specified city and filters by month and day if applicable.

        Args:
            (str) city - name of the city to analyze
            (str) month - name of the month to filter by, or "all" to apply no month filter
            (str) day - name of the day of week to filter by, or "all" to apply no day filter
        Returns:
            df - Pandas DataFrame containing city data filtered by month and day
        """

    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day'] = df['Start Time'].dt.weekday_name
    if month != 'all':
        months = ['January', 'February', 'March', 'April', 'May', 'June']
        month = months.index(month) + 1
        df = df[df['month'] == month]
    if day != 'all':
        df = df[df['day'] == day.title()]
    print(df)

    def time_stats(df):
        """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

        # TO DO: display the most common month
    most_common_month = df['month'].mode()[0]
    print('Most Common Month is: ', most_common_month)
        # TO DO: display the most common day of week
    most_common_day = df['day'].mode()[0]
    print('Most Common day of the week is: ', most_common_day)

        # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    most_common_hour = df['hour'].mode()[0]
    print('Most Common hour is: ', most_common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    def station_stats(df):
        """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

        # TO DO: display most commonly used start station
    most_common_st_station = df['Start Station'].mode()[0]
    print('The Most Commonly used Start Station is: ', most_common_st_station)

        # TO DO: display most commonly used end station
    most_common_end_station = df['End Station'].mode()[0]
    print('The Most Commonly used End Station is: ', most_common_end_station)

        # TO DO: display most frequent combination of start station and end station trip
    df['combination'] = df['Start Station'] + ' to ' + df['End Station']
    most_common_combination = df['combination'].mode()[0]
    print('The Most Frequent Combiantion of start and end Station is: ', most_common_combination)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    def trip_duration_stats(df):
        """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

        # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('Total Travel time is: ', total_travel_time)

        # TO DO: display mean travel time
    average_travel_time = df['Trip Duration'].mean()
    print('Average Travel time is: ', average_travel_time)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    def user_stats(df):
        """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

        # TO DO: Display counts of user types
    user_stats = df['User Type'].value_counts()
    print('Counts of User Type is:\n ',user_stats)
        # TO DO: Display counts of gender
    if 'Gender' in df:
        gender = df['Gender'].value_counts()
        print(gender)
    else:
        print("There is no gender information in this city.")
        # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
        earliest_year = int(df['Birth Year'].min())
        print('Eariest year of birth is :', earliest_year)

        most_common_year = int(df['Birth Year'].mode()[0])
        print('Most Common year of birth is :', most_common_year)

        most_recent_year = int(df['Birth Year'].max())
        print('Most recent year of birth is :', most_recent_year)
    
    else:
        print("There is no birth year information in this city.")
    

    restart = input('\nWould you like to restart? Enter yes or no.\n')
    if restart.lower() == 'yes':
        main()
main()