import re
names = []
numbers=[]
emails=[]
with open('task.txt', 'r') as f:
    for line in f:
        name = re.findall(r'[A-Z][a-z]+', line)
        names.append(name)
        number = re.findall(r'\d{10}',line)
        numbers.append(number)
        email = re.findall(r'[a-z]+@gmail\.com',line)
        emails.append(email)
print(emails)
print(numbers)
print(names)

#task.txt
#Ahmed Hafez-0102345678-ahmed@gmail.com
#ali@gmail.com,0124342342,Ali Osama