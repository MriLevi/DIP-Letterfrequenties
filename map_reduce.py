from collections import defaultdict


def map_reduce(mapper, reducer, inputs):
    """
    Generic map-reduce function.
    source: https://freecontent.manning.com/implementing-a-mapreduce-framework-using-python-threads/
    """
    map_results = map(mapper, inputs)
    shuffler = defaultdict(list)
    for key, value in map_results:
        shuffler[key].append(value)
    return map(reducer, shuffler.items())
