#zigzag conversion. py

dictofrows = {}
text = input("text: ")
length = len(text)
numrows = int(input("number of rows: "))
currentrow = 1
add = 1
for i in range(1, numrows+1):
    dictofrows[i] = []
for i in range (0, length):
    t = text[i]
    dictofrows[currentrow].append(t)
    if currentrow == numrows:
        add = -1
    if currentrow == 1:
        add = 1 
  
    currentrow += add

print(dictofrows)
finallist = []
for k in range (1, numrows+1):
    for i in range(len(dictofrows[k])):
        finallist.append(dictofrows[k][i])

joined = "".join(finallist)

print(joined)