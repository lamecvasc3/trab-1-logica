
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
                print('Erro 1')
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
            if check_binary_connective(formula[a+1]) or formula[a+1] == ')':
                print('erro 5')
                return False
            continue
        else:
            print('erro 6')
            return False
    return True
          
def divide_formulas (formula):
    first_half = ''
    second_half = ''
    for a in formula:
        if check_binary_connective(a):
            formula = formula.split(a, 1)
            count1 = formula[0].count('&') + formula[0].count('>') + formula[0].count('#')
            count2 = formula[1].count('&') + formula[1].count('>') + formula[1].count('#')
            if count1 == 0:
                formula[0] = formula[0].replace('(', '')
                formula[0] = formula[0].replace(')', '')
            
            if count2 == 0:
                formula[1] = formula[1].replace(')', '')
                formula[1] = formula[1].replace('(', '')

            first_half = formula[0]
            second_half = formula[1]

            return first_half, second_half
 
def is_atomic(formula):
    if (len(formula) == 1 and formula.isalpha()) or (len(formula) == 2 and check_unary_connective(formula[0]) and formula[1].isalpha()):
        return True
    return False

def list_subformulas(formula, subformulas):
    first_half = ''
    second_half = ''
    if(check_unary_connective(formula[0])):
            subformulas.append(formula)
            formula = formula.replace('-', '', 1)

    subformulas.append(formula)

    if (len(formula) == 1):
        return subformulas

    if (len(formula) == 2 and check_unary_connective(formula[0]) and formula[1].isalpha()):
        subformulas.append(formula[1])
        return subformulas
    
    first_half, second_half = divide_formulas(formula)

    subformulas.append(first_half)
    subformulas.append(second_half)
    
    if(is_atomic(first_half)):
        if(check_unary_connective(first_half[0])):
            subformulas.append(first_half[1])
    else:
        list_subformulas(first_half, subformulas)

    if(is_atomic(second_half)):
        if(check_unary_connective(second_half[0])):
            subformulas.append(second_half[1])
    else:
        list_subformulas(second_half, subformulas)

    return subformulas
     
def complexity_formula(formula):
    complexity = 0
    for a in formula:
        for b in a:
            if(check_unary_connective(b) or check_binary_connective(b)):
                complexity += 1
    return complexity

def main():
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

main()