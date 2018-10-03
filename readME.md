# Data Warehouse Architect Position at Sephora SEA

You can write your code in the language of your choice. But we have preferences for the language of our stack:

- Go (Highly recommended)
- Python
- NodeJS

Please organise, document and write some tests.
Please also inform on any specific setup which is required to make your code run.

## Context

At Sephora SEA, we are building business schemas on top of the e-commerce databases.
For instance, we have a __products__ table which is a consolidation of 30 other tables.
It contains information for each of our products (ids, descriptions, categories...).

Our tables are organised in datasets (folders), _eg._ `final`, `raw`, `tmp`

This clean schema is created from a bunch of dependent SQL scripts which execution is the following:

1. Pull tables from the e-commerce databases and are push the exact copies to a raw dataset (`raw` folder)
2. Clean and consolidate the data on top of these raw tables using SQL scripts stored in the `tmp` folder. For instance, the result of the `tmp/inventory_items.sql` script will be stored in the `tmp/inventory_items` table.
3. Create the final products table (from the `final/products.sql` script)

## Your task

Your task is to code the aforementioned process, for the `final/products` table:

1. Write a clean structure (from scratch, no external library!) that shows the dependencies between all the sql scripts
2. How would you run the scripts in order? Code it and test it

*Going further, we would like to parallelize the execution of few of these scripts. If you think of the dependencies as a tree: scripts from different nodes can work simultaneously, but, still, must not be executed before its children's tasks are done.*

3. If you had to parallelize these tasks' executions, how would you do that?
4. Apply on your structure, and test it

*Sample of task function (in js):

```js
function tmp_inventory_items (callback){
    // This is execution time of the tmp.inventory_items script
    setTimeout(callback, parseInt(1000 * Math.random()));
}
```
