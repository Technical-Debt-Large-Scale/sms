# Replication kit to SMS 

The replication kit is essential to reproduce all steps in a Systematic Mapping Study. 

# Dataset

The dataset organize all studies used in this case. We created a spreadsheet to group the selected papers with all critical characteristics evaluated in this SMS.

The spreadsheet is available on [Extraction_form](https://github.com/Technical-Debt-Large-Scale/sms/blob/master/dataset/Extraction_form_basic.xlsx)

# Systematic Mapping Process

The main activities of this SMS follow five main phases: 

 - Define research questions 
 - Search process 
 - Selection process 
 - Extraction process 
 - Analysis process

Figure 1 ![SMS Process](https://github.com/Technical-Debt-Large-Scale/sms/blob/master/images/sms-process.png) show the flow used in this SMS

We used the following [Form](https://github.com/Technical-Debt-Large-Scale/sms/blob/master/md/mytable_extract_data_eg.md) | [Script](https://github.com/Technical-Debt-Large-Scale/sms/blob/master/python/auxiliary/Convert_tables_to_latex_form.ipynb) to extract and analyze the data from the spreadsheet. 

# Scripts used to analyse the dataset

## Publications and Venue Types

[Selected Papers](https://github.com/Technical-Debt-Large-Scale/sms/blob/master/md/mytable_papers.md) | [Venues](https://github.com/Technical-Debt-Large-Scale/sms/blob/master/md/mytable_venues.md)

The following scripts [Selected papers](https://github.com/Technical-Debt-Large-Scale/sms/blob/master/python/auxiliary/Convert_tables_to_latex_sps.ipynb) and [sms_extraction](https://github.com/Technical-Debt-Large-Scale/sms/blob/master/python/analyses/sms_extraction.ipynb) is used to generate results about publications and venue types. 

## Research type of publication - according to Wieringa et al. (2006)

[Research types](https://github.com/Technical-Debt-Large-Scale/sms/blob/master/md/mytable_q7_distribution_detailed.md)

The following script  [Research type](https://github.com/Technical-Debt-Large-Scale/sms/blob/master/python/auxiliary/Convert_tables_to_latex_rs_type.ipynb) is used to generate results about research type classification. 

## RQ1 - Type of Architectural Technical Debt

[ATD Types](https://github.com/Technical-Debt-Large-Scale/sms/blob/master/md/mytable_q1_updated.md) | [ATD Types before findings](https://github.com/Technical-Debt-Large-Scale/sms/blob/master/md/mytable_q1.md)

The following script [ATD types](https://github.com/Technical-Debt-Large-Scale/sms/blob/master/python/auxiliary/Convert_tables_to_latex_q1.ipynb) is used to generate results about ATD's type classification. 

## RQ2 - Measurement of ATD

[Measurement](https://github.com/Technical-Debt-Large-Scale/sms/blob/master/md/mytable_q2_distribution_detailed.md) 

The following script [Measurement](https://github.com/Technical-Debt-Large-Scale/sms/blob/master/python/auxiliary/Convert_tables_to_latex_q2.ipynb)  is used to generate results about ATD's measurement classification. 

## RQ3 - Monitoring of ATD

[Monitoring](https://github.com/Technical-Debt-Large-Scale/sms/blob/master/md/mytable_q3_distribution_detailed.md) 

The following script [Monitoring](https://github.com/Technical-Debt-Large-Scale/sms/blob/master/python/auxiliary/Convert_tables_to_latex_q4.ipynb)  is used to generate results about ATD's monitoring classification. 

## RQ4 - Tools and Methods to Identify ATD

[Tools](https://github.com/Technical-Debt-Large-Scale/sms/blob/master/md/mytable_q4_tools_and_other_distribution_detailed.md) | [Tools with more features](https://github.com/Technical-Debt-Large-Scale/sms/blob/master/md/mytable_q4_tools_and_other_distribution_detailed_new_features.md) | [Methods](https://github.com/Technical-Debt-Large-Scale/sms/blob/master/md/mytable_q4_methods_detailed.md) | [Methods and SPs](https://github.com/Technical-Debt-Large-Scale/sms/blob/master/md/mytable_q4_methods_detailed_with_sp.md)

The following scripts [Tools and Methods](https://github.com/Technical-Debt-Large-Scale/sms/blob/master/python/auxiliary/Convert_tables_to_latex_q4.ipynb) are used to generate ATD's tools and ATD's method classification results. 

WordCloud of methods [methods](https://github.com/Technical-Debt-Large-Scale/sms/blob/master/images/atdmethods.png)

## RQ5 - Calculate the Cost of ATD item

[Calculate cost of ATD](https://github.com/Technical-Debt-Large-Scale/sms/blob/master/md/mytable_q5_distribution_detailed.md) 

The following script [Cost of ATD](https://github.com/Technical-Debt-Large-Scale/sms/blob/master/python/auxiliary/Convert_tables_to_latex_q5.ipynb) is used to generate results about how to calculate ATD item cost
