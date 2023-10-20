if __name__ == '__main__':
    '''
    to know what type a variable is use: type()
    
    convertion types:
    float()
    int()
    bool()
    
    '''
    birth_year = input('Birth year: ')

    type(birth_year)

    age = 2023 - int(birth_year)

    print('You are ', age, ' years old')
