def trim_txt_file(txt_path):
    """
    Function that trims the txt of alice in wonderland
    Removes illustration lines
    chapter lines
    and empty lines
    """
    with open(txt_path, 'r', encoding='UTF8') as f:
        lines = f.readlines()
    with open(txt_path[:-4]+'_conv.txt', 'w', encoding='UTF8') as f:
        for line in lines:
            if not '[' or not ']' in line: #remove string specified
                if line != '\n': #trim empty lines
                    if not line.isupper(): #trim capitalized lines
                        if line.upper().isupper(): #trim lines without text
                            f.write(line.replace('_', '').replace('\t', '')) #remove italicized and tabbed lines