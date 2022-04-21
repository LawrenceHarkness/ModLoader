#importing plugins
import random
import pandas as pd
import numpy as np
import fstrings

#importing the lists and getting the length

names = pd.read_csv('list.txt', header=0)
Nlength = len(names)

countries = pd.read_csv('Countrylists.txt', header=0)
Clength = len(countries)

jobs = pd.read_csv('jobslist.txt', header=0)
Jlength = len(jobs)

sirNames = pd.read_csv('sirlist.txt', header=0)
Slength = len(sirNames)


# getting the list value of the persons atrbuites
Name = random.randint(0,Nlength)
country = random.randint(0,Clength)
job = random.randint(0,Jlength)
sirname = random.randint(0,Slength)
print(jobs)
print(jobs[3])




print(F'names: {Nlength}, Countries: {Clength}, Jobs: {Jlength}, sirnames: {Slength}')





