import math

class Money():

    def value(value, decimals, method):  #Arredondamento 10.787 -> 10.79 / 10.784 -> 10.78
        if(method == 'round'):
            return round(value, decimals)
        elif(method == 'truncation'):  #Truncamento 10.787 -> 10.78
            multiplier = pow(10, decimals)
            value_int = int(value * multiplier)
            return float(value_int/multiplier)
        else:
            print("Method não encontrado!")
            return False