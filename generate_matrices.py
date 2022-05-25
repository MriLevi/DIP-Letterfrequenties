import numpy as np
from map_reduce import map_reduce
from data_parser import data_parser
from mappers_and_reducers import bigram_emitter, bigram_reducer, reduce_to_matrix, no_map

def generate_matrices(lang1, lang2):
    """
    Generates the bigram matrices for the two languages.
    :param lang1:
    :param lang2:
    :return:
    """

    print(f'Generating {lang1} matrix...')
    # generate the bigram matrix for the first language
    # call data parser to get the data and split it into bigrams
    # call map_reduce with bigram emitter and bigram redurcer to get the bigram frequencies
    # call np sum on the output of map_reduce with no map and reduce_to_matrix to get the frequencies matrix
    # convert the matrix to a percentage of occurance matrix
    lang1_frequency_dict = dict(map_reduce(bigram_emitter, bigram_reducer, data_parser(f'input_{lang1.lower()}.txt', bigram_split=True)))
    seperate_matrices_lang1 = list(map_reduce(no_map, reduce_to_matrix, list(lang1_frequency_dict.items())))
    combined_matrices_lang1 = np.sum(seperate_matrices_lang1, axis=0)
    percentage_lang1 = combined_matrices_lang1/np.sum(combined_matrices_lang1)


    print(f'Generating {lang2} matrix...')
    lang2_frequency_dict = dict(map_reduce(bigram_emitter, bigram_reducer, data_parser(f'input_{lang2.lower()}.txt', bigram_split=True)))
    seperate_matrices_lang2 = list(map_reduce(no_map, reduce_to_matrix, list(lang2_frequency_dict.items())))
    combined_matrices_lang2 = np.sum(seperate_matrices_lang2, axis=0)
    percentage_lang2 = combined_matrices_lang2/np.sum(combined_matrices_lang2)

    # generate the identifier matrix, where positive values indicate lang1, negative values indicate lang2
    identification_matrix = percentage_lang1 - percentage_lang2

    # save the matrix to a file
    print('Saving identification matrix...')
    name_string = f'identification_matrix_{lang1}_{lang2}'
    np.save(name_string+'.npy', identification_matrix)