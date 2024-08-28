# Function to Parse the variables in individual condition
def parse_variables(sub_condition,):
    operators = [">=", "<=", "=>", "=<", ">", "<", "="]
    for op in operators:
        if op in sub_condition:
            lhs = sub_condition.split(op)[0].strip()
            rhs = sub_condition.split(op)[1].strip()
            return lhs, rhs
