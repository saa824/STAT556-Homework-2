# STAT556-Homework-2
# External Data, Visualization & Modular Code
A Repository for STA556 Homework 2 for Samuel Anoff Addo

## Purpose
This project builds a small, reproducible data-analysis pipeline for ExpressMart retail sales data. It reads an external CSV file, cleans it with reusable functions, answers questions about where, when and what customers buy, and shows the findings in figures.

## Data source
1. **Dataset:** ExpressMart retail sales data, where each row is one product on one order
2. **Source:** Only quality data, ExpressMart
3. **Format:** CSV, stored at `data/raw/expressmart_orders.csv`
4. **Size:** 185,950 rows and 8 columns: Order ID, Product, Quantity Ordered, Price Each, Order Date, Purchase Address, Time, Sales
4. **Period:** 2019 after cleaning


## Project structure
```
README.md                         project description and how to run
requirements.txt                  packages needed to run the notebooks
data/raw/         original data, never edited - ExpressMartData.TOT.csv
data/processed/   cleaned data written by notebook 01 - ExpressMart_processed.csv
src/              reusable functions (clean.py, summaries.py, validate.py)
notebooks/
  01_Read_Cleaning.ipynb          reading, inspection and cleaning (Parts 1 & 2)
  02_Exploratory_Analysis.ipynb   summaries and data questions (Part 3)
  03_Visualization.ipynb          figures and captions (Part 4)
figures/          saved figures
```


## How to Run This project
1. Clone this repository.
2. Install the packages: `pip install -r requirements.txt` in the terminal
3. Open the notebooks and run them **from inside the `notebooks/` folder** (the paths are relative to it).
- Run `notebooks/01_Read_Cleaning.ipynb` first. It inspects the raw data, cleans the raw data and saves `data/processed/ExpressMart_processed.csv` (Part 1 & 2).
- Run `notebooks/02_Exploratory_Analysis.ipynb` second. It reads the processed file and answers the data questions with summaries (Part 3).
- Run `notebooks/03_Visualization.ipynb` third. It reads the processed file, make visualizations about the data questions and answers to make the summary more informative and saves the figures to `figures/` (Part 4).


## Cleaning steps
The functions are in `src/clean.py`, and each one returns a new table without changing its input.
1. `clean_column_names()`: Changes column names containing spaces and capital letters to lowercase names and no space
2. `parse_order_datetime()`: Converts the serial date and time fraction into a timestamp, and adds `month` and `hour`.
3. `filter_year()`: Keeps only 2019 observations. This removes 34 orders from 1 January 2020. Since the analysis is from January 1, 2029 to December 31, 2019.
4. `add_location()`: Rarses city and state from the purchase address. I use a combined `city_state` column because Portland, Oregon and Portland, Maine are different cities that share a name.
5. `drop_exact_duplicates()`: Removes 264 rows duplicates in every column, which look like the same line entered twice. Repeated Order IDs are kept, because one order can contain several products.
6.  `clean_raw_data`: runs all the steps in order

`src/validate.py` checks the result (no missing values, sales equal quantity times price, 19 products, 10 locations, all dates in 2019). The final data has 185,652 rows.

`src/summaries.py` has two summary functions:
- `summarize_group(data, group_col)` returns, for each value of a column, `purchases` (rows), `quantity_sold` (items), `total_sales` (dollars), `avg_sale` (dollars per purchase) and `percentage_of_total_sales` (as a decimal).
- `summarize_numeric(data, column)` returns the mean, median, minimum and maximum of a numeric column, such as `sales` or `price_each`.


## Main finding
The products that sell the most items are not the products that earn the most money. Cheap accessories lead in quantity sold thus AAA Batteries sold 30,981 items but brought in only about $93,000. Expensive electronics lead in total salesthus the Macbook Pro Laptop sold     4,724 items and brought in about $8.03 million. Across the 19 products, price and quantity sold have a correlation of about -0.60. Peak sales period around noon and 7 pm and are lowest around 3 am.

Other findings:
1. San Francisco was the city with has highest total_sales (23.9% of the total sales) and Portland, ME the lowest (1.3% of the total sales). The average sale is about the same in every city, so the differences come from the number of quantity sold.
2. Sales are skewed: the median purchase is $14.95 and the mean is $185.60.

## Suggestions for the store

### Products
The products with the highest quantity sold (batteries, charging cables and headphones) are cheap and bought often, so the store should make sure they are always in stock and easy to find to bring people into the shop. Customers who come for these items may also see the high-total sales products, such as laptops, phones and monitors, displayed nearby, and some may decide to buy them as well.

### Time of day
Sale peak period maybe explained by customers' daily routines, such as lunchtime shopping and increased activity in the early evening. Based on these findings, the store could schedule additional staff during the peak hours around noon and early evening to serve customers more efficiently. It could also introduce targeted promotions during these periods to maximize sales, while using the quieter hours to manage staffing and other operational activities more effectively.