
from pysize import registry


def category(unit):
    for name, cat in registry.base.items():
        units = cat['units']
        unit_query = units.get(unit, None)
        if unit_query:
            return cat
    raise ValueError('Defined unit does not match anything in the registry')


def conversion(unit):
    cat = category(unit)
    valid_dict = cat['units']
    return valid_dict[unit]


def base(unit):
    cat = category(unit)
    return cat['base']


def options(unit):
    cat = category(unit)
    units = cat['units']
    return sorted([key for key, value in units.items()])


class Base:

    def __init__(self, value, frm_unit):
        self.value = value
        self.frm_unit = frm_unit
        self.registry = registry.base

    def to(self, unit):
        con = 1.0
        num, den = parse(unit)
        for n in num:
            con *= conversion(n)
        for d in den:
            con /= conversion(d)
        return self.value / con  # convert to new unit

    def options(self):
        return options(self.frm_unit)


class Unconverted:

    def __init__(self, value):
        self.value = value
        self.registry = registry.base

    def frm(self, unit):
        con = 1.0
        num, den = parse(unit)
        for n in num:
            con *= conversion(n)
        for d in den:
            con /= conversion(d)
        val = Base(self.value * con, unit)  # convert to base unit
        return val


def parse(unit):
    if '/' in unit:
        split = unit.split('/', maxsplit=1)
        num, den = split[0], split[1]
    else:
        num, den = unit, None
    num_split = num.split('-')
    den_split = den.split('-') if den else []
    for i in [num_split, den_split]:
        for j in i:
            if '^' in j:
                split = j.split('^', maxsplit=1)
                bas, exp = split[0], split[1]
                index = i.index(j)
                i[index:index + 1] = [bas] * int(exp)
    return num_split, den_split


def convert(value):
    con = Unconverted(value)
    return con
