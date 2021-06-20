# Backend-Data-Engineer-Internship
# Assignment submission

File location need to be edited and proper file location should be given where actual data is present where ever required in all python files.

Steps for execution:<br>
     1. Run the convert_to_csv.py file
     2. Run downsample.py file
     3. Run Low_pass_filter.ipynb file
     4. To perform cProfile use following code in command line prompt:
            python -m cProfile -o output1.txt downsample.py
            python -m cProfile -o output1.txt convert_to_csv.py
     5. To read cProfile text file write the following code in python:
         Code:
              import pstats
              p = pstats.Stats('output.txt')
              p.sort_stats('cumulative').print_stats(10)
              
              
