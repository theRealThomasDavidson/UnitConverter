def convert(unitFrom = None, unitTo = None, density=1):
    pressure={
        "Pa":1., "bar": 100000., "at": 98066.5, "atm": 101325., "Torr": 133.322, "pfin": 6894.76
    }

    dimensions={"pressure": pressure, "test1":{}, "dimen": {}}
    for dim in dimensions:
        if unitFrom in dimensions[dim] and unitTo in dimensions[dim]:
            return dimensions[dim][unitTo]/dimensions[dim][unitFrom]
    if unitFrom == None:
        string="These are the available dimension types: "
        for key in dimensions:
            string= string + key+", "

        return string[:-2]+"."
    if unitFrom in dimensions:
        string="These are the available unit types: "
        for key in dimensions[unitFrom]:
            string= string + key+", "

        return string[:-2]+"."
    return "Dimension type not available or are not printed right. try using convert([name of dimension type]) to find the names of available units."
print convert("pressure")