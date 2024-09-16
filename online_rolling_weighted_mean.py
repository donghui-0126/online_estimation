def update_weighted_rolling_mean(prev_weighted_mean, weights, new_value, old_value):
    total_weight = sum(weights)
    return prev_weighted_mean + (weights[-1] * new_value - weights[0] * old_value) / total_weight