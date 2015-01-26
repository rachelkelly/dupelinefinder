# a program to see if there are duplicates in a file

print "what file"
f = raw_input("> ")
f = open(f, 'r')

nodelist = []
dupenodelist = []

for line in f.readlines():
    latestline = line # so as to separate iterator from variable - clearer?
    if latestline in nodelist:
        print "duplicate - adding to dupenodelist"
        dupenodelist.append(latestline)
    else:
        nodelist.append(latestline)

print "duplicate nodes are the following: \n"
print dupenodelist
