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

# ITERATE THRU SQUAD LIST 
# for name in squad_713:
#   print(name)

# def get_names(list):
#   for name in list:


# CREATE FILE WITH PYTHON
ga_file = open('general_assembly.txt', 'r+')
# print(ga_file.readlines())
for name in squad_713:
  ga_file.write(f'{name} \n')
ga_file.close()

# WRITE EACH PERSON TO A FILE

# PUT EACH PERSON ON A NEW LINE
