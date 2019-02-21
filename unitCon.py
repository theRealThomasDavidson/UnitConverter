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
        ("unit * L","unit / s"): 1., "cubftpmin": 2.11888, "cubmps": 0.001, "galps": 0.264172, "igillphr":25340.4
    }
    flowRateMass={

        "kgps": 1., "lbps": 0.453592, "gphr": (2.77778*10**(-7)),"gpm":(1.66667*10**(-5)), "gps": 0.001, "gpms":1.,
        "kgpms": 1000., "lbphr":12599.8,
    }
    length={"base":"unit * m",
        "unit * m": 1./.00254,"unit * in":1.,"unit * ft":12.,"unit * yd":36.,"unit * mile":12.*5280.,"unit * ly":372469703644913410.,
        "unit * au": 149597870700. / .00254
    }
    mass={"base":"unit * g",
        "unit * g": 1.
    }
    time={"base":"unit * s",
        "unit * s": 1.,"unit * min":60., "unit * hr":360.
    }
    elecCurr={"base":"unit * A",
        "unit * A": 1.
    }
    temperature={"base":"unit * K",
        "unit * K": 1.
    }
    luminous={"base":"unit * cd",
        "unit * cd": 1.
    }
    mol={"base":"unit * mol",
        "unit * mole": 1.
    }


    ###############
    #Add your dimensions here
    ##############
    dimensions={
        "Pressure": pressure, "Volumetric Flow Rate":flowRateVol}#,"Mass Flow Rate": flowRateMass, "Length":length}

    baseUnits={"length":length, "mass":mass, "time":time, "Current":elecCurr, "temperature":temperature,
               "intensity":luminous, "mole":mol }
    #TODO: test how units in lists are handled.
    for units in baseUnits:
        for item in baseUnits[units]:
            if item!="base":
                #print("this is the item",item[6:],units).
                #print(item)
                #print(parseUnit(item[7:])[0][0])

                if parseUnit(item[7:])[0][0]!= item:
                    print item,parseUnit(item[7:])[0][0],"\n"

    uListFrom,scaleFrom=parseUnit(unitFrom)
    #uListTo=parseUnit(unitTo)

    uListFrom= tuple(uListFrom)


    """
    for dimension in baseUnits:
        print(uListFrom)
        if uListFrom in dimensions[dimension]:
            print("hello")
    """


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
        "/": "div", "*": "mul", "^": "exp"}


    lookForPref = 42
    unit = ""
    functPlace="*"
    expBool=0
    for char in toParse:

        holdLength = len(retList)
        if holdLength > 0:
            if expBool:
                if char=="-":
                    for ii in range(holdLength):
                        if functPlace =="/":
                            functPlace="*"
                            break
                        if functPlace =="*":
                            functPlace="/"
                            break
                    retList[-1]=retList[-1][:5]+functPlace+retList[-1][6:]
                    if holdLength>1:
                        if retList[-2][:4]=="pfix":
                            retList[-2] = retList[-2][:5] + functPlace + retList[-2][6:]
                else:
                    repeatList=[]
                    number=int(char)
                    repeatList.append(retList[-1])
                    if holdLength>1:
                        if retList[-2][:4] == "pfix":
                            repeatList.append(retList[-2][:5] + functPlace + retList[-2][6:])
                    for ii in range (1,number):
                        for item in repeatList:
                            retList.append(item)
                    lookForPref=42
                    expBool=0
                continue


        if char in prefix and lookForPref:

            retList.append("pfix "+ functPlace +" "+char)
            lookForPref=0
            if len(unit)!=0:
                retList.append("unit "+ functPlace +" "+unit)
                unit=""
        elif char in functs:
            #print char, functs[char]
            lookForPref=42
            if len(unit)!=0:
                retList.append("unit "+ functPlace +" "+unit)
                unit=""
            if retList[-1][:4]=="pfix":
                temp="unit "+retList[-1][4:]
                del retList[-1]
                retList.append(temp)
            if char != "^":
                functPlace=char
            else:
                expBool=42
        elif not expBool:
            lookForPref=0
            unit=unit+char
            #print unit
    if len(unit) != 0:
        retList.append("unit "+functPlace+" "+unit)
        unit = ""
    if retList[-1][:4] == "pfix":
        temp = "unit " + retList[-1][5:]
        del retList[-1]
        retList.append(temp)
    #by here the list is handled well but we need to
    retList=sorted(retList)
    for possPfix in retList:
        if possPfix[:4]=="pfix":
            exp = 1
            if possPfix[5] =="/":
                exp=-1
            scale*=prefix[possPfix[7]]**exp
    retList=filter(lambda x: x[:4] != "pfix", retList)
    return (retList, scale)





def main():
    string = "dL/s"
    #print(parseUnit("m^-1*thisisaunits*alsoaunit/notreqprefix/in^4"))
    print convert(string)

def testForprefixbreaks()
if __name__=="__main__":
    main()



#print sorted( parseUnit(string)[0]), string

"""
testString="false: 0, true: 1"

print(bool(int(testString[7])))
"""
"""
       if char in prefix and lookForPref:
            if len(retList) > 0:
                for ii in range(len(retList)):
                    if retList[-ii] =="/":
                        scale /=prefix[char]
                    if retList[-ii] =="*":
                        scale *= prefix[char]"""