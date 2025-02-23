# Programa de Serviços de Limpeza 
Este é um projeto desenvolvido como parte da disciplina de Lógica de Programação e Algoritmos da Faculdade Uninter. O objetivo é criar uma solução de software para calcular o valor de serviços de limpeza, levando em consideração a metragem do local, o tipo de limpeza e os adicionais selecionados pelo cliente.

## Descrição do Problema
O programa foi desenvolvido para atender uma empresa de serviços de limpeza, cuja precificação é baseada nos seguintes parâmetros:

**Metragem:** A metragem (em metros quadrados) influencia diretamente no valor do serviço. As faixas de metragem e seus respectivos valores estão descritas abaixo:

**30 <= metragem < 300:** R$ 60 + 0,3 * metragem
**300 <= metragem < 700:** R$ 120 + 0,5 * metragem
**Outros valores:** Não são aceitos

**Tipo de Limpeza:** O tipo de limpeza selecionado afeta o preço total através de um multiplicador:
**B – Básica:** Indicada para sujeiras semanais ou quinzenais (Multiplicador: 1.00)
**C – Completa:** Indicada para sujeiras antigas e/ou não rotineiras (Multiplicador: 1.30)


**Adicionais:** O cliente pode escolher adicionais que também afetam o valor final:
0: Não desejo mais nada (R$ 0,00)
1: Passar 10 peças de roupas (R$ 10,00)
2: Limpeza de 1 Forno/Micro-ondas (R$ 12,00)
3: Limpeza de 1 Geladeira/Freezer (R$ 20,00)

## Funcionalidades
O programa realiza os seguintes passos:

**Metragem da limpeza:** O programa solicita a metragem do local para determinar o valor inicial. A partir dessa metragem, ele define quantas pessoas são necessárias para realizar o serviço, conforme as faixas de metragem especificadas.
**Tipo de limpeza:** O usuário escolhe o tipo de limpeza desejada, entre "Básica" e "Completa". O programa valida a escolha e calcula o multiplicador adequado.
**Adicionais:** O programa pergunta ao usuário se ele deseja adicionar algum serviço extra. Ele continua perguntando até o usuário escolher a opção "0", que indica que não há mais adicionais. O valor total é então calculado, incluindo todos os serviços adicionais escolhidos.

![Texto alternativo](Imagem/nome_da_imagem.png)

