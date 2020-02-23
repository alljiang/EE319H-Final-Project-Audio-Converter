import wave, struct, math
import matplotlib.pyplot as pyplot

#
#   Output format:
#   First 4 bytes is 32 bit integer, describes how many frames exist
#   The rest is all level data out of 255
#
#
# Use input 8 bit, 44.1 khz sample rate, mono

# ====CONFIGURE HERE====
name = "321go"
scaleToMaxAmplitude = True
# ======================

obj = wave.open('input/' + name + '.wav', 'r')

sampleWidth = obj.getsampwidth()
framerate = obj.getframerate()
frames = obj.getnframes()

print('Framerate: ' + str(framerate))
print('Sample Width: ' + str(sampleWidth))
print('Number of Frames: ' + str(frames))
numFrames = frames

print("Reading audio...")
array = obj.readframes(numFrames)
print("Read complete!")

maxVal = 0

# for a in range(0, 100):
#     print("\t" + str(array[a]))

out = open('output/' + name + '.txt', 'wb')
out.write((int(frames)).to_bytes(4, byteorder="big", signed=False))
i = 0

if scaleToMaxAmplitude:
    # get amplify ratio
    while i < int(numFrames):
        if maxVal < array[int(i)]:
            maxVal = array[int(i)]
        i += 1

    ratio = 255. / float(maxVal)
    print('Ratio: ' + str(ratio))
else:
    ratio = 1

i = 0
toPrint = ""
while i < int(numFrames):
    level = max(1, min(int(array[i] * ratio), 255))
    out.write((level & 0xFF).to_bytes(1, byteorder="big", signed=False))
    toPrint += str(level) + "\n"
    i += 1

print(toPrint)
print('Frames Written: ' + str(int(i)))
out.close()

obj.close()
