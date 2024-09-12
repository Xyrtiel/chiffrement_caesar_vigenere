import random

print(" - TASK 1 -")
print("---------------------------------")

# 1.1
print(42 > 12) # Affiche true
# print(12 = 12) # Affiche une erreur 
print(12 == 12) # Affiche true
print("hello" == "world") # Affiche false
print(218 >= 118) # Affiche true
print("a".upper() == "A") # Affiche true 
# print(1*2*3∗4 <= 9) # Affiche true
print("z" in "azerty") # Affiche true

print("---------------------------------")

# 1.2 
reponse = int(input("Ecrivez 42 : "))
if reponse == 42:
    print("Good job")
else:
    print("...")

print("---------------------------------")

# 1.3
'''inconnu = random.randint(1, 100)
recherche_joueur = int(input("Essaie de deviner mon nombre"))
while inconnu != recherche_joueur :
    if inconnu < recherche_joueur:
        print("Plus petit")
        recherche_joueur = int(input("Essaie de deviner mon nombre"))
    elif inconnu > recherche_joueur:
        print("Plus grand")
        recherche_joueur = int(input("Essaie de deviner mon nombre"))
'''

print("---------------------------------")

# 1.4
reponse = str(input("Bonjour je suis Gandalf. Dis moi un argument pour que je fasse ouvrir la porte : "))
if reponse == "open sesame":
    print("Access Granted")
elif reponse == "Ouvre la porte connard":
    print("J'adore la violence")
else:
    print("Non.")

print("---------------------------------")

# 1.5
reponse = int(input("Ecris un nombre au pif :"))
if reponse == 42:
    print("Ok")
elif reponse <= 21:
    print("OK")
elif reponse > 21 :
    print("OKKKK")
elif reponse/2 < 21 :
    print("Okkkkkkkkkkk")
elif reponse < 45 and reponse >= 45:
    print("Okkkkkkkkkkkkk")
else: 
    print("Faux i guess ?")

print("---------------------------------")

# 1.6 
a = 42
b = 41
if a == b:
    print ("A and B are the sames ")
elif b < a:
    print ("B is equal or lower as A")
elif b != a:
    print ("B his different from A")

print("---------------------------------")
print("- TACHE 2 -")

# 2.1 
for i in range(1, 1001):
    print(i)

print("---------------------------------")

# 2.2
mot = str(input("Ecris moi un mot :"))
mot_double = ""
for i in mot:
    mot_double = mot_double + i*2
print(mot_double) 
print("---------------------------------")

# 2.3
for i in reversed(range(1, 10000)):
    if i % 7 == 0:
        print(i)
print("---------------------------------")

# 2.4
nombre_tres_aleatoire = int(input("Ecris moi encore un nombre : "))
if nombre_tres_aleatoire > -30 and nombre_tres_aleatoire < 30:
    if nombre_tres_aleatoire % 3 == 0 and nombre_tres_aleatoire % 5 == 0:
        print("Fizz Buzz")
    elif nombre_tres_aleatoire % 3 == 0:
        print("Fizz")
    elif nombre_tres_aleatoire % 5 == 0:
        print("Buzz")
else:
    print(nombre_tres_aleatoire)
print("---------------------------------")

# 2.5 
def sing(n):
	if (n == 1):
		objects = 'bottle'
		objectsMinusOne = 'bottles'
	elif (n == 2):
		objects = 'bottles'
		objectsMinusOne = 'bottle'
	else:
		objects = 'bottles'
		objectsMinusOne = 'bottles'


	if (n > 0):
		print(str(n) + " " + objects + " of beer on the wall, " + str(n) + " " + objects + " of beer.")
		print("Take one down and pass it around, " + str(n-1) + " " + objectsMinusOne + " of beer on the wall.")
		print(" ")
	elif (n == 0):
		print("No more bottles of beer on the wall, no more bottles of beer.")
		print("Go to the store and buy some more, 99 bottles of beer on the wall.")
	else:
		print("Error: Wheres the booze?")
bottles = 99

while bottles >= 0:
	sing(bottles)
	bottles -= 1
print("---------------------------------")

# 2.6
def multiples_du_nombre(nombre):
    print("Pour", nombre, "j'ai :")
    for i in reversed(range(2, nombre)):
        if nombre % i == 0:
            multiples = [j for j in range(nombre-1, 1, -1) if j % i == 0]
            print(" ".join(map(str, multiples)))

nombre_alea = int(input("Ecrivez un nombre pour afficher ces multiples : "))
multiples_du_nombre(nombre_alea)
print("---------------------------------")

print("\n", "---")
# CHALLENGE
print("CHALLENGE")
def court_string():
    nombre = int(input("Ecris 1 nombre :"))
    string = str(input("Ecris 1 string :"))
    liste_voyelles=["a","e","i","o","u","y"]
    for i in range(1, len(string)):
        if string[i] == liste_voyelles[i]:
             print(nombre)
             break
        if nombre >= 42:
             print(nombre)
             break
        if nombre == 0:
             break
        else:
             print(string)
             break

court_string()
print("---------------------------------")

print(" - TACHE 3 - ")
# 3.1
def caesar(texte):
    texte = texte.upper()
    cle = 4 # Décalage de trois lettres
    caesared_text = ""
    for i in range(len(texte)):
        if texte[i]==' ':
            caesared_text+=' '
        else:
            asc=ord(texte[i])+cle
            caesared_text+=chr(asc+26*((asc<65)-(asc>=90)))
    print(caesared_text)

caesar("Hello world")
print("---------------------------------")

# 3.2 
def decaesar(texte_ceasered, cle):
    MessageClair=""
    for i in range(len(texte_ceasered)):
        if texte_ceasered[i]==' ':
            MessageClair+=' '
        else:
            asc=ord(texte_ceasered[i])-cle
            MessageClair+=chr(asc+26*((asc<65)-(asc>90)))
    print(MessageClair)

decaesar("JC QAPGNR NMSP BCAMBCP LC BCTPYGR NYQ CRPC JMLE Y DYGPC HC JC BMLLCPYG QSP AC KCKC DMPSK", 24)
print("---------------------------------")

# 3.3
def vigenere(texte_decrypt, cle):
    indice_cle = 0
    msg_code = ""
    for i in range(0, len(texte_decrypt)):
        if 'A' <= texte_decrypt[i] <= 'Z':
            msg_code += chr(((((ord(texte_decrypt[i]) - ord('A')) + ord(cle[indice_cle]) - ord('A'))) % 26) + ord('A'))
            ''' Ici, on ajoute le caractère ASCII du texte décrypté que l'on doit récupérer via la fonction ord(). 
            Ensuite il nous faut enlever le décimal de A pour enlever tout le reste des caractères ASCII
            et d'y ajouter derrière le décimal de la lettre de la clé, qui elle, correspond au caractère de la clé correspondante. 
            On doit alors récupérer le reste avec %. Enfin, il ne reste plus qu'à ajouter le décimal de A pour obtenir la nouvelle lettre
            correspondante avec la fonction chr(). '''
        if 'a' <= texte_decrypt[i] <= 'z':
            msg_code += chr(((((ord(texte_decrypt[i]) - ord('a')) + ord(cle[indice_cle]) - ord('A'))) % 26) + ord('a'))
        else:
             msg_code += texte_decrypt[i]
    print(msg_code)

print("Je chiffre, je chiffre, je chiffre :")
vigenere("JE SUIS SUIS LIBERTINEUHH", "JE SUIS UNE CATHIN")
vigenere("Chaussésss au Moinneeeeee", "Jadore le beurre")
print("---------------------------------")

def devigenere(texte_decrypt, cle):
    indice_cle = 0
    msg_decode = ""
    for i in range(len(texte_decrypt)):
        if 'A' <= texte_decrypt[i] <= 'Z':
            msg_decode += chr((ord(texte_decrypt[i]) - ord(cle[indice_cle]) + 26) % 26 + ord('A'))
            ''' Ici, on ajoute le caractère ASCII du texte décrypté que l'on doit récupérer via la fonction ord(). 
            Ensuite il nous faut enlever le décimal de A pour enlever tout le reste des caractères ASCII
            et d'y ajouter derrière le décimal de la lettre de la clé, qui elle, correspond au caractère de la clé correspondante. 
            On doit alors récupérer le reste avec %. Enfin, il ne reste plus qu'à ajouter le décimal de A pour obtenir la nouvelle lettre
            correspondante avec la fonction chr(). '''
            indice_cle = (indice_cle + 1) % len(cle)
        elif 'a' <= texte_decrypt[i] <= 'z':
            msg_decode += chr((ord(texte_decrypt[i]) - ord(cle[indice_cle].upper()) + 26) % 26 + ord('a'))
            indice_cle = (indice_cle + 1) % len(cle)
        else:
            msg_decode += texte_decrypt[i]
    print(msg_decode)

print("---------------------------------")
print("Je déchiffre, je déchiffre, je déchiffre :")
devigenere("LXFOPVEFRNHR", "LEMON")
print("---------------------------------")

# 3.4
# AIDE : https://stackoverflow.com/questions/59094006/breaking-vigenere-only-knowing-key-length
# Code traduit à partir d'un code en Javascript :
def vigenere_sans_contenu_cle(encrypted_text, key_length):
    most_common_char_overall = 'E'
    blocks = [encrypted_text[i:i + key_length] for i in range(0, len(encrypted_text), key_length)]

    print("Individual blocks are:")
    for block in blocks:
        print(block)

    digit_to_counts = [{} for _ in range(key_length)]

    for block in blocks:
        for i, char in enumerate(block):
            digit_to_counts[i][char] = digit_to_counts[i].get(char, 0) + 1

    digit_to_frequencies = []
    for counts in digit_to_counts:
        total_character_count = sum(counts.values())
        frequencies = sorted([(char, count / total_character_count) for char, count in counts.items()], key=lambda x: x[1], reverse=True)
        digit_to_frequencies.append(frequencies)

    print("Frequency distribution for each digit is:")
    for frequencies in digit_to_frequencies:
        print(frequencies)

    key_builder = []
    for frequencies in digit_to_frequencies:
        most_frequent_char = frequencies[0][0]
        key_int = ord(most_frequent_char) - ord(most_common_char_overall)
        key_int = key_int if key_int >= 0 else key_int + 26
        key = chr(ord('A') + key_int)
        key_builder.append(key)

    key = ''.join(key_builder)
    print("The guessed key is:", key)

    print("Decrypted message:")
    print(decrypt(encrypted_text, key))

def decrypt(encrypted_message, key):
    decrypt_builder = []
    digit = 0
    for encrypted_char in encrypted_message:
        key_for_digit = key[digit]
        decrypted_char_int = ord(encrypted_char) - ord(key_for_digit)
        decrypted_char_int = decrypted_char_int if decrypted_char_int >= 0 else decrypted_char_int + 26
        decrypted_char = chr(decrypted_char_int + ord('A'))
        decrypt_builder.append(decrypted_char)
        digit = (digit + 1) % len(key)
    return ''.join(decrypt_builder)

vigenere_sans_contenu_cle("BYOIZRLAUMYXXPFLPWBZLMLQPBJMSCQOWVOIJPYPALXCWZLKXYVMKXEHLIILLYJMUGBVXBOIRUAVAEZAKBHXBDZQJLELZIKMKOWZPXBKOQALQOWKYIBKGNTCPAAKPWJHKIAPBHKBVTBULWJSOYWKAMLUOPLRQOWZLWRSLEHWABWBVXOLSKOIOFSZLQLYKMZXOBUSPRQVZQTXELOWYHPVXQGDEBWBARBCWZXYFAWAAMISWLPREPKULQLYQKHQBISKRXLOAUOIEHVIZOBKAHGMCZZMSSSLVPPQXUVAOIEHVZLTIPWLPRQOWIMJFYEIAMSLVQKWELDWCIEPEUVVBAZIUXBZKLPHKVKPLLXKJMWPFLVBLWPDGCSHIHQLVAKOWZSMCLXWYLFTSVKWELZMYWBSXKVYIKVWUSJVJMOIQOGCNLQVXBLWPHKAOIEHVIWTBHJMKSKAZMKEVVXBOITLVLPRDOGEOIOLQMZLXKDQUKBYWLBTLUZQTLLDKPLLXKZCUKRWGVOMPDGZKWXZANALBFOMYIXNGLZEKKVCYMKNLPLXBYJQIPBLNMUMKNGDLVQOWPLEOAZEOIKOWZZMJWDMZSRSMVJSSLJMKMQZWTMXLOAAOSTWABPJRSZMYJXJWPHHIVGSLHYFLPLVXFKWMXELXQYIFUZMYMKHTQSMQFLWYIXSAHLXEHLPPWIVNMHRAWJWAIZAAWUGLBDLWSPZAJSCYLOQALAYSEUXEBKNYSJIWQUKELJKYMQPUPLKOLOBVFBOWZHHSVUIAIZFFQJEIAZQUKPOWPHHRALMYIAAGPPQPLDNHFLBLPLVYBLVVQXUUIUFBHDEHCPHUGUM", 6)

print("---------------------------------")

'''
# 3.5
def vigenere_sans_cle(encrypted_text):
'''