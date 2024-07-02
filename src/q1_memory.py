import json
from collections import defaultdict, Counter
from typing import List, Tuple
import datetime

def q1_memory(file_path: str) -> List[Tuple[datetime.date, str]]:
    counts = defaultdict(Counter)
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            tweet = json.loads(line)
            date = datetime.datetime.strptime(tweet['date'][:10], "%Y-%m-%d").date()
            counts[date][tweet['user']['username']] += 1

    top_dates = Counter({date: sum(users.values()) for date, users in counts.items()}).most_common(10)
    return [(date, counts[date].most_common(1)[0][0]) for date, _ in top_dates]
