import pandas as pd
usuarios = dict()
votos = {"Team Green": 0,"Team Black": 0,}

def registrar_voto():
    pass

def ver_resultados():
    pass

def reiniciar_votacion():
    pd.DataFrame(list(usuarios.items()), columns=["usuario", "voto"]).to_csv(
        "usuarios.csv", index=False
    )

    pd.DataFrame(list(votos.items()), columns=["team", "votos"]).to_csv(
        "votos.csv", index=False
    )


reiniciar_votacion()
while True:
    pass