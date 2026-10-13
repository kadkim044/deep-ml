def empirical_pmf(samples):
    """
    Given an iterable of integer samples, return a list of (value, probability)
    pairs sorted by value ascending.
    """
    total = len(samples)

    if total == 0:
        return []

    values = sorted(set(samples))

    return [
        (value, samples.count(value) / total)
        for value in values
    ]