def get_reliability_score(weight, related_weights):
    count = len(related_weights))
    average_weight = sorted(related_weights, reverse=True)[:min(10, count]/float(min(10, count))
    return weight*0.5+average_weight*0.35+min(count, 100)*0.15


