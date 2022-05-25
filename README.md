# DIP-Letterfrequenties

## Requirements
Python3
Numpy
Language corpus files in the form of .txt files must be present in the following format:
```
input_{language1}.txt
input_{language2}.txt
```
These can be simple ebooks. In utils.py, a simple text file trimmer is included that can trim down text files to a more generic and cleaner state.



## Usage

Download the repository, unzip the files to a folder
Open a command prompt and direct it to that folder, then
```
python3 main.py lang1 lang2 {file_to_classify.txt}
```

## Example
sentences_to_classify.txt are the sentences supplied by the HU, they contain 118 english lines and 73 dutch lines. We will use it for this example

input:
```
python3 main.py english dutch sentences_to_classify.txt
```

output:
```
Generating dutch matrix...
Generating english matrix...
Saving identification matrix...
Loading identification_matrix_dutch_english...
Parsing data...
Classifying...
Done!
---- Results ----
english: 118 lines
dutch: 73 lines
```
