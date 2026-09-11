import pandas as pd
usuarios = dict()

def registrar_voto():
    pass

def ver_resultados():
    pass

def reiniciar_votacion():
    pd.DataFrame(list(usuarios.items()), columns=["usuario", "voto"]).to_csv(
        "usuarios.csv", index=False
    )


while True:
    pass