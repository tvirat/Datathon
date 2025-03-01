import pandas as pd
import csv

subway_data = pd.read_csv('subway-data.csv')
subway_data_list = subway_data.values.tolist()
subway_delay_codes = pd.read_csv('subway-delay-codes.csv')
subway_delay_codes_list = subway_delay_codes.values.tolist()

delay_code_dict = {}

class generate_delay_code_dict:
    """Create a dictionary of delay codes from subway-delay-codes.csv. 
    Key is the SUB RMENU CODE and Value is CODE DESCRIPTION.
    """

    for i in range(len(subway_delay_codes_list)):
        key = subway_delay_codes_list[i][1].strip()
        value = subway_delay_codes_list[i][2].strip()
        delay_code_dict[key] = value


def read_delay_code(code: str) -> str:
    """
    Return the value of corresponding key from delay_code_dict where key is code.
    """
    return delay_code_dict[code]


def add_delay_code_description():
    """Modify subway_data by adding new 'Code Description' column 
    corresponding to the 'Code'. If 'Code' is not defined in delay_code_dict
    the 'Code' itself will be returned.
    """
    
    subway_data['Code Description'] = subway_data['Code'].map(lambda x: delay_code_dict.get(x, x))    
    
    subway_data.to_csv('subway-data-code-described.csv', index=True)
    
    return subway_data