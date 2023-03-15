r = open('pelican.txt', 'r')
# content = r.read()

# print(type(r))
# print(r)
#
# print(content)
# print(type(content))
#
# lines = content.splitlines()
# print(lines)
# print(len(lines))


# lines2 = r.readlines()
# print(lines2)

for line in r:
    print(line, end="")
