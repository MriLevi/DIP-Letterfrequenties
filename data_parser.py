def data_parser(filename, bigram_split=True, line_split=False):

    with open(filename, 'r', encoding='UTF8') as f:
        data = f.readlines()
    whitelist = 'abcdefghijklmnopqrstuvwxyz' #only letters
    new_data = ["".join([char if char in whitelist else '_' if char == ' ' else '#' for char in line.lower()]) for line in data] #convert spaces to underscores and all other characters to #
    if not bigram_split: #if bigram_split is false, don't split the data into bigrams
        return new_data

    else: #if bigram_split is true, split the data into bigrams
        bigrams = []
        for line in new_data:
            line_bigrams = []
            for i in range(len(line) - 1):
                if not line_split: #if line_split is false, we don't care about lines and just want bigrams
                    bigrams.append(line[i:i + 2])
                else: #if line_split is true, we want to split the text into lines, for example for classifications
                    line_bigrams.append(line[i:i + 2])
            if line_split:
                bigrams.append(line_bigrams)
        return bigrams
