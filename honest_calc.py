msg_ = [
    "Enter an equation\n",
    "Do you even know what numbers are? Stay focused!",
    "Yes ... an interesting math operation. You've slept through all classes, haven't you?",
    "Yeah... division by zero. Smart move...",
    "Do you want to store the result? (y / n):\n",
    "Do you want to continue calculations? (y / n):\n",
    " ... lazy",
    " ... very lazy",
    " ... very, very lazy",
    "You are",
    "Are you sure? It is only one digit! (y / n)\n",
    "Don't be silly! It's just one number! Add to the memory? (y / n)\n",
    "Last chance! Do you really want to embarrass yourself? (y / n)\n",
]
memory = 0.0
operation = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '*': lambda x, y: x * y,
    '/': lambda x, y: x / y
}
main = True


def is_one_digit(v):
    return -10 < v < 10 and v.is_integer()


def check(v1, v2, v3):
    msg = ""
    msg += msg_[6] if is_one_digit(v1) and is_one_digit(v2) else ""
    msg += msg_[7] if v1 == 1 or v2 == 1 and v3 == "*" else ""
    msg += msg_[8] if v1 == 0 or v2 == 0 and v3 in ["*", "+", "-"] else ""
    print(msg_[9] + msg) if msg != "" else ""


def ask(msg):
    """Ask a question hoping only yes or no answer(y/n).
    If not it will ask again the 'msg' until it gets y/n"""
    answer = ""
    while answer != 'y' and answer != 'n':
        answer = input(msg)
    return answer == 'y'



def save(memory, result):
    if is_one_digit(result):
        msg_index = 10
        while True:
            if ask(msg_[msg_index]):
                if msg_index < 12:
                    msg_index += 1
                else:
                    return result
            else:
                return memory
    else:
        return result


while main:
    x, oper, y = input(msg_[0]).split()
    try:
        x = memory if x == "M" else float(x)
        y = memory if y == "M" else float(y)
        check(x, y, oper)
        result = operation[oper](x, y)
        print(result)
        if ask(msg_[4]):
            memory = save(memory, result)
        main = ask(msg_[5])
    except ValueError:
        print(msg_[1])
    except KeyError:
        print(msg_[2])
    except ZeroDivisionError:
        print(msg_[3])
