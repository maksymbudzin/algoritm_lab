from helpers import algo_analysis


class GemManager:
    @staticmethod
    def sort_price_desc_insertion(gem_list):

        for iterator in range(1, len(gem_list)):
            value_to_sort = gem_list[iterator].price
            while iterator > 0 and value_to_sort > gem_list[iterator - 1].price:
                algo_analysis.insertion_comparison_counter += 2
                gem_list[iterator], gem_list[iterator - 1] = gem_list[iterator - 1], gem_list[
                    iterator]
                algo_analysis.insertion_swap_counter += 1
                iterator -= 1

    @staticmethod
    def sort_carats_amount_asc_quicksort(gem_list, low_index, high_index):

        if len(gem_list) == 1:
            return gem_list
        if low_index < high_index:
            median = GemManager._get_best_carat(gem_list, low_index, high_index)
            gem_list[median], gem_list[high_index] = gem_list[high_index], gem_list[median]
            algo_analysis.quicksort_swap_counter += 1
            carat_index = GemManager._partition(gem_list, low_index, high_index)
            GemManager.sort_carats_amount_asc_quicksort(gem_list, low_index, carat_index - 1)
            GemManager.sort_carats_amount_asc_quicksort(gem_list, carat_index + 1, high_index)

    @staticmethod
    def _partition(gem_list, low_index, high_index):

        carat = gem_list[high_index].carats_amount
        border = low_index - 1
        for iterator in range(low_index, high_index):
            if gem_list[iterator].carats_amount <= carat:
                algo_analysis.quicksort_comparison_counter += 1
                border += 1
                gem_list[border], gem_list[iterator] = gem_list[iterator], gem_list[border]
                algo_analysis.quicksort_swap_counter += 1
        gem_list[border + 1], gem_list[high_index] = gem_list[high_index], gem_list[border + 1]
        algo_analysis.quicksort_swap_counter += 1
        return border + 1

    @staticmethod
    def _get_best_carat(gem_list, low_index, high_index):

        middle_index = (low_index + high_index) // 2
        carat = high_index
        if gem_list[low_index].carats_amount < gem_list[middle_index].carats_amount < \
                gem_list[high_index].carats_amount:
            algo_analysis.quicksort_comparison_counter += 2
            carat = middle_index
        elif gem_list[low_index].carats_amount < gem_list[high_index].carats_amount:
            algo_analysis.quicksort_comparison_counter += 1
            carat = low_index
        return carat
