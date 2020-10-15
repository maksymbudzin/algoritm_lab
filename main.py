import sys

from algorithms.gem_manager import GemManager
from helpers import csv_reader, algo_analysis

if __name__ == '__main__':

    if len(sys.argv) > 1:
        file_name = sys.argv[1]
    else:
        file_name = input('Enter file name: ')

    gem_quicksort = csv_reader.read_gem_from_csv(file_name)
    quicksort = GemManager.sort_carats_amount_asc_quicksort(gem_quicksort, 0,
                                                            len(gem_quicksort) - 1)
    deltatime_quicksort = algo_analysis.get_function_time('quicksort')
    quicksort_result = [gem.carats_amount for gem in gem_quicksort]

    gem_insertion = csv_reader.read_gem_from_csv(file_name)
    insertion = GemManager.sort_price_desc_insertion(gem_insertion)
    deltatime_insertion = algo_analysis.get_function_time('insertion')
    insertion_result = [gems.price for gems in gem_insertion]

    print(algo_analysis.represent_algorithm('Quicksort', deltatime_quicksort, algo_analysis.quicksort_swap_counter,
                                            algo_analysis.quicksort_comparison_counter, quicksort_result))

    print(algo_analysis.represent_algorithm('Insertion', deltatime_insertion, algo_analysis.insertion_swap_counter,
                                            algo_analysis.insertion_comparison_counter, insertion_result))
