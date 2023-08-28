#!/usr/bin/python3
def magic_calculation(a, b):
    outcome = 0
    for idx in range(1, 3):
        try:
            if idx > a:
                raise Exception('Too far')
            else:
                outcome += (a ** b) / idx
        except Exception:
            outcome = b + a
            break
    return (outcome)
