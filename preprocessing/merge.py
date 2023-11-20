import sys

import pandas as pd
import numpy as np
from functools import reduce
import warnings
warnings.filterwarnings('ignore')

# run function from ADR-predict directory

def merge_data():
    periods = ['2022q1', '2022q2', '2022q3', '2022q4', '2023q1', '2023q2', '2023q3']
    periods = periods[::-1]

    for period in periods:
        demo = pd.read_csv("unprocessed_data/demo{0}.csv".format(period), dtype={'to_mfr': str})
        to_drop = ["i_f_code", "i_f_code_num", "rept_cod", "rept_cod_num", "auth_num", "mfr_num", "e_sub", "rept_dt_num",
                   "to_mfr", 'caseid', 'event_dt', 'event_dt_num', 'init_fda_dt', 'init_fda_dt_num',
                   'fda_dt', 'fda_dt_num']
        demo_dropped = demo.drop(labels=to_drop, axis=1)
        del demo

        case_id = ['caseid']
        drug_info = pd.read_csv("unprocessed_data/drug{0}.csv".format(period))
        drug_info = drug_info.drop(labels=case_id, axis=1)
        #dataframes = [demo_dropped, drug_info]
        #df_merged = reduce(lambda left, right: pd.merge(left, right, on=['primaryid'], how='outer'), dataframes)
        #print('merge 1', sys.getsizeof(df_merged), sys.getsizeof(drug_info), sys.getsizeof(demo_dropped))
        #del drug_info
        #del demo_dropped
        #print('merge 1', sys.getsizeof(df_merged))
        reac_info = pd.read_csv("unprocessed_data/reac{0}.csv".format(period))
        reac_info = reac_info.drop(labels=case_id, axis=1)
        #dataframes = [df_merged, reac_info]
        #df_merged = reduce(lambda left, right: pd.merge(left, right, on=['primaryid'], how='outer'), dataframes)
        #del reac_info
        #print('merge 2', sys.getsizeof(df_merged))
        outcome = pd.read_csv("unprocessed_data/outc{0}.csv".format(period))
        outcome = outcome.drop(labels=case_id, axis=1)
        #dataframes = [df_merged, outcome]
        #df_merged = reduce(lambda left, right: pd.merge(left, right, on=['primaryid'], how='outer'), dataframes)
        #del outcome
        #print('merge 3', sys.getsizeof(df_merged))

        response_source = pd.read_csv("unprocessed_data/rpsr{0}.csv".format(period))
        response_source = response_source.drop(labels=case_id, axis=1)
        #dataframes = [df_merged, response_source]
        #df_merged = reduce(lambda left, right: pd.merge(left, right, on=['primaryid'], how='outer'), dataframes)
        #del response_source
        #print('merge 4')

        therapy = pd.read_csv("unprocessed_data/ther{0}.csv".format(period))
        therapy = therapy.drop(labels=case_id, axis=1)
        #dataframes = [df_merged, therapy]
        #df_merged = reduce(lambda left, right: pd.merge(left, right, on=['primaryid'], how='outer'), dataframes)
        #del therapy
        #print('merge 5')
        med_dra = pd.read_csv("unprocessed_data/indi{0}.csv".format(period))
        med_dra = med_dra.drop(labels=case_id, axis=1)
        #dataframes = [df_merged, med_dra]
        #df_merged = reduce(lambda left, right: pd.merge(left, right, on=['primaryid'], how='outer'), dataframes)
        #del med_dra
        #print('merge 6')

        #dataframes = pd.concat([demo_dropped, drug_info, reac_info, outcome, response_source, therapy, med_dra], axis=1)

        dataframes = [demo_dropped, drug_info, reac_info, outcome, response_source, therapy, med_dra]

        df_merged = reduce(lambda left, right: pd.merge(left, right, on=['primaryid'], how='outer'), dataframes)
        for i in range(len(dataframes)):
            del dataframes[i]
        del dataframes
        print(period, ": ", df_merged.shape)

        df_merged.to_csv("./data/all_merged.csv", mode='a', index=False)
        del df_merged



merge_data()
