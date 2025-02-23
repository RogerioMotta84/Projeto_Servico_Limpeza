# Início da função Metragem Limpeza
def metragemLimpeza():
    print('---------------------------- Menu 1 de 3 - Metragem Limpeza ---------------------------')
    while True:
        try:
            metragemL = int(input('Entre com a metragem da casa: '))

            if (30 <= metragemL) and (metragemL < 300):
                print('É necessário contratar 1 pessoa')
                return 60 + 0.3 * metragemL
            elif (300 <= metragemL) and (metragemL < 701):
                print('Serão necessários (as) dois(duas) funcionários(as) para a limpeza')
                return 120 + 0.5 * metragemL
            else:
                print('!! Não aceitamos casas com metragem menor que 30m² ou maior que 700m² !!')
                continue  # retorna para a pergunta

        except ValueError:  # caso o usuário digite uma letra ou número quebrado 0.30
            print('Pare de digitar valores não inteiros')

# Fim da função Metragem Limpeza

# Início da função Tipo de Limpeza
def tipoLimpeza():
    print('***************************************************************************************')
    print('------------------------------ Menu 2 de 3 - Tipo de Limpeza --------------------------')
    while True:
        tipoL = input('Entre com tipo de Limpeza: \n' +
                      'B - Básica - Indicada para sujeiras semanais ou quinzenais \n' +
                      'C - Completa (30% a mais) - Indicada para sujeiras antigas e/ou não rotineiras \n' +
                      '>> ')
        tipoL = tipoL.lower()
        tipoL = tipoL.strip()
        if tipoL == 'b':
            print('Você selecionou a limpeza básica')
            return 1.00
        elif tipoL == 'c':
            print('Você selecionou a limpeza completa')
            return 1.30
        else:
            print('!!!!!!! Opção inválida !!!!!!!')
            continue  # voltar para o inicio

# Fim da função Tipo de Limpeza

# Início da função Adicional de Limpeza
def adicionalLimpeza():
    print('***************************************************************************************')
    print('------------------------- Menu 3 de 3 - Adicional de Limpeza --------------------------')
    acumulador = 0
    while True:
        adicionalL = input('Deseja mais algum adicional?: \n' +
                            '0 - Não desejo mais nada (encerrar) \n' +
                            '1 - Passar 10 peças de roupas - R$ 10,00 \n' +
                            '2 - Limpeza de 1 Forno/Micro-ondas - R$ 12,00 \n' +
                            '3 - Limpeza de 1 Geladeira/Freezer - R$ 20,00 \n' +
                            '>> ')
        if adicionalL == '0':
            return acumulador
        elif adicionalL == '1':
            acumulador = acumulador + 10
            continue  # volta para o inicio do while True
        elif adicionalL == '2':
            acumulador = acumulador + 12
            continue  # volta para o inicio do while True
        elif adicionalL == '3':
            acumulador = acumulador + 20
            continue  # volta para o inicio do while True
        else:
            print('Pare de digitar opções diferentes de 0/1/2/3!')

# Fim da função Adicional de Limpeza

# Início do Main
print('Bem-vindo ao Programa de Serviços de Limpeza')
print('***************************************************************************************')

metragem = metragemLimpeza()
tipo = tipoLimpeza()
adicional = adicionalLimpeza()
total = (metragem * tipo) + adicional
print('***************************************************************************************')
print(' O Total Ficou R$ {:.2f} (metragem: R$ {:.2f} * tipo: R$ {:.2f} + adicional: R$ {:.2f})'.format(total, metragem, tipo, adicional))
print('***************************************************************************************')



