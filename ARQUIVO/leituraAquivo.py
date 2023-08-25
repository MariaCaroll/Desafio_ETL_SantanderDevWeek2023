import pandas as pd
promocao = ["Maria LIma", 5]
var_intContador = 0


def alerta(promocao):
     


     nome = promocao[0]
     desconto = promocao[1]

     print(nome)
     print(desconto)

     if pd.isna(desconto) is True:
        return f"🌟 Hey {nome}, que tal aproveitar nossos incríveis cartões de crédito? Eles podem tornar suas compras ainda mais especiais!"   

     if desconto == 5:
        return f"📢 Ei,o bastante seu cartão. Vamos dar um check nos gastos? Lembrete: Criar um orçamento pode ajudar a gerenciar suas despesas de forma eficiente."
     elif desconto == 10:
        return f"🎉dar uma olhada nas despesas para manter tudo nos eixos? Dica: Revisar suas transações pode ajudar a identificar oportunidades de economia."
     elif desconto >  10:
        return f"🤑 e assim e sua conta vai sorrir de alegria! Sugestão: Considere criar um plano de economia para investir o dinheiro economizado."
     else:
        return f"🤑 Sem desconto."
            
print(alerta(promocao))
