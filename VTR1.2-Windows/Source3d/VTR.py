#VTR v1.2 entry for windows
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
     chainrtt1 = input("Choose the first chain for " + rtt_protein +"(A, B ..., press enter for run all x all chains):")
     if chainrtt1 == "":
          chainrtt1 = "/"
     chainrtt2 = input("Choose the second chain for " + rtt_protein +"(A, B ..., press enter for run all x all chains):")
     if chainrtt2 == "":
          chainrtt2 = "/"
     chainstc1 = input("Choose the first chain for " + stc_protein +"(A, B ..., press enter for run all x all chains):")
     if chainstc1 == "":
          chainstc1 = "/"
     chainstc2 = input("Choose the second chain for " + stc_protein +"(A, B ..., press enter for run all x all chains):")
     if chainstc2 == "":
          chainstc2 = "/"

     question = "x"
     while (question != "y" and question != "n" and question != "Y" and question != "N"):
          question = input("Do you want the detailed analysys? (y/n)")
     if (question == "y" or question == "Y"):
          execute = "python VTR_Geometric.py ../Data/" + rtt_protein + ".pdb ../Data/" + stc_protein + ".pdb " + cutoff + " " + chainrtt1 + " " + chainrtt2 + " " + chainstc1 + " " + chainstc2 + " d"
     else:
          execute = "python VTR_Geometric.py ../Data/" + rtt_protein + ".pdb ../Data/" + stc_protein + ".pdb " + cutoff + " " + chainrtt1 + " " + chainrtt2 + " " + chainstc1 + " " + chainstc2
    
     os.system(execute)
     input("Press Enter")
