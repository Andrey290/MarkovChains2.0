import random

new_corpus = input()  # будет браться из json файла

SEPARATOR = "#РАЗДЕЛИТЕЛЬ&"
STRING_OPENING = "#СТАРТ&"
STRING_ENDING = "#КОНЕЦ&"
END_SYMBOLS = ["!", "?", ".", "...", "\n"]


# функция рассчёта вероятности каждого звена(link) в цепи(chain)
def chain_probability_calc(word_dictionary):
    # можно было заранее задать его в самом словаре, но я не думаю, что это повредит
    total_score = len(word_dictionary["variants"])
    for key in word_dictionary["variants"]:
        word_dictionary[key][1] = word_dictionary["variants"].count(key) / total_score
    return word_dictionary


def generation(bigrams_dictionary):
    work_massive = [STRING_OPENING]  # рабочая строка
    while work_massive[-1] != STRING_ENDING:
        cont = bigrams_dictionary[work_massive[-1]]  # словарь продолжений
        work_list = []  # рабочий список
        control_list = []  # костыль чтобы не думать
        for elem in cont["variants"]:
            if elem not in control_list:
                work_list.append([elem, cont[elem][1]])
                control_list.append(elem)

        random.shuffle(work_list)  # перемешивание порядка
        fit_count = random.randrange(0, int(sum([i[1] * 10 for i in work_list])) - 1, 1)
        j = 0
        chosen_word = STRING_ENDING
        # while fit_count > 0 and j < len(work_list):
        n = 0
        while n < 15:
            fit_count -= work_list[j][1] * 10
            chosen_word = work_list[j][0]
            n += 1
        work_massive.append(chosen_word)
    if len(work_massive) > 2:
        work_massive = work_massive[:-1]
        work_massive = work_massive[1::]
        work_massive[-1] += "."
        return " ".join(work_massive).capitalize()
    return "Ничего не придумалось."



phrases = new_corpus.lower()
# phrases = phrases.replace(",", " ")
# print(phrases)
for elem in END_SYMBOLS:
    phrases = phrases.replace(elem, SEPARATOR)
list_of_phrases = [f"{STRING_OPENING} {elem} {STRING_ENDING}" for elem in phrases.split(SEPARATOR)]

# запись биграм
dct_of_bigrams = {}
bigram_keys = []
for phrase in list_of_phrases:
    phrase = phrase.split()
    if phrase != [STRING_OPENING, STRING_ENDING]:
        for i in range(len(phrase) - 1):
            if phrase[i] not in bigram_keys:
                bigram_keys.append(phrase[i])
                dct_of_bigrams[phrase[i]] = {"variants": [phrase[i + 1]],  # возможные варианты слов
                                             phrase[i + 1]: [1, 1],  # слово : [чило вхождений, процент вероятности]
                                             }
            elif [phrase[i + 1]] in dct_of_bigrams[phrase[i]]["variants"]:
                dct_of_bigrams[phrase[i]][phrase[i + 1]][0] += 1
            else:
                dct_of_bigrams[phrase[i]]["variants"].append(phrase[i + 1])
                dct_of_bigrams[phrase[i]][phrase[i + 1]] = [1, 1]

# словарь{слово: {список продолжений: [продолжение1],
#                  продолжение1: [количество, верояность]}}
for word in bigram_keys:
    dct_of_bigrams[word] = chain_probability_calc(dct_of_bigrams[word])

print(bigram_keys)
print(dct_of_bigrams)
print(generation(dct_of_bigrams))
