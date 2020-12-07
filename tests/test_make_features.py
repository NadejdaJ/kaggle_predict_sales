import unittest
import numpy as np
from pandas.testing import assert_frame_equal
from src.make_features.make_features_functions import *


class MyCleanDataTestCase(unittest.TestCase):

    def test_prepare_df(self):
        shop_ids_in = [0, 2, 4, 8]
        item_ids_in = [900, 400, 600]

        expected = pd.DataFrame({"ID": [i for i in range(12)],
                                 "shop_id": [0] * 3 + [2] * 3 + [4] * 3 + [8] * 3,
                                 "item_id": [400, 600, 900] * 4})

        out = prepare_df(shop_ids_in, item_ids_in)

        assert_frame_equal(out, expected)


if __name__ == '__main__':
    unittest.main()
