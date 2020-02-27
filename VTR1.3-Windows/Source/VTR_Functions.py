#VTR Functions

import Contacts
import matplotlib
import matplotlib.pyplot as plt
import numpy

class match:
    def __init__(self,rtt_contact,stc_contact):
        self.rtt_contact = rtt_contact
        self.stc_contact = stc_contact
    def Vector11(self):
        return (Contacts.adistance(self.rtt_contact.atom1,self.stc_contact.atom1))
    def Vector12(self):
        return (Contacts.adistance(self.rtt_contact.atom1,self.stc_contact.atom2))
    def Vector21(self):
        return (Contacts.adistance(self.rtt_contact.atom2,self.stc_contact.atom1))
    def Vector22(self):
        return (Contacts.adistance(self.rtt_contact.atom2,self.stc_contact.atom2))
    def VMD(self):
        VMD=[]
        VMD.append((self.Vector11() + self.Vector22())/2)
        VMD.append((self.Vector12() + self.Vector21())/2)
        return (min(VMD))
            
            

def minVMD(matches,blacklist,cutoff):
    minVMD = cutoff
    match = 0
    for i in matches:
        if not((i.rtt_contact in blacklist) or (i.stc_contact in blacklist)):
            if (i.VMD() < minVMD):
                match = i
                minVMD = match.VMD()
    return match

def pltcolor(index):
    colors = ["aquamarine","violet","beige","black","blue","brown","chartreuse","coral","crimson","cyan","darkblue","pink","fuchsia","gold","green","grey","chartreuse","chocolate","cyan","darksalmon"]
    return (colors[(index)%(len(colors))])
    
def RMSD(matches, protein1, protein2):
    RMSD = 0
    for i in matches:
        RMSD += (i.VMD()**2)
    RMSD = (RMSD/len(matches))*(1/2)
    return RMSD

def VTR(matches, protein1, protein2):
    VTR = 0
    for i in matches:
        VTR += i.VMD()
    VTR = (VTR/len(matches))*(1+abs(protein1.size()-protein2.size()))
    return VTR

def match_contacts(rtt_contacts,stc_contacts,cutoff,chain11,chain12,chain21,chain22):
    all_matches = []
    blacklist = []
    matches = []
    allow = 0 
    for i in rtt_contacts:
        for j in stc_contacts:
            if chain11 == chain12 == "/":
                if (chain21 == j.chain1.id and chain22 == j.chain2.id)or(chain22 == j.chain1.id and chain21 == j.chain2.id):
                    allow = 1
                elif (chain21 == j.chain1.id and "/" == chain22) or ("/" == chain22 and chain21 == j.chain2.id):
                    allow = 1
                elif (chain22 == j.chain1.id and "/" == chain21) or ("/" == chain21 and chain22 == j.chain2.id):
                    allow = 1
                elif chain21 == chain22 == "/":
                    allow = 1
                
            if (chain11 == i.chain1.id and chain12 == i.chain2.id)or(chain12 == i.chain1.id and chain11 == i.chain2.id):
                if (chain21 == j.chain1.id and chain22 == j.chain2.id)or(chain22 == j.chain1.id and chain21 == j.chain2.id):
                    allow = 1
                elif (chain21 == j.chain1.id and "/" == chain22) or ("/" == chain22 and chain21 == j.chain2.id):
                    allow = 1
                elif (chain22 == j.chain1.id and "/" == chain21) or ("/" == chain21 and chain22 == j.chain2.id):
                    allow = 1
                elif chain21 == chain22 == "/":
                    allow = 1

            elif (chain11 == i.chain1.id and chain12 == "/")or(chain12 == "/" and chain11 == i.chain2.id):
                if (chain21 == j.chain1.id and chain22 == j.chain2.id)or(chain22 == j.chain1.id and chain21 == j.chain2.id):
                    allow = 1
                elif (chain21 == j.chain1.id and "/" == chain22) or ("/" == chain22 and chain21 == j.chain2.id):
                    allow = 1
                elif (chain22 == j.chain1.id and "/" == chain21) or ("/" == chain21 and chain22 == j.chain2.id):
                    allow = 1
                elif chain21 == chain22 == "/":
                    allow = 1

            elif (chain11 == "/" and chain12 == i.chain2.id)or(chain12 == i.chain1.id and chain11 == "/"):
                if (chain21 == j.chain1.id and chain22 == j.chain2.id)or(chain22 == j.chain1.id and chain21 == j.chain2.id):
                    allow = 1
                elif (chain21 == j.chain1.id and "/" == chain22) or ("/" == chain22 and chain21 == j.chain2.id):
                    allow = 1
                elif (chain22 == j.chain1.id and "/" == chain21) or ("/" == chain21 and chain22 == j.chain2.id):
                    allow = 1
                elif chain21 == chain22 == "/":
                    allow = 1
            
            if allow:
                _match = match(i,j)
                if _match.VMD() <= cutoff:
                    all_matches.append(_match)
            allow = 0
                    
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


def freq_VMD(matches,cutoff,detail):
    x = [i for i in numpy.arange(0,float(cutoff),cutoff/20)]
    y = []
    vmd = []
    for match in matches:
        y.append(match.VMD())
    pic = plt.figure(figsize=(18, 5))
    pic.patch.set_facecolor((1,0.79607843137,0.85882352941))
    plt.subplot(121)
    frequency, _vmd, thrash = plt.hist(y,bins = x,color = 'k')
    for i in range(1,len(_vmd)):
        vmd.append((_vmd[i-1] + _vmd[i])/2)
    plt.title('Frequency histogram')
    plt.xticks(x)
    plt.ylabel('Frequency')
    plt.xlabel('VMD')

    plt.subplot(122)
    plt.plot(vmd,frequency,'k')
    plt.title('Frequency distribuition')
    plt.ylabel('Frequency')
    plt.xlabel('VMD')
    plt.subplots_adjust(left=0.04, bottom=0.05, right=0.99, top=0.90, wspace=0.09, hspace=0.41)
                
    plt.savefig('../Graphs/VMD')
    plt.show()

    if detail == "d":
        fig = 1
        rtt_freq = { "ALA" : [0 for i in range(0,20)],
                     "ARG" : [0 for i in range(0,20)],
                     "ASN" : [0 for i in range(0,20)],
                     "ASP" : [0 for i in range(0,20)],
                     "CYS" : [0 for i in range(0,20)],
                     "GLN" : [0 for i in range(0,20)],
                     "GLY" : [0 for i in range(0,20)],
                     "GLU" : [0 for i in range(0,20)],
                     "HIS" : [0 for i in range(0,20)],
                     "ILE" : [0 for i in range(0,20)],
                     "LEU" : [0 for i in range(0,20)],
                     "LYS" : [0 for i in range(0,20)],
                     "MET" : [0 for i in range(0,20)],
                     "PHE" : [0 for i in range(0,20)],
                     "PRO" : [0 for i in range(0,20)],
                     "SER" : [0 for i in range(0,20)],
                     "THR" : [0 for i in range(0,20)],
                     "TRP" : [0 for i in range(0,20)],
                     "TYR" : [0 for i in range(0,20)],
                     "VAL" : [0 for i in range(0,20)]}
                    
        stc_freq = { "ALA" : [0 for i in range(0,20)],
                     "ARG" : [0 for i in range(0,20)],
                     "ASN" : [0 for i in range(0,20)],
                     "ASP" : [0 for i in range(0,20)],
                     "CYS" : [0 for i in range(0,20)],
                     "GLN" : [0 for i in range(0,20)],
                     "GLY" : [0 for i in range(0,20)],
                     "GLU" : [0 for i in range(0,20)],
                     "HIS" : [0 for i in range(0,20)],
                     "ILE" : [0 for i in range(0,20)],
                     "LEU" : [0 for i in range(0,20)],
                     "LYS" : [0 for i in range(0,20)],
                     "MET" : [0 for i in range(0,20)],
                     "PHE" : [0 for i in range(0,20)],
                     "PRO" : [0 for i in range(0,20)],
                     "SER" : [0 for i in range(0,20)],
                     "THR" : [0 for i in range(0,20)],
                     "TRP" : [0 for i in range(0,20)],
                     "TYR" : [0 for i in range(0,20)],
                     "VAL" : [0 for i in range(0,20)]}

        residues = ["ALA","ARG","ASN","ASP","CYS","GLN","GLY","GLU","HIS","ILE","LEU","LYS","MET","PHE","PRO","SER","THR","TRP","TYR","VAL"]

        x = 1
        for ref in rtt_freq:
            for i in range(0,len(residues)):
                for match in matches:
                    if (match.rtt_contact.residue1.id == ref):
                        if (match.rtt_contact.residue2.id == residues[i]):
                            rtt_freq[ref][i] += 1
                    elif (match.rtt_contact.residue2.id == ref):
                        if (match.rtt_contact.residue1.id == residues[i]):
                            rtt_freq[ref][i] += 1
                    if (match.stc_contact.residue1.id == ref):
                        if (match.stc_contact.residue2.id == residues[i]):
                            stc_freq[ref][i] += 1
                    elif (match.stc_contact.residue2.id == ref):
                        if (match.stc_contact.residue1.id == residues[i]):
                            stc_freq[ref][i] += 1
        _max = 0
        for ref in rtt_freq:
            for index in rtt_freq[ref]:
                if index > _max:
                    _max = index

            for index in stc_freq[ref]:
                if index > _max:
                    _max = index
        pic2 = plt.figure(figsize=(14, 10))  
        for ref in rtt_freq:                
            sub = "42"+str(x)
            plt.subplot(sub)
            plt.bar(residues, rtt_freq[ref],width=0.7)
            plt.axis([-1,20,0,_max])
            plt.title('Frequency '+ref)
            plt.ylabel('Frequency')
            plt.xlabel('Residue')
            x+=1

            sub = "42"+str(x)
            plt.subplot(sub)
            plt.bar(residues, stc_freq[ref],width=0.7)
            plt.axis([-1,20,0,_max])
            plt.title('Frequency '+ref)
            plt.ylabel('Frequency')
            plt.xlabel('Residue')
            x+=1
        
            if x == 9:
                plt.subplots_adjust(left=0.04, bottom=0.05, right=0.99, top=0.97, wspace=0.09, hspace=0.41)
                plt.savefig('../Graphs/Resi-'+str(fig))
                plt.show()
                fig+=1
                plt.clf()
                x = 1     
    

def writer(protein1,protein2,rtt_protein,stc_protein,rtt_contacts,stc_contacts,matches):
    outfile = "../Results/Matches/" + protein1[protein1.rfind("/")+1:-4] + "x" + protein2[protein2.rfind("/")+1:-4] + ".txt"
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
        out.write(" ")
        out.write(str(i.rtt_contact.atom1.id))
        out.write(" ----------- ")
        out.write(i.rtt_contact.chain2.id)
        out.write(" ")
        out.write(i.rtt_contact.residue2.id)
        out.write(" ")
        out.write(str(i.rtt_contact.residue2.parameter))
        out.write(" ")
        out.write(i.rtt_contact.atom2.type)
        out.write(" ")
        out.write(str(i.rtt_contact.atom2.id))
        out.write("\n")
        out.write(i.stc_contact.chain1.id)
        out.write(" ")
        out.write(i.stc_contact.residue1.id)
        out.write(" ")
        out.write(str(i.stc_contact.residue1.parameter))
        out.write(" ")
        out.write(i.stc_contact.atom1.type)
        out.write(" ")
        out.write(str(i.stc_contact.atom1.id))
        out.write(" ----------- ")
        out.write(i.stc_contact.chain2.id)
        out.write(" ")
        out.write(i.stc_contact.residue2.id)
        out.write(" ")
        out.write(str(i.stc_contact.residue2.parameter))
        out.write(" ")
        out.write(i.stc_contact.atom2.type)
        out.write(" ")
        out.write(str(i.stc_contact.atom2.id))
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
    out.close()
    
