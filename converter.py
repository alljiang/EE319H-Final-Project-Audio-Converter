import wave, struct, math
import matplotlib.pyplot as pyplot

#
#   Output format:
#   First 4 bytes is 32 bit integer, describes how many frames exist
#   The rest is all data in format:
#
#
# Use input 16 bit, 44.1 khz sample rate

name = "smash"

obj = wave.open('input/' + name + '.wav', 'r')

sampleWidth = obj.getsampwidth()
framerate = obj.getframerate()
frames = obj.getnframes()

print('Framerate: ' + str(framerate))
print('Number of Frames: ' + str(frames))
numFrames = frames

print("Reading audio...")
array = obj.readframes(numFrames)
print("Read complete!")

maxVal = 0

# for a in range(0, 100):
#     print("\t" + str(array[a]))

out = open('output/' + name + '.txt', 'wb')
i = 0

# get amplify ratio
while i < int(numFrames):
    if maxVal < array[int(i)]:
        maxVal = array[int(i)]
    i += 1

out.write((int(i)).to_bytes(4, byteorder="big", signed=False))
ratio = 255. / float(maxVal)
print(str(ratio))
# ratio = 1
i = 0

toPrint = ""
while i/2 < int(numFrames):
    level = int(array[i] * ratio)
    out.write((level & 0xFF).to_bytes(1, byteorder="big", signed=False))
    toPrint += str(level) + "\n"
    # print(str(level))
    i += 2

print(toPrint)
print('Frames Written: ' + str(int(i/2)))
out.close()

obj.close()
