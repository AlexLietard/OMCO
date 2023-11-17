import os
import shutil

path = os.getcwd()
folder = "\\initial"
for i, participant in enumerate([p.path for p in os.scandir(path+folder) if p.is_dir()]):
    os.mkdir(participant[0:-1]+ str(i +1) + "_clean")
    nouvel_essai = ""
    for d, old_path in enumerate([f.path for f in os.scandir(participant)]):
        print(old_path)
        if str(old_path)[-4:] == ".bsf":
            nouvel_essai = "Trial" + str(d+1) + ".bsf"
            new_path = participant[0:-1] + str(i +1) + "_clean" + "\\" + nouvel_essai
            shutil.copy(old_path, new_path)
