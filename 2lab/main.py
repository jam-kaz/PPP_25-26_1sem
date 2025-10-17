s = input('Введите строку из букв латинского алфавита разных регистров:')
for char in s:
    if not ('a' <= char.lower() <= 'z'):
      s = input("Введите строку корректно, по условию!:")

     
def clean_string(input_str):
    count_lower = {}
    count_upper = {}
   
    for char in input_str:
        if char.islower(): 
            count_lower[char] = count_lower.get(char, 0) + 1
        elif char.isupper(): 
            count_upper[char.lower()] = count_upper.get(char.lower(), 0) + 1
   
    cleaned = ''
    for char in input_str:
        lower_char = char.lower()
        if lower_char not in count_lower or lower_char not in count_upper:
            cleaned += char
        else:
            if count_lower[lower_char] <= count_upper[lower_char]:
                cleaned += char
               
    return cleaned
