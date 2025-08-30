def ejecutar_cisc(memoria, start_v1, start_v2, n, start_res):
    instrucciones = 0
    ciclos = 0

    for i in range(n):
        # Simulación de instrucción SUMMEM
        v1 = memoria[start_v1 + i][start_v1 + i]
        v2 = memoria[start_v2 + i][start_v2 + i]
        resultado = v1 + v2
        memoria.append({start_res + i: resultado})

        instrucciones += 1
        ciclos += 3  # cada SUMMEM tarda 3 ciclos

    return instrucciones, ciclos
