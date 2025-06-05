def circuit_resistance(*data, connection='serial', conductivity=False):
    if connection == 'serial':
        total = sum(data)
    elif connection == 'parallel':
        if any(r == 0 for r in data):
            return 0.0
        total = 1 / sum(1 / r for r in data)
    else:
        raise ValueError("Invalid connection type. Use 'serial' or 'parallel'.")

    if conductivity:
        total = 1 / total if total != 0 else float('inf')

    return round(total, 4)