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
    print("1 - erro | 2 - erro | 3 - erro")
    escolha = input("Digite o número (6456, 435623 ou 34563): ")
    if escolha == "1": lamina_19()
    elif escolha == "2": exame_pulmonar_164()
    elif escolha == "3": consusta_laboratorial_42()
    else: print("Opção inválida.")
laboratorio_quimico()
print("O médico que te receitou o consumo desse experimento foi avisado de sua adquirição.")
print("Obrigado, volte sempre!")