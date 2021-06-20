# Backend-Data-Engineer-Internship
# Assignment submission<br>

File location need to be edited and proper file location should be given where actual data is present where ever required in all python files.<br>

Steps for execution:<br>
     1. Run the convert_to_csv.py file<br>
     2. Run downsample.py file<br>
     3. Run Low_pass_filter.ipynb file<br>
     4. To perform cProfile use following code in command line prompt:<br>
            python -m cProfile -o output1.txt downsample.py<br>
            python -m cProfile -o output1.txt convert_to_csv.py<br>
     5. To read cProfile text file write the following code in python:<br>
         Code:<br>
              import pstats<br>
              p = pstats.Stats('output.txt')<br>
              p.sort_stats('cumulative').print_stats(10)
              
              
