#Linux function
import os

def TMAlign(protein1,protein2):
    if (not(os.path.exists("tmalign.exe"))):
        os.system("g++ TMAlign.cpp -o tmalign")
        print("TMAlign compilado!")
    path = protein1[protein1.rfind("/")+1:-4] + "x" + protein2[protein2.rfind("/")+1:-4] + "_align"
    if os.path.exists("../Data/" + path):
        os.system("rm -r ../Data/" + path)
    os.system("mkdir ../Data/" + path)
    callalign = "./tmalign " + protein1 + " " + protein2 + " -o " + "../Data/" + path + "/" + protein1[-8:-4]
    os.system(callalign)
    return(path)

def create_dir(rtt_path,stc_path):
    folder = rtt_path[rtt_path.rfind("/")+1:rtt_path.rfind("_")] + "_x_" + stc_path[stc_path.rfind("/")+1:-4]
    if (os.path.exists("../Plots/" + folder)):
        pmlname = "rm -r ../Plots/" + folder
        os.system(pmlname)
    pmlname = "mkdir ../Plots/" + folder
    os.system(pmlname)
    return(folder)
