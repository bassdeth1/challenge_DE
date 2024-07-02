import json
from collections import defaultdict, Counter
from typing import List, Tuple
import datetime

def q1_memory(file_path: str) -> List[Tuple[datetime.date, str]]:
    # Diccionario que contará los posts por usuario para cada fecha
    counts = defaultdict(Counter)
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            # Leer cada línea del archivo JSON y parsear el contenido
            tweet = json.loads(line)
            # Extraer y formatear la fecha del tweet
            date = datetime.datetime.strptime(tweet['date'][:10], "%Y-%m-%d").date()
            # Contar los tweets por usuario para cada fecha
            counts[date][tweet['user']['username']] += 1

    # Obtener las 10 fechas con más actividad
    top_dates = Counter({date: sum(users.values()) for date, users in counts.items()}).most_common(10)
    # Devolver el usuario más activo para las 10 fechas con más actividad
    return [(date, counts[date].most_common(1)[0][0]) for date, _ in top_dates]
