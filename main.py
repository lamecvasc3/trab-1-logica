from formula import check_formula, list_subformulas, complexity_formula
     

if __name__ == '__main__':
    formula = input('Insira a fórmula proposicional desejada: ')
    option = int(input('Digite o número da opção desejada: \n 1- Verificador de fórmula proposicional \n 2- Listar todas as subfórmulas \n 3- Calcular a complexidade \n'))

    if(option == 1):
        if(check_formula(formula)):
            print('É fórmula')
        else:
            print('Não é fórmula')
    elif(option == 2):
        if(check_formula(formula)):
            subformulas = []
            subformulas = list_subformulas(formula, subformulas)
            print(set(subformulas))
        else:
            print('Não é fórmula')
    elif(option == 3):
        if(check_formula(formula)):
            subformulas = []
            subformulas = list_subformulas(formula, subformulas)
            complexity = complexity_formula(set(subformulas))
            print('Complexidade: ', complexity)
    else:
        print('Dígito não reconhecido.')

