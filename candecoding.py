f = open("BMS_S1C12_V4_VTriggerF.txt", "r")
g = open("test2.txt", "w")

data = f.readlines()[4:]
for i in data:
    if i.strip():
        g.write("".join(i.split()[6:]) + "\n")
f.close()
g.close()
with open ("test2.txt", "r") as file:
    len = len(file.read())
    print(len)
