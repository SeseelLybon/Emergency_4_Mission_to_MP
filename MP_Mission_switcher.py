import os
import sys
from shutil import copyfile


loc_game = str(sys.argv[1])

loc_maps = loc_game+"Data\\Maps\\"
loc_specs = loc_game+"Data\\Specs\\"
specs_filename = "fp_params_endless_mp.xml"
mp_map_filename = "multiplayer"

map_file_extentions = [".dds", ".e4m", ".eft"]

mission2mp = 0


# TODO: Let user pick a mission (with names?)
mission_names = {0:"Restore MP",
                 1:"Construction Crane Falls On Church",
                 2:"Fire in Tyre Warehouse",
                 3:"Undercover Transaction",
                 4:"Monster Truck accident",
                 5:"Motorway Brigde Collapses",
                 6:"Bomb Attack During Summit",
                 7:"Hacker Causes Power Failure In The City",
                 8:"Breeched Levee Floods The Town",
                 9:"Police Raid Downtown",
                 10:"Explosion In Polar Station",
                 11:"Oil Rig On Fire",
                 12:"Train Rams Tourist Coach",
                 13:"Accident In Mining Facility",
                 14:"Traffic Accident In Motorway Tunnel",
                 15:"Explosion At Fireworks Company",
                 16:"Witness Protection",
                 17:"Hostage Drama",
                 18:"Outbreak Of Fire In Outside Concert",
                 19:"Catastrophic Accident At The Airport",
                 20:"Great One"
                 }

mission_file_names = {0:"multiplayer.b",
                      1:"m01",
                      2:"m02",
                      3:"m03",
                      4:"m04",
                      5:"m05",
                      6:"m06",
                      7:"m07",
                      8:"m08",
                      9:"m09",
                      10:"m10",
                      11:"m11",
                      12:"m12",
                      13:"m13",
                      14:"m14",
                      15:"m15",
                      16:"m16",
                      17:"m17",
                      18:"m18",
                      19:"m19",
                      20:"m20"
                      }





# TODO: Backup the MP mission files
for i in range(3):
    try:
        os.rename(loc_maps+mp_map_filename+map_file_extentions[i], loc_maps+mp_map_filename+".b"+map_file_extentions[i] )
    except FileNotFoundError:
        print("There is no multiplayer.x file to copy.")
    except FileExistsError:
        print("A backup of multiplayer.x already exists.")


# TODO: Copy and remane the mission files to MP mission files.

for i in range(3):
    copyfile(loc_maps+mission_file_names[mission2mp]+map_file_extentions[i],loc_maps+mp_map_filename+map_file_extentions[i])

# TODO: Replace the mission spec file with one that doesn't cause events (or an alternate file?)

# TODO: Tell the user he's ready
print("Done?")

# TODO: keep program running to put files back manually when done? Alternate option to reset files?

# TODO: Create github repo