def evaluate(expression):
    log = []
    def recursive_eval(expr):
        while '(' in expr:
            start = expr.rfind('(')
            end = expr.find(')', start)
            if start != -1 and end != -1:
                inner_expr = expr[start+1:end]
                result = str(eval(inner_expr))
                log.append(f'Вычисляем выражение {inner_expr} = {result}')    
                expr = expr[:start] + result + expr[end+1:]
        final_result = eval(expr)
        log.append(f'Итоговый результат: {final_result}')
        return final_result, log
    return recursive_eval(expression)

if __name__ == "__main__":
    expression = input("Введите выражение: ")
    result, steps = evaluate(expression)
    print("путь вычислений:")
    for step in steps:
        print(step)
    print(f'Окончательный результат: {result}')
