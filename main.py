usuarios = dict()
votos = {"Team Green":0,"Team Black":0}

def registrar_voto():
    pass

def ver_resultados():
    total_votos = len(usuarios)

    if total_votos == 0:
        print("\nAún no hay votos registrados.\n")
        return

    votos_black = sum(1 for voto in usuarios.values() if voto == "team black")
    votos_green = sum(1 for voto in usuarios.values() if voto == "team green")

    porcentaje_black = (votos_black / total_votos) * 100
    porcentaje_green = (votos_green / total_votos) * 100

    print("\n--- Resultados de la votación ---")
    print(f"Team Black: {votos_black} votos ({porcentaje_black:.1f}%)")
    print(f"Team Green: {votos_green} votos ({porcentaje_green:.1f}%)")
    print(f"Total de votos: {total_votos}\n")

def reiniciar_votacion():
    pass


while True:
    pass