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
base_path = os.path.dirname(os.path.abspath(__file__))
base_path = base_path.split("src")[0]

raw_data_path = base_path + "data/raw/"
interim_data_path = base_path + "data/interim/"
processed_data_path = base_path + "data/processed/"
model_path = base_path + "data/model/"

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
    "shop_name": "shop_name",
    "city_name": "city_name",
}
# ===============================================================
# Outliers from data exploration
# ===============================================================
max_item_price = 2124  # Q1 = 249.0    Q3 = 999.0   k = 1.5
max_item_count = 650  # Q1 = 1   Q3 = 1   k = 1.5
rare_cutoff = 1e-4

# ===============================================================
# Grouping categories
# ===============================================================
groups_dict = {"Игры": "games",
               "Карты оплаты": "payment_card",
               "Кино": "movies",
               "Книги": "books",
               "Музыка": "music",
               "Подарки": "gifts",
               "Программы": "programs",
               "Служебные": "service",
               "Чистые носители": "storage",
               "Игровые": "consoles",
               "Аксессуары": "accessories"}

# ===============================================================
# Definition of recent! How many months without sales mean that product is outdated?
# ===============================================================
delta_months = 6

# ===============================================================
# Grouping cities
# ===============================================================
geo_cities = {
    "Балашиха": "moscow",
    "Волжский": "vologda",
    "Вологда": "vologda",
    "Якутск": "yakutsk",
    "Адыгея": "adygeya",
    "Воронеж": "voronezh",
    "Выездная": "unknown",
    "Жуковский": "moscow",
    "Интернет-магазин": "online",
    "Казань": "kazan",
    "Калуга": "kaluga",
    "Коломна": "moscow",
    "Красноярск": "krasnoyarsk",
    "Курск": "kursk",
    "Москва": "moscow",
    "Мытищи": "moscow",
    "ННовгород": "novgorod",
    "Новосибирск": "novosibirsk",
    "Омск": "omsk",
    "РостовНаДону": "rostovnadonu",
    "СПб": "stpetersburg",
    "Самара": "samara",
    "Сергиев": "moscow",
    "Сургут": "surgut",
    "Томск": "tomsk",
    "Тюмень": "tumen",
    "Уфа": "ufa",
    "Химки": "moscow",
    "Цифровой": "online",
    "Чехов": "moscow",
    "Ярославль": "yaroslavl"
}
