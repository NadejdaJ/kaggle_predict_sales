"""
=========================================
Project: Predict Future Sales - Kaggle
=========================================
Script: run_make_features.py

Purpose: running make features script for extracting features

Creation date: 7/12/2020
Contact: Nadejda Jaeverberg
Email address: nadejda@kth.se
"""

from src.make_features.make_features_functions import *
import matplotlib.pyplot as plt

# ===============================================================
# Read in cleaned data
# ===============================================================
items = pd.read_csv(interim_data_path + interim_items_name)
item_categories = pd.read_csv(interim_data_path + interim_item_categories_name)
shops = pd.read_csv(interim_data_path + interim_shops_name)
train = pd.read_csv(interim_data_path + interim_sales_train_name)

print("\nFinished reading in raw data.")

# ===============================================================
# Extract features from date column in train dataset
# ===============================================================
train["date"] = pd.to_datetime(train["date"], format="%d.%m.%Y")
train["dayofweek"] = train["date"].dt.dayofweek
train["month"] = train["date"].dt.month
train["year"] = train["date"].dt.year
print(train)

# Consider median price

# Assemble shop_id, item_id dataframe
all_shop_ids = list(shops[COLUMN_NAMES["shop_id"]].unique())
all_item_ids = list(items[COLUMN_NAMES["item_id"]].unique())

# Make the shop_id, item_id dataframe
df = prepare_df(all_shop_ids, all_item_ids)

print(df.shape)
print(df.groupby("shop_id")["item_id"].count())
print(df[df["shop_id"] == 0])
