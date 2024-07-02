import pandas as pd
from collections import Counter
import emoji
from concurrent.futures import ThreadPoolExecutor

def q2_time(file_path: str):
    # Leer el archivo JSON en un DataFrame de pandas
    df = pd.read_json(file_path, lines=True)
    
    def count_emojis(text):
        # Contar todos los emojis en un texto
        return Counter(c for c in text if c in emoji.EMOJI_DATA)
    
    counts = Counter()
    # Utilizar ThreadPoolExecutor para paralelizar el conteo de emojis
    with ThreadPoolExecutor() as executor:
        for emojis in executor.map(count_emojis, df['content']):
            counts.update(emojis)
    
    # Devolver los 10 emojis más comunes
    return counts.most_common(10)
