has_high_incoming = False
has_good_credit = True
has_criminal_record = True

if has_high_incoming and has_good_credit and not has_criminal_record:
    print('Eligible to loan')
elif has_high_incoming or has_good_credit and not has_criminal_record:
    print('Possible to lean')

name = input('Insert a name: ')

if len(name) < 3:
    print('Name is too short')

elif len(name) > 50:
    print('Name is too long')

else:
    print('Perfect')