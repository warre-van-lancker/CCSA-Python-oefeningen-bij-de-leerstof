def evalueer_postfix(expressie):
    stapel = []
    for symbool in expressie:
        if symbool in ['+', '-', '*', '/']:
            b = stapel.pop()
            a = stapel.pop()
            match symbool:
                case '+': resultaat = a + b
                case '-': resultaat = a - b
                case '*': resultaat = a * b
                case '/': resultaat = a / b
            stapel.append(resultaat)
        else:
            stapel.append(float(symbool))
    return stapel.pop()

def infix_naar_postfix(expressie):
    stapel = []
    postfix = []
    for symbool in expressie:
        if symbool in ['+', '-', '*', '/']:
            while len(stapel) > 0 and gelijke_of_hogere_prioriteit(stapel[-1], symbool):
                postfix.append(stapel.pop())
            stapel.append(symbool)
        elif symbool == '(':
            stapel.append(symbool)
        elif symbool == ')':
            while len(stapel) > 0 and stapel[-1] != '(':
                postfix.append(stapel.pop())
            stapel.pop()
        else:
            postfix.append(symbool)
    while len(stapel) > 0:
        postfix.append(stapel.pop())
    return postfix

def rekenmachine(s):
    return evalueer_postfix(infix_naar_postfix(s.split()))

def gelijke_of_hogere_prioriteit(symbool, top):
    prioriteiten = {'(': 0, '+': 1, '-': 1, '*': 2, '/': 2}
    return prioriteiten[symbool] >= prioriteiten[top]