first_name = "karim"
last_name = "adel"
note = "award: Nobel Peace Prizr"

first_name_cap = first_name.capitalize()  # can capitalize first char
last_name_cap = last_name.capitalize()
print(first_name_cap + " " + last_name_cap)

# To Finding Text ==> find() , index() , rfind() , rindex()

# award_location = note.find("award: ")  # reterun first index of text
award_location = note.index("award: ")
print(award_location)

# Slicing => Getting part of a string value ==> string[start : end]

award_text = note[7:]  # that mean end of string
print(award_text)
