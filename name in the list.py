print ("Hello! You can check if the above name is in the list")
data = {"Александр", "Сергей","Дмитрий","Елена","Андрей","Анастасия","Анна","Екатерина","Алексей","Максим","Иван","Наталья","Владимир","Евгений","Татьяна","Виктория","Ольга","Михаил"}

print ("Enter the name you want to check")
name = input()

exists = name in data
if exists == True:
    print ("Your name is on the list")
if exists == False:
    print ("Your name is not on the list")