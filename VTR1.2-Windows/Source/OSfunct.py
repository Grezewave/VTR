import os

def TMAlign(protein1,protein2):
    if (not(os.path.exists("tmalign.exe"))):
        os.system("g++ TMAlign.cpp -o tmalign")
        print("TMAlign compilado!")
    path = protein1[-8:-4] + "x" + protein2[-8:-4] + "_align"
    if os.path.exists("../Data/" + path):
        os.system("rd ..\\Data\\" + path + "/s /q")
    os.system("md ..\\Data\\" + path)
    callalign = "tmalign " + protein1 + " " + protein2 + " -o " + "../Data/" + path + "/" + protein1[-8:-4]
    os.system(callalign)
    return(path)

def create_dir(rtt_path,stc_path):
    folder = rtt_path[-15:-11] + "_x_" + stc_path[-8:-4]
    if (os.path.exists("../Plots/" + folder)):
        pmlname = "rd ..\\Plots\\" + folder + "/s /q"
        os.system(pmlname)
    pmlname = "md ..\\Plots\\" + folder
    os.system(pmlname)
    return(folder)

