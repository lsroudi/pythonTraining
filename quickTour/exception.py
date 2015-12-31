try:
    file = open('notExistFile.txt')
except IOError as e:
    print(e)
    
try:
    for line in file.readlines() :
        print(line,end='')
except Exception as e:
    print('impossible d\'ouvrir ce fichier')
