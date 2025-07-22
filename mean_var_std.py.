import numpy as np

def calculate(input_list):
    # Validate input length
    if len(input_list) != 9:
        raise ValueError("List must contain nine numbers.")
    
    # Convert to 3x3 numpy array
    arr = np.array(input_list).reshape(3, 3)
    
    # Build the result dictionary
    calculations = {
        'mean': [
            arr.mean(axis=0).tolist(),    # mean of each column
            arr.mean(axis=1).tolist(),    # mean of each row
            float(arr.mean())             # mean of all elements
        ],
        'variance': [
            arr.var(axis=0).tolist(),
            arr.var(axis=1).tolist(),
            float(arr.var())
        ],
        'standard deviation': [
            arr.std(axis=0).tolist(),
            arr.std(axis=1).tolist(),
            float(arr.std())
        ],
        'max': [
            arr.max(axis=0).tolist(),
            arr.max(axis=1).tolist(),
            int(arr.max())
        ],
        'min': [
            arr.min(axis=0).tolist(),
            arr.min(axis=1).tolist(),
            int(arr.min())
        ],
        'sum': [
            arr.sum(axis=0).tolist(),
            arr.sum(axis=1).tolist(),
            int(arr.sum())
        ]
    }
    
    return calculations
