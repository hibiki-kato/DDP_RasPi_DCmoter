from typing import List
import csv

def read_motor_instructions(filepath: str) -> List[List[float]]:
        """
        Read motor instructions from a CSV file.

        Args:
        - filepath (str): The path to the CSV file.

        Returns:
        - A list of lists containing the motor instructions.
        """
        with open(filepath, 'r') as f:
            reader = csv.reader(f)
            instructions = []
            for row in reader:
                instructions.append([float(x) for x in row])
        return instructions
    

lst = read_motor_instructions("instruction.csv")
print(lst)