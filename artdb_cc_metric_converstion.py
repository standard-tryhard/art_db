import math



def round_half_up(n, decimals=0):
    multiplier = 10 ** decimals
    return math.floor(n*multiplier + 0.5) / multiplier


def convert_in_to_cm(_numb):
    _numb_as_cm = _numb * 2.54
    _res = round_half_up(_numb_as_cm)
    return(_res)

def convert_cm_to_in(_numb):
    _numb_as_cm = _numb / 2.54
    _res = round_half_up(_numb_as_cm)
    return(_res)


