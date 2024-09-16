import math

def update_rolling_variance(prev_mean, prev_var, n, new_value, old_value):
    new_mean = prev_mean + (new_value - old_value) / n
    new_var = prev_var + (new_value - old_value) * (new_value - new_mean + old_value - prev_mean) / n
    return new_mean, new_var

def update_rolling_std(prev_mean, prev_var, n, new_value, old_value):
    new_mean, new_var = update_rolling_variance(prev_mean, prev_var, n, new_value, old_value)
    return math.sqrt(max(0, new_var)), new_mean, new_var