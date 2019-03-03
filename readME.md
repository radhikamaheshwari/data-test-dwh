### Dependancy MacOS:
brew install graphviz
### Dependancy Ubuntu:
  sudo apt-get install graphviz

## Task

To build parts of the tool that will orchestrate the aforementioned process, in order to create the `final.products` table:


1. Created a file which implements functionality of parsing all files and creates edges for the directed acyclic graph. Topological sort is implemented which gives one of the possible orders in which all files must be visited in-order.

For giving a better visual representation `graphviz` has been used :
pip install graphviz


2. Write a function that, using the previous question, runs the sql scripts in the correct order. Please provide documentation as of how you are proceeding.

*Going further, we would like to parallelize the execution of few of these scripts. If you think of the dependencies as a tree: scripts from different nodes can work simultaneously, but, still, must not be executed before its children's tasks are done.*

3. Write a function that paralellizes the execution of the SQL scripts, ensuring they respect their dependencies. Please provide documentation as of how you are proceeding. 
