import os
while (1):
     os.system("md ..\\Results")
     os.system("md ..\\Results\\Contacts")
     os.system("md ..\\Results\\Matches")
     os.system("md ..\\Plots3d")
     os.system("md ..\\Results\\Outs")
     os.system("cls")
     os.system("echo ____________________________________________________________\n")
     os.system("echo VTR Geometric v 1.1\n")
     os.system("echo ____________________________________________________________\n")
     os.system("echo Proteins in directory: ")
     os.system("dir ..\Data /a-d /on")
     os.system("echo  ___________________________________________________________\n")
     rtt_protein = input("Choose the first:")
     while (not(os.path.exists("..\\Data\\" + rtt_protein + ".pdb"))):
          print("This file does not exist...")
          rtt_protein = input("Choose the first:")
     stc_protein = input("Choose the second:")
     while (not(os.path.exists("..\\Data\\" + stc_protein + ".pdb"))):
          print("This file does not exist...")
          stc_protein = input("Chooe the second:")
     cutoff = input("Choose the cutoff:")
     execute = "python VTR_Geometric.py ../Data/" + rtt_protein + ".pdb ../Data/" + stc_protein + ".pdb " + cutoff 
     os.system(execute)
     input("Press Enter")
