def update_rolling_mean(prev_mean, n, new_value, old_value):
    return prev_mean + (new_value - old_value) / n