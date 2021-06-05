propositional_symbols = 'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'
auxiliary_symbols = '(', ')'
unary_connective =  '−'
binary_conective =  '&', '#', '>'

def check_auxiliary_simbols = 

def check_formula (formula):
    counter_parentheses_esq = 0
    counter_parentheses_dir = 0
    counter_binary_conective = 0
    for a in formula:
        if a == 
    pass

def list_subformulas(formula, subformula):
    pass

def complexity_formula():
    pass



def main():
    formula = input('Insira a fórmula proposicional desejada: ')
    option = int(input('Digite o número da opção desejada: \n 1- Verificador de fórmula proposicional \n 2- Listar todas as subfórmulas \n 3- Calcular a complexidade \n'))

    if(option == 1):
        retorno = check_formula(formula)
        if(retorno):
            print('É fórmula')
        else:
            print('Não é fórmula')
    elif(option == 2):
        retorno = check_formula(formula)
        if(retorno):
            subformulas = []
            subformulas = list_subformulas(formula, subformulas)
            print(subformulas)
        else:
            print('Não é fórmula')
    elif(option == 3):
        complexity_formula()
    else:
        print('Dígito não reconhecido.')

main()