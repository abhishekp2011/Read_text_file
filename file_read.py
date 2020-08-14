fname = "mbox-short.txt"

fh = open(fname)
count = 0
c=0
for line in fh:
    c=c+1
    if not line.startswith('From:'):
        continue
    count=count+1
    word=line.split()
    print(word[1])
print("There were", count, "lines in the file with From as the first word")
print(c)
