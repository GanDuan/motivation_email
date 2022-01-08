import smtplib
import datetime as dt
import random


try:
    file = open("quotes_rest.txt")
except FileNotFoundError:
    file = open("quotes.txt")
finally:
    data = file.readlines()
    sentence = random.choice(data)

    data.remove(sentence)
    with open("quotes_rest.txt", "w") as file:
        for item in data:
            file.write(item)
    file.close()

now = dt.datetime.now()
now_weekday = now.weekday()

my_email = "gan.duan001@gmail.com"
password = "zswdmm111"
receiver = "gan.duan1993@gmail.com"

with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    if now_weekday == 3:
        message = sentence
        connection.sendmail(from_addr=my_email, to_addrs=receiver, msg=f"Subject:Monday motivation\n\n{message}")
#
