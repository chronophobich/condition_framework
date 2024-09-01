import re
import pandas as pd
# Default values
default_values = {
    'vm': 1,
    'it': 2,
    # 'aid': 111111111111111,
    # 'cid': 222222222222,
    # 'asid': 3333333333333,
    'vcp': 0,
    'sivt': 0,
    'givt': 0,
    'fco': 2000,
    'MRC_Viewed': True,
    'VIDEO_STARTED': True,
    'VIDEO_MRC_VIEWED': True,
    'q1': 0,
    'q2': 0,
    'q3': 0,
    'q4': 0
}

# excel_path = './linkedin_tc.xlsx'
# sheet_name = 'Sheet5'

# df_excel = pd.read_excel(excel_path, sheet_name=sheet_name)


# conditions_list = df_excel['Test Definition'].dropna().tolist()


# def extract_variables(conditions_list):

#     variables = set() 
#     for condition in conditions_list:
        
#         found_vars = re.findall(r'\b[a-zA-Z_]+\d*\b', condition)
#         for var in found_vars:
           
#             if var not in ['and', 'or', 'not', 'then', 'THEN', 'True', 'TRUE', 'false', 'FALSE', 'is_call', 'AND']:
#                 variables.add(var)
#     print(variables)
# extract_variables(conditions_list)
