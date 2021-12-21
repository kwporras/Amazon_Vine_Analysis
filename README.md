# Amazon_Vine_Analysis
## Overview of the analysis
We've chosen a dataset containing amazon reviews of digital video games. The goal is to review the specifics of each product the use PySpark to perform the ETL process. After the ETL process, we will connect to an AWS RDS instance to load and transformed data into pgAdmin. After the dataset has been loaded into pgAdmin we used PySpark to determine if there is any bias toward favorable reviews from Vine members in your dataset. This process will serve as a repeatable example which we can run to create a database in pgAdmin and analysis in PySpark for any of the ~50 other [available amazon datasets](https://s3.amazonaws.com/amazon-reviews-pds/tsv/index.txt)


## Results
#### Vine review count (paid)
![alt_text](https://github.com/kwporras/Amazon_Vine_Analysis/blob/ca368f88df4fc60e34a17e7df2120471a5c0f7a4/Resources/paid_review_total_count.PNG)
#### Non-Vine review count (unpaid)
![alt_text](https://github.com/kwporras/Amazon_Vine_Analysis/blob/ca368f88df4fc60e34a17e7df2120471a5c0f7a4/Resources/unpaid_review_total_count.PNG)
#### 5-star Vine review count (paid)
![alt_text](https://github.com/kwporras/Amazon_Vine_Analysis/blob/ca368f88df4fc60e34a17e7df2120471a5c0f7a4/Resources/paid_review_five_star_count.PNG)
#### 5-star non-Vine review count (unpaid)
![alt_text](https://github.com/kwporras/Amazon_Vine_Analysis/blob/ca368f88df4fc60e34a17e7df2120471a5c0f7a4/Resources/unpaid_review_five_star_count.PNG)
#### Percentage of 5-star Vine reviews (paid)
![alt_text](https://github.com/kwporras/Amazon_Vine_Analysis/blob/ca368f88df4fc60e34a17e7df2120471a5c0f7a4/Resources/paid_review_percentage_five_star_count.PNG)
#### Percentage of 5-star non-Vine reviews (unpaid)
![alt_text](https://github.com/kwporras/Amazon_Vine_Analysis/blob/ca368f88df4fc60e34a17e7df2120471a5c0f7a4/Resources/unpaid_review_percentage_five_star_count.PNG)

## Summary
There is not potential for bias in the Vine program reviews in this example by coincidence. After reviewing the entirety of the original database without any filters there were zero Vine reviews. The question of bias is not applicable in this situation. 
![alt_text](https://github.com/kwporras/Amazon_Vine_Analysis/blob/255cddc1de630c3042d8ad4b0d469160822a0666/Resources/df_tests_for_vine.PNG)

