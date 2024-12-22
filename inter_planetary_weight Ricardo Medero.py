#Inter Planetary Weights
#Author: Ricardo Medero
#Date 02-07-2024 updated 02-21-2024

#Contants
nSURFACE_MERCURY = 0.38
nSURFACE_VENUS = 0.91
nSURFACE_MOON = 0.165
nSURFACE_MARS = 0.38
nSURFACE_JUPITER = 2.34
nSURFACE_SATURN = 0.93
nSURFACE_URANUS = 0.92
nSURFACE_NEPTUNE = 1.12
nSURFACE_PLUTO = 0.066

#Variable input

print("Welcome to Inter Planetary Weights:")

sname = input("What is your name?: ")

fEarthWeight = float(input("What is yor weight?: "))

#Logic.

fWeightMercury = fEarthWeight * nSURFACE_MERCURY
fWeightVenus = fEarthWeight * nSURFACE_VENUS
fWeightMoon = fEarthWeight * nSURFACE_MOON
fWeightMars = fEarthWeight * nSURFACE_MARS
fWeightJupiter = fEarthWeight * nSURFACE_JUPITER
fWeightSaturn = fEarthWeight * nSURFACE_SATURN
fWeightUranus = fEarthWeight * nSURFACE_URANUS
fWeightNeptune = fEarthWeight * nSURFACE_NEPTUNE
fWeightPluto = fEarthWeight * nSURFACE_PLUTO


#Result Output/print.

print(f"{'Weight on Mercury:':25}  {fWeightMercury:.2f}")
print(f"{'Weight on Venus:':25} {fWeightVenus:.2f}")
print(f"{'Weight on Moon:':25}  {fWeightMoon:.2f}")
print(f"{'Weight on Mars:':25}  {fWeightMars:.2f}")
print(f"{'Weight on Jupiter:':25} {fWeightJupiter:.2f}")
print(f"{'Weight on Saturn:':25} {fWeightSaturn:.2f}")
print(f"{'Weight on Uranus:':25} {fWeightUranus:.2f}")
print(f"{'Weight on Neptune:':25} {fWeightNeptune:.2f}")
print(f"{'Weight on Pluto:':25}  {fWeightPluto:.2f}")




