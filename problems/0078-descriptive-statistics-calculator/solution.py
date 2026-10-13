
import numpy as np

def descriptive_statistics(data: list | np.ndarray) -> dict:
    """
    Calculate descriptive statistics for a dataset.
    """
    data = np.asarray(data)

    if data.size == 0:
        raise ValueError("data must not be empty")

    values, counts = np.unique(data, return_counts=True)
    max_count = counts.max()
    modes = values[counts == max_count].tolist()

    
    return {
    "mean": float(np.mean(data)),
    "median": float(np.median(data)),
    "mode": modes[0],
    "variance": float(np.var(data)),
    "standard_deviation": float(np.std(data)),
    "25th_percentile": float(np.percentile(data, 25)),
    "50th_percentile": float(np.percentile(data, 50)),
    "75th_percentile": float(np.percentile(data, 75)),
    "interquartile_range": float(
        np.percentile(data, 75) - np.percentile(data, 25)
    ),
    }
