
def send_email(message, recipient, sender="university.help@gmail.com"):
    if ("@" and (".com" or ".ru" or ".net")) not in (recipient or sender):
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")

    elif recipient == sender:
        print("Нельзя отправить письмо самому себе!")

    elif sender == "university.help@gmail.com":
        print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}.")

    elif sender != "university.help@gmail.com":
        print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.")


send_email('письмо', 'vasyok1337@gmail.com')
send_email('письмо', 'university.help@gmail.com')
send_email('письмо', 'vasyok1337@gmail.net', 'university.help@gmail.com')
send_email('письмо', 'vasyok1337@gmail.net', 'university.help@gmail.net')
