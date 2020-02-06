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
    if (len(sys.argv)) != 9 and (len(sys.argv)) != 8 :
        print("Insufficient paramenters(min: 8, Protein 1, Protein 2, cutoff ,chain11 ,chain12 ,chain21 ,chain22)")
        sys.exit()
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
    result = str(len(matches)) + " matches found"
    print(result)
    if (0 == len(matches)):
        sys.exit()
    print("RMSD = "+str(vtr.RMSD(matches, rtt_protein, stc_protein)))
    vtr.writer(protein1,protein2,rtt_protein,stc_protein,rtt_contacts,stc_contacts,matches)
    
    Plot.default_ploter(rtt_name, protein2, matches)
    if (len(sys.argv) == 9):
        if (sys.argv[8] == "d"):
            Plot.detailed_ploter(rtt_name, protein2, matches, int(sys.argv[3]))
            Plot.multi_ploter(rtt_name, protein2, matches, int(sys.argv[3]))
        vtr.freq_VMD(matches,int(sys.argv[3]),sys.argv[8])
    else:
        vtr.freq_VMD(matches,int(sys.argv[3]),"x")
main()
