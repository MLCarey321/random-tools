# random-tools
Random tools/scripts I make for myself

## wordle-helper
This is a script I use to help me figure out what words are possible given what I already know from previous guesses.
It depends on [nltk][1].corpus's `words` package, which requires you to:
1. Install nltk
1. Run the following in `python`: `nltk.download('words')`

It accepts a 3-line `input.txt` containing the following:
* Line 1: Known letters in known places (aka "green" letters)
* Line 2: Known letters in unknown places (aka "yellow" letters)
* Line 3: Known absent letters (aka "black" or "grey" letters)

The first two lines include zero-based indices for the respective letters, and any of the three lines can be empty. For example:
| Guess | Letter (color) | Letter (color) | Letter (color) | Letter (color) | Letter (color) |
| ----- | -------------- | -------------- | -------------- | -------------- | -------------- |
| 1     | A (black/grey) | U (black/grey) | D (black/grey) | I (green)      | O (black/grey) |
| 2     | S (black/grey) | T (black/grey) | R (black/grey) | I (green)      | P (yellow)     |

The contents of `input.txt` would be as follows:
```
i3
p4
audostr
```

Which would result in this output:
```
pinic
pilin
pixie
pylic
pyxie
pekin
lipin
```

These are all of the 5-letter words that meet the constraints of what we already know about the word. In this case, the word ended up being `pixie`, which was the 3rd word in our output.

[1]: https://www.nltk.org/install.html
