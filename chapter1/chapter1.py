import numpy
import pandas
import statsmodels.api as sm

def complex_heuristic(file_path):
    '''
    Here's the algorithm, predict the passenger survived if:
    1) If the passenger is female or
    2) if his/her socioeconomic status is high AND if the passenger is under 18
    
    Write your prediction back into the "predictions" dictionary. The
    key of the dictionary should be the Passenger's id (which can be accessed
    via passenger["PassengerId"]) and the associated value should be 1 if the
    passenger survived or 0 otherwise. 
    '''

    predictions = {}
    df = pandas.read_csv(file_path)
    for passenger_index, passenger in df.iterrows():
        passenger_id = passenger['PassengerId']

        if passenger['Sex'] == 'female' or \
            (passenger['Pclass'] == 1 and passenger['Age'] < 18):
            predictions[passenger_id] = 1
        else:
            predictions[passenger_id] = 0

    return predictions


print complex_heuristic('titanic_data.csv')

