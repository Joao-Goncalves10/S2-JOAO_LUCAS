print("Olá, aqui eu te trarei um experimento de acordo com sua necessidade que foi acordada com seu médico.")
input(print("Qual foi o médico que te receitou essareação?(Importante para a culpabilização de receitas equivocadas): "))
print("Médico registrado!")

def experimento_1():
    print("Reação de combustão: CH4 + 2O2 -> CO2 + 2H2O.")
def experimento_2():
    print("Neutralização ácido-base: HCl + NaOH -> NaCl + H2O.")
def experimento_3():
    print("Dissolução de sal: NaCl + H2O.")
def laboratorio_quimico():
    print("Escolha um experimento:")
    print("1 - Combustão | 2 - Neutralização | 3 - Dissolução")
    escolha = input("Digite o número (1, 2 ou 3): ")
    if escolha == "1": experimento_1()
    elif escolha == "2": experimento_2()
    elif escolha == "3": experimento_3()
    else: print("Opção inválida.")
laboratorio_quimico()
print("O médico que te receitou o consumo desse experimento foi avisado de sua adquirição.")
print("Obrigado, volte sempre!")