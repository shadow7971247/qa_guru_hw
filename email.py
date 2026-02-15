from datetime import datetime

# Создайте словарь email
email = {
    "subject": "Quarterly Report",
    "from": "Alice.Cooper@Company. ",
    "to": " bob_smith@Gmail.com ",
    "body": "Hello Bob,\n\tHere is the quarterly report."
    "\n\tPlease review and let me know your feedback."
    "\n\nBest,\nAlice",
}


# 2. Добавьте дату отправки
send_date = datetime.now().strftime("%Y-%m-%d")
email["date"] = send_date


# 3. Нормализуйте e-mail адреса
email["from"] = email["from"].strip().lower()
email["to"] = email["to"].strip().lower()


# 4. Извлеките логин и домен отправителя
login, domain = email["from"].split("@")


# 5. Создайте сокращённую версию текста
short_body: str = email["body"][:10] + "..."
email["short_body"] = short_body


# 6. Списки доменов
personal_domains = [
    "gmail.com",
    "list.ru",
    "yahoo.com",
    "outlook.com",
    "hotmail.com",
    "icloud.com",
    "yandex.ru",
    "mail.ru",
    "list.ru",
    "bk.ru",
    "inbox.ru",
]
corporate_domains = [
    "company.ru",
    "corporation.com",
    "university.edu",
    "organization.org",
    "company.ru",
    "business.net",
]


# 7. Проверьте что в списке личных и корпоративных доменов нет пересечений
no_domain_overlap = not (set(personal_domains) & set(corporate_domains))


# 8. Проверьте «корпоративность» отправителя
is_corporate = domain in corporate_domains


# 9. Соберите «чистый» текст сообщения
email["clean_body"] = email["body"].replace("\t", " ").replace("\n", " ")


# 10. Сформируйте текст отправленного письма
email["sent_text"] = f"""
Кому: {email['to']}, от {email['from']}
Тема: {email['subject']}, дата {email['date']}
{email['clean_body']}
"""


# 11. Рассчитайте количество страниц печати
text_length = len(email["sent_text"])
pages = (text_length + 499) // 500


# 12. Проверьте пустоту темы и тела письма
(is_subject_empty, is_body_empty) = (not email["subject"], not email["body"])


# 13. Создайте «маску» e-mail отправителя
masked_from_v2 = f"{login[:2]}***@{domain}"


# 14. Удалите из списка личных доменов
personal_domains.remove("list.ru")
personal_domains.remove("bk.ru")
if "list.ru" in personal_domains:
    personal_domains.remove("list.ru")


print(f"1. Создайте словарь email:\n{email}")
print(f"2. Добавьте дату отправки: {email["date"]}")
print(f"3. Нормализуйте e-mail адреса: {email["from"]}, {email["to"]}")
print(f"4. Извлеките логин и домен отправителя: {login}, {domain}")
print(f"5. Создайте сокращённую версию текста: {email["short_body"]}")
print(f"7. Проверьте что в списке личных и корпоративных доменов нет пересечений: {no_domain_overlap}")
print(f"8. Проверьте «корпоративность» отправителя: {is_corporate}")
print(f"9. Соберите «чистый» текст сообщения:\n{email["clean_body"]}")
print(f"10. Сформируйте текст отправленного письма:\n{email["sent_text"]}")
print(f"11. Рассчитайте количество страниц печати: {pages}")
print(f"12. Проверьте пустоту темы и тела письма: Тема пустая? {is_subject_empty}, тело пустое? {is_body_empty}")
print(f"13. Создайте «маску» e-mail отправителя: {masked_from_v2}")
print(f"14. Удалите из списка личных доменов: {personal_domains}")