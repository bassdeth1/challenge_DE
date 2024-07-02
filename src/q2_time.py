import pandas as pd
from collections import Counter
import emoji
from concurrent.futures import ThreadPoolExecutor

def q2_time(file_path: str):
    df = pd.read_json(file_path, lines=True)
    
    def count_emojis(text):
        return Counter(c for c in text if c in emoji.EMOJI_DATA)
    
    counts = Counter()
    with ThreadPoolExecutor() as executor:
        for emojis in executor.map(count_emojis, df['content']):
            counts.update(emojis)
    
    return counts.most_common(10)
