import pandas as pd
import numpy as np


# function that looks at all columns and checks if they have one value assigned to it.
# drops all such columns
def drop_cols(data):
    empty_cols = []
    for col in data.columns:
        if len(data[col].unique()) <= 1:
            #print(col, data[col].unique())
            empty_cols.append(col)

    data.drop(labels=empty_cols, axis=1, inplace=True)

    return data





if __name__ == '__main__':
    # Main function
    data = pd.read_csv('../data/merged.csv')
    dropped_col_data = drop_cols(data=data)

    # commented out for now
    #pd.to_csv('../data/dropped_col.csv')

