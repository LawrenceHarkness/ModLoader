import os
import shutil

mod16 = r"C:\Users\lawre\Documents\GitHub\ModLoader\mods\1.16"
mod18 = r"C:\Users\lawre\Documents\GitHub\ModLoader\mods\1.8"
mod12 = r"C:\Users\lawre\Documents\GitHub\ModLoader\mods\1.12"
destination = r"C:\Users\lawre\AppData\Roaming\.minecraft\mods"
DELmod = r"C:\Users\lawre\AppData\Roaming\.minecraft\mods"

def moving(path, destination):
    ## move origin.file to destination.file
    shutil.copytree(path, destination, copy_function = shutil.copy)


def deleting(destination):
    try:
        shutil.rmtree(destination)
    except OSError as error:
        print(error)


out = eval(input('1.8 or 1.16 (1 or 2)'))

if 1 == out:
    deleting(DELmod)
    moving(mod18,destination)
    print('mods are now 1.8 ready')

elif 2 == out:
    deleting(DELmod)
    moving(mod16, destination)
    print('mods are now 1.16 ready')

elif 3 == out:
    deleting(DELmod)
    moving(mod12, destination)
    print('mods are now 1.12 ready')



print('ended')