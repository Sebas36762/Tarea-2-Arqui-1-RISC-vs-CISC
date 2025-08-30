def crear_memoria(vector1, vector2):
    memoria = []
    direccion = 0
    for v in vector1 + vector2:  # precarga vectores en memoria
        memoria.append({direccion: v})
        direccion += 1
    return memoria
