from check import check_auxiliary_symbols, check_binary_connective, check_unary_connective

def check_formula(formula):
    counter_letter = 0
    counter_unary_connective = 0
    counter_auxiliary_symbols = 0
    counter_binary_connective = 0

    if (len(formula) == 1 and formula.isalpha()) or (len(formula) == 2 and (check_unary_connective(formula[0]) and formula[1].isalpha)):
        return True

    ##Feito dia 12
    if ((formula.count('-') == (len(formula)-1)) and formula[-1].isalpha()):
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
                    return False
            else:
                if(formula[a-1] == '(' or check_unary_connective(formula[a-1]) or check_binary_connective(formula[a-1])):
                    return False
            continue
        elif(check_unary_connective(formula[a])):
            #Verifica se o caractere é um conectivo unário MUDEI DIA 12
            if (formula[a+1].isalpha or formula[a+1] == '(') or check_unary_connective(formula[a+1]):
                continue
            else:
                return False
        elif(check_binary_connective(formula[a])):
            #Verifica se o caractere é um conectivo binário
            if check_binary_connective(formula[a+1]) or formula[a+1] == ')':
                return False
            continue
        else:
            return False
    return True
          
def divide_formulas (formula):
    first_half = ''
    second_half = ''
    contAuxiliarySymbol = 0
    contBinaryConnectiveSymbol = 0
    for a in formula:
        if (a == '('):
            contAuxiliarySymbol += 1
        elif check_binary_connective(a):
            contBinaryConnectiveSymbol += 1
        if contAuxiliarySymbol == contBinaryConnectiveSymbol:
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

def remove_extra_parentheses(formula):
    count1 = formula.count('(')
    count2 = formula.count(')')
    while(count1!=count2):
        if(count1>count2):
            formula = formula.replace('(','',1)
            count1 = formula.count('(')
        if(count1<count2):
            formula = formula.replace(')','',1)
            count2 = formula.count(')')
    return formula
            
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

    first_half = remove_extra_parentheses(first_half)
    second_half = remove_extra_parentheses(second_half)

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
