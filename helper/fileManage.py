import glob
import shutil

mod16 = r"C:\Users\lawre\Documents\GitHub\ModLoader\mods\1.16"
mod18 = r"C:\Users\lawre\Documents\GitHub\ModLoader\mods\1.8"
mod12 = r"C:\Users\lawre\Documents\GitHub\ModLoader\mods\1.12"
destination = r"C:\Users\lawre\AppData\Roaming\.minecraft\mods"
GlobDestination = r"C:/Users/lawre/AppData/Roaming/.minecraft/mods/*"
DELmod = r"C:\Users\lawre\AppData\Roaming\.minecraft\mods"


def getModVersions():
    folders = glob.glob("mods/*")
    modVersions = []

    for folder in folders:
        modVersions.append(folder.split('\\')[1])


    return modVersions

def GetMineCraftMods():

    folders = glob.glob(GlobDestination)
    MineCraftMods = []

    for folder in folders:
        MineCraftMods.append(folder.split('\\')[1])


    return MineCraftMods





def getMods(modVersion):
    files = glob.glob(f"mods/{modVersion}/*")
    mods = []
    for file in files:
        mods.append(file.split('\\')[1])


    return mods


def moving(path, destination):
    ## move origin.file to destination.file
    shutil.copytree(path, destination, copy_function = shutil.copy)


def deleting(destination):
    try:
        shutil.rmtree(destination)
    except OSError as error:
        print(error)

def cleanModFolder():
    deleting(DELmod)

def MoveMod(modversion):
    cleanModFolder()
    moving(f"mods/{modversion}", destination)

def GetArray(Array1,Array2):

    output = []

    for mod in Array1:

        if mod in Array2:
            output.append('*')
        else:
            output.append('')

    return(output)


if __name__ == "__main__":
   print(getMods('1.16'))
   print(getModVersions())
   print(GetMineCraftMods())
   print(GetArray(getMods('1.16'),GetMineCraftMods()))