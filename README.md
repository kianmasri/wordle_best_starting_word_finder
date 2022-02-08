

# Best Word Finder for Wordle
A quick program I made to find what the best starting word would be in wordle, can be pretty quickly converted into a full player but I didn't really care to do so
## Warning
The wordle_answer_dictionary.json contains the answers to all wordles past and future in order, if you do not wish to spoil the wordles for yourself do not open the file.

## Assumptions
The program is written assuming you are playing on https://www.powerlanguage.co.uk/wordle/ as it assumes the answer can only be from its answer list, if you would like to know the best word for other answer lists you can create your own word dictionaries for such scenarios however be warned that the runtime is pretty lengthy. (~13.5 hours for current configuration, ~15 days if you configure it for the entire 5 word dictionary)

If someone would like to optimize my regex or write custom functions for each filtering operation to improve performance, I will gladly accept them.

## What's the best starting word already?
Disclaimer: This isn't actually guarenteed to be the best starting word, however it is certainly very good, this just finds the word that eliminates the most words with a single guess on average.

**roate** which averages 60.41 possible words after the first guess.

To see all how all words performed or how your favorite starting word stacks up, see word_performance.txt for a sorted list of how all words performed
