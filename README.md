# FranceLab 2 - Kordel K. France

This project was constructed for the Foundations of Algorithms course, 605.621 section 83, instructed by Dr. Eleanor Chlan at Johns
Hopkins University. The project performs an analysis of different sorting algorithms under different conditions and 
shows how performance changes between algorithms.

**Quick Look**
- Each of 3 quicksort sorting algorithms (vanilla quicksort, randomized quicksort, and MOT quicksort) is evaluated 
 against 4 other sorting algorithms (natural merge sort, 2-way merge sort, 3-way merge sort, and heap sort) and performed over
 6 different file sizes (50, 500, 1000, 1500, 2000) and 3 different data types (sorted, reverse-sorted, and randomized)
 for a total of 5 * 7 * 3 = 105 total runs.
- The file `Metric.py` contains an object that stores details and performance characteristics about each run. Think of
one `Metric` object as one run.
- The file `file_manager.py` contains functions that generate all of the data files automatically.
- The file `constants.py` contains all of the sorting parameters - file sizes, sorting algorithms, and data types as 
defined in the assignment requirements.
- Each of the 7 sorting algorithms contains its own file. Each of the sorting algorithms uses recursion, not iteration.


***Note to Graders:*** For the required output files, I figured it was easier to open and read a `.csv` file of the data run
instead of analyzing it from the console. Files are named as `{algorithm_name}-{date_type}-{n}count.csv` such that the
50-count sorted data file with the randomized quicksort algorithm is named as `quicksort_rand-sorted_50count.csv`. Hopefully 
this is easier; reading from the console seemed like a nightmare.

Required input files are hard coded in `constants.py` and saved as `{algorithm_name}-{data_type}-50count.csv`.


## Running FranceLab2
1. **Ensure Python 3.7 is installed on your computer.**

2. **Navigate to the Lab2 directory.** For example, `cd User\Documents\PythonProjects\Lab2`.
Do NOT `cd` into the `Lab2` module.

3. **Run the program as a module: `python -m Lab2 -h`.** This will print the help message.

4. **Run the program as a module (with no inputs): `python -m Lab2`.** All data is automatically generated; there is no 
need to pass in any inputs / arguments.

5. **Monitor the program as it performs the analysis.** The program will output a status and metrics to the screen as 
computation is performed.

6. **Plots of all of the data runs will appear.** Once sorting is completed, the program displays the numbers of comparisons
 and exchanges of each sorting algorithm through line graphs. Do dismiss the plot and move to the next plot, simply 
 enter any key into the command prompt. One plot for each of the 3 data types will appear.

7. **View the Summary Table and Output Files.** A summary table illustrating the performance of all 72 runs is presented
on the screen. An output file of each sorting run can be found in the `output_files` directory. Each of these 72 files 
contains the following details: 
    1) the data type
    2) file count
    3) sorting algorithm name
    4) number of comparisons performed
    5) number of exchanges performed
    6) an equation that plots the trajectory of the number of comparisons made by the algorithm over this data type as
     `n` scales along with the correlation coefficient between the equation and the observed data.
    7)  an equation that plots the trajectory of the number of exchanges made by the algorithm over this data type as
     `n` scales along with the correlation coefficient between the equation and the observed data.
    8) the initial dataset for each run **before** it entered the sorting algorithm
    9) the final dataset for each run **after** it entered the sorting algorithm and was fully sorted
    10) the execution time (in seconds) for the algorithm to completely sort the data

8. **Open `output_files/FINAL_ANALYSIS.csv`.** This file contains a direct copy of the `Summary` table in the output but
as an archived `.csv` file.

### FranceLab2 Usage

```commandline
usage: python -m Lab2

positional arguments:
  none

optional arguments:
  none
```
Copy the output below and paste into the command line as a quick start:
```buildoutcfg
python -m Lab2
```

### Project Layout

Here is how the project is structured and organized.

* FranceLab2: `The parent folder of the project. This should be the last subdirectory you navigate to to run the
project.`
    * README.md:
      `A guide on what the project does, how to run the project.`
      
    * Lab2: 
      `This is the module of the entire program package. It is not a directory. Do not navigate into it.`
      
      * __init__.py 
        `As the name suggests, this file initializes the program and gives access to the algorithms capabilities
        to other programs.`
        
      * __main__.py 
        `This file contains the driver code for the sorting complexity analysis program. All other files may be viewed 
        as helpers that are pooled together here for use.`
        
      * **file_manager.py** 
        `This file provides public-accessible functions to generate a sorted, reverse-sorted, or random data stream. 
        Each function returns an array of it's designated sorting distribution. Let it be emphasized that all data is 
        automatically generated. This file ontains the circular singly linked list where each node represents a 
        polynomial term.`

      * **constants.py**
        `This file contains the specification for which file sizes, file types, and sorting algorithms should be used for
        analysis. These act as hyperparameters that may be edited to add / delete an analysis parameter.`

      * **graph_data.py**
        `This file provides functions to categorize, filter, graph, and save analyzed sorting data.
        The data is first categorized by data type and algorithm, then graphed and saved, and finally summarized.
`
      * **Metric.py**
        `This file provides functions to categorize, filter, graph, and save analyzed sorting data.
        The data is first categorized by data type and algorithm, then graphed and saved, and finally summarized.`

      * **quicksort.py**
        `This file provides functions to sort an array of integers in ascending order using original quicksort.`

      * **quicksort_mot.py**
        `This file provides functions to sort an array of integers in ascending order using quicksort with median-of-three
        partitioning.`

      * **quicksort_randomized.py**
        `This file provides functions to sort an array of integers in ascending order using quicksort with randomized
        partitioning.`

      * **heap_sort.py**
        `This file provides functions to construct a heap from a passed array (list) argument and sort it in ascending 
        order.`

      * **merge_sort_2way.py**
        `This file provides functions to sort an array of integers in ascending order using a two-way merge sort.`

      * **merge_sort_3way.py**
        `This file provides functions to sort an array of integers in ascending order using a three-way merge sort.`

      * **merge_sort_4way.py**
        `This file provides functions to sort an array of integers in ascending order using a four-way merge sort. It is
        not complete nor fully tested. It was made as an attempt for an enhancement.`

      * **merge_sort_natural.py**
        `This file provides functions to sort an array of integers in ascending order using the natural merge sort 
        algorithm.`


###Enhancements
   There are several enhancements for this project. The analysis document has a more comprehensive list, but here are
   highlights for a few:
   
   * Time Delays - processing is paused briefly throughout the program to allow the user time to read and interpret the
   output. This creates for a much better user experience.
   
   * An additional count of `10,000` was added to provide additional insight into algorithm performance.
   
   * Execution time is tracked and monitored for each sorting algorithm.
   
   * Each sorting run is graphed in a `.csv` file. Files are named {algorithm_name}-{date_type}-{n} count.csv such as 
   'quicksort_random_1000count.csv'. Each file is located in the `output_files` directory and contains the following 
   properties:
    
        1) the data type
        2) file count
        3) sorting algorithm name
        4) number of comparisons performed
        5) number of exchanges performed
        6) an equation that plots the trajectory of the number of comparisons made by the algorithm over this data type as
     `n` scales along with the correlation coefficient between the equation and the observed data.
        7)  an equation that plots the trajectory of the number of exchanges made by the algorithm over this data type as
     `n` scales along with the correlation coefficient between the equation and the observed data.
        8) the initial dataset for each run **before** it entered the sorting algorithm
        9) the final dataset for each run **after** it entered the sorting algorithm and was fully sorted
        10) the execution time (in seconds) for the algorithm to completely sort the data
    
   * A `Summary Table` is provided at the very end of the program that shows the performance of each algorithm over 
   different data distributions. A `FINAL_ANALYSIS.csv` file is a direct copy of the `Summary Table`, but in a `.csv`
   file that shows performance over all 72 sorting runs.
   
   * Equations for trajectory curves were calculated to extrapolate the number of comparisons \ exchanges  that would be 
   theoretically needed for very large `n` as the algorithm scales. This was accomplished by calculating coefficients of 
   power regression  to define the trajectory path based on the data gathered for similar sorts.
   If one opens `Metric.py` where the regression algorithms are located, they will notice the regression curve is 
   computed from scratch with no "packages" - the regression equation is derived from low-level statistics functions.
   The `numpy` package is only used to cast an array type to one of a type easier to manipulate with these statistics
   functions.
   
   * Correlation values are calculated (again from scratch and without any use of packages) to show how well the above
   regression curve fits the empirically gathered data in our analysis. More details on this reside in the 
   `FranceLab2_Analysis.docx` document.
   
   * A status is communicated to the user as a % complete in the `__main__.py` file while the data is being processed
   and sorted. This allows for a more appealing user interface and lets the user have an idea of where the program is at
   in its execution steps.
   
   * Plots of all of the data runs for each algorithm are shown and allowed for easy comparison against other algorithms. 
   This makes it simple for the user to spot analytical trends and spot which algorithms out-perform others on certain
   datasets.
   
   
   
###References
The following items were used as references for the construction of this project. 
1)	Cormen, T. H., & Leiserson, C. E. (2009). Introduction to Algorithms, 3rd edition.
 
2)	Miller, B. N., & Ranum, D. L. (2014). Problem solving with algorithms and data structures using Python (2nd ed.). Decorah, IA: Brad Miller, David Ranum

3)	Merge Sort. GeeksforGeeks. (2021, June 20). https://www.geeksforgeeks.org/merge-sort/.

4)	Rayapati, P. (2019, August 20). 3-Way merge sort. Retrieved April 25, 2021, from https://www.geeksforgeeks.org/3-way-merge-sort/.

5)	Woltmann, S. (2021, January 13). Merge sort – ALGORITHM, source code, time complexity. Retrieved April 24, 2021, from https://www.happycoders.eu/algorithms/merge-sort/#Natural_Merge_Sort.

6)	K-way merge algorithm. (2021, April 09). Retrieved April 24-27, 2021, from https://en.wikipedia.org/wiki/K-way_merge_algorithm

7)	Artificial Intelligence: A Modern Approach. Third Edition. Russel, Stuart J.; Norvig, Peter. 2015, Pearson India Education Services Pvt. Ltd. p 961-962.

8)	Deep Learning. Goodfellow, Ian; Bengio, Yoshua; Courville, Aaron. 2016, Massachusetts Institute of Technology. p 147 -149, 525 – 527.

9)	Garey, M. R., & Johnson, D. S. (2003). Computers and Intractability: A Guide to the Theory of NP - Completeness. W.H. Freeman and Co. 

10)	Kleinberg, J., & Tardos, É. (2014). Algorithm Design. Pearson India Education Services Pvt Ltd.
