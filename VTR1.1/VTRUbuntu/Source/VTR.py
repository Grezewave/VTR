#VTR v1.0
import os
while (1):
     os.system("mkdir ../Results")
     os.system("mkdir ../Results/Contacts")
     os.system("mkdir ../Results/Matches")
     os.system("mkdir ../Plots")
     os.system("mkdir ../Results/Outs")
     os.system("clear")
     os.system("echo ____________________________________________________________\n")
     os.system("echo VTR Geometric v 1.1\n")
     os.system("echo ____________________________________________________________\n")
     os.system("echo Proteins in directory: ")
     os.system("find ../Data -maxdepth 1 -not -type d")
     os.system("echo  ___________________________________________________________\n")
     rtt_protein = input("Choose the first:")
     while (not(os.path.exists("../Data/" + rtt_protein + ".pdb"))):
          print("This file does not exist...")
          rtt_protein = input("Choose the first:")
     stc_protein = input("Choose the second:")
     while (not(os.path.exists("../Data/" + stc_protein + ".pdb"))):
          print("This file does not exist...")
          stc_protein = input("Choose the second:")
     cutoff = input("Choose the cutoff:")
     question = "x"
     while (question != "y" and question != "n" and question != "Y" and question != "N"):
          question = input("Do you want the detailed analysys? (y/n)")
     if (question == "y" or question == "Y"):
          execute = "python3 VTR_Geometric.py ../Data/" + rtt_protein + ".pdb ../Data/" + stc_protein + ".pdb " + cutoff + " d"
     else:
          execute = "python3 VTR_Geometric.py ../Data/" + rtt_protein + ".pdb ../Data/" + stc_protein + ".pdb " + cutoff 
     os.system(execute)
     if (question == "y" or question == "Y"):
          plot = "pymol -Q ../Plots/c_scale" + rtt_protein + "_x_" + stc_protein + ".pml"
     else:
          plot = "pymol -Q ../Plots/default" + rtt_protein + "_x_" + stc_protein + ".pml"
     os.system(plot)
