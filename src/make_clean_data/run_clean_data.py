"""
=========================================
Project: Predict Future Sales - Kaggle
=========================================
Script: run_clean_data.py

Purpose: clean data to prepare to predict future sales

Creation date: 27/10/2020
Contact: Nadejda Jaeverberg
Email address: nadejda@kth.se
"""

from src.make_clean_data.clean_data_functions import *
import matplotlib.pyplot as plt
# ===============================================================
# Read in raw data
# ===============================================================
raw_items = pd.read_csv(raw_data_path + raw_items_name)
raw_item_categories = pd.read_csv(raw_data_path + raw_item_categories_name)
raw_shops = pd.read_csv(raw_data_path + raw_shops_name)
raw_train = pd.read_csv(raw_data_path + raw_sales_train_name)

print("\nFinished reading in raw data.")

# ===============================================================
# Remove outliers
# ===============================================================
train_wo_outliers = remove_outliers(raw_train)

print("\nOutliers were removed")

# ===============================================================
# Group item categories to larger groups
# ===============================================================
item_categories = group_item_categories(raw_item_categories)
items = update_items_with_new_categories(raw_items, item_categories)

print("\nCleaned items and re-grouped item categories")

# ===============================================================
# Marking outdated products, i.e. those that haven't been sold recently
# ===============================================================
# Add outdated tag to items
item_sales_overtime = \
    train_wo_outliers[train_wo_outliers["item_cnt_day"] >
                      0].groupby(["date_block_num", "item_id"])["item_cnt_day"].sum().reset_index()

# If no item sales in the last "delta_months" months then mark item as "outdated"
sold = item_sales_overtime[item_sales_overtime["date_block_num"] >=
                           train_wo_outliers["date_block_num"].max() - delta_months]["item_id"].unique()

# Tagging outdated items in the train dataset
train_wo_outliers["outdated"] = False
train_wo_outliers.loc[~train_wo_outliers["item_id"].isin(sold), "outdated"] = True

print("\nOutdated products were marked in the train dataset.")

# If no sales in shop in the last 6 months then mark shop as "closed"
# Find all shops that are still open, i.e. at least something was sold in the last 6 months
open_shops = \
    train_wo_outliers[train_wo_outliers["item_cnt_day"] >
                      0].groupby(["date_block_num", "shop_id"])["item_cnt_day"].sum().reset_index()

open_shops = open_shops[open_shops["date_block_num"] >=
                        train_wo_outliers["date_block_num"].max() - delta_months]["shop_id"].unique()

# Mark open shops in train dataset
train_wo_outliers["shop_open"] = False
train_wo_outliers.loc[train_wo_outliers["shop_id"].isin(open_shops), "shop_open"] = True

print("\nOpen shops were marked in the train dataset")

# ===============================================================
# Cleaning up shops dataframe
# ===============================================================
# Extract city names for
proc_shops = extract_city(raw_shops, COLUMN_NAMES["shop_name"])

print("\nProcessed shops dataset")

# ===============================================================
# Save clean results
# ===============================================================
# Save processed files into interim data folder
train_wo_outliers.to_csv(interim_data_path + interim_sales_train_name, index=False)
proc_shops.to_csv(interim_data_path + interim_shops_name, index=False)
items.to_csv(interim_data_path + interim_items_name, index=False)
item_categories.to_csv(interim_data_path + interim_item_categories_name, index=False)
