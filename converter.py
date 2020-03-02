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
name = "smash"
scaleToMaxAmplitude = True
middle = 128
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

maxAmplitude = 0

# for a in range(0, 100):
#     print("\t" + str(array[a]))

out = open('output/' + name + '.txt', 'wb')
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
    print('Ratio: ' + str(ratio))
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

print(toPrint)
print(str(sum))
print('Frames Written: ' + str(int(i)))
out.close()

obj.close()
