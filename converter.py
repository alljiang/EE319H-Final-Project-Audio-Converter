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

out = open('output/' + name + '.txt', 'wb')
i = 0

# get amplify ratio
while i < int(numFrames/int(inputBitrate / outputBitrate)):
    if (max < array[int(i)]): max = array[int(i)]
    i += 1

out.write((i).to_bytes(4, byteorder="big", signed=False))
ratio = 255. / float(max)
i = 0
x = 0

toPrint = ""
while i < int(numFrames/int(inputBitrate / outputBitrate)):
    level = int(array[int(i)]*ratio)
    if outputBitrate <= 8:
        out.write((level & 0xFF).to_bytes(1, byteorder="big", signed=False))
    elif outputBitrate <= 16:
        out.write((level & 0xFF).to_bytes(2, byteorder="big", signed=False))
    i += int(inputBitrate / outputBitrate)
    out.write((x & 0xFF).to_bytes(1, byteorder="big", signed=False))
    toPrint += str(level) + "\n"
    x += 1
# count = 0
# for s in range(0, 1000):
#     x = 0
#     while x < 256:
#         out.write((x & 0xFF).to_bytes(1, byteorder="big", signed=False))
#         x += 1
#         count += 1
#     x = 254
#     while x >= 0:
#         out.write((x & 0xFF).to_bytes(1, byteorder="big", signed=False))
#         x -= 1
#         count += 1
#
# out.write((count).to_bytes(4, byteorder="big", signed=False))
#
# for s in range(0, 1000):
#     x = 0
#     while x < 256:
#         out.write((x & 0xFF).to_bytes(1, byteorder="big", signed=False))
#         x += 1
#         print(x)
#     x = 254
#     while x >= 0:
#         out.write((x & 0xFF).to_bytes(1, byteorder="big", signed=False))
#         x -= 1
#         print(x)

print(toPrint)
print('Frames Written: ' + str(i))
out.close()

obj.close()
