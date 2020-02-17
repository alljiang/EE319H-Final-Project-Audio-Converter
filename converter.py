import wave, struct, math
import matplotlib.pyplot as pyplot

# Use input 8 bit, 44.1 khz sample rate

obj = wave.open('smash.wav','r')

sampleWidth = obj.getsampwidth()
framerate = obj.getframerate()
frames = obj.getnframes()

print('Framerate: ' + str(framerate))
print('Number of Frames: ' + str(frames))
numFrames = 200000

array = obj.readframes(numFrames)
max = 1

out = open('output.txt', 'w')
out.write('{')
i = 0.0
elementCount = 0

# get amplify ratio
while i < numFrames:
    if (max < array[int(i)]): max = array[int(i)]
    i += 1

ratio = 255. / float(max)
i = 0
while i < numFrames:
    out.write(str(int(array[int(i)]*ratio)) + ",")
    i += 1
    elementCount += 1

print('Frames Written: ' + str(elementCount))
out.write('};')
out.close()

obj.close()