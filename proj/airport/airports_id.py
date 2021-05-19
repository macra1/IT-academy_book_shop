
# Читает файл и ищет совпадение с заданным code(кодом аэропорта)
# Возвращает Город и Страну
def read_and_filter(code, filename="sup.txt"):
    code = code.upper()
    with open(filename, encoding="utf-8") as file:
        for i in file:
            i = i.split("	")
            if i[0] == code:
                if len(i) == 5:
                    answer = f"{i[4]}, {i[3]}"
                    return answer
                else:
                    return i[-1]


if __name__ == "__main__":
    a = read_and_filter("zzz")
    print(a)
