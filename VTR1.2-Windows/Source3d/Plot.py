import OSfunct
import os

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

def multi_ploter(rtt_path, stc_path, matches):
    folder = OSfunct.create_dir(rtt_path,stc_path)
    for i in matches:
        pmlname = "../Plots3d/" + folder + "/" + i.rtt_contact.residue1.id + str(i.rtt_contact.residue1.parameter) + "-" + str(i.rtt_contact.atom1.id) + "--" + i.rtt_contact.residue2.id + str(i.rtt_contact.residue2.parameter) + "-" + str(i.rtt_contact.atom2.id) + "_x_" + i.stc_contact.residue1.id + str(i.stc_contact.residue1.parameter) + "-" + str(i.stc_contact.atom1.id) + "--" + i.stc_contact.residue2.id + str(i.stc_contact.residue2.parameter) + "-" + str(i.stc_contact.atom2.id) + ".html"
        pml = open(pmlname,'w')
        pml.write("<!DOCTYPE html>\n")
        pml.write('<html lang = "pt-br">\n')
        pml.write('<body>\n<table width="400" cellspacing="1" cellpadding="3" border="0" >\n        <tr>\n')
        pml.write('            <div style="height: 400px; width: 400px; position: relative;"\n')
        pml.write("                class='viewer_3Dmoljs'\n")
        pml.write("                data-backgroundcolor='0x000000'\n")
        
        pml.write("                data-href =  '../Data/" + rtt_path[rtt_path.rfind("/")+1:-11] + "x" + stc_path[stc_path.rfind("/")+1:-4] + "_align/" + rtt_path[rtt_path.rfind("/")+1:] + "'\n")
        pml.write("                data-select='model:0'\n")
        pml.write("                data-style ='cross:hidden=true'\n")
        
        pml.write("                data-select1='model:0;resi:"+str(i.rtt_contact.residue1.parameter)+"'\n")
        pml.write("                data-style1 ='stick:color=yellow'\n")
        pml.write("                data-select2='model:0;resi:"+str(i.rtt_contact.residue2.parameter)+"'\n")
        pml.write("                data-style2 ='stick:color=white'\n")
        
        pml.write("                data-select3='model:0;serial:"+str(i.rtt_contact.atom1.id)+"'\n")
        pml.write("                data-style3 ='stick:color=red'\n")
        pml.write("                data-select4='model:0;serial:"+str(i.rtt_contact.atom2.id)+"'\n")
        pml.write("                data-style4 ='stick:color=red'\n")
        
        pml.write("                data-href1 =  '../Data/"+stc_path[stc_path.rfind("/")+1:] + "'\n")
        pml.write("                data-select5='model:1'\n")
        pml.write("                data-style5 ='cross:hidden=true'\n")
        
        pml.write("                data-select6='model:1;resi:"+str(i.stc_contact.residue1.parameter)+"'\n")
        pml.write("                data-style6 ='stick:color=green'\n")
        pml.write("                data-select7='model:1;resi:"+str(i.stc_contact.residue2.parameter)+"'\n")
        pml.write("                data-style7 ='stick:color=orange'\n")
        
        pml.write("                data-select8='model:1;serial:"+str(i.stc_contact.atom1.id)+"'\n")
        pml.write("                data-style8 ='stick:color=blue'\n")
        pml.write("                data-select9='model:1;serial:"+str(i.stc_contact.atom2.id)+"'\n")
        pml.write("                data-style9 ='stick:color=blue'\n")
        
        pml.write('            ></div>\n        </tr>\n        <tr>\n            <td bgcolor="red"><font color="#FFFFFF" face="arial, verdana, helvetica">\n')
        pml.write("                <b>Distance = "+str(round(i.Vector1(),2))+" A</b>\n")
        pml.write('            </font></td>\n            <td bgcolor="blue"><font color="#FFFFFF" face="arial, verdana, helvetica">\n')
        pml.write("                <b>Distance = "+str(round(i.Vector2(),2))+" A</b>\n")
        pml.write('            </font></td>\n            <td><font color="#000000" face="arial, verdana, helvetica">\n')
        pml.write("                <b>VMD = "+str(round(i.VMD(),2))+"</b>\n")
        pml.write("            </font></td>\n        </tr>\n")

        pml.write('        <tr>\n            <td bgcolor="yellow"><font color="#000000" face="arial, verdana, helvetica">\n')
        pml.write("                <b>"+rtt_path[rtt_path.rfind("/")+1:-11]+"-"+i.rtt_contact.residue1.id+str(i.rtt_contact.residue1.parameter)+" A</b>\n")
        pml.write('            </font></td>\n            <td bgcolor="white"><font color="#000000" face="arial, verdana, helvetica">\n')
        pml.write("                <b>"+rtt_path[rtt_path.rfind("/")+1:-11]+"-"+i.rtt_contact.residue2.id+str(i.rtt_contact.residue2.parameter)+" A</b>\n")
        pml.write("            </font></td>\n        </tr>\n")

        pml.write('        <tr>\n            <td bgcolor="green"><font color="#000000" face="arial, verdana, helvetica">\n')
        pml.write("                <b>"+stc_path[stc_path.rfind("/")+1:-4]+"-"+i.stc_contact.residue1.id+str(i.stc_contact.residue1.parameter)+" A</b>\n")
        pml.write('            </font></td>\n            <td bgcolor="orange"><font color="#000000" face="arial, verdana, helvetica">\n')
        pml.write("                <b>"+stc_path[stc_path.rfind("/")+1:-4]+"-"+i.stc_contact.residue2.id+str(i.stc_contact.residue2.parameter)+" A</b>\n")
        pml.write("            </font></td>\n        </tr>\n    </table>")

        pml.write('</body>\n<footer>    <script src="3Dmol.js"></script>\n</footer>')
