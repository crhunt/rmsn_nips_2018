# Forecasting Treatment Responses Over Time Using Recurrent Marginal Structural Networks
> by Bryan Lim, Ahmed Alaa and Mihaela van der Schaar, **NeurIPS 2018**

## Usage instructions
* To generate a new simulation, run hyperparameter optimisation and tests for the RMSN use : 


    > **bash test_rmsn.sh**
* This produces the raw MSEs into the "*results*" folder, and saves calibrated models into the "*models*" folder
* Note that for the paper, results are imported in normalised root mean-squared error terms -> i.e. sqrt(mse) / 1150

## Compatibility with TensorFlow v2

This fork extends the RMSN model to be compatible with TensorFlow v2 up to TensorFlow 2.15 and Keras v2 up to 2.15. 

To set the TensorFlow version, and related dependencies, set an environment variable `RMSN_VERSION` to either `compat` for TensorFlow v2 (<= 2.15) or to `v1` for TensorFlow v1. This is done on line 13 in the script test_rmsn.sh.