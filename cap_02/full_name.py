#!/usr/bin/env python3

first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}" # como formatar string com f-strings
# full_name = "{} {}".format(first_name, last_name) # como formatar usando o método .format
message = f"Hello, {full_name.title()}!"
print(message)
