# Regular Expression => Allow you to create a description of a pattern that you want to match
import re  # ro include regx library

five_digit_zip = "98101"
nine_digit_zip = "98101-0003"
phone_number = "234-567-8901"

five_digit_exper = r'\d{5}'
print(re.search(five_digit_exper, five_digit_zip))
print(re.search(five_digit_exper, nine_digit_zip))
print(re.search(five_digit_exper, phone_number))
