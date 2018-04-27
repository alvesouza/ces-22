def invertFile(readFile,invertedFile):
    read = open((readFile + ".txt"),"r")
    lines = read.readlines()
    read.close()
    n = len(lines) - 1
    write = open(invertedFile + ".txt","w")
    write.write(lines[n]+"\n")
    n -= 1
    while n >= 0:
        write.write(lines[n])
        n -= 1

invertFile("texto teste","invertido")
