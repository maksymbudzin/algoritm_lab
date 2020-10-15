import timeit

quicksort_swap_counter = insertion_swap_counter = 0

quicksort_comparison_counter = insertion_comparison_counter = 0


def get_function_time(function_name):
    return timeit.timeit(function_name, 'from __main__ import ' + function_name)


def represent_algorithm(algorithm_name, execution_time, amount_of_swaps, amount_of_comparison, result):
    return algorithm_name + '\n' + \
           'Comparisons: ' + str(amount_of_comparison) + '\n' + \
           'Swaps: ' + str(amount_of_swaps) + '\n' + \
           'Time: ' + str(execution_time) + '\n' + \
           'Result: ' + str(result) + '\n'
