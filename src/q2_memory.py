import json
from collections import Counter
import emoji

def q2_memory(file_path: str):
    counts = Counter()
    
    def extract_emojis(text: str):
        return [char for char in text if char in emoji.EMOJI_DATA]
    
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            counts.update(extract_emojis(json.loads(line)['content']))
    
    return counts.most_common(10)
