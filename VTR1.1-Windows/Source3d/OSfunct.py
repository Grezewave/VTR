import os

def TMAlign(protein1,protein2):
    if (not(os.path.exists("tmalign.exe"))):
        os.system("g++ TMAlign.cpp -o tmalign")
        print("TMAlign compilado!")
    path = protein1[-8:-4] + "x" + protein2[-8:-4] + "_align"
    os.system("md ..\\Data\\" + path)
    callalign = "tmalign " + protein1 + " " + protein2 + " -o " + "../Data/" + path + "/" + protein1[-8:-4]
    os.system(callalign)
    return(path)

def create_dir(rtt_path,stc_path):
    folder = rtt_path[-15:-11] + "_x_" + stc_path[-8:-4]
    pmlname = "rd ..\\Plots3d\\" + folder + " /s /q"
    os.system(pmlname)
    pmlname = "md ..\\Plots3d\\" + folder
    os.system(pmlname)
    return(folder)

