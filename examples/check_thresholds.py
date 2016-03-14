from __future__ import absolute_import, print_function, division

import os

import numpy as np


def main():
    """Example of how to read the fitted parameters, and checking that the
    basic thresholds match the description in the paper."""

    # determine the path to the csv file
    eg_path = os.path.abspath(__file__)
    eg_dir = os.path.dirname(eg_path)

    fit_path = os.path.abspath(
        os.path.join(
            eg_dir,
            "..",
            "ss_timing_data_fits.npz"
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

    fit_data = np.load(fit_path)["fit_params"]

    # p1040 wasn't collected...
    all_subj_ids = [
        "p{n:d}".format(n=n)
        for n in range(1001, 1101 + 1)
        if n not in [1040,]
    ]

    # work out the rows where valid subjects lie
    i_valid = [
        all_subj_ids.index(subj_id)
        for subj_id in all_subj_ids
        if subj_id not in excluded_ids
    ]

    # and restrict the data to those indices
    fit_data = fit_data[i_valid, ...]

    # now calculate the SS effect
    alpha_estimates = fit_data[...,0,0]

    cond = ["Sim", "Pre"]
    ori = ["Orth", "Par"]

    for i_cond in (1, 0):
        for i_ori in (0, 1):

            print(
                "Mean {c:s}{o:s}: {m:.3f}".format(
                    m=np.mean(alpha_estimates[:, i_cond, i_ori], axis=0) * 100,
                    c=cond[i_cond],
                    o=ori[i_ori]
                )
            )


if __name__ == "__main__":
    main()
