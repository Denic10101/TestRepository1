import random
import datetime

times = ["утром", "днём", "вечером", "ночью", "после обеда", "перед сном"]
advices = ["ожидайте", "предостерегайтесь", "будьте открыты для"]
promises = ["гостей из забытого прошлого", "встреч со старыми знакомыми",
            "неожиданного праздника", "приятных перемен"]


def generate_prophecies(total_num=5, num_sentences=3):
    prophecies = []

    i = 0
    while i < total_num:
        j = 0
        forecast = ""
        while j < num_sentences:
            t = random.choice(times)
            a = random.choice(advices)
            p = random.choice(promises)

            full_sentence = t.title() + " " + a + " " + p + "."
            if j != num_sentences - 1:
                full_sentence = full_sentence + " "

            forecast = forecast + full_sentence
            j = j + 1

        prophecies.append(forecast)
        i = i + 1

    return prophecies
fp = open("index.html", "w", encoding="utf-8")
print('<meta charset="utf-8">', file=fp)
print("<h1> Что день " + str(datetime.date.today()) + " готовит </h1>", file=fp)
for item in generate_prophecies():
    print("<p> " + item + " </p>", file=fp)
    print("<p> </p>", file=fp)

fp.close()
#print(len(generate_prophecies()))
