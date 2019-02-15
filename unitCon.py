def convert(unitFrom = None, unitTo = None):
    """
    Basically this is a function that converts well known units in the same dimensions to another well known unit in
    that dimension.
    :param unitFrom: can be a None or str placeholder for testing what is available in the unit converter or the units
    that you convert from
    :param unitTo: can be a none type placeholder or a unit to convert to
    :return: either a string of instructions or the ratio of the unit conversion
    """
    pressure={
        "Pa":1., "bar": 100000., "at": 98066.5, "atm": 101325., "Torr": 133.322, "pfin": 6894.76
    }
    flowRateVol={"Lps": 1., "cubftpmin": 2.11888, "cubmps": 0.001, "galps": 0.264172, "igillphr":25340.4

    }

    dimensions={
        "pressure": pressure, "Volumetric Flow Rate":flowRateVol,
    }
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
    return "Dimension type not available or are not printed right. Try using convert([name of dimension type]) " \
           "to find the names of available units."
