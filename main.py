import pandas as pd
usuarios = dict()
votos = {"Team Green": 0,"Team Black": 0,}

def registrar_voto():
    identificador = input("Ingresa tu identificador (cédula o usuario): ").strip()

    if identificador in usuarios:
        print("Ya registraste tu voto. No puedes votar dos veces.")
        return

    print("Opciones disponibles: 1) Team Green   2) Team Black")
    opcion_num = input("Elige tu opción (1 o 2): ").strip()

    if opcion_num == "1":
        opcion = "Team Green"
    elif opcion_num == "2":
        opcion = "Team Black"
    else:
        print("Opción inválida. Debes elegir 1 o 2.")
        return

    usuarios[identificador] = True
    votos[opcion] += 1

    print("Voto registrado correctamente. ¡Gracias por participar!")


def ver_resultados():
    pass

def reiniciar_votacion():
    pd.DataFrame(list(usuarios.items()), columns=["usuario", "voto"]).to_csv(
        "usuarios.csv", index=False
    )

    pd.DataFrame(list(votos.items()), columns=["team", "votos"]).to_csv(
        "votos.csv", index=False
    )


def menu():
    print("""
1. Registrar voto
2. Ver resultados
3. Reiniciar votación
4. Salir
""")

while True:
    menu()
    opcion = input("Elige una opción: ").strip()
    if opcion == "1":
        registrar_voto()
    elif opcion == "2":
        ver_resultados()
    elif opcion == "3":
        reiniciar_votacion()
    elif opcion == "4":
        print("Saliendo del sistema...")
        break
    else:
        print("Opción inválida.")