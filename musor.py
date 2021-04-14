import sqlite3

a = {'#СТАРТ&': {
        'variants': ['современная'], 'современная': [1, 1.0]
                    },
     'современная': {
         'variants': ['война'], 'война': [1, 1.0]
                     },
     'война': {
         'variants': ['—', 'машин,', 'промышленности,', 'торговли,', 'контор,', 'газет,', 'генералов,', 'министров,', 'железа', 'передовой'],
               '—': [1, 0.1],
               'машин,': [1, 0.1],
               'промышленности,': [1, 0.1],
               'торговли,': [1, 0.1],
               'контор,': [1, 0.1],
               'газет,': [1, 0.1],
               'генералов,': [1, 0.1],
               'министров,': [1, 0.1],
               'железа': [1, 0.1],
               'передовой': [1, 0.1]
                }
     }


with open("max_id.txt") as mifile:
    max_id = int(mifile.read())

# работа с базой данных
con = sqlite3.connect("chain_info")
cur = con.cursor()

string = f"SELECT * FROM words"
words_with_ids = cur.execute(string).fetchall()
memoried_words = [elem[0] for elem in words_with_ids]
for elem in a:
    # коли нет ещё слова из ввода в памяти
    if elem not in memoried_words:
        # создание записи в таблицей слов
        max_id += 1
        string = f"INSERT INTO words(word, id) VALUES({elem}, {max_id})"
        cur.execute(string).fetchall()
        # создание теблицы продолжений этого слова
        string = f"CREATE TABLE {max_id} (cont TEXT, prob);"
        # запись продолжений
        for variant in a[elem]["variants"]:
            string = f"INSERT INTO {max_id}(cont, prob) VALUES({variant}, {a[elem][variant][1]})"
            cur.execute(string).fetchall()
    else:
        pass


con.close()

with open("max_id.txt", "w") as mifile:
    mifile.write(str(max_id))