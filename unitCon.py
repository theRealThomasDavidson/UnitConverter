def convert(unitFrom = None, unitTo = None):
    """
    Basically this is a function that converts well known units in the same dimensions to another well known unit in
    that dimension.
    :param unitFrom: can be a None or str placeholder for testing what is available in the unit converter or the units
    that you convert from
    :param unitTo: can be a none type placeholder or a unit to convert to
    :return: either a string of instructions or the ratio of the unit conversion
    """

    ###############
    #define your units here
    #then add your dimension after the block below
    ##############
    pressure={
        "Pa": 1., "bar": 100000., "at": 98066.5, "atm": 101325., "Torr": 133.322, "pfin": 6894.76
    }
    flowRateVol={
        "Lps": 1., "cubftpmin": 2.11888, "cubmps": 0.001, "galps": 0.264172, "igillphr":25340.4
    }
    flowRateMass={

        "kgps": 1., "lbps": 0.453592, "gphr": (2.77778*10**(-7)),"gpm":(1.66667*10**(-5)), "gps": 0.001, "gpms":1.,
        "kgpms": 1000., "lbphr":12599.8,
    }
    length={
        "m": 1.,"in":.00254
    }


    ###############
    #Add your dimensions here
    ##############
    dimensions={
        "Pressure": pressure, "Volumetric Flow Rate":flowRateVol,"Mass Flow Rate": flowRateMass, "Length":length
    }

    #TODO: handle dimensional analysis

    #TODO: handle prefixes for metric




    return "Dimension type not available or are not printed right. Try using convert([name of dimension type]) " \
           "to find the names of available units."

def parseUnit(toParse):
    """
    this function should give me a unit in its most basic form
    :param toParse:
    :return: a tuple of the form (list, dbl) where the first a list of units and the ops that are preformed on them in it's base state, and the second is the mutiplier for that unit.
    """
    retList=[]
    scale=1
    prefix = {
        "Y": float(10 ** (24)), "Z": float(10 ** (21)), "E": float(10 ** (18)), "P": float(10 ** (15)),
        "T": float(10 ** (12)),
        "G": float(10 ** (9)), "M": float(10 ** (6)), "k": float(10 ** (3)), "h": float(10 ** (2)),
        "da": float(10 ** (1)),
        "d": float(10 ** (-1)), "c": float(10 ** (-2)), "m": float(10 ** (-3)), "u": float(10 ** (-6)),
        "n": float(10 ** (-9)),
        "p": float(10 ** (-12)), "f": float(10 ** (-15)), "a": float(10 ** (-18)), "z": float(10 ** (-21)),
        "y": float(10 ** (-24)),
    }
    functs = {
        "/": "div", "*": "mul", "^": "exp"
    }


    lookForPref = 42
    unit = ""

    for char in toParse:
        if len(retList)>0:
            if retList[-1]=="^":
                if char=="-":
                    for ii in range(len(retList)):
                        if retList[-ii] =="/":
                            retList[-ii]="*"
                            break
                        if retList[-ii] =="*":
                            retList[-ii]="/"
                            break
                else:
                    retList[-1]="^"+char
                continue

        if char in prefix and lookForPref:
            if len(retList) > 0:
                for ii in range(len(retList)):
                    if retList[-ii] =="/":
                        scale /=prefix[char]
                    if retList[-ii] =="*":
                        scale *= prefix[char]

            lookForPref=0
            if len(unit)!=0:
                retList.append(unit)
                unit=""
        elif char in functs:
            #print char, functs[char]
            lookForPref=42
            if len(unit)!=0:
                retList.append(unit)
                unit=""

            retList.append(char)
        else:
            unit=unit+char
            #print unit
    if len(unit) != 0:
        retList.append(unit)
        unit = ""
    return (retList, scale)

print parseUnit("nm*uin^2/Ys")