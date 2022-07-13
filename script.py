import os
import sys

current_dir = os.path.dirname(os.path.abspath(__file__))

# Split item

def file_split(directory_path, file, chunk_size = 80000000):

    # File to open and break apart
    fileR = open(directory_path+"\\"+file, "rb")
    byte = fileR.read(chunk_size)

    chunk = 0
    while byte:

        # Open a temporary file and write a chunk of bytes
        fileN = current_dir + "\\chunk" + str(chunk) + "_" + file
        fileT = open(fileN, "wb")
        fileT.write(byte)
        fileT.close()
            
        # Read next 1024 bytes
        byte = fileR.read(chunk_size)
        chunk += 1

    fileR.close()
    os.remove(current_dir + "\\" + file)

def directory_split(folder, min_size_file = 100000000):
    list = os.listdir(folder)
    for item in list:
        size = os.path.getsize(folder + "\\" + item)
        if(size > min_size_file):
            print(item + "  " + str(size))
            file_split(folder, item)
    return 

# Merge items
def file_merge(current_dir, file, chunkCount, chunkSize = 80000000):
    fileM = open(current_dir + "\\" + file, "wb")
    
    # Piece the file together using all chunks
    chunk = 0
    while chunk <= chunkCount:
        print("[" + str(chunkCount) + "/" + str(chunk) + "] done.")
        fileName =  current_dir + "\\chunk" + str(chunk) + "_" + file
        fileTemp = open(fileName, "rb")
    
        byte = fileTemp.read(chunkSize)
        fileM.write(byte)
        fileTemp.close()
        os.remove(fileName)
        chunk += 1
    
    fileM.close()

def directory_merge(folder):
    list = os.listdir(folder)
    dictionary = {}
    for item in list:
        if item.__contains__("chunk"):
            dic_item = item.split("_")
            if dic_item[1] in dictionary.keys():
                dictionary[dic_item[1]] = dictionary[dic_item[1]] + 1
            else:
                dictionary[dic_item[1]] = 0
    
    for key in dictionary.keys():
        print(key + " -> " + str(dictionary[key]))
        file_merge(current_dir, key, dictionary[key])

if len(sys.argv) > 0 and sys.argv[1] == "split":
    directory_split(current_dir)
elif len(sys.argv) > 0 and sys.argv[1] == "merge":
    directory_merge(current_dir)
else:
    print('''Send 1 agument. 
     split - Separete all files greater than 1Gb inside of the tree in the current folder
     merge - combine all chink files inside of the tree in the current folder''')
