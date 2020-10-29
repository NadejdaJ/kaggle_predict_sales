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
print(items)
