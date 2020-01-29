class proteins:
    def __init__(self):
        self.idPDB = ""
        self.header = ""
        self.title = ""
        self.chains = []
    def size(self):
        size = 0
        for i in self.chains:
            for e in i.residues:
                size += len(e.atoms)
        return size
class chain:
    def __init__(self):
        self.id = ""
        self.seqres = []
        self.residues = []
class residue:
    def __init__(self):
        self.id = ""
        self.parameter = 0
        self.atoms = []
class atom:
    def __init__(self):
        self.id = ""
        self.type = ""
        self.x = 0
        self.y = 0
        self.z = 0
        self.occupancy = 0
        self.b_factor = 0
        
def tellme(text,data):
    while(len(text)<6):
        text += " "
    j = 6
    info = ""
    for i in data:
        if i[0:6] == text:
            while i[j] == " ":
                j+=1
            k = j
            while i[k+1] != "\n":
                k+=1
            info += i[j:k]
    return info

def idPDB(data):
    return data[0][62:66]
        
def chainslist(data):
    info = []
    for i in data:
        if i[0:6] == "SEQRES":
            if not(i[11] in info):
                info.extend(i[11])
    return info
            
def chainsdef(chainlist,data):
    info = ""
    o = 0
    e = 0
    x = 0
    guard = []
    for i in data:
        if i[0:6] == "SEQRES":
            if (i[11] == chainlist[o]):
                info = chainlist[o]
                chainlist[o] = chain()
                chainlist[o].id = info
                j = 19
                k = j
                while i[k] != " " or i[k+1] != " ":
                    k = j
                    while i[k] != " ":
                        k+=1
                    chainlist[o].seqres.append(i[j:k])
                    j = k + 1
            elif i[11] == chainlist[o].id:
                j = 19
                k = j
                while i[k] != " " or i[k+1] != " ":
                    k = j
                    while i[k] != " ":
                        k+=1
                    chainlist[o].seqres.append(i[j:k])
                    j = k + 1
            else:
                o+=1
                if (i[11] == chainlist[o]):
                    info = chainlist[o]
                    chainlist[o] = chain()
                    chainlist[o].id = info
                    j = 19
                    k = j
                    while i[k] != " " or i[k+1] != " ":
                        k = j
                        while i[k] != " ":
                            k+=1
                        chainlist[o].seqres.append(i[j:k])
                        j = k + 1
        elif i[0:4] == "ATOM":
            if i[21] == chainlist[e].id:
                if int(i[22:26]) not in guard:
                    guard.append(int(i[22:26]))
                    chainlist[e].residues.append(i[17:20])
            else:
                e+=1
                guard = []
                if i[21] == chainlist[e].id:
                    if int(i[22:26]) not in guard:
                        guard.append(int(i[22:26]))
                        chainlist[e].residues.append(i[17:20])
    return chainlist

def residuedef(data,reslist,chain):
    o = -1
    info = reslist[:]
    guard = []
    for i in range(0,len(reslist)):
        reslist[i] = residue()
        reslist[i].id = info[i]
    for i in data:
        if i[0:4] == "ATOM":
            if i[21] == chain:
                if int(i[22:26]) not in guard:
                    guard.append(int(i[22:26]))
                    o+=1
                    if i[17:20] == reslist[o].id:
                        reslist[o].parameter = int(i[22:26])
                        reslist[o].atoms.append(i[13:17])
                else:
                    if i[17:20] == reslist[o].id:
                        reslist[o].parameter = int(i[22:26])
                        reslist[o].atoms.append(i[13:17])
    return reslist
    
def proteindef(data):
    protein = proteins()
    protein.idPDB = idPDB(data)
    protein.header = tellme("HEADER",data)
    protein.title = tellme("TITLE",data)
    protein.chains = chainslist(data)
    protein.chains = chainsdef(protein.chains,data)
    for i in protein.chains:
        i.seq = residuedef(data,i.residues,i.id)
        for e in i.residues:
            e.atoms = atomdef(data,e.atoms,e.id,e.parameter,i.id)
    return protein

                
def atomdef(data,atomlist,resname,parameter,chain):
    info = atomlist[:]
    x = 0
    for e in range(0,len(atomlist)):
        atomlist[e] = atom()
        atomlist[e].type = info[e]
    for i in data:
        if i[0:4] == "ATOM":
            if i[17:20] == resname and i[21] == chain and int(i[22:26]) == parameter:
                if i[13:17] == atomlist[x].type:
                    atomlist[x].id = int(i[6:11])
                    atomlist[x].x = float(i[30:38])
                    atomlist[x].y = float(i[38:46])
                    atomlist[x].z = float(i[46:54])
                    atomlist[x].occupancy = float(i[54:60])
                    atomlist[x].b_factor = float(i[60:66])
                    x+=1
    return atomlist

def classify(file):
    reader = open(file,'r')
    data = reader.readlines()
    reader.close()
    protein = proteindef(data)
    protein.title = protein.title.replace("  ","")
    return protein
                
    
