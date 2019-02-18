So this program started out as a dictionary based unit converter that I wanted to use to allow for converting between flow rates.
I started going to a full dimensional analysis type of system with this unit conversions at the end.
In the read in/parse I want to break metric units down to their base units and their prefixes.
(prefixes are in ascii, so instead of mu for micro, I used "u". other than this the prefixes are as normally described (case sensitive))

When reading in values we only use the functions multiply, divide, and exponential.
They are described in the input as "*", "/", and "^". respectivly.

 

# UnitConverter
a good base way to cover various unit conversions 
