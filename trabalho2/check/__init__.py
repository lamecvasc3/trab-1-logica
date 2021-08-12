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
