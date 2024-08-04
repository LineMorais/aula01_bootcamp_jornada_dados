# %% Cálculo de Bônus com Entrada do Usuário:

# 1. O programa deve começar solicitando ao usuário que insira seu nome.

# 2. Em seguida, o programa deve pedir ao usuário para inserir o valor do seu salário. 
# Considere que este valor pode ser um número decimal.

# 3. Depois, o programa deve solicitar a porcentagem do bônus recebido pelo usuário, 
# que também pode ser um número decimal.

# 4. O cálculo do KPI do bônus de 2024 é de 1000 + salario * bônus

# 5. Finalmente, o programa deve imprimir uma mensagem no seguinte formato: "Olá [nome], o seu valor bônus foi de 5000".

# Entrada: Se o usuário digitar "Luciano" como nome, "5000" como salário e "1.5" como bônus, o programa deve imprimir:

# Saída: Olá Luciano, o seu bônus foi de 8500

# 6. Salve esse script python como kpi.py

# 7. Faça uma documentação simples de como executar esse programa, utilize o README

# 8. Salve no Git e no Github.

# %% 
CONSTANTE_BONUS = 1000

nome = input('Digite o seu nome: ').upper()

salario = float(input('Digite o valor do seu sálario: ').replace('.','').replace(',','.'))

porcentagem_bonus = float(input('Digite qual é porcentagem do bônus que irá receber: '))

kpi_bonus = CONSTANTE_BONUS + (salario * (porcentagem_bonus/100))

print(f'Olá {nome}, o seu bônus foi de {kpi_bonus}') 
