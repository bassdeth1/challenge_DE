import json
from collections import Counter

def q3_memory(file_path: str):
    counts = Counter()
    
    def extract_mentions(text: str):
        return [word for word in text.split() if word.startswith('@')]
    
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            counts.update(extract_mentions(json.loads(line)['content']))
    
    return counts.most_common(10)
