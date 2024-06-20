import numpy as np
def get_significances(model, signal_values, bkg_values, signal_weights, bkg_weights):
    # Model prediction
    signal_prediction = model.predict(signal_values)
    bkg_prediction = model.predict(bkg_values)

    # Transform predicton to array
    signal_prediction = np.array([element[0] for element in signal_prediction])
    bkg_prediction = np.array([element[0] for element in bkg_prediction])
    
    # Calculate the significance for different cut values in a for loop
    cut_values = []
    significances = []
    for cut_value in np.linspace(0, 1, 1000):
        # Number of signal and background events passing the prediction selection
        n_signal = signal_weights[signal_prediction > cut_value].sum()
        n_bkg = bkg_weights[bkg_prediction > cut_value].sum()

        # Break if less than 10 background events
        if n_bkg < 10:
            break

        # Significance calculation
        significance = n_signal / np.sqrt(n_bkg)
        
        # Append the cut value and the significances to their lists
        cut_values.append(cut_value)
        significances.append(significance)
    return cut_values, significances
