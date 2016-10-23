
# from pysize import unit


# meter = Unit()     # distance
# gram = Unit()      # mass
# second = Unit()    # time
# amphere = Unit()   # electric current
# kelvin = Unit()    # kelvin
# mole = Unit()      # amount of substance
# candela = Unit()   # intensity of light


base = {
    'distance': {
        'base': 'm',
        'units': {
            'km': 1000,
            'm': 1,
            'dm': 1/10,
            'cm': 1/100,
            'mm': 1/1000,
            'mi': 1/3.2808*5280,
            'yd': 1/3.2808*3,
            'ft': 1/3.2808,
            'in': 1/3.2808/12,
        }
    },
    'mass': {
        'base': 'g',
        'units': {
            'kg': 1000,
            'g': 1,
            'mg': 1/1000,
        }
    },
    'second': {
        'base': 's',
        'units': {
            's': 1,
            'min': 60,
            'h': 60*60,
            'd': 60*60*24,
            'week': 60*60*24*7,
            'month': 60*60*24*7*4,
            'year': 60*60*24*7*52,
            'decade': 60*60*24*7*365*10,
            'century': 60*60*24*7*365*100,
            'millennium': 60*60*24*7*365*1000,
        }
    },
}

# def register(key, conv, base):
#     registry[key] = unit(conv, base)
