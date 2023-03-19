ofile = open('5letters.txt')
kl = input('Enter the letters in the correct positions. Write a period in places of unknown ones\n')
cl = input('Enter the letters you know, but do not know their exact location\n')
ncl = input('Enter the letters that cannot be in the word\n')
print('\nResults:')
sol = True
count = 0
for line in ofile:
    line = line.strip()
    for c in range(len(cl)):
        if cl[c] in line:
            sol=True
        else:
            sol=False
            break
    if sol == True:
        for c in range(len(ncl)):
            if ncl[c] in line:
                sol=False
                break
    if sol==True:
        if (line[0]==kl[0] or kl[0]=='.') and (line[1]==kl[1] or kl[1]=='.') and (line[2]==kl[2] or kl[2]=='.') and (line[3]==kl[3] or kl[3]=='.') and (line[4]==kl[4] or kl[4]=='.'):
                print(line)
                count+=1
print('Number of results:',count)
input()