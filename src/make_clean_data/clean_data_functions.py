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
    keys = list(groups_dict.keys())
    found_match = [key for key in keys if key in row]

    if found_match:
        return groups_dict[found_match[0]]
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

    out = df[[COLUMN_NAMES["item_name"], COLUMN_NAMES["item_id"],
              COLUMN_NAMES["item_category_name"],
              COLUMN_NAMES["item_category_id"]]].drop_duplicates().reset_index(drop=True)
    return out


def extract_city(df, col):
    """
    This function extract city name from the shop name and maps it according to dictionary as defined in config
    :param df: raw shops dataframe
    :param col: column name for shop_name
    :return: processed dataframe with extracted city names
    """
    out = df.copy()
    out["tmp"] = df[col].str.strip().str.split(" ").str[0]
    out["tmp"].replace({r"[.,!?]+": ""}, inplace=True, regex=True)
    out[COLUMN_NAMES["city_name"]] = out["tmp"].map(geo_cities)
    out.loc[pd.isnull(out[COLUMN_NAMES["city_name"]]), "city_name"] = \
        out.loc[pd.isnull(out[COLUMN_NAMES["city_name"]])]["tmp"]
    out.drop("tmp", axis=1, inplace=True)
    return out
