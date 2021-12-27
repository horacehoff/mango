# This is only R&D
input = 'declare my_var = "Hello There"'
output = ""
tokens = input.split(" ")
action_token = tokens[1]
value_token = input.split("=", 1)[1].lstrip()