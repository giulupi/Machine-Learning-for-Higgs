import numpy as np
def reweight_weights(weights, classification):
    # Take the absolute value of the weight
    weights_abs = np.abs(weights)
    # Split in signal and background weights
    weights_signal = weights_abs*classification
    weights_background = weights_abs*(1 - classification)
    # Scale the signal events
    weights_signal_scaled = weights_signal * sum(weights_background) / sum(weights_signal)
    # Merge the signal and background events
    weights_reweighted = weights_background + weights_signal_scaled
    # Normalize mean weight to one
    weights_reweighted /= weights_reweighted.mean()
    return weights_reweighted
