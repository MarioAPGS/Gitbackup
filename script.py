import os
import sys
import math

current_dir = os.path.dirname(os.path.abspath(__file__))

def print_percent_done(index, total, bar_len=20, title='Please wait'):
    '''
    index is expected to be 0 based index. 
    0 <= index < total
    '''
    percent_done = (index+1)/total*100
    percent_done = round(percent_done, 1)

    done = round(percent_done/(100/bar_len))
    togo = bar_len-done

    done_str = '█'*int(done)
    togo_str = '░'*int(togo)

    print(f'\t⏳{title}: [{done_str}{togo_str}] [{index+1}/{total}] {percent_done}% done', end='\r')

    if round(percent_done) == 100:
        print('\t✅')

# Split item
def file_split(directory_path, file, chunk_size):

    # File to open and break apart
    fileR = open(directory_path + "\\" + file, "rb")
    byte = fileR.read(chunk_size)
    total_chunks = math.ceil(os.path.getsize(directory_path + "\\" + file) / chunk_size)
    chunk = 0
    while byte:
        #print("[" + str(chunk+1) + "/" + str(total_chunks) + "]")
        print_percent_done(chunk+1, total_chunks, title="[spliting] "+ file)
        # Open a temporary file and write a chunk of bytes
        fileN = directory_path + "\\chunk" + str(chunk) + "_" + file
        fileT = open(fileN, "wb")
        fileT.write(byte)
        fileT.close()
            
        # Read next 1024 bytes
        byte = fileR.read(chunk_size)
        chunk += 1

    fileR.close()
    os.remove(directory_path + "\\" + file)

def  directory_split(folder, chunk_size = 80000000, min_size_file = 100000000):
    list = os.listdir(folder)
    for dirpath, dirnames, filenames in os.walk(folder):
        for filename in filenames:
            item = dirpath + "\\" + filename
            size = os.path.getsize(item)
            if size > min_size_file and not item.__contains__(".git"):
                print(item + " " + str(size))
                file_split(dirpath, filename, chunk_size)
    return 

# Merge items
def file_merge(current_dir, file, chunkCount, chunkSize):
    fileM = open(current_dir + "\\" + file, "wb")
    
    # Piece the file together using all chunks
    chunk = 0
    while chunk <= chunkCount:
        #print("[" + str(chunk+1) + "/" + str(chunkCount+1) + "] done.")
        print_percent_done(chunk+1, chunkCount+1, title="[merging] "+file)
        fileName =  current_dir + "\\chunk" + str(chunk) + "_" + file
        fileTemp = open(fileName, "rb")
    
        byte = fileTemp.read(chunkSize)
        fileM.write(byte)
        fileTemp.close()
        os.remove(fileName)
        chunk += 1
    
    fileM.close()

def directory_merge(folder, chunk_size = 80000000):
    dictionary = {}
    for dirpath, dirnames, filenames in os.walk(folder):
        for filename in filenames:
            item = dirpath + "\\" + filename
            if item.__contains__("chunk"):
                chunk_file = dirpath + "\\" + item.split("_")[1]
                if chunk_file in dictionary.keys():
                    dictionary[chunk_file] = dictionary[chunk_file] + 1
                else:
                    dictionary[chunk_file] = 0
    
    for key in dictionary.keys():
        print(key + " -> " + str(dictionary[key]))
        tail, head = os.path.split(key)
        file_merge(tail, head, dictionary[key], chunk_size)


if len(sys.argv) > 0:
    if len(sys.argv) == 3:
            current_dir = sys.argv[2]

    if len(sys.argv) == 1:
        print('''Arguments: [split/merge] [(optional)folder_path]
        split - Separete all files greater than 1Gb inside of the tree in the current folder
        merge - combine all chink files inside of the tree in the current folder
        
        folder_path - (optional) indicate the path where script will operate''')

    if len(sys.argv) >= 2:
        if sys.argv[1] == "split":
            directory_split(current_dir, chunk_size=50000000)
        elif sys.argv[1] == "merge":
            directory_merge(current_dir, chunk_size=50000000)

else:
    print('''Arguments: [split/merge] [(optional)folder_path]
    split - Separete all files greater than 1Gb inside of the tree in the current folder
    merge - combine all chink files inside of the tree in the current folder
    
    folder_path - (optional) indicate the path where script will operate''')