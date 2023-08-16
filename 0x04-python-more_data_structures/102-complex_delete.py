#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    del_keys = []
    for keys in a_dictionary:
        if a_dictionary[keys] == value:
            del_keys.append(keys)
        for key in del_keys:
            del a_dictionary[key]
        return a_dictionary