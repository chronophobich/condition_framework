from .evaluator import evaluate_expression


# Function to Generate the row data
def generate_row(condition, default_values):
    row = default_values.copy()
    for cond in condition.split(" AND "):
        cond = cond.strip()
        cond = cond.replace("=>", ">=").replace("=<", "<=")

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
                if rhs is not None:
                    row[lhs] = max(row[lhs], rhs_value)

        elif "<=" in cond:
            lhs, rhs = cond.split("<=")
            lhs, rhs = lhs.strip(), rhs.strip()
            if rhs.isdigit():
                row[lhs] = row[rhs]
            elif rhs in row:
                if row[lhs] > row[rhs]:
                    row[lhs] = row[rhs]
            else:
                rhs_value = evaluate_expression(rhs, row)
                if rhs is not None:
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