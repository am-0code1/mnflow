# ----------------------------------------------------------------------------
# Copyright (c) 2024 Aryan Mehboudi
# Licensed under the GNU Affero General Public License v3 or later (AGPLv3+).
# You should have received a copy of the License along with the code. If not,
# see <https://www.gnu.org/licenses/>.
# ----------------------------------------------------------------------------


"""Test block.DLD"""

from tests.test_dld import Test_DLD
from tests.test_dld import get_block_DLD


def test_1():

    dld = get_block_DLD(
        d_c=1.0,
        Np=10,
        rotation_angle_deg_before_array=90,
        verbose=False,
    )

    ground_truth = {
        "Np": 10,
        "Nw": 12,
        "d_c": 1.0,
        "gap_w": 2.157108371715726,
        "pitch_w": 4.314216743431452,
        "gap_a": 2.157108371715726,
        "pitch_a": 4.314216743431452,
        "height": 8.628433486862903,
        "boundary_treatment": "pow_3",
        #
        "num_unit": 14,
        "opt_mirror": False,
        "array_counts": [1, 1],
        "opt_mirror_before_array": [False, False],
        #
        "bb": [(-601.831, -11.355), (2.157, 51.771)],
    }

    Test_DLD(dld=dld, ground_truth=ground_truth)


def test_2():

    dld = get_block_DLD(
        gap_w=3.5,
        verbose=False,
    )

    ground_truth = {
        "Np": 50,
        "Nw": 8,
        "d_c": 0.7493599494873922,
        "gap_w": 3.5,
        "pitch_w": 7.0,
        "gap_a": 3.5,
        "pitch_a": 7.0,
        "height": 14.0,
        "boundary_treatment": "pow_3",
        #
        "num_unit": 9,
        "opt_mirror": False,
        "array_counts": [1, 1],
        "opt_mirror_before_array": [False, False],
        #
        "bb": [(-18.31, -3.5), (56.0, 3146.5)],
    }

    Test_DLD(dld=dld, ground_truth=ground_truth)


if __name__ == "__main__":
    test_1()
    test_2()
