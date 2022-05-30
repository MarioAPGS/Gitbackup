import os

CHUNK_SIZE = 80000000
current_dir = os.path.dirname(os.path.abspath(__file__))
file = "video.mp4"

# File to open and break apart
fileR = open(current_dir+"\\"+file, "rb")
byte = fileR.read(CHUNK_SIZE)

chunk = 0
while byte:

    # Open a temporary file and write a chunk of bytes
    fileN = current_dir + "\\chunk" + str(chunk) + "_" + file
    fileT = open(fileN, "wb")
    fileT.write(byte)
    fileT.close()
        
    # Read next 1024 bytes
    byte = fileR.read(CHUNK_SIZE)
    chunk += 1

os.remove(current_dir + "\\" + file)