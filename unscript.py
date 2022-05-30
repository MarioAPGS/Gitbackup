import os

# Open original file for reconstruction
CHUNK_SIZE = 100000000
fileM = open("video.mp4", "wb")
 
# Manually enter total amount of "chunks"
current_dir = os.path.dirname(os.path.abspath(__file__))
chunks = 3
 
# Piece the file together using all chunks
chunk = 0
while chunk <= chunks:
    print(" - Chunk #" + str(chunk) + " done.")
    fileName =  current_dir + "\\chunk_" + str(chunk) + "_video.mp4"
    fileTemp = open(fileName, "rb")
 
    byte = fileTemp.read(CHUNK_SIZE)
    fileM.write(byte)
 
    chunk += 1
 
fileM.close()