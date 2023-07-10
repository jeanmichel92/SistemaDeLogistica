# Sistema de Logística - Calculadora de Preço de Encomenda 🗺️🚚

Este repositório contém um programa Python para calcular o preço de uma encomenda com base em suas dimensões, peso e rota de entrega. O programa foi desenvolvido para atender a uma empresa de logística que opera entre três cidades.

## Funcionalidades
O programa possui as seguintes funcionalidades:

Cálculo de Dimensões: Permite calcular o valor da encomenda com base nas dimensões informadas. As dimensões aceitas são altura, comprimento e largura, todas em centímetros.

Cálculo de Peso: Permite calcular o valor da encomenda com base no peso informado. O peso deve ser fornecido em quilogramas.

Cálculo de Rota: Permite calcular o valor da encomenda com base na rota de entrega escolhida. O usuário deve informar a rota desejada utilizando siglas predefinidas para representar as cidades.

Cálculo Total: Combina os valores calculados nas etapas anteriores e exibe o preço total da encomenda.

## Exemplo de Saída do Console

Aqui está um exemplo de saída do console com base nas funcionalidades do programa:

Calculadora de Preço de Encomenda

Informe as dimensões da encomenda:
Altura (cm): 25
Comprimento (cm): 30
Largura (cm): 20

Informe o peso da encomenda (kg): 1.8

Informe a rota de entrega (utilize siglas):
1. RS - De Rio de Janeiro até São Paulo
2. SR - De São Paulo até Rio de Janeiro
3. BS - De Brasília até São Paulo
4. SB - De São Paulo até Brasília
5. BR - De Brasília até Rio de Janeiro
6. RB - De Rio de Janeiro até Brasília

Rota: SR

Preço Total da Encomenda: R$ 60.00


## Exemplo de tratamento de erro:

Calculadora de Preço de Encomenda

Informe as dimensões da encomenda:
Altura (cm): abc
As dimensões devem ser valores numéricos. Tente novamente.

Informe as dimensões da encomenda:
Altura (cm): 40
Comprimento (cm): 30
Largura (cm): 50

Informe o peso da encomenda (kg): 500
O peso deve ser um valor numérico. Tente novamente.

Informe o peso da encomenda (kg): 2

Informe a rota de entrega (utilize siglas):
1. RS - De Rio de Janeiro até São Paulo
2. SR - De São Paulo até Rio de Janeiro
3. BS - De Brasília até São Paulo
4. SB - De São Paulo até Brasília
5. BR - De Brasília até Rio de Janeiro
6. RB - De Rio de Janeiro até Brasília

Rota: AB
Opção inválida. Tente novamente.

Rota: RS

Preço Total da Encomenda: R$ 30.00


## Sinta-se à vontade para explorar outras funcionalidades e interagir com o programa de acordo com suas necessidades.
