#!/usr/bin/python
import sys
import pandas as pd

if __name__ == "__main__":
    file_to_open = sys.argv[1]  # 0 is the index of name of python prog, 1 is the index of first argument in command line.
    data = pd.read_csv(file_to_open, sep=',')
    print(data.head(3))
    for arg in sys.argv[2:]:
        print(arg)
        arr = arg.split(':')
        data.rename(columns={arr[0]: arr[1]}, inplace=True)
        print(data.columns)
    renamed_standard_columns = data.to_csv('standard_columns_EOD-HD.csv', index=False)



