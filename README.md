# Drifts-NN
150 km Equatorial Vertical Drifts
###################################
Based on:
F.   S.   Rodrigues,   J.   M.   Smith,   M.   Milla,   and   R.   A.   Stoneback,“Daytime  ionospheric  equatorial  vertical  drifts  during  the  2008–2009extreme  solar  minimum,”Journal  of  Geophysical  Research:  SpacePhysics,  vol.  120,  no.  2,  pp.  1452–1459,  2015.  [Online]. Available:https://agupubs.onlinelibrary.wiley.com/doi/abs/10.1002/2014JA020478.
###################################
3 layers Feedforward Neural Network.
###################################

1) It uses 19 years of Magnetometer and Coherent Scatter Radar data sets in order to train a 6 inpunt nodes -- 5 hidden layer nodes and 1 output node.

2) Input variables: daily F10.7 solar index activity, hourly Kp geomagnetic index activity, Local Time (real number), Day of Year (integer) and year.

3) Output: ExB vertical drift (real number)

