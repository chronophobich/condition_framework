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

print(df)

