if __name__ == '__main__':

    import string

    # Read the file
    with open("1000000.txt") as f:
        lines = f.readlines()
    f.close()

    # Create a string variable containing 1 million decimals of pi
    pi_string = ''.join([line.replace('\n', '') for line in lines])

    # Create conversion dictionnary
    d = dict(enumerate(string.ascii_lowercase, 1))
    # Invert dictionnary
    d = {v: k for k, v in d.items()}
    # Add space to create sentence
    d[' '] = 0

    # Convert a sequence in an integer
    def convert_sequence(sequence):     
        return ''.join([str(d[letter]) for letter in sequence]) 

    # Loop of requests
    while True:
        # Instruction to quit
        print('To quit, enter the word "stop"')
        string_to_convert = str(input())
        if string_to_convert == 'stop':
            break
        # Conversion and search   
        string_to_test = convert_sequence(string_to_convert)
        if string_to_test in pi_string:
            index_search = pi_string.find(string_to_test)
            print(f'We can find the sequence "{string_to_convert}" to the {index_search:,}th decimale place of pi') 
        else:
            print('Your sequence is not in the first million digits of pi')
        print('-'*50, '\n')