import configparser
import os
import random
import numpy as np
import pandas as pd
from windtexter.inputs import parameters

CONFIG = configparser.ConfigParser()
CONFIG.read(os.path.join(os.path.dirname(__file__), 'script_config.ini'))
BASE_PATH = CONFIG['file_locations']['base_path']
DATA = os.path.join(BASE_PATH)

def generate_coordinates(transmitters):
    """
    This function generate 
    coordinates for the transmitter, 
    interceptor and receiver
    Parameters
    ----------
    transmitters : int.
        Number of radio transmitters.
    """

    print('Generating random coordinates for a case of {} transmitters'.format(transmitters))
    df_merge = pd.DataFrame()

    for key, item in parameters.items():

        transmitter_powers = ([random.uniform((item['power_db'] - 5), 
                            (item['power_db'] + 5)) for _ in range(10)])
        
        antenna_gains = ([random.uniform((item['antenna_gain_db'] - 3), 
                        (item['antenna_gain_db'] + 3)) for _ in range(10)])
        
        low_gain = np.percentile(antenna_gains, 25)
        high_gain = np.percentile(antenna_gains, 65)
        
        technologies = item['technologies']
        
        for technology in technologies:

            for trans_power in transmitter_powers:

                for antenna_gain in antenna_gains:

                    if antenna_gain < low_gain:
                        
                        power_scenario = 'low'

                    elif antenna_gain > high_gain:

                        power_scenario = 'high'

                    else:

                        power_scenario = 'baseline'

                    if transmitters == 1:

                        transmitter_number = [1]

                    elif transmitters == 2:

                        transmitter_number = [1, 2]

                    elif transmitters == 3:

                        transmitter_number = [1, 2, 3]

                    elif transmitters == 4:

                        transmitter_number = [1, 2, 3, 4]

                    else:

                        transmitter_number = [1, 2, 3, 4, 5]

                    for tran in transmitter_number:

                        range_number = 50

                        if transmitters == 1:

                            transmitter_x = ([random.uniform(0, item['grid_length']) 
                                            for _ in range(range_number)])
                            transmitter_y = ([random.uniform(0, item['grid_length']) 
                                            for _ in range(range_number)])
                            receiver_x = ([random.uniform(0, (item['grid_length'] + 5)) 
                                        for _ in range(range_number)])
                            receiver_y = ([random.uniform(0, (item['grid_length'] + 5)) 
                                        for _ in range(range_number)])
                            interceptor_x = ([random.uniform(0, item['grid_length']) 
                                            for _ in range(range_number)]) 
                            interceptor_y = ([random.uniform(0, item['grid_length']) 
                                            for _ in range(range_number)])
                            
                        elif transmitters == 5:

                            transmitter_x = ([random.uniform(0, item['grid_length']) 
                                            for _ in range(range_number)])
                            transmitter_y = ([random.uniform(0, item['grid_length']) 
                                            for _ in range(range_number)])
                            receiver_x = ([random.uniform(0, (item['grid_length'] - 8)) 
                                        for _ in range(range_number)])
                            receiver_y = ([random.uniform(0, (item['grid_length'] - 8)) 
                                        for _ in range(range_number)])
                            interceptor_x = ([random.uniform(0, item['grid_length']) 
                                            for _ in range(range_number)]) 
                            interceptor_y = ([random.uniform(0, item['grid_length']) 
                                            for _ in range(range_number)])
                            
                        else:

                            transmitter_x = ([random.uniform(0, item['grid_length']) 
                                            for _ in range(range_number)])
                            transmitter_y = ([random.uniform(0, item['grid_length']) 
                                            for _ in range(range_number)])
                            receiver_x = ([random.uniform(0, (item['grid_length'] - 3)) 
                                        for _ in range(range_number)])
                            receiver_y = ([random.uniform(0, (item['grid_length'] - 3)) 
                                        for _ in range(range_number)])
                            interceptor_x = ([random.uniform(0, item['grid_length']) 
                                            for _ in range(range_number)]) 
                            interceptor_y = ([random.uniform(0, item['grid_length']) 
                                            for _ in range(range_number)])
                            
                        df = pd.DataFrame({'transmitter_x': transmitter_x, 
                                        'transmitter_y': transmitter_y,
                                        'receiver_x': receiver_x,
                                        'receiver_y': receiver_y,
                                        'interceptor_x': interceptor_x,
                                        'interceptor_y': interceptor_y,
                                        'no_transmitters': transmitters,
                                        'transmitter_power_db': trans_power,
                                        'antenna_gain_db': antenna_gain,
                                        'technology': technology,
                                        'power_scenario': power_scenario})
                        df_merge = pd.concat([df_merge, df], ignore_index = True)

    fileout = '{}_transmitters_inputs.csv'.format(transmitters) 
    folder_out = os.path.join(DATA)    
    if not os.path.exists(folder_out):

        os.makedirs(folder_out)

    path_out = os.path.join(folder_out, fileout) 
    df_merge.to_csv(path_out, index = False)


    return None


def secure_text_data(transmitters):

    print('Generating random coordinates for a case of {} transmitters'.format(transmitters) )
    df_merge = pd.DataFrame()
    for key, item in parameters.items():

        transmitter_powers = ([random.uniform((item['power_db'] - 5), 
                            (item['power_db'] + 5)) for _ in range(10)])
        
        antenna_gains = ([random.uniform((item['antenna_gain_db'] - 3), 
                        (item['antenna_gain_db'] + 3)) for _ in range(10)])
        
        low_gain = np.percentile(antenna_gains, 25)
        high_gain = np.percentile(antenna_gains, 65)
        
        technologies = item['technologies']
        applications = item['application_area']

        for application in applications:
   
            for technology in technologies:

                for trans_power in transmitter_powers:

                    for antenna_gain in antenna_gains:

                        if antenna_gain < low_gain:
                            
                            power_scenario = 'low'

                        elif antenna_gain > high_gain:

                            power_scenario = 'high'

                        else:

                            power_scenario = 'baseline'

                        if transmitters == 1:

                            transmitter_number = [1]
                            text_scenario = 'baseline'

                        elif transmitters == 3:

                            transmitter_number = [1, 2, 3]
                            text_scenario = 'partial'

                        else:

                            transmitter_number = [1, 2, 3, 4, 5]
                            text_scenario = 'full'

                        for tran in transmitter_number:

                            range_number = 50

                            if transmitters == 1:

                                transmitter_x = ([random.uniform(0, item['grid_length']) 
                                                for _ in range(range_number)])
                                transmitter_y = ([random.uniform(0, item['grid_length']) 
                                                for _ in range(range_number)])
                                receiver_x = ([random.uniform(0, item['grid_length']) 
                                            for _ in range(range_number)])
                                receiver_y = ([random.uniform(0, item['grid_length']) 
                                            for _ in range(range_number)])
                                interceptor_x = ([random.uniform(0, item['grid_length']) 
                                                for _ in range(range_number)]) 
                                interceptor_y = ([random.uniform(0, item['grid_length']) 
                                                for _ in range(range_number)])
                                
                            elif transmitters == 5:

                                transmitter_x = ([random.uniform(0, item['grid_length']) 
                                                for _ in range(range_number)])
                                transmitter_y = ([random.uniform(0, item['grid_length']) 
                                                for _ in range(range_number)])
                                receiver_x = ([random.uniform(0, (item['grid_length'] - 6)) 
                                            for _ in range(range_number)])
                                receiver_y = ([random.uniform(0, (item['grid_length'] - 6)) 
                                            for _ in range(range_number)])
                                interceptor_x = ([random.uniform(0, item['grid_length']) 
                                                for _ in range(range_number)]) 
                                interceptor_y = ([random.uniform(0, item['grid_length']) 
                                                for _ in range(range_number)])
                                
                            else:

                                transmitter_x = ([random.uniform(0, item['grid_length']) 
                                                for _ in range(range_number)])
                                transmitter_y = ([random.uniform(0, item['grid_length']) 
                                                for _ in range(range_number)])
                                receiver_x = ([random.uniform(0, (item['grid_length'] - 3)) 
                                            for _ in range(range_number)])
                                receiver_y = ([random.uniform(0, (item['grid_length'] - 3)) 
                                            for _ in range(range_number)])
                                interceptor_x = ([random.uniform(0, item['grid_length']) 
                                                for _ in range(range_number)]) 
                                interceptor_y = ([random.uniform(0, item['grid_length']) 
                                                for _ in range(range_number)])
                            df = pd.DataFrame({'transmitter_x': transmitter_x, 
                                            'transmitter_y': transmitter_y,
                                            'receiver_x': receiver_x,
                                            'receiver_y': receiver_y,
                                            'interceptor_x': interceptor_x,
                                            'interceptor_y': interceptor_y,
                                            'no_transmitters': transmitters,
                                            'transmitter_power_db': trans_power,
                                            'antenna_gain_db': antenna_gain,
                                            'technology': technology,
                                            'text_scenario': text_scenario,
                                            'power_scenario': power_scenario,
                                            'application_area': application})
                            df_merge = pd.concat([df_merge, df], ignore_index = True)

    fileout = '{}_secure_data.csv'.format(transmitters) 
    folder_out = os.path.join(DATA)    
    if not os.path.exists(folder_out):

        os.makedirs(folder_out)

    path_out = os.path.join(folder_out, fileout) 
    df_merge.to_csv(path_out, index = False)
        
    return None


if __name__ == "__main__": 

    transmitters = [1, 3, 5]
    for transmitter in transmitters:

        generate_coordinates(transmitter)
        #secure_text_data(transmitter)