squad_713 = [
    'Alice',
    'Alpha',
    'Anthony',
    'Barent',
    'Branden',
    'Channee',
    'Cristina',
    'Cabassa',
    'Elaine',
    'Han',
    'Irene',
    'Joshua',
    'Levin',
    'Lizz',
    'Margaret',
    'Martin',
    'Nicholas',
    'Philip',
    'Rohun',
    'Sameh',
    'Shane',
    'Steven',
    'Subrata',
    'Tanner',
    'Adam',
    'Pete',
    'Rome',
    'Taylor'
]


# DONE create file
ga_file = open('general_assembly.txt', 'r+')
# DONE iterate thru squad list
for name in squad_713:
  # DONE write each person to a file on a new line
  ga_file.write(f'{name} \n')
ga_file.close()
