"""
=========================================
Project: Predict Future Sales - Kaggle
=========================================
Script: make_features_functions.py

Purpose: prepare features

Creation date: 7/12/2020
Contact: Nadejda Jaeverberg
Email address: nadejda@kth.se
"""

from src.setup.config import *


def prepare_df(shop_ids, items_ids):
    """
    Preparing dataframe in the same way as defined by the Kaggle project description
    :param shop_ids: all shop ids in a list
    :param items_ids: all item ids in a list
    :return: a dataframe with columns "ID", "shop_id" and "item_id" for all combinations of shop_id, item_id
    """
    # Calculate number of combinations
    total_numbers = len(shop_ids) * len(items_ids)

    # Sort lists
    shop_ids.sort()
    items_ids.sort()

    # Assemble dataframe
    df = pd.DataFrame({"ID": [i for i in range(total_numbers)],
                       COLUMN_NAMES["shop_id"]: [item for sublist in [[s_id] * len(items_ids) for s_id in shop_ids]
                                                 for item in sublist],
                       COLUMN_NAMES["item_id"]: [it_id for it_id in items_ids] * len(shop_ids)})
    return df
