#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    for element in set_1:
        for item in set_2:
            if element != item:
                return element