def sort_tuples(tuples_list):
    return sorted(tuples_list, key=lambda x: (x[2], x[1], len(x[0]), -x[1]))