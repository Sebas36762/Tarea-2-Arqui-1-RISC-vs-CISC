def ejecutar_risc(memoria, start_v1, start_v2, n, start_res):
    instrucciones = 0
    ciclos = 0

    for i in range(n):
        # LOAD v1
        v1 = memoria[start_v1 + i][start_v1 + i]
        instrucciones += 1
        ciclos += 1

        # LOAD v2
        v2 = memoria[start_v2 + i][start_v2 + i]
        instrucciones += 1
        ciclos += 1

        # ADD
        resultado = v1 + v2
        instrucciones += 1
        ciclos += 1

        # STORE
        memoria.append({start_res + i: resultado})
        instrucciones += 1
        ciclos += 1

    return instrucciones, ciclos
