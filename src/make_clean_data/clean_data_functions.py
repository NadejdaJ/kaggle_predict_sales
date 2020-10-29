"""
=========================================
Project: Predict Future Sales - Kaggle
=========================================
Script: clean_data_functions.py

Purpose: functions required for data cleaning

Creation date: 27/10/2020
Contact: Nadejda Jaeverberg
Email address: nadejda@kth.se
"""

from src.setup.config import *


def remove_refunds(df, col):
    """
    Removing refunds and only keeping sales
    :param df: pandas dataframe
    :param col: column name
    :return: dataframe with refunds removed
    """
    return df[df[col] >= 0].reset_index(drop=True)


def get_quartiles(df, col):
    """
    Getting lower and upper quartiles for values in column col
    :param df: pandas dataframe
    :param col: column name
    :return: lower and upper quartiles
    """
    df_q1 = df[col].quantile([0.25]).reset_index()[col].values[0]
    df_q3 = df[col].quantile([0.75]).reset_index()[col].values[0]
    return df_q1, df_q3


def remove_outliers(df):
    """
    Using upper borders from config.
    :param df: pandas dataframe
    :return: pandas dataframe with outliers removed
    """
    # Remove refunds
    df = remove_refunds(df, COLUMN_NAMES["item_price"])
    df = remove_refunds(df, COLUMN_NAMES["item_cnt_day"])

    # Remove outliers
    df = df[df[COLUMN_NAMES["item_price"]] <= max_item_price].reset_index(drop=True)
    df = df[df[COLUMN_NAMES["item_cnt_day"]] <= max_item_count].reset_index(drop=True)
    return df


def groupings(row):
    if "Игры" in row:
        return "games"
    elif "Карты оплаты" in row:
        return "payment_card"
    elif "Кино" in row:
        return "movies"
    elif "Книги" in row:
        return "books"
    elif "Музыка" in row:
        return "music"
    elif "Подарки" in row:
        return "gifts"
    elif "Программы" in row:
        return "programs"
    elif "Служебные" in row:
        return "service"
    elif "Чистые носители" in row:
        return "storage"
    elif "Игровые" in row:
        return "consoles"
    elif "Аксессуары" in row:
        return "accessories"
    else:
        return row


def group_item_categories(df_item_categories):
    """
    Applying categories to overarching categories
    :param df_item_categories: pandas dataframe with item categories
    :return: pandas dataframe with new groupings
    """
    # Group categories into larger groups
    df_item_categories[COLUMN_NAMES["item_category_name"]] = \
        df_item_categories[COLUMN_NAMES["item_category_name"]].apply(groupings)

    # Rename old category id column
    df_item_categories.rename(columns={COLUMN_NAMES["item_category_id"]: "original_category_id"},
                              inplace=True)

    # Define new category groups
    new_categories = list(df_item_categories[COLUMN_NAMES["item_category_name"]].unique())

    # Create a mapping dictionary for new categories
    new_ids_mappings = {new_categories[i]: i for i in range(len(new_categories))}

    # Map the new categores to new codes
    df_item_categories[COLUMN_NAMES["item_category_id"]] = \
        df_item_categories[COLUMN_NAMES["item_category_name"]].map(new_ids_mappings)
    return df_item_categories


def update_items_with_new_categories(df_items, df_categories):
    """
    Merge in new categories to the items dataframe
    :param df_items: dataframe with items
    :param df_categories: dataframe with item categories
    :return: updated dataframe
    """
    df = df_items.merge(df_categories, left_on=COLUMN_NAMES["item_category_id"],
                        right_on="original_category_id", how="left")
    df.rename(columns={COLUMN_NAMES["item_category_id"]+"_y": COLUMN_NAMES["item_category_id"]},
              inplace=True)
    return df[[COLUMN_NAMES["item_name"], COLUMN_NAMES["item_id"],
               COLUMN_NAMES["item_category_name"], COLUMN_NAMES["item_category_id"]]]
