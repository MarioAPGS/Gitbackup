import os

# Open original file for reconstruction
 
# Manually enter total amount of "chunks"
current_dir = os.path.dirname(os.path.abspath(__file__))
CHUNK_SIZE = 80000000
chunks = 3

fileM = open(current_dir+"\\video.mp4", "wb")
 
# Piece the file together using all chunks
chunk = 0
while chunk <= chunks:
    print(" - Chunk #" + str(chunk) + " done.")
    fileName =  current_dir + "\\chunk" + str(chunk) + "_video.mp4"
    fileTemp = open(fileName, "rb")
 
    byte = fileTemp.read(CHUNK_SIZE)
    fileM.write(byte)
 
    chunk += 1
 
fileM.close()