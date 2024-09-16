import math

def update_rolling_skew(prev_mean, prev_var, prev_m3, n, new_value, old_value):
    delta = new_value - old_value
    delta_n = delta / n
    term1 = delta * delta_n * (n - 1)
    
    new_mean = prev_mean + delta_n
    
    m2 = prev_var * (n - 1)
    new_m2 = m2 + term1
    new_var = new_m2 / n
    
    m3 = prev_m3 * (n - 1)
    new_m3 = m3 + term1 * (n - 2) * delta_n - 3 * delta_n * m2
    
    new_skew = (n * new_m3) / (new_m2 * math.sqrt(new_m2))
    
    return new_skew, new_mean, new_var, new_m3