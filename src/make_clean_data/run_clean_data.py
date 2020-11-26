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

# ===============================================================
# Remove outliers
# ===============================================================
train_wo_outliers = remove_outliers(raw_train)

# ===============================================================
# Group item categories to larger groups
# ===============================================================
item_categories = group_item_categories(raw_item_categories)
items = update_items_with_new_categories(raw_items, item_categories)

# Add outdated tag to items
item_sales_overtime = \
    train_wo_outliers[train_wo_outliers["item_cnt_day"] >
                      0].groupby(["date_block_num", "item_id"])["item_cnt_day"].sum().reset_index()
print(item_sales_overtime)

# If no item sales in the last 6 months then mark item as "outdated"
sold = item_sales_overtime[item_sales_overtime["date_block_num"] >= 27]["item_id"].unique()

train_wo_outliers["outdated"] = False
train_wo_outliers.loc[~train_wo_outliers["item_id"].isin(sold), "outdated"] = True
print(train_wo_outliers)
print(train_wo_outliers.describe())

# If no sales in shop in the last 6 months then mark shop as "closed"
open_shops = \
    train_wo_outliers[train_wo_outliers["item_cnt_day"] >
                      0].groupby(["date_block_num", "shop_id"])["item_cnt_day"].sum().reset_index()

open_shops = open_shops[open_shops["date_block_num"] >= 27]["shop_id"].unique()
print(len(open_shops))

train_wo_outliers["shop_open"] = False
train_wo_outliers.loc[train_wo_outliers["shop_id"].isin(open_shops), "shop_open"] = True
print(train_wo_outliers)

# Combine
