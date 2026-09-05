# PersonalStockScreener
Pulls 10+ years of data from SEC and other international sources. Uses query and filters to present data in a more precise and custom format than free stock screeners.

## Generate ticker JSON
Takes CLI input to create a JSON file with every ticker sorted by their main exchange.

## Fetch company data
Reads tickers from JSON file
For USA exchanges, requests data from the SEC.
For foreign exchanges, data is requested from OpenBB.
Raw data is taken from the request and stored in a JSON file unique to every company.

## Filter data
Each company will have its data processed into common metrics. The metrics will be stored as a row in a .csv file.
Metrics will be analyzed algorithmically to determine strength of company and its category.
A configuration file will allow the filter to be easily modified.
Once companies are put into one of more categories, each category will be returned as a .csv file. 
The columns of each .csv will be metrics from the company, relevant to the category.
