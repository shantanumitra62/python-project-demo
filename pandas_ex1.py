import os
import pandas as pd
import numpy as np
import random
import subprocess
import uuid

class Solution:
    def __init__(self, input_file, output_file):
        self.input_file = input_file
        self.output_file = output_file
    size=0   
    # Generating corelation_id
    corelation_id=str(uuid.uuid4())
    print("This is generating the corelation id", corelation_id)
    
    # Generating random numbers
    def generate_random_data(self, num_rows):
        """ Generate a randomo data with numpy and random """
        ids=random.randint(1000,9999,num_rows)
        names=[f'Names{random.randint(1,100)}' for _ in range(num_rows)]
        ages = np.random.randint(18, 90)
        scores = np.random.uniform(0, 100)
    
        data=pd.DataFrame(
            {
                'ID': ids,
                'Name': names,
                'Age': ages,
                'Score': scores
            }
        )
        return data
    def read_file(self,input_file):
        if os.path.exists(self.input_file):
            data=pd.read_csv(self.input_file)
            print("File read successfully!")
            print(data)
            return data
        else:
            print(f"File (self.input_file) does not exist!")
    
    def write_to_file(self, data):
        """ Writing data to a file """
        try:
            data.to_csv(self.output_file, index=False)
            print(f"Data written successfully to file: {self.output_file}.")
        except Exception as e:
            print(f"File was unwritten with Error:{e}")
            
    def process_file(self, num_rows):
        """ Main method to generate data and write to a file """
        random_data=self.generate_random_data(num_rows)
        self.write_to_file(random_data)
        
        data_from_file=self.read_file()
    
if __name__=="__main__":
    input_file="./sampledata.csv"
    output_file="sampledata.csv"
    solution1=Solution(input_file,output_file)
    solution1.process_file(10)
    
            
