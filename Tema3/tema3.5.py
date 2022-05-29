
s = "În livada noastra avem ciresi, meri, peri și pruni. Care fructe credeti ca se coc primele? \
Variante: perele, merele, prunele și apoi ciresele. Foarte gresit! Corect este: ciresele, merele, perele și apoi prunele."
print(s)

# punctul a)
my_list = s.lower().split()
cleaned_list = []
for element in my_list:
    e = str(element).rstrip(',.?!:')
    if e not in cleaned_list:  # ma asigur ca nu e duplicat
        cleaned_list.append(e)
print("\na) Lista cu cuvinte unice:")
print(cleaned_list)
print("===========================================")

# punctul b)
print("b) Lista ordonata alfabetic folosind functia sorted():")
print(sorted(cleaned_list))
print("===========================================")

# punctul c)
print("c) Lista ordonata alfabetic folosind metoda proprie de sortare:")
unsorted_list = list(cleaned_list)
sl = []

while unsorted_list:   # bucla ruleaza cat timp mai avem elemente in lista initiala
    temp_max = ""
    for i in range(len(unsorted_list)):
        if unsorted_list[i] > temp_max:
            temp_max = unsorted_list[i]  # caut elementul cel mai mare din lista

    unsorted_list.remove(temp_max)  # il sterg din lista initiala
    sl.insert(0, temp_max)          # il adaug in lista ordonata pe prima pozitie

print(sl)
