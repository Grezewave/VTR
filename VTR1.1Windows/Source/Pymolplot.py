import Winfunct
import os

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
    folder = Winfunct.create_dir(rtt_path,stc_path)
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
