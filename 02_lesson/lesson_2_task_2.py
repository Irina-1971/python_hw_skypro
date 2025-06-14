def is_year_leap(num):
    if num % 4 == 0:
        return True
    else:
        return False
    
year = input("Введите год: ")
result = is_year_leap(int(year))
print("Год ", year, ":", result)
