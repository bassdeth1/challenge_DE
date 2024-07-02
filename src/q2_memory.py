import json
from collections import Counter
import emoji

def q2_memory(file_path: str):
    # Contador para los emojis
    counts = Counter()
    
    def extract_emojis(text: str):
        # Extraer todos los emojis del texto
        return [char for char in text if char in emoji.EMOJI_DATA]
    
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            # Leer cada línea del archivo JSON y extraer emojis
            counts.update(extract_emojis(json.loads(line)['content']))
    
    # Devolver los 10 emojis más comunes
    return counts.most_common(10)
