# constants.py
# Kordel France
########################################################################################################################
# This file contains the specification for which file sizes, file types, and sorting algorithms should be used for
#    analysis. These act as hyperparameters that may be edited to add / delete an analysis parameter.
########################################################################################################################

# sorting file sizes
# file_sizes = [50, 500, 1000, 2000, 5000, 10000]
file_sizes = [50, 500, 1000, 1500, 2000]
# sorting file distribution types
file_types = ['sorted',
              'reverse_sorted',
              'random']
# sorting algorithms
sort_algos = ['quicksort', 'quicksort_rand', 'quicksort_mot', 'natural merge sort', '2-way merge sort', '3-way merge sort', 'heap sort']


req_input_sorted = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50]
req_input_revsorted = [50,49,48,47,46,45,44,43,42,41,40,39,38,37,36,35,34,33,32,31,30,29,28,27,26,25,24,23,22,21,20,19,18,17,16,15,14,13,12,11,10,9,8,7,6,5,4,3,2,1]
req_input_random = [48,35,22,7,16,32,39,44,43,45,4,49,28,50,33,23,15,11,19,40,29,8,36,24,46,1,21,14,42,38,9,25,12,13,30,37,31,6,41,34,5,10,17,47,3,20,27,18,26,2]
