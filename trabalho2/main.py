from formula import check_formula, list_subformulas

def create_table(n_row, n_column):
    table = []
    for a in range(n_row+1):
        row = []
        for b in range(n_column):
            row.append('#')
        table.append(row)
    return table

def add_atomic_values(table, n_letters, complete):
    if (n_letters == 1):
        table[1][0] = 0
        table[2][0] = 1
        complete.append(table[0][0])
    elif(n_letters == 2):
        for a in range(1, 3):
           table[a][0] = 0
           table[a+2][0] = 1
        for a in range(1,4,2):
            table[a][1] = 0
            table[a+1][1] = 1
        complete.append(table[0][0])
        complete.append(table[0][1])
    elif(n_letters==3):
        for a in range(1,5):
            table[a][0] = 0
            table[a+4][0] = 1
        for a in range(1,3):
            table[a][1] = 0
            table[a+2][1] = 1 
            table[a+4][1] = 0
            table[a+6][1] = 1
        for a in range(1,8,2):
            table[a][2] = 0
            table[a+1][2] = 1
        complete.append(table[0][0])
        complete.append(table[0][1])
        complete.append(table[0][2])
    elif(n_letters==4):
        for a in range(1,9):
            table[a][0] = 0
            table[a+8][0] = 1
        for a in range(1,5):
            table[a][1] = 0
            table[a+4][1] = 1
            table[a+8][1] = 0
            table[a+12][1] = 1
        for a in range(1,3):
            table[a][2] = 0
            table[a+2][2] = 1 
            table[a+4][2] = 0
            table[a+6][2] = 1
            table[a+8][2] = 0
            table[a+10][2] =1
            table[a+12][2] = 0
            table[a+14][2] = 1
        for a in range(1,17,2):
            table[a][3] = 0
            table[a+1][3] = 1
        complete.append(table[0][0])
        complete.append(table[0][1])
        complete.append(table[0][2])
        complete.append(table[0][3])
 
    return table,complete

def add_negative_atomic_values(table, subformulas, complete):
    negative = []
    index = []
    index_negative = []
    for a in subformulas:
        if(a[0] == '-' and len(a)==2):
            negative.append(a)
            index_negative.append(subformulas.index(a))

    for a in negative:
        for b in subformulas:
            if(a[1:] == b):
                index.append(subformulas.index(b))

    for b,c in zip(index_negative, index): 
        for a in range(1, len(table)):
            table[a][b] = 0 if table[a][c] == 1 else 1
        complete.append(table[0][b])
    
    return table, complete

def add_negative_formula_values(table, subformulas, complete, formula, b):
    index_formula = subformulas.index(b)
    index_negative_formula = subformulas.index(formula)

    for a in range(1, len(table)):
        table[a][index_negative_formula] = 0 if table[a][index_formula] == 1 else 1
    
    complete.append(formula)

    return table, complete

def add_formula_values(table, subformulas, complete, formula):
    first_half = ''
    second_half = ''
    contAuxiliarySymbol = 0
    contBinaryConnectiveSymbol = 0
    binaryConnectiveSymbol = ''
    for a in range(len(formula)):
        if (formula[a]=='('):
            contAuxiliarySymbol += 1
        elif ((formula[a]=='#') or (formula[a]=='&') or (formula[a]=='>')):
            contBinaryConnectiveSymbol += 1
        if contAuxiliarySymbol == contBinaryConnectiveSymbol:
            if((formula[a]=='#') or (formula[a]=='&') or (formula[a]=='>')):
                binaryConnectiveSymbol = formula[a]
                first_half = formula[:a].replace('(','',1)
                second_half = formula[a:].replace(')','',1).replace(formula[a],'',1)
                break
 
    if first_half in complete:
        index_first_half = subformulas.index(first_half)
    if second_half in complete:
        index_second_half = subformulas.index(second_half)
    
    index_formula = subformulas.index(formula)

    for a in range(1, len(table)):
        if binaryConnectiveSymbol == '&':
            if(table[a][index_first_half] == 1 and table[a][index_second_half] ==1):
                table[a][index_formula] = 1
            else:
                table[a][index_formula] = 0

        elif binaryConnectiveSymbol == '>':
            if(table[a][index_first_half] == 1 and table[a][index_second_half] == 0):
                table[a][index_formula] = 0
            else:
                table[a][index_formula] = 1

        elif binaryConnectiveSymbol == '#':
            if(table[a][index_first_half] == 0 and table[a][index_second_half] == 0):
                table[a][index_formula] = 0
            else:
                table[a][index_formula] = 1

    complete.append(formula)
    return table, complete

def add_values(table, subformulas, complete):
    subformulas = sorted(subformulas, key=len)
    
    for formula in subformulas:
        if formula in complete:
            continue
        else:
            b=formula[1:]
            if b in complete:
                table, complete = add_negative_formula_values(table, subformulas, complete, formula, b)
            else:
                table, complete = add_formula_values(table, subformulas, complete, formula)
                
    return table

def truth_table(subformulas):
    subformulas = sorted(subformulas, key=len)
    n_column =  len(subformulas)
    n_letters = 0
    complete = []
    for a in subformulas:
        if len(a) == 1:
            n_letters += 1
    
    n_row = 2**n_letters
    
    table = create_table(n_row, n_column)
    
    for a in range(len(subformulas)):
        table[0][a] = subformulas[a]

    if(len(subformulas)==1):
        table, complete = add_atomic_values(table, n_letters, complete)
        return table

    if((len(subformulas)==2) and (subformulas[1][0]=='-')):
        table, complete = add_atomic_values(table, n_letters, complete)
        table, complete = add_negative_atomic_values(table, subformulas, complete)
        return table

    table, complete = add_atomic_values(table, n_letters, complete)
    table, complete = add_negative_atomic_values(table, subformulas, complete)
    table = add_values(table,subformulas, complete)

    return table
    
def logical_consequence(table):
    for a in range(1, len(table)):
        counter = table[a].count(0)
        if (counter > 0):
            continue
        else:
            return 'Válida'
    return 'Inválida'

def check_satisfiability(table, satisfiability):
    cont0 = 0
    cont1 = 0
    for a in range(1, len(table)):
        if(table[a][-1] == 0):
            cont0 +=1
        elif(table[a][-1] == 1):
            cont1 +=1
    if(cont0==(len(table)-1)):
        satisfiability.append('Insatisfazível')
    if(cont1 == (len(table)-1)):
        satisfiability.append('Válida')
    if(cont0>0):
        satisfiability.append('Falsificável')
    if(cont1>0):
        satisfiability.append('Satisfazível')
    
    
    return satisfiability
    
def main():
    option = int(input('Digite o número da opção desejada: \n 1- Tabela verdade \n 2- Consequência Lógica \n'))

    if(option == 1):
        formula = input('Insira a fórmula proposicional desejada: ')
        if(check_formula(formula)):
            subformulas = []
            satisfiability = []
            subformulas = set(list_subformulas(formula, subformulas))
            table = truth_table(subformulas)
            satisfiability = check_satisfiability(table, satisfiability)
            for a in range(len(table)):
                print(table[a]) 
            print(satisfiability)
            
    elif(option == 2):
        quantity_formulas = int(input('Insira quantas formulas tem seu conjunto de fórmulas: '))
        count = 0 
        conjunto_formulas = []
        subformulas = []
        while(count != quantity_formulas):
            formula = input('Insira a fórmula:')
            conjunto_formulas.append(formula)
            count+=1
        
        for a in conjunto_formulas:
            subformulas = (list_subformulas(a, subformulas))

        formula = input('Insira a formula para verificar a consequência lógica: ')
        subformulas = list_subformulas(formula, subformulas)

        subformulas = set(subformulas)
        print(subformulas)
        table = truth_table(subformulas)

        res = logical_consequence(table)
        print(res)
    else:
        print('Dígito não reconhecido.')

main()