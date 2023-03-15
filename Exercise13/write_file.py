p = open('pelican.txt', 'w')

p.write("A wonderful bird is the pelican,\n")
p.write("His bill holds more than his belican.\n")

lines = ["He can take in his beak,\n", "Enough food or a week, \n", "But I'm damned if I see how the helican.\n"]

p.writelines(lines)

#\n is needed or else the limerick lines wouldn't print on new lines
