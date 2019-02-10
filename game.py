import random
i=1
array_P = []
array_AI =[]
#comp = random.randint(1, 5)
score_AI=0
score_P=0
def score_count():
    global first,comp,score_P,score_AI
    if first > comp:
        score_P=score_P+1
        print("Вы победили. Счет: ",score_P, score_AI )
    elif first == comp:
        print("Ничья. Счет: ",score_P, score_AI )
    elif first<comp:
        score_AI=score_AI+1
        print("Вы проиграли. Счет: ",score_P ,score_AI )

def input_ppl():
    global first,comp, array_P, array_AI
    first = input("Введите число: ")
    first = int(first)

    if first in array_P:
        print("Вы уже вводили такое число. Используйте другое")
        return input_ppl()
    else:
        print("Ваше число: ",first)
        array_P.append(first)

    comp = random.randint(1, 5)
    while comp in array_AI:
        comp = random.randint(1, 5)
    array_AI.append(comp)
    
    print("Число противника: ", comp)


while len(array_AI)<5:
    print("Раунд",i)
    input_ppl()
    score_count()
    i=i+1
