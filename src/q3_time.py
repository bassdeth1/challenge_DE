import pandas as pd
from collections import Counter
from concurrent.futures import ThreadPoolExecutor

def q3_time(file_path: str):
    df = pd.read_json(file_path, lines=True)
    
    def count_mentions(text):
        return Counter(word for word in text.split() if word.startswith('@'))
    
    counts = Counter()
    with ThreadPoolExecutor() as executor:
        for mentions in executor.map(count_mentions, df['content']):
            counts.update(mentions)
    
    return counts.most_common(10)
