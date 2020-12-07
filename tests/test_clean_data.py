import unittest
import numpy as np
from pandas.testing import assert_frame_equal
from src.make_clean_data.clean_data_functions import *


class MyCleanDataTestCase(unittest.TestCase):

    def test_remove_refunds(self):
        df_in = pd.DataFrame({"col1": [0, -1, 3, 5],
                              "col2": [9, 8, -1, 3]})

        df_out = remove_refunds(df_in, "col1")

        df_exp = pd.DataFrame({"col1": [0, 3, 5],
                              "col2": [9, -1, 3]})
        assert_frame_equal(df_exp, df_out)

    def test_get_quartiles(self):
        df_in = pd.DataFrame({"col1": [8, 2, 4, 0, 5],
                              "col2": [9, 8, -1, 3, 11]})

        q1, q2 = get_quartiles(df_in, "col1")
        self.assertEqual(q1, 2)
        self.assertEqual(q2, 5)

    def test_remove_outliers(self):
        df_in = pd.DataFrame({"item_price": [2*max_item_price, -3, 0, max_item_price,
                                             max_item_price],
                              "item_cnt_day": [9, 10, max_item_count, 2*max_item_count,
                                               max_item_count/100]})
        df_out = remove_outliers(df_in)

        df_exp = pd.DataFrame({"item_price": [0, max_item_price],
                               "item_cnt_day": [max_item_count, max_item_count/100]})

        assert_frame_equal(df_exp, df_out)

    def test_groupings(self):
        list_in = ["Игры 4", "random", "Карты оплаты", "Кино", "Книги 2", "Подарки", "Музыка",
                   "Программы", "Служебные", "Игровые", "Чистые носители", "Аксессуары",
                   "Игры 7"]
        list_exp = ["games", "random", "payment_card", "movies", "books", "gifts", "music",
                    "programs", "service", "consoles", "storage", "accessories", "games"]

        list_out = [groupings(i) for i in list_in]

        self.assertListEqual(list_out, list_exp)

    def test_group_item_categories(self):
        df_in = pd.DataFrame({"item_category_name": ["Игры 7", "random", "Карты оплаты 0", "Игры 3", "Карты оплаты"],
                              "item_category_id": [1, 6, 9, 4, 8]})

        df_out = group_item_categories(df_in)

        df_exp = pd.DataFrame({"item_category_name": ["games", "random", "payment_card", "games", "payment_card"],
                               "original_category_id": [1, 6, 9, 4, 8],
                               "item_category_id": [0, 1, 2, 0, 2]})

        assert_frame_equal(df_out, df_exp)

    def test_extract_city(self):
        df_in = pd.DataFrame({COLUMN_NAMES["shop_name"]: [np.nan, "Krym", "Химки", "Омск"]})
        expected = pd.DataFrame({COLUMN_NAMES["shop_name"]: [np.nan, "Krym", "Химки", "Омск"],
                                 COLUMN_NAMES["city_name"]: [np.nan, "Krym", "moscow", "omsk"]})
        df_out = extract_city(df_in, COLUMN_NAMES["shop_name"])
        assert_frame_equal(expected, df_out)


if __name__ == '__main__':
    unittest.main()
