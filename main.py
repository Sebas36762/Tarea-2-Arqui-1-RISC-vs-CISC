from memoria import crear_memoria
from cisc import ejecutar_cisc
from risc import ejecutar_risc

if __name__ == "__main__":
    # Vectores iniciales
    v1 = [i for i in range(1, 11)]          # [1,2,3,...,10]
    v2 = [i for i in range(11, 21)]         # [11,12,...,20]

    # Crear memorias independientes
    memoria_cisc = crear_memoria(v1, v2)
    memoria_risc = crear_memoria(v1, v2)

    # Direcciones: v1=0..9, v2=10..19, resultado a partir de 20
    inst_cisc, ciclos_cisc = ejecutar_cisc(memoria_cisc, 0, 10, 10, 20)
    inst_risc, ciclos_risc = ejecutar_risc(memoria_risc, 0, 10, 10, 20)

    # Resultados
    print("CISC:")
    print("Instrucciones ejecutadas:", inst_cisc)
    print("Ciclos totales:", ciclos_cisc)

    print("\nRISC:")
    print("Instrucciones ejecutadas:", inst_risc)
    print("Ciclos totales:", ciclos_risc)
