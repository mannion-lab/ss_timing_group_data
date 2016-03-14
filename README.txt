This contains the group data for the Mannion, Donkin, & Whitford schizotypy study.

'ss_timing_subj_resp_data_2d.csv' is the plain-text data for each of the valid participants. It also contains the participant's overall O-LIFE score, which is probably not very useful.

'ss_timing_all_subj_resp_data.npy' is the data for all participants, in numpy format. The array dimensions are subjects (100), surround onset condition (2; pre, simultaneous), surround orientation (2; orthogonal, parallel), trial (240), trial data (2; target contrast, correct response).

'ss_timing_all_subj_resp_data_2d.npy' is the same as the above, but as a 2d array (tabular form). The columns are (i_subj, i_onset, i_ori, i_trial, contrast, resp_correct).

'ss_timing_all_subj_resp_data_binned.npy' is the same again, but now the contrast and responses are binned.

'ss_timing_data_fits.npz' contains three numpy arrays: fit_params, fit_fine, and boot_all.
The fit_params array is subjects (all), surround onset, surround orientation, parameter (2; alpha, beta), parameter property (3; estimate, 2.5% CI, 97.5% CI).
The fit_fine array is subjects (all), surround onset, surround orientation, contrast (100), bootstraps (10000). It holds the evaluated fitted function of each bootstrap.
The boot_all array is subjects (all), surround onset, surround orientation, parameter (2; alpha, beta), bootstraps (10000). It holds the fitted parameters for each bootstrap.

'ss_timing_dem.csv' is the comma-separated values version of the demographic information. This summarises the scores on each of the O-LIFE dimensions, along with other demographic information. Note that this includes the excluded participants.

