# Function to Generate the row data
import re
from core.evaluator import evaluate_expression

def evaluate_condition(condition, row):

    try:
        return eval(condition, {}, row)
    except Exception as e:
        print(f"Evaluation error for condition '{condition}': {e}")
        return False


def generate_row(condition, default_values):
    row = default_values.copy()
    
    condition = condition.replace("AND", "and").replace("OR", "or").replace("TRUE", "True").replace("FALSE", "False")
    condition = condition.replace("THEN", "then").replace("=>", ">=").replace("=<", "<=")
    condition = condition.replace('(', "").replace(')', "")

    if "then" in condition:
        condition_part, action_part = condition.split("then")
        condition_part = condition_part.strip()
        action_part = action_part.strip()

        
        if all(evaluate_condition(cond.strip(), row) for cond in condition_part.split(" and ")):
            
            if "=" in action_part:
                lhs, rhs = action_part.split("=")
                lhs, rhs = lhs.strip(), rhs.strip()
                if rhs.isdigit():
                    row[lhs] = int(rhs)
            elif "<" in action_part and "=" not in action_part:
                lhs, rhs = action_part.split("<")
                lhs, rhs = lhs.strip(), rhs.strip()
                if rhs.isdigit():
                    row[lhs] = min(row.get(lhs, 0), int(rhs) - 1)
        return row

    
    for cond in condition.split(" and "):
        cond = cond.strip()
        cond = re.sub(r'\s+', ' ', cond).strip()
        print(cond)

        if ">=" in cond:
            lhs, rhs = cond.split(">=")
            lhs, rhs = lhs.strip(), rhs.strip()
            if rhs.isdigit():
                row[lhs] = max(row[lhs], int(rhs))
            elif rhs in row:
                if row[lhs] < row[rhs]:
                    row[lhs] = row[rhs]
            else:
                rhs_value = evaluate_expression(rhs, row)
                if rhs_value is not None:
                    row[lhs] = max(row[lhs], rhs_value)

        elif "<=" in cond:
            lhs, rhs = cond.split("<=")
            lhs, rhs = lhs.strip(), rhs.strip()
            if rhs.isdigit():
                row[lhs] = min(row[lhs], int(rhs))
            elif rhs in row:
                if row[lhs] > row[rhs]:
                    row[lhs] = row[rhs]
            else:
                rhs_value = evaluate_expression(rhs, row)
                if rhs_value is not None:
                    row[lhs] = min(row[lhs], rhs_value)

        elif ">" in cond and ">=" not in cond:
            lhs, rhs = cond.split(">")
            lhs, rhs = lhs.strip(), rhs.strip()
            if rhs.isdigit():
                row[lhs] = int(rhs) + 1
            else:
                rhs_value = evaluate_expression(rhs, row)
                if rhs_value is not None and row[lhs] <= rhs_value:
                    row[lhs] = rhs_value + 1

        elif "<" in cond and "<=" not in cond:
            lhs, rhs = cond.split("<")
            lhs, rhs = lhs.strip(), rhs.strip()
            if rhs.isdigit():
                row[lhs] = int(rhs) - 1
            else:
                rhs_value = evaluate_expression(rhs, row)
                if rhs_value is not None and row[lhs] >= rhs_value:
                    row[lhs] = rhs_value - 1

        elif "==" in cond:
            lhs, rhs = cond.split("==")
            lhs, rhs = lhs.strip(), rhs.strip()
            if rhs.isdigit():
                row[lhs] = int(rhs)
            else:
                rhs_value = evaluate_expression(rhs, row)
                if rhs_value is not None:
                    row[lhs] = rhs_value

        elif "=" in cond and "==" not in cond:
            lhs, rhs = cond.split("=")
            lhs, rhs = lhs.strip(), rhs.strip()
            if rhs.isdigit():
                row[lhs] = int(rhs)
            else:
                rhs_value = evaluate_expression(rhs, row)
                if rhs_value is not None:
                    row[lhs] = rhs_value

    return row
