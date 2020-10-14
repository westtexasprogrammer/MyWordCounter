from collections import Counter


Text = "Sample text: my name is oscar chavez oscar"

# Cleaning text and lower casing all words
# Should clean for other types of character or punctuation on the text
for char in '-.,:\n':
    Text = Text.replace(char,' ')
Text = Text.lower()

# split returns a list of words delimited by sequences of whitespace (including tabs, newlines, etc, like re's \s)
word_list = Text.split()

print(Counter(word_list).most_common())