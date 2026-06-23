## Descrição

Desafio da aula 01 KPI
Descrição

Este programa realiza o cálculo do bônus de um colaborador com base no salário informado e no percentual de bônus aplicado.

Ao executar o programa, o usuário deverá informar:

Nome do colaborador;
Salário;
Percentual de bônus.

O sistema calcula o valor final do bônus utilizando uma constante fixa de R$ 1.000,00.

Regra de Negócio

A fórmula utilizada para o cálculo é:

Bônus Final = 1000 + (Salário × Percentual de Bônus)

Ou, considerando o percentual:

Bônus Final = 1000 + (Salário × (Percentual / 100))
Pré-requisitos
Python 3.8 ou superior instalado.
Terminal, Prompt de Comando ou IDE compatível.
Código Fonte
CONSTANTE_BONUS = 1000

nome = input('Digite o seu nome: ').upper()

salario = float(
    input('Digite o valor do seu salário: ')
    .replace('.', '')
    .replace(',', '.')
)

porcentagem_bonus = float(
    input('Digite qual é porcentagem do bônus que irá receber: ')
)

kpi_bonus = CONSTANTE_BONUS + (
    salario * (porcentagem_bonus / 100)
)

print(f'Olá {nome}, o seu bônus foi de {kpi_bonus}')
Como Executar
1. Salve o arquivo

Crie um arquivo chamado:

calculo_bonus.py

Cole o código dentro do arquivo.

2. Abra o terminal

Navegue até a pasta onde o arquivo foi salvo:

cd caminho/do/projeto
3. Execute o programa
python calculo_bonus.py

ou

python3 calculo_bonus.py

Exemplo de Execução

Entrada
Digite o seu nome: Aline
Digite o valor do seu salário: 5.000,00
Digite qual é porcentagem do bônus que irá receber: 10

Processamento
Bônus = 1000 + (5000 × 10%)
Bônus = 1000 + 500
Bônus = 1500

Saída
Olá ALINE, o seu bônus foi de 1500.0
Tratamento do Salário

O programa permite informar o salário nos formatos:

5000
5000,00
5.000,00

Os caracteres são convertidos automaticamente para o formato numérico aceito pelo Python.

Engenharia de Dados / Python Básico

Programa desenvolvido para demonstrar conceitos de:

Entrada de dados (input)
Conversão de tipos (float)
Manipulação de strings
Operadores matemáticos
Formatação de saída (f-string)
