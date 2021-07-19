# Drifts-NN
150 km Equatorial Vertical Drifts
###################################
Author: J. P. Velásquez.
Email: jpvelasquez@pucp.edu.pe
Based on:
Anderson, D., Anghel, A., Chau, J., and Veliz, O. (2004), Daytime vertical E × B drift velocities inferred from ground-based magnetometer observations at low latitudes, Space Weather, 2, S11001, doi:10.1029/2004SW000095.
###################################
3 layers Feedforward Neural Network.
###################################

1) It uses 19 years of Magnetometer and Coherent Scatter Radar data sets in order to train a 6 inpunt nodes -- 5 hidden layer nodes and 1 output node.

2) Input variables: daily F10.7 solar index activity, hourly Kp geomagnetic index activity, Local Time (real number), Day of Year (integer) and year.

3) Output: ExB vertical drift (real number)

