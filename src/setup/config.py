"""
=========================================
Project: Predict Future Sales - Kaggle
=========================================
Script: config.py

Purpose: definitions and paths necessary for running the pipeline

Creation date: 27/10/2020
Contact: Nadejda Jaeverberg
Email address: nadejda@kth.se
"""
import pandas as pd
import os

# ===============================================================
# Defining paths
# ===============================================================
raw_data_path = "./data/raw/"
interim_data_path = "./data/interim/"
processed_data_path = "./data/processed/"
model_path = "./data/model/"

# ===============================================================
# Defining filenames
# ===============================================================
raw_item_categories_name = "item_categories.csv"
raw_items_name = "items.csv"
raw_sales_train_name = "sales_train.csv"
raw_shops_name = "shops.csv"
raw_test_name = "test.csv"

# ===============================================================
# Outliers from data exploration
# ===============================================================
COLUMN_NAMES = {
    "shop_id": "shop_id",
    "item_id": "item_id",
    "item_price": "item_price",
    "item_cnt_day": "item_cnt_day",
    "date_block_num": "date_block_num",
    "item_category_id": "item_category_id",
    "item_category_name": "item_category_name",
    "item_name": "item_name",
    "date": "date",
    "shop_name": "shop_name"
}
# ===============================================================
# Outliers from data exploration
# ===============================================================
max_item_price = 2124  # Q1 = 249.0    Q3 = 999.0   k = 1.5
max_item_count = 650  # Q1 = 1   Q3 = 1   k = 1.5
