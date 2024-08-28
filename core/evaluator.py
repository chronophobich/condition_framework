# Function to evaluate expressions
def evaluate_expression(expression, row):
    for var in row:
        try:
            result = eval(expression, {}, row)
            return int(result)
        except Exception as e:
            print(f"Error -> {e}")
            return None
