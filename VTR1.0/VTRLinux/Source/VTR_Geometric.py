#V1.2
#Contacts match by geometric propertie, VMD(Vector Medium Distance)
#Some entry changes
#Write a plot .pml file
#Match skill improved and refined
#Most detailed analisys avaiable(by residue and color scale)

import os
import sys
import Classify
import Contacts
import matplotlib.pyplot as plt
import numpy

class match:
    def __init__(self,rtt_contact,stc_contact):
        self.rtt_contact = rtt_contact
        self.stc_contact = stc_contact
    def Vector1(self):
        return (Contacts.adistance(self.rtt_contact.atom1,self.stc_contact.atom1))
    def Vector2(self):
        return (Contacts.adistance(self.rtt_contact.atom2,self.stc_contact.atom2))
    def VMD(self):
        return ((self.Vector1() + self.Vector2())/2)

def colorchange(index):
    colors = ["aquamarine","blue","bluewhite","br0","br1","br2","br3","br4","br5","br6","br7","br8","br9","brightorange","brown","carbon","chartreuse","chocolate","cyan","darksalmon","dash","deepblue","deepolive","deeppurple","deepsalmon","deepteal","density","dirtyviolet","firebrick","forest","gray","green","greencyan","grey","hotpink","hydrogen","lightblue","lightmagenta","lightorange","lightpink","lightteal","lime","limegreen","limon","magenta","marine","nitrogen","olive","orange","oxygen","palecyan","palegreen","paleyellow","pink","purple","purpleblue","raspberry","red","ruby","salmon","sand","skyblue","slate","smudge","splitpea","sulfur","teal","tv_blue","tv_green","tv_orange","tv_red","tv_yellow","violet","violetpurple","warmpink","wheat","white","yellow","yelloworange"]
    return (colors[(index)%(len(colors)-1)])

def colorscale(VMD, cutoff, out):
    Redest = [255,0,0]
    Bluest = [0,0,255]
    R = (((-255)/cutoff)*VMD)+255
    G = 0
    B = (((255)/cutoff)*VMD)
    if out == 'l':
        color = [int(R),int(G),int(B)]
    elif out == 't':
        color = (float(B)/255,float(G),float(R)/255)
    return(color)
    

def TMAlign(protein1,protein2):
    os.system("g++ TMAlign.cpp -o tmalign.exe")
    path = protein1[-8:-4] + "x" + protein2[-8:-4] + "_align"
    os.system("mkdir ../Data/" + path)
    callalign = "./tmalign.exe " + protein1 + " " + protein2 + " -o " + "../Data/" + path + "/" + protein1[-8:-4]
    os.system(callalign)
    return(path)

def minVMD(matches,blacklist,cutoff):
    minVMD = cutoff
    match = 0
    for i in matches:
        if not((i.rtt_contact in blacklist) or (i.stc_contact in blacklist)):
            if (i.VMD() < minVMD):
                match = i
                minVMD = match.VMD()
    return match

def RMSD(matches, protein1, protein2):
    RMSD = 0
    for i in matches:
        RMSD += (i.VMD()**2)
    RMSD = (RMSD/(protein1.size()*protein2.size()))**(1/2)
    return RMSD

def match_contacts(rtt_contacts,stc_contacts,cutoff):
    all_matches = []
    blacklist = []
    matches = []
    for i in rtt_contacts:
        for j in stc_contacts:
            _match = match(i,j)
            if _match.VMD() <= cutoff:
                all_matches.append(_match)
    control = True
    while control:
        _match = minVMD(all_matches, blacklist, cutoff)
        if _match != 0:
            blacklist.append(_match.rtt_contact)
            blacklist.append(_match.stc_contact)
            matches.append(_match)
        else:
            control = False
    return matches

def freq_VMD(matches,cutoff):
    x = [i for i in numpy.arange(0,float(cutoff),cutoff/20)]
    y = []
    vmd = []
    for match in matches:
        y.append(match.VMD())
    plt.subplot(131)
    frequency, _vmd, thrash = plt.hist(y,bins = x)
    for i in range(1,len(_vmd)):
        vmd.append((_vmd[i-1] + _vmd[i])/2)
    plt.title('Frequency histogram')
    plt.xticks(x)
    plt.ylabel('Frequency')
    plt.xlabel('VMD')
    #plt.show()
    
    plt.subplot(132)
    plt.plot(vmd,frequency,'r')
    plt.title('Frequency distribuition')
    plt.ylabel('Frequency')
    plt.xlabel('VMD')
    #plt.show()

    residues = ["VAL","LEU","TRP","PRO","ILE","MET","FEN","ALA","TRE","GLI","ASN","GLN","CIS","SER","TIR","ARG","HIS","LIS","GLU","ASP"]
    freq = [0 for i in range(0,20)]
    for i in range(0,len(residues)):
        for match in matches:
            if (match.rtt_contact.residue1.id == residues[i]):
                freq[i] += 1
            if (match.rtt_contact.residue2.id == residues[i]):
                freq[i] += 1
            if (match.stc_contact.residue1.id == residues[i]):
                freq[i] += 1
            if (match.stc_contact.residue2.id == residues[i]):
                freq[i] += 1
        
    plt.subplot(133)
    for i in range(0,20):
        plt.bar(residues[i], freq[i], color = colorscale(freq[i],max(freq), 't'), width = 0.7)
    plt.title('Frequency distribuition')
    plt.ylabel('Frequency')
    plt.xlabel('Residue')
    plt.show()
    
def default_ploter(rtt_path, stc_path, matches):
    pmlname = "../Plots/default" + rtt_path[-15:-11] + "_x_" + stc_path[-8:-4] + ".pml"
    pml = open(pmlname,'w')
    pml.write("load ../" + rtt_path[3:] + "\n")
    pml.write("load ../" + stc_path[3:] + "\n")
    x = 0
    for i in matches:
        selection1 = rtt_path[-15:-11] + str(i.rtt_contact.atom1.id)
        entry = "select " + selection1 + ",model " + rtt_path[-15:-4] + " and id " + str(i.rtt_contact.atom1.id) + "\n"
        pml.write(entry)
        selection2 = rtt_path[-15:-11] + str(i.rtt_contact.atom2.id)
        entry = "select " + selection2 + ",model " + rtt_path[-15:-4] + " and id " + str(i.rtt_contact.atom2.id) + "\n"
        pml.write(entry)
        entry = "distance " + selection1 + "-" + selection2 + ", " + selection1 + ", " + selection2 + "\n"
        pml.write(entry)
        entry = "color " + colorchange(x) + ", " + selection1 + "-" + selection2 + "\n"
        pml.write(entry)
        selection1 = stc_path[-8:-4] + str(i.stc_contact.atom1.id)
        entry = "select " + selection1 + ",model " + stc_path[-8:-4] + " and id " + str(i.stc_contact.atom1.id) + "\n"
        pml.write(entry)
        selection2 = stc_path[-8:-4] + str(i.stc_contact.atom2.id)
        entry = "select " + selection2 + ",model " + stc_path[-8:-4] + " and id " + str(i.stc_contact.atom2.id) + "\n"
        pml.write(entry)
        entry = "distance " + selection1 + "-" + selection2 + ", " + selection1 + ", " + selection2 + "\n"
        pml.write(entry)
        entry = "color " + colorchange(x) + ", " + selection1 + "-" + selection2 + "\n"
        pml.write(entry)
        x+=1
    hideH = "sele resn HOH\nhide (sele)" 
    pml.write(hideH)
    pml.close()

def detailed_ploter(rtt_path, stc_path, matches, cutoff):
    pmlname = "../Plots/c_scale" + rtt_path[-15:-11] + "_x_" + stc_path[-8:-4] + ".pml"
    pml = open(pmlname,'w')
    pml.write("load ../" + rtt_path[3:] + "\n")
    pml.write("load ../" + stc_path[3:] + "\n")
    x = 0
    for i in matches:
        color = colorscale(i.VMD(),cutoff,'l')
        entry = "set_color " + str(color[0]) + "_" + str(color[1]) + "_" + str(color[2]) + ", [" + str(color[0]) + "," + str(color[1]) + "," + str(color[2]) + "]\n"
        pml.write(entry)
        selection1 = rtt_path[-15:-11] + str(i.rtt_contact.atom1.id)
        entry = "select " + selection1 + ",model " + rtt_path[-15:-4] + " and id " + str(i.rtt_contact.atom1.id) + "\n"
        pml.write(entry)
        selection2 = rtt_path[-15:-11] + str(i.rtt_contact.atom2.id)
        entry = "select " + selection2 + ",model " + rtt_path[-15:-4] + " and id " + str(i.rtt_contact.atom2.id) + "\n"
        pml.write(entry)
        entry = "distance " + selection1 + "-" + selection2 + ", " + selection1 + ", " + selection2 + "\n"
        pml.write(entry)
        entry = "color " + str(color[0]) + "_" + str(color[1]) + "_" + str(color[2]) + ", " + selection1 + "-" + selection2 + "\n"
        pml.write(entry)
        selection1 = stc_path[-8:-4] + str(i.stc_contact.atom1.id)
        entry = "select " + selection1 + ",model " + stc_path[-8:-4] + " and id " + str(i.stc_contact.atom1.id) + "\n"
        pml.write(entry)
        selection2 = stc_path[-8:-4] + str(i.stc_contact.atom2.id)
        entry = "select " + selection2 + ",model " + stc_path[-8:-4] + " and id " + str(i.stc_contact.atom2.id) + "\n"
        pml.write(entry)
        entry = "distance " + selection1 + "-" + selection2 + ", " + selection1 + ", " + selection2 + "\n"
        pml.write(entry)
        entry = "color " + str(color[0]) + "_" + str(color[1]) + "_" + str(color[2]) + ", " + selection1 + "-" + selection2 + "\n"
        pml.write(entry)
        x += 1
    hideH = "sele resn HOH\nhide (sele)" 
    pml.write(hideH)
    pml.close()

def multi_ploter(rtt_path, stc_path, matches, cutoff):
    folder = rtt_path[-15:-11] + "_x_" + stc_path[-8:-4]
    pmlname = "rm -r ../Plots/" + folder + " /s /q"
    os.system(pmlname)
    pmlname = "mkdir ../Plots/" + folder
    os.system(pmlname)
    for i in matches:
        pmlname = "../Plots/" + folder + "/" + i.rtt_contact.residue1.id + str(i.rtt_contact.residue1.parameter) + "--" + i.rtt_contact.residue2.id + str(i.rtt_contact.residue2.parameter) + "_x_" + i.stc_contact.residue1.id + str(i.stc_contact.residue1.parameter) + "--" + i.stc_contact.residue2.id + str(i.stc_contact.residue2.parameter) + ".pml"
        pml = open(pmlname,'a')
        pml.write("load ../../" + rtt_path[3:] + "\n")
        pml.write("load ../../" + stc_path[3:] + "\n")
        entry = "hide all\n"
        pml.write(entry)
        selection1 = rtt_path[-15:-11] + i.rtt_contact.residue1.id + str(i.rtt_contact.residue1.parameter)
        entry = "select " + selection1 + ",model " + rtt_path[-15:-4] + " and resi " + str(i.rtt_contact.residue1.parameter) + "\n"
        pml.write(entry)
        selection2 = rtt_path[-15:-11] + i.rtt_contact.residue2.id + str(i.rtt_contact.residue2.parameter)
        entry = "select " + selection2 + ",model " + rtt_path[-15:-4] + " and resi " + str(i.rtt_contact.residue2.parameter) + "\n"
        pml.write(entry)
        entry = "show sticks, " + selection1 + " " + selection2 + "\n"
        pml.write(entry)
        selection1 = stc_path[-8:-4] + i.stc_contact.residue1.id + str(i.stc_contact.residue1.parameter)
        entry = "select " + selection1 + ",model " + stc_path[-8:-4] + " and resi " + str(i.stc_contact.residue1.parameter) + "\n"
        pml.write(entry)
        selection2 = stc_path[-8:-4] + i.stc_contact.residue2.id + str(i.stc_contact.residue2.parameter)
        entry = "select " + selection2 + ",model " + stc_path[-8:-4] + " and resi " + str(i.stc_contact.residue2.parameter) + "\n"
        pml.write(entry)
        entry = "show sticks, " + selection1 + " " + selection2 + "\n"
        pml.write(entry)
        entry = "sele resn HOH\nhide (sele)\n"
        pml.write(entry)
    for i in matches:
        pmlname = "../Plots/" + folder + "/" + i.rtt_contact.residue1.id + str(i.rtt_contact.residue1.parameter) + "--" + i.rtt_contact.residue2.id + str(i.rtt_contact.residue2.parameter) + "_x_" + i.stc_contact.residue1.id + str(i.stc_contact.residue1.parameter) + "--" + i.stc_contact.residue2.id + str(i.stc_contact.residue2.parameter) + ".pml"
        pml = open(pmlname,'a')
        color = colorscale(i.VMD(),cutoff,'l')
        entry = "set_color " + str(color[0]) + "_" + str(color[1]) + "_" + str(color[2]) + ", [" + str(color[0]) + "," + str(color[1]) + "," + str(color[2]) + "]\n"
        pml.write(entry)
        selection1 = rtt_path[-15:-11] + str(i.rtt_contact.atom1.id)
        entry = "select " + selection1 + ",model " + rtt_path[-15:-4] + " and id " + str(i.rtt_contact.atom1.id) + "\n"
        pml.write(entry)
        selection2 = rtt_path[-15:-11] + str(i.rtt_contact.atom2.id)
        entry = "select " + selection2 + ",model " + rtt_path[-15:-4] + " and id " + str(i.rtt_contact.atom2.id) + "\n"
        pml.write(entry)
        entry = "distance " + selection1 + "-" + selection2 + ", " + selection1 + ", " + selection2 + "\n"
        pml.write(entry)
        entry = "color " + str(color[0]) + "_" + str(color[1]) + "_" + str(color[2]) + ", " + selection1 + "-" + selection2 + "\n"
        pml.write(entry)
        selection1 = stc_path[-8:-4] + str(i.stc_contact.atom1.id)
        entry = "select " + selection1 + ",model " + stc_path[-8:-4] + " and id " + str(i.stc_contact.atom1.id) + "\n"
        pml.write(entry)
        selection2 = stc_path[-8:-4] + str(i.stc_contact.atom2.id)
        entry = "select " + selection2 + ",model " + stc_path[-8:-4] + " and id " + str(i.stc_contact.atom2.id) + "\n"
        pml.write(entry)
        entry = "distance " + selection1 + "-" + selection2 + ", " + selection1 + ", " + selection2 + "\n"
        pml.write(entry)
        entry = "color " + str(color[0]) + "_" + str(color[1]) + "_" + str(color[2]) + ", " + selection1 + "-" + selection2 + "\n"
        pml.write(entry)
        
        
    

def writer(protein1,protein2,rtt_protein,stc_protein,rtt_contacts,stc_contacts,matches):
    outfile = "../Results/Matches/" + protein1[-8:-4] + "_x_" + protein2[-8:-4] + ".txt"
    out = open(outfile,'w')
    out.write("Rotate Protein: ")
    out.write(rtt_protein.idPDB)
    out.write("\n")
    out.write(rtt_protein.header)
    out.write("\n\nStatic Protein: ")
    out.write(stc_protein.idPDB)
    out.write("\n")
    out.write(stc_protein.header)
    out.write("\n")
    for i in matches:
        out.write(i.rtt_contact.chain1.id)
        out.write(" ")
        out.write(i.rtt_contact.residue1.id)
        out.write(" ")
        out.write(str(i.rtt_contact.residue1.parameter))
        out.write(" ")
        out.write(i.rtt_contact.atom1.type)
        out.write(" ----------- ")
        out.write(i.rtt_contact.chain2.id)
        out.write(" ")
        out.write(i.rtt_contact.residue2.id)
        out.write(" ")
        out.write(str(i.rtt_contact.residue2.parameter))
        out.write(" ")
        out.write(i.rtt_contact.atom2.type)
        out.write("\n")
        out.write(i.stc_contact.chain1.id)
        out.write(" ")
        out.write(i.stc_contact.residue1.id)
        out.write(" ")
        out.write(str(i.stc_contact.residue1.parameter))
        out.write(" ")
        out.write(i.stc_contact.atom1.type)
        out.write(" ----------- ")
        out.write(i.stc_contact.chain2.id)
        out.write(" ")
        out.write(i.stc_contact.residue2.id)
        out.write(" ")
        out.write(str(i.stc_contact.residue2.parameter))
        out.write(" ")
        out.write(i.stc_contact.atom2.type)
        out.write("\n")
        out.write("VMD: ")
        out.write(str(i.VMD()))
        out.write("            Contact types: ")
        for e in i.rtt_contact.contacts:
            out.write(e)
            out.write(", ")
        out.write(" / ")
        for e in i.stc_contact.contacts:
            out.write(e)
            out.write(", ")    
        out.write("\n\n")
    output = "File " + protein1[-8:-4] + "_x_" + protein2[-8:-4] + ".txt" + " generated"
    print(output)
    out.close()
    
def main():
    if (len(sys.argv)) != 5 and (len(sys.argv)) != 4 :
        print("Insufficient paramenters(min: 3, Protein 1, Protein 2, VMD )")
        sys.exit()
    protein1 = sys.argv[1]
    protein2 = sys.argv[2]
    
    path = TMAlign(protein1,protein2)
    rtt_name = "../Data/" + path + protein1[protein1.rfind("/"):-4] + "_rotate.pdb"
    rtt_protein = Classify.classify(rtt_name)
    stc_protein = Classify.classify(protein2)
    rtt_contacts = Contacts.contacts(rtt_protein,protein1[protein1.rfind("/"):-4] + "_rotate")
    stc_contacts = Contacts.contacts(stc_protein,protein2[protein2.rfind("/"):-4])

    matches = match_contacts(rtt_contacts,stc_contacts,int(sys.argv[3]))
    result = str(len(matches)) + " matches found" 
    print(result)
    print(RMSD(matches, rtt_protein, stc_protein))
    writer(protein1,protein2,rtt_protein,stc_protein,rtt_contacts,stc_contacts,matches)
    
    default_ploter(rtt_name, protein2, matches)
    if (len(sys.argv) == 5):
        if (sys.argv[4] == "d"):
            detailed_ploter(rtt_name, protein2, matches, int(sys.argv[3]))
            multi_ploter(rtt_name, protein2, matches, int(sys.argv[3]))
    freq_VMD(matches,int(sys.argv[3]))
    
main()
