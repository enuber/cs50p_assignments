def main():
    x, y, z = input('Expression ').split(' ')
    answer = doMath(x, y, z)
    print(f"{answer:.1f}")

def doMath(n1, operation, n2):
    n1 = float(n1)
    n2 = float(n2)
    match operation:
        case '+':
            return n1 + n2
        case '-':
            return n1 - n2
        case '*':
            return n1 * n2
        case '/':
            return n1 / n2

main()

# check50 cs50/problems/2022/python/interpreter
