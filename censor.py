#Anthony Gandini

def main():
    fileCensored = input("Enter the name of the censored words file: ")
    fileCensor = input("Enter the name of the file to censor: ")
    censoredFile = open(fileCensored , "r")
    fileToCensor = open(fileCensor , "r")
    
    censorWords = censoredFile.read().split(" ")
    words = fileToCensor.read().split(" ")
    
    for i in censorWords:
        for j in range(0 , len(words)):
            if i == words[j]:
                words[j] = "*" * len(i)
                
    censoredFile.close()
    fileToCensor.close()
    fileToCensor = open(fileCensor , "w")
                
    for i in words:
        fileToCensor.write(i)
        fileToCensor.write(" ")
        
    fileToCensor.close()
    
main()
    