from __future__ import absolute_import, print_function, division

import os

import numpy as np
import scipy.stats


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

    with open(dem_csv_path, "r") as dem_csv:

        header = dem_csv.readline().strip().split(",")

        all_data = dem_csv.readlines()

        data = [
            subj_data.strip().split(",")
            for subj_data in all_data
        ]

    fit_path = os.path.abspath(
        os.path.join(
            eg_dir,
            "..",
            "ss_timing_data_fits.npz"
        )
    )

    fit_data = np.load(fit_path)["fit_params"]

    # pull out orth and par for the sim condition
    fit_data = fit_data[:, 1, :, 0, 0]

    excluded_ids = [
        "p1027",
        "p1039",
        "p1048",
        "p1051",
        "p1060",
        "p1079",
        "p1098"
    ]

    olife_dim = "un_ex"

    olife_scores = []
    ss_sim = []

    for i_subj in xrange(len(data)):

        subj_dem = data[i_subj]
        subj_data = fit_data[i_subj, :]

        if subj_dem[header.index("subj_id")] not in excluded_ids:

            olife_scores.append(
                subj_dem[header.index("olife_" + olife_dim)]
            )

            ss_sim.append(subj_data[1] - subj_data[0])

    (r, p) = scipy.stats.spearmanr(olife_scores, ss_sim)

    print("r = {r:.3f}, p = {p:.3f}".format(r=r, p=p))


if __name__ == "__main__":
    main()
