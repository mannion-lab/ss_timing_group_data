from __future__ import absolute_import, print_function, division

import os


def main():
    """Reading and checking the demographic information"""

    # determine the path to the csv file
    eg_path = os.path.abspath(__file__)
    eg_dir = os.path.dirname(eg_path)

    dem_csv_path = os.path.abspath(
        os.path.join(
            eg_dir,
            "..",
            "ss_timing_dem.csv"
        )
    )

    excluded_ids = [
        "p1027",
        "p1039",
        "p1048",
        "p1051",
        "p1060",
        "p1079",
        "p1098"
    ]

    with open(dem_csv_path, "r") as dem_csv:

        header = dem_csv.readline().strip().split(",")

        all_data = dem_csv.readlines()

        data = [
            subj_data.strip().split(",")
            for subj_data in all_data
        ]

    valid_data = [
        subj_data
        for subj_data in data
        if subj_data[header.index("subj_id")] not in excluded_ids
    ]

    n_female = 0
    n_in_age_range = 0
    n_right_handed = 0

    for subj_data in valid_data:

        if subj_data[header.index("gender")] == "F":
            n_female += 1

        if 18 <= int(subj_data[header.index("age")]) <= 20:
            n_in_age_range += 1

        if subj_data[header.index("handedness")] == "R":
            n_right_handed += 1

    n = len(valid_data)

    print("Female: {f:d}/{n:d}".format(f=n_female, n=n))
    print("Age 18-20: {a:d}/{n:d}".format(a=n_in_age_range, n=n))
    print("Right handed: {r:d}/{n:d}".format(r=n_right_handed, n=n))



if __name__ == "__main__":
    main()
