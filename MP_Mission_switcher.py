import os
import sys
from shutil import copyfile


print("debug", sys.argv);
#loc_game = str(sys.argv[1]);
loc_game = ""
#mission2mp = int(sys.argv[2]);

loc_maps = loc_game+"Data\\Maps\\";
loc_specs = loc_game+"Data\\Specs\\";
specs_filename = "fp_params_endless_mp.xml";
mp_map_filename = "multiplayer";

map_file_extentions = [".dds", ".e4m", ".eft"];


# TODO: Let user pick a mission (with names?)
mission_names = {0:"0:  Restore MP",
                 1:"1:  Construction Crane Falls On Church",
                 2:"2:  Fire in Tyre Warehouse",
                 3:"3:  Undercover Transaction",
                 4:"4:  Monster Truck accident",
                 5:"5:  Motorway Brigde Collapses",
                 6:"6:  Bomb Attack During Summit",
                 7:"7:  Hacker Causes Power Failure In The City",
                 8:"8:  Breeched Levee Floods The Town",
                 9:"9:  Police Raid Downtown",
                 10:"10: Explosion In Polar Station",
                 11:"11: Oil Rig On Fire",
                 12:"12: Train Rams Tourist Coach",
                 13:"13: Accident In Mining Facility",
                 14:"14: Traffic Accident In Motorway Tunnel",
                 15:"15: Explosion At Fireworks Company",
                 16:"16: Witness Protection",
                 17:"17: Hostage Drama",
                 18:"18: Outbreak Of Fire In Outside Concert",
                 19:"19: Catastrophic Accident At The Airport",
                 20:"20: The Great One"
                 };

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
                      };

print("Which mission to use for MP?:",end="\n");
for k,v in mission_names.items():
    print(v);
userinput = input();
mission2mp = int(userinput);


if mission2mp == 0:
    print("Restoring MP");
else:
    print("Turning mission",mission_names[mission2mp], "into mp map" );

    # TODO: Backup the MP mission files
    print("Making backup of mp mission files if there is none");

    for i in range(3):
        try:
            copyfile(loc_maps + mp_map_filename + map_file_extentions[i],
                     loc_maps + mp_map_filename + ".b" + map_file_extentions[i]);
            print("backing up  " + loc_maps + mp_map_filename + map_file_extentions[i]);
        except FileNotFoundError:
            print("There is no multiplayer." + map_file_extentions[i] + " file to copy.");
        except FileExistsError:
            print("A backup of multiplayer." + map_file_extentions[i] + " already exists.");




# TODO: Copy and remane the mission files to MP mission files.
print("Copy and renaming ");
for i in range(3):
    copyfile(loc_maps+mission_file_names[mission2mp]+map_file_extentions[i],loc_maps+mp_map_filename+map_file_extentions[i]);


# TODO: Replace the mission spec file with one that doesn't cause events (or an alternate file?)


# TODO: Tell the user he's ready
print("Done?");


# TODO: keep program running to put files back manually when done? Alternate option to reset files?
