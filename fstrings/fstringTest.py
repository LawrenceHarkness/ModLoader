#importing plugins
import random
import pandas as pd
import numpy as np
import fstrings

#importing the lists and getting the length

names = pd.read_csv('list.csv', header=0)
Nlength = len(names)

countries = pd.read_csv('Countrylists.csv', header=0)
Clength = len(countries)

jobs = pd.read_csv('jobslist.csv', header=0)
Jlength = len(jobs)

sirNames = pd.read_csv('sirlist.csv', header=0)
Slength = len(sirNames)

# getting the list value of the persons atrbuites
Name = names.loc[random.randint(0,Nlength),'names']
job = jobs.loc[random.randint(0,Jlength),'jobs']
country = countries.loc[random.randint(0,Clength),'countries']
Sirname = sirNames.loc[random.randint(0,Slength),'sirNames']

print(f'{Name}{Sirname} works as {job} and lives in {country}   ')
