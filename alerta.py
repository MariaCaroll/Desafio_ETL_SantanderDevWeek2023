#Função para gerar os alertas
import pandas as pd
def generate_new_alert(nome, desconto):

     if pd.isna(desconto) is True:
        return f"🌟 Caro {nome}, infelizmente não temos desconto disponível. Mas não desanime, fique de olho nos alertas. !"   

     if desconto == 5:
        return f"📢 Ei, {nome}, Aproveite o {desconto}% de deconto que disponibilizamos para você."
     elif desconto == 10:
        return f"🎉 {nome}, Aproveite o {desconto}% de deconto que disponibilizamos para você."
     elif desconto >  10:
        return f"🤑 Uhulll, {nome} aproveite o desconto imperdivem de {desconto}% que disponibilizamos especialmente para você."
     else:
        return f"🤑 Sem desconto."