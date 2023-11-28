from collections import Counter

def get_count_visits_from_ip(ips):
    counts = Counter(ips)
    return counts

def get_frequent_visit_from_ip(ips):
    counts = Counter(ips)
    return counts.most_common(1)[0]

