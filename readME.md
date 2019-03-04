### Dependancy MacOS:
brew install graphviz
### Dependancy Ubuntu:
  sudo apt-get install graphviz

## Task

To build parts of the tool that will orchestrate the aforementioned process, in order to create the `final.products` table:


1. Created a file which implements functionality of parsing all files and creates edges for the directed acyclic graph. Topological sort is implemented which gives one of the possible orders in which all files must be visited in-order. Graph for dependancy is generated in a new directory `Output`. 

For giving a better visual representation `graphviz` has been used :
pip install graphviz

The user can refer to the `.pdf` file generated to visualize the dependencies.

2. Write a function that, using the previous question, runs the sql scripts in the correct order and paralleizes the execution.
Use Apache Spark 2.x for parallelizing the execution of the sql scripts.

### Apache Spark:
Apache Spark is an open-source distributed general-purpose cluster-computing framework. Originally developed at the University of California, Berkeley's AMPLab, the Spark codebase was later donated to the Apache Software Foundation, which has maintained it since.

https://spark.apache.org/

a) The empty datasets in the `raw` folder are given a schema to be used at the time of creating dataframe.
b) All the files in `raw` folder are used to create dataframes with a suffix `raw_[DATASET_NAME]`.
c) Modified the contents of the `.sql` files to be compatible with the sparksql standards.
d) The ordered list/dag calculated in the step 1 is passed as a list to the spark_execute.py file. The code then creates a table for each `.sql` files under `tmp` with the suffix `tmp_[FILE_NAME]. For the Sql scripts dependent on the `raw_` as well as `tmp_` tables the ordered list passed from test.py makes sure these sql scripts are executed after the parent scripts have been executed.
e) At last the `final/products.sql` is called with creates a table with name `final_products`. 
f) The user can query this final table for end result.
