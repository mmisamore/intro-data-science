import pandas
import pandasql


def num_rainy_days(filename):
    '''
    The SQL query should return one column and
    one row - a count of the number of days in the dataframe where
    the rain column is equal to 1 (i.e., the number of days it
    rained).
    https://dev.mysql.com/doc/refman/5.1/en/counting-rows.html

    cast(column as integer)
    
    You can see the weather data that we are passing in below:
    https://www.dropbox.com/s/7sf0yqc9ykpq3w8/weather_underground.csv
    '''
    weather_data = pandas.read_csv(filename)

    q = """
    select count(1) 
    from weather_data
    where rain = 1
    """
    
    #Execute your SQL command against the pandas frame
    rainy_days = pandasql.sqldf(q.lower(), locals())
    return rainy_days

print num_rainy_days('weather_underground.csv')

