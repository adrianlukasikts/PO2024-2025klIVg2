import matplotlib.pyplot as plt
import matplotlib
from file import get_filtered_words

fig, ax = plt.subplots()

fig = matplotlib.pyplot.gcf()


dictionary = get_filtered_words("test1.txt")
words = list(map(lambda pair: pair[0], dictionary))
counts = list(map(lambda pair: pair[1], dictionary))


ax.bar(words, counts)
ax.set_ylabel("Number of words")
ax.set_xlabel("Words")

fig.set_size_inches(18.5, 10.5)
fig.savefig('diagram.png')
