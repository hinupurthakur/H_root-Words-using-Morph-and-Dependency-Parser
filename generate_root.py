
# coding: utf-8

# In[2]:
#To run: python generate_root.py <path+hindi.morph.dat> <path+hindi_dep_parser_original.dat>

import re,sys
tmp_path="/".join(sys.argv[2].split("/")[:-1])
out=open(tmp_path+"/H_headid-root_info_from_morph_and_parser.dat","w")
err=open(tmp_path+"/morph_and_parser_root_info_log","w")
exception=[]
POS_Dict={"PRON":"p","VERB":"v","ADP":("sh","prsg"),"NOUN":"n","ADJ":"adj","AUX":"v","DET":"v","PROPN":"n","SCONJ":"adj"}
def POS_check(morph_pos,dep_pos) :
    
    try :
        if dep_pos != "PUNCT":
            if dep_pos == "ADP":
                if POS_Dict["ADP"][0] == morph_pos :
                    return 1
                elif POS_Dict["ADP"][1] == morph_pos :
                    return 1
            else :
                if POS_Dict[dep_pos] == morph_pos :
                    return 1
        
        else :
            return 0
    except KeyError :
        ex="Key Error because of absence of morph POS of "+dep_pos
        if ex not in exception:
            exception.append(ex)
    
def Select_Root(filename,depname):
    log=[]
    head_root=[]
    with open(filename, "r") as f:
        data = f.read().split("\n")
        while "" in data:
            data.remove("")
    with open(depname, "r") as f:
        dep_data = f.read().split("\n")
        while "" in dep_data:
            dep_data.remove("")
    #with open(writeFile, 'w') as w:
    for entry in data:
        for dep in dep_data :
            if re.findall("H_word-root-cat-vib-case-gen-num-per-tam",entry) :
                #print(entry.split("\t")[2]) #[3] is POS
                if entry.split("\t")[2] != '' :
                    if entry.split("\t")[1]==dep.split("\t")[1]:
                        if POS_check(entry.split("\t")[3],dep.split("\t")[3]) :
                            
                            #print(dep.split("\t")[0],entry.split("\t")[2])
                            str="(H_headid-root\t" +dep.split("\t")[0]+"\t"+entry.split("\t")[2]+")"
                            if str not in head_root:
                                head_root.append(str)
                else :
                    str="Root for " +entry.split("\t")[1] + " doesn't exist"
                    if str not in log:
                        log.append(str)
                        

    for i in head_root:
        out.write(i+"\n")
    for j in log:
        err.write(j+"\n")
    
    for i in exception :
        err.write(i+"\n")
    #writeFile = "H_headid-root_info.dat"
morphfile=sys.argv[1]
depfile=sys.argv[2]
Select_Root(morphfile,depfile)

