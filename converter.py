import wave, struct, math
import matplotlib.pyplot as pyplot
import os

#
#   Output format:
#   First 4 bytes is 32 bit integer, describes how many frames exist
#   The rest is all level data out of 255
#
#
# Use input 8 bit, 32 khz sample rate, mono

# ====CONFIGURE HERE====
# name = "321go"
folderName = "input-valvano"
scaleToMaxAmplitude = True
middle = 128
# ======================

numFiles = len(os.listdir(os.getcwd() + '/' + folderName))

for name in os.listdir(os.getcwd() + '/' + folderName):

    obj = wave.open(folderName + '/' + name, 'r')

    sampleWidth = obj.getsampwidth()
    framerate = obj.getframerate()
    frames = obj.getnframes()

    if framerate != 32000:
        print("ERROR: Framerate not 32000 on file: " + name)
        while(1): pass

    print('Framerate: ' + str(framerate))
    print('Sample Width: ' + str(sampleWidth))
    print('Name: ' + str(name))
    print('Number of Frames: ' + str(frames))
    numFrames = frames

    print("Reading audio...")
    array = obj.readframes(numFrames)
    print("Read complete!")

    maxAmplitude = 0

    out = open('output/' + name.split('.')[0] + '.txt', 'wb')
    out.write((int(frames)).to_bytes(4, byteorder="big", signed=False))
    i = 0

    if scaleToMaxAmplitude:
        # get amplify ratio
        while i < int(numFrames):
            amplitude = array[int(i)] - middle
            if maxAmplitude < amplitude:
                maxAmplitude = amplitude
            i += 1

        ratio = 255. / float(maxAmplitude)
    else:
        ratio = 1

    i = 0
    toPrint = ""
    sum = 0
    while i < int(numFrames):
        amplitude = array[i] - middle
        level = max(1, min(int(amplitude * ratio + middle), 255))
        out.write((level & 0xFF).to_bytes(1, byteorder="big", signed=False))
        # toPrint += str(level) + "\n"
        toPrint += str(level) + ","
        if i < 10000:
            sum += level
        i += 1

    print('Frames Written: ' + str(int(i)))
    out.close()

    obj.close()

    print('\n\n')