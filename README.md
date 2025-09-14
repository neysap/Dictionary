# Word Count & Dictionary Utilities (Python)

Small, focused Python exercises that show clean dictionary patterns and a simple word-frequency tool. Great for reading, quick review, and unit-tested examples.

## What’s inside
- **Word-frequency counter** with a tiny CLI (`freq_count`, `most_frequent`). :contentReference[oaicite:0]{index=0}  
- **Gradebook (dict-of-dicts)** example: iterate, aggregate, compute averages. :contentReference[oaicite:1]{index=1}  
- **Copying dictionaries safely** (shallow vs deep copy). :contentReference[oaicite:2]{index=2}  
- **Multiple ways to build dicts** (literal, `update`, `dict(zip(...))`). :contentReference[oaicite:3]{index=3}  
- **Unit tests** with `unittest` for the word-count functions. :contentReference[oaicite:4]{index=4}

## Project structure
.
├─ cd_wordcount.py # word-frequency CLI + helpers
├─ word_count_dict_test.py # unit tests for the word-count logic
├─ ca_grade_attend.py # gradebook dict-of-dicts walkthrough
├─ copying_dict.py # shallow vs deepcopy examples
├─ otherways_dict.py # building dictionaries several ways
└─ README.md

makefile
Copy code

## Quick start
**Requirements:** Python 3.9+

```bash
# run the word-frequency tool
python cd_wordcount.py
# type lines of text, then `quit` to see counts and the most frequent word
Run tests:

bash
Copy code
python -m unittest -v
Examples
Word count (snippet):

text
Copy code
Enter text, line by line, and use 'quit' to exit the program
Here is a line of text.
here is another line of text.
quit
a occurs 1 times
another occurs 1 times
...
The most frequent word is here which occurs 2 times

