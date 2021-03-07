import pandas as pd

def get_csv():
    file = open("../owid_covid_data.csv", "r")
    return file

def transform_csv(file):
    df = pd.read_csv(file)
    return df

def series_handler(dataframe):
    data_dict = dataframe.to_dict()
    index = list(data_dict['location'].keys())[0]

    data_dict['location'] = data_dict['location'][index]
    data_dict['continent'] = data_dict['continent'][index]

    for key, value in data_dict.items():
        if key == 'location' or key == 'continent':
            continue
        data_dict[key] = {str(key):value for key, value in value.items()}

    return data_dict