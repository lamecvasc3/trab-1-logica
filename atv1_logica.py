auxiliary_symbols = '(', ')'
unary_connective =  '-'
binary_connective =  '&', '#', '>'


def check_auxiliary_symbols(a):
    for auxiliary in auxiliary_symbols:
        if(a == auxiliary):
            return True
    return False

def check_unary_connective(a):
    for unary in unary_connective:
        if (a==unary):
            return True
    return False
     
def check_binary_connective(a):
    for binary in binary_connective:
        if (a==binary):
            return True
    return False

def check_formula(formula):
    counter_letter = 0
    counter_unary_connective = 0
    counter_auxiliary_symbols = 0
    counter_binary_connective = 0

    if (len(formula) == 1 and formula.isalpha()) or (len(formula) == 2 and (check_unary_connective(formula[0]) and formula[1].isalpha)):
        return True

    for a in range(len(formula)):
        if formula[a].isalpha():
            counter_letter += 1
        if check_auxiliary_symbols(formula[a]):
            counter_auxiliary_symbols += 1
        if check_binary_connective(formula[a]):
            counter_binary_connective += 1
        if check_unary_connective(formula[a]):
            counter_unary_connective += 1
        
    if (counter_letter < 2) or (2*counter_binary_connective != counter_auxiliary_symbols) or (counter_auxiliary_symbols < 2) or (counter_binary_connective < 1):
        return False

    for a in range(len(formula)):
        #Verifica se o caractere é uma letra
        if (formula[a].isalpha()):
            if(formula[a+1].isalpha() or check_unary_connective(formula[a+1]) or (formula[a+1] == '(')):
                return False
            continue
        elif (check_auxiliary_symbols(formula[a])):
            #Verifica se o caractere é um símbolo auxiliar
            if(formula[a] == '('):
                if(formula[a+1] == ')' or check_binary_connective(formula[a+1])):
                    print('erro 2')
                    return False
            else:
                if(formula[a-1] == '(' or check_unary_connective(formula[a-1]) or check_binary_connective(formula[a-1])):
                    print('erro 3')
                    return False
            continue
        elif(check_unary_connective(formula[a])):
            #Verifica se o caractere é um conectivo unário
            if (formula[a+1].isalpha or formula[a+1] == '('):
                continue
            else:
                print('erro 4')
                return False
        elif(check_binary_connective(formula[a])):
            #Verifica se o caractere é um conectivo binário
            if check_binary_connective(formula[a+1]) or formula[a+1] == '(':
                print('erro 5')
                return False
            continue
        else:
            print('erro 6')
            return False
    return True
          
def divide_formulas (formula):
    controller = 0
    first_half = ''
    second_half = ''
    for caractere in formula:
        if caractere == '>':
            controller = 1
            continue
        if(controller == 0):
            first_half += caractere
        else:
            second_half += caractere

    return first_half, second_half

def list_subformulas(formula, subformulas):
    subformulas.append(formula)
    first_half = ''
    second_half = ''
    first_half, second_half = divide_formulas(formula)
    subformulas.append(first_half)
    subformulas.append(second_half)
    return subformulas


    '''
    subformulas = []
    subformulas.append(formula)
    controller = 0
    first = ''
    second = ''
    for a in formula:
        if a == '>':
            controller = 1
            continue
        if controller == 0:
            first += a
        if controller == 1:
            second += a

    subformulas.append(first)
    subformulas.append(second)
    print(subformulas)
    '''
    
def complexity_formula(formula):
    print('Chegamos em complexity')
    pass

def main():
    formula = input('Insira a fórmula proposicional desejada: ')
    option = int(input('Digite o número da opção desejada: \n 1- Verificador de fórmula proposicional \n 2- Listar todas as subfórmulas \n 3- Calcular a complexidade \n'))

    if(option == 1):
        if(check_formula(formula)):
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