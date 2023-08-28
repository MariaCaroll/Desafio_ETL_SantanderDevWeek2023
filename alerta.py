# Função para gerar os alertas
def generate_new_alerta(var_strNome, var_intDesconto):
     
    desconto = int(var_intDesconto)

    if desconto == 5:
        var_strMensagem = f"📢 Ei, {var_strNome}, Aproveite o {desconto}% de deconto que disponibilizamos para você."
        return var_strMensagem
    elif desconto == 10:
        var_strMensagem = f"🎉 {var_strNome}, Aproveite o {desconto}% de deconto que disponibilizamos para você."
        return var_strMensagem
    elif desconto > 10:
        var_strMensagem = f"🤑 Uhulll, {var_strNome}, aproveite o desconto imperdivel de {desconto}% que disponibilizamos especialmente para você."
        return var_strMensagem
    else:
        var_strMensagem = f"🌟 Caro {var_strNome}, infelizmente não temos desconto disponível. Mas não desanime, fique de olho nos alertas.!"
        return var_strMensagem
