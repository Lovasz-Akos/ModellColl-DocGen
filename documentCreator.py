from os import read
from pprint import pprint

with open("objExport.obj",'r') as fi:
    id = []
    for ln in fi:
        if ln.startswith("#") and (ln.__contains__("object") or ln.__contains__("polygons")):
            id.append(ln[2:])

for ln in id:
    finalArray = []
    for ln in id:
        ln = ln.replace("object","Név:")
        ln = ln.replace("polygons","polygon")
        ln = ln.replace("triangles","háromszög")
        ln = ln.replace('\n','')
        finalArray.append(ln)


with open('docExport.txt', 'w', encoding='utf8') as f:
    f.write("GotoMoCap QNSZT Modellkollekció tartalma\n\n")
    for item in range(len(finalArray)):
        if item % 2 == 0:
            f.write("%s: " % finalArray[item])
        else:
            f.write("%s\n" % finalArray[item])

print('done :)')