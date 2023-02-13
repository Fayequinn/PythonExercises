#!/usr/bin/python

Belgium = 'Belgium,10445852,Brussels,737966,Europe,1830,Euro,Catholicism,Dutch,French,German'

#part a
#here I found the length first and manually asked it to print this many hyphens
a=len(Belgium)
print(a)
for i in range(0,81):
    print("-", end=' ')
print()
#try it using len in the range
for i in range(0, len(Belgium)):
    print("-", end=' ')
print()
#part b
print(Belgium.replace(",",":"))

#part c
# print(Belgium[8:16])
# print(Belgium[26:32])
# bel_pop=int(Belgium[8:16])
# bru_pop=int(Belgium[26:32])
# print(bel_pop+bru_pop)

# print("The population of Belgium is: " + str(bel_pop))
# print("The population of Brussels is: " + str(bru_pop))

#part c after Martina's feedback
Belg_list=Belgium.split(",")
print(Belg_list)

pop_bel=int(Belg_list[1])
pop_bru=int(Belg_list[3])

print(pop_bel+pop_bru)