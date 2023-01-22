import re
from pprint import pprint
# читаем адресную книгу в формате CSV в список contacts_list
import csv
with open("phonebook_raw.csv", encoding="utf8") as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)

# TODO 1: выполните пункты 1-3 ДЗ
fio_pattern = "(\w+)\s(\w+)\s(\w+)*"
phone_pattern = "(\+7|8)\s*\(*(\d{3,})\)*[\s-]*(\d{3,})[\s-]*(\d{2,})[\s-]*(\d{2,})\s*\(*\w*[.]*\s*(\d{4})*\)*"
contacts_list_new = []

for record in contacts_list:
  for element in record:
    result = re.search(phone_pattern, element)
    if result != None:
      formatted_result = f'+7({result.group(2)}){result.group(3)}-{result.group(4)}-{result.group(5)}'
      if result.group(6) != None:
        formatted_result = formatted_result + f' доб.{result.group(6)}'
      record[5] = formatted_result

  fio = record[0]+" "+record[1]+" "+record[2]
  fio_strip = fio.lstrip()
  fio_groups = re.search(fio_pattern, fio_strip)
  record[0] = fio_groups.group(1)
  record[1] = fio_groups.group(2)
  if fio_groups.group(3) != None:
    record[2] = fio_groups.group(3)

  for i, x in enumerate(contacts_list_new):
    # print(i, x)
    if record[0] and record[1] in x:
      print(f'lastname and name {record[0]} {record[1]} match! merging...')

      # идём по списку обрабатываемой записи, начиная с отчества
      for item in record[2:]:
        # если какой то елемент данных есть, то добавляем его в найденную запись
        if item != "":
          print(f"данные записи для слияния: {item}")
          print(f"данные изменяемой записи: {contacts_list_new[i][record.index(item)]}")
          if contacts_list_new[i][record.index(item)] == "":
            print("надо добавить")
            contacts_list_new[i][record.index(item)] = item
      break
  else:
    print("adding to list")
    contacts_list_new.append(record)

print(contacts_list_new)

# pprint(f'{contacts_list_new}')

# TODO 2: сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV
with open("phonebook_new.csv", "w") as f:
  datawriter = csv.writer(f, delimiter=',')
  # Вместо contacts_list подставьте свой список
  datawriter.writerows(contacts_list_new)