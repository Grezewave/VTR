#V1.2
#Contacts match by geometric propertie, VMD(Vector Medium Distance)
#Some entry changes
#Write a plot .pml file
#Match skill improved and refined
#Most detailed analisys avaiable(by residue and color scale)
#Most Graphic detail and execution stats
#More run options(Chain filter)

import sys
import Classify
import Contacts
import OSfunct
import Plot
import time
import VTR_Functions as vtr

def main():
    start = time.time()
    protein1 = sys.argv[1]
    protein2 = sys.argv[2]
    path = OSfunct.TMAlign(protein1,protein2)
    rtt_name = "../Data/" + path + protein1[protein1.rfind("/"):-4] + "_rotate.pdb"
    rtt_protein = Classify.classify(rtt_name)
    stc_protein = Classify.classify(protein2)
    rtt_contacts = Contacts.contacts(rtt_protein,protein1[protein1.rfind("/"):-4] + "_rotate")
    stc_contacts = Contacts.contacts(stc_protein,protein2[protein2.rfind("/"):-4])

    matches = vtr.match_contacts(rtt_contacts,stc_contacts,int(sys.argv[3]),sys.argv[4],sys.argv[5],sys.argv[6],sys.argv[7])
    end = time.time()
    print("Match execution time: " + str(end-start))
    result = str(len(matches)) + " matches found" + "\n"
    print(result)
    print("RMSD = "+str(vtr.RMSD(matches, rtt_protein, stc_protein)))
    vtr.writer(protein1,protein2,rtt_protein,stc_protein,rtt_contacts,stc_contacts,matches)

    Plot.multi_ploter(rtt_name, protein2, matches)
    if (len(sys.argv) == 9):
        vtr.freq_VMD(matches,int(sys.argv[3]),sys.argv[8])
    else:
        vtr.freq_VMD(matches,int(sys.argv[3]),"x")
main()
