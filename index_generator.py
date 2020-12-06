fp = open("index.html", "w", encoding="utf-8")

print('<meta charset="utf-8">', file=fp)
print("<h1> Заголовок </h1>", file=fp)
print("<p> Обычный текст </p>", file=fp)

fp.close()