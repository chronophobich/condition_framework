import pandas as pd

from config.conditions_list import conditions_list
from config.default_values import default_values
from core.generator import generate_row
from core.sorter import sort_sub_conditions

# Parse and sort the conditions

sorted_conditions_list = [sort_sub_conditions(condition, default_values) for condition in conditions_list]

# Generate the data
data = [generate_row(condition, default_values) for condition in sorted_conditions_list]

# Create the DataFrame
df = pd.DataFrame(data)

df['aid'] = '111111111111111'
df['cid'] = '222222222222'
df['asid'] = '3333333333333'
df['VIDEO_STARTED'] = df['VIDEO_STARTED'].astype(bool)
df['VIDEO_MRC_VIEWED'] = df['VIDEO_MRC_VIEWED'].astype(bool)

custom_index = []
for i, row in df.iterrows():
    base_index = f'QAimpression{str(i+1).zfill(3)}'
    if row['it'] == 1:
        custom_index.append(f'{base_index}display')
    elif row['it'] == 2:
        custom_index.append(f'{base_index}video')
    else:
        custom_index.append(base_index)

df.index = custom_index


excel_path = 'conditions_output.xlsx'  
df.to_excel(excel_path, index=True)
print(df)
