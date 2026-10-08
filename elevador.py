def coletar_respostas(pergunta, respostas_possiveis):
     while True:
        resposta = input(pergunta).upper()
        if resposta not in respostas_possiveis:
            print("Valor inválido.")
        else:
            return resposta

contador_elevador = {"A": 0, "B": 0, "C": 0} 
contador_periodo = {"M": 0, "V": 0, "N": 0} 

coletando = True
while coletando:
    elevador = coletar_respostas("Informe o elevador (A, B ou C): ", contador_elevador)
    periodo = coletar_respostas("Informe o periodo (M, V ou N): ", contador_periodo)
        
    contador_elevador[elevador] += 1
    contador_periodo[periodo] += 1

    
    if coletar_respostas("Deseja continuar? (S/N): ", ["S", "N"]) == "N":
        coletando = False

elevador_mais = max(contador_elevador, key=contador_elevador.get)
print(f'O elevador mais utilizado é o {elevador_mais}')

periodo_mais = max(contador_periodo, key=contador_periodo.get)
print(f'O período mais utilizado é o {periodo_mais}')
periodo_menos = min(contador_periodo, key=contador_periodo.get)

total = sum(contador_periodo.values())

percentual_menos = contador_periodo[periodo_menos] / total
percentual_mais = contador_periodo[periodo_mais] / total
diferenca = percentual_mais - percentual_menos

print(f'Diferença percentual: {diferenca}')