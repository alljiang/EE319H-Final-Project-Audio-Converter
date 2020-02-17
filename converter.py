import wave, struct, math
import matplotlib.pyplot as pyplot

#
#   Output format:
#   First 4 bytes is 32 bit integer, describes how many frames exist
#   The rest is all data in format:
#
#
# Use input 16 bit, 44.1 khz sample rate

name = "menu"
inputBitrate = 16
outputBitrate = 8

obj = wave.open('input/' + name + '.wav','r')

sampleWidth = obj.getsampwidth()
framerate = obj.getframerate()
frames = obj.getnframes()

print('Framerate: ' + str(framerate))
print('Number of Frames: ' + str(frames))
numFrames = frames

array = obj.readframes(numFrames)
max = 1

out = open('output/' + name + '.audio', 'wb')
i = 0

# get amplify ratio
while i < numFrames:
    if (max < array[int(i)]): max = array[int(i)]
    i += int((inputBitrate / outputBitrate))
out.write((i).to_bytes(4, byteorder="big", signed=False))
ratio = 255. / float(max)
i = 0
while i < numFrames:
    level = int(array[int(i)]*ratio)
    if outputBitrate <= 8:
        out.write((level & 0xFF).to_bytes(1, byteorder="big", signed=False))
    elif outputBitrate <= 16:
        out.write((level & 0xFF).to_bytes(2, byteorder="big", signed=False))
    i += int(inputBitrate / outputBitrate)

print('Frames Written: ' + str(i))
out.close()

obj.close()

asdf = open('output/' + name + '.audio', 'rb')

r = (asdf.read(10))