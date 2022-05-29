
s = "În livada noastra avem ciresi, meri, peri și pruni. Care fructe credeti ca se coc primele? \
Variante: perele, merele, prunele și apoi ciresele. Foarte gresit! Corect este: ciresele, merele, perele și apoi prunele."
print(s)

# a)
nr_propozitii = 0
for l in s:
    if l == "." or l == "?" or l == "!":
        nr_propozitii += 1
print("a) Numarul de propozitii: " + str(nr_propozitii))

# b)
nr_cuvinte = 1  # compensez lipsa spatiului de la sfarsitul ultimului cuvant
for i in s:
    if i == " ":
        nr_cuvinte += 1
print("b) Numarul de cuvinte: " + str(nr_cuvinte))

# c)
my_list = s.lower().split()
cleaned_list = []
for element in my_list:
    cleaned_list.append(str(element).strip(',.?!:'))
print("c) Lista curatata:")
print(cleaned_list)

