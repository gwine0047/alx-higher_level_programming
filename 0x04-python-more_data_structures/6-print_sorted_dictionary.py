def print_sorted_dictionary(a_dictionary):
    keys = a_dictionary.keys()
    for key in sorted(keys):
        print("{}: {}".format(key, a_dictionary[key]))
