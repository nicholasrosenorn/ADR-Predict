import math

import pandas as pd
import numpy as np


# function that looks at all columns and checks if they have one value assigned to it.
# drops all such columns


class PreProcess:
    def __init__(self, data):
        self.data = data

    def drop_features(self):
        constant_cols = []
        for col in self.data.columns:
            if len(self.data[col].unique()) <= 1:
                #print(col, self.data[col].unique())
                constant_cols.append(col)

        self.data.drop(labels=constant_cols, axis=1, inplace=True)

        # drop columns:
        drop_cols = ['primaryid', 'caseid_x', 'caseid_y', 'event_dt', 'event_dt_num', 'init_fda_dt', 'init_fda_dt_num',
                     'fda_dt', 'fda_dt_num', 'age_cod', 'rept_dt', 'occp_cod_num', 'val_vbm', 'dose_vbm', 'exp_dt',
                     'nda_num', 'dsg_drug_seq', 'start_dt', 'start_dt_num', 'end_dt', 'end_dt_num',
                     'dur', 'dur_cod', 'caseid_x.1', 'caseid_x.2','caseid_y.1', 'caseid_y.2', 'indi_drug_seq',
                     'dose_amt', 'dose_unit']
        self.data.drop(labels=drop_cols, axis=1, inplace=True)

    # function to preprocess age and weight
    # also do gender here
    def bin_features(self):
        # age
        ages = [-1,0,10,20,30,40,50,60,70,80,90,100,200]
        self.data['age'] = pd.cut(x=self.data['age'], bins=ages)

        # weight
        self.data.loc[self.data['wt_cod'].eq('LBS'), 'wt'] *= 0.45359237
        max_weight = max(self.data['wt'])
        bin_size = max_weight / 10
        index = bin_size
        weights = [-1, 0]

        while index < max(self.data['wt']):
            weights.append(index)
            index += bin_size

        weights[-1] += 1
        self.data['wt'] = pd.cut(x=self.data['wt'], bins=weights)
        self.data.drop(labels=['wt_cod'], axis=1, inplace=True)

        self.data['sex'] = self.data['sex'].map(dict(zip(['F', 'M'], [0, 1])))


    # function that encodes all the remaining necessary features
    def encode_features(self):
        features = ['occp_cod', 'reporter_country', 'role_cod', 'drugname', 'prod_ai', 'route', 'dechal', 'rechal',
                    'lot_num', 'dose_form', 'dose_freq', 'pt', 'outc_cod', 'rpsr_cod', 'indi_pt']

        for column in features:
            self.data[column] = self.data[column].str.lower()

        print('Before Encoding')
        encoded_data = pd.get_dummies(data=self.data, columns=features, drop_first=True, dtype=int, prefix=features)
        #encoded_data.to_csv('./data/encoded_data.csv')
        pp.data = pd.concat([pp.data, encoded_data], axis=1)
        pp.data.drop(labels=features, axis=1, inplace=True)






if __name__ == '__main__':
    # Main function
    #data = pd.read_csv('../data/merged.csv') # if running in preprocessing/ dir
    data = pd.read_csv('./data/merged.csv') # if running in ADR-Predict/ dir

    pp = PreProcess(data=data)

    pp.drop_features()
    #pp.data.fillna(value=int(-1), inplace=True)

    pp.bin_features()

    #pp.data.to_csv('./data/binned_data.csv', index=False)
    pp.encode_features()

    #pp.data.fillna(value=int(-1), inplace=True)

    pp.data.to_csv('./data/preprocessed_data.csv', index=False)  # from ADR-Predict/ dir


    # commented out for now
    #pd.to_csv('../data/dropped_col.csv')

