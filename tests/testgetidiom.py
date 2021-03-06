import random


# read in the list of idioms
fl = open("..\source\idioms.txt",encoding="utf8")
lines = []
for l in fl.readlines():
    lines.append(l.rstrip().split("|"))

# eliminate those IDs that have recently been selected
fl = open("..\source\\recentlyUsed.txt")
recentlyUsedID = []
for l in fl.readlines():
    recentlyUsedID.append(l)

for l in lines:
    if l[0] in recentlyUsedID:
        lines.remove(l)

# now pick a line out of those left
randNumber = random.randint(1, lines.__len__()) - 1
print('%s' % lines[randNumber])
ID, idiom, meaning = lines[randNumber][:3]
print("The idiom's ID is: %s.\nThe idiom is: %s.\nThe idiom's meaning is: %s." % (ID, idiom, meaning))

# Remove the oldest ID and add the newest
"""del recentlyUsedID[0]
recentlyUsedID.append(ID)

# write the new IDs to file
fl = open("..\source\\recentlyUsed.txt", 'w')

for l in recentlyUsedID:
    fl.write(l+"\\n")
"""
