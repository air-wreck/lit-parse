import sys
from textblob import TextBlob, blob
import matplotlib.pyplot as plt
import numpy as np

in_file = 'input.txt'
if len(sys.argv) > 1:
    in_file = sys.argv[1]
try:
    fin = open(in_file, 'r')
except:
    print 'Error: input file \'%s\' not found' % in_file
    sys.exit(0)

text = ''
for line in fin:
    text += line

blob = TextBlob(text)
step = 1
if len(sys.argv) > 2:
    try:
        step = int(sys.argv[2])
    except:
        print 'Error: step must be an integer'
        sys.exit(0)

time = []
fortune = []

sentences = blob.sentences
length = len(sentences)
current_buffer = []
for (i, sentence) in enumerate(sentences):
    current_buffer += [sentence.sentiment.polarity]
    if (i+1) % step == 0 or length-i == 1:
        time += [i]
        fortune += [np.average(current_buffer)]
        current_buffer = []

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.spines['bottom'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
plt.axis([0, time[len(time)-1], -1, 1])
plt.title('Shape Curve of Story \''+in_file+'\'')
plt.ylabel('fortune (sentiment polarity)')
ax.annotate('time (sentences)', xy=(0.5,0), xytext=(0,0),
            ha='center', va='top', xycoords='axes fraction',
            textcoords='offset points', annotation_clip=False)

plt.plot(time, fortune)
plt.show()
