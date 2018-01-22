

def type_check( input , type="int" ):

    output = False


    return output

def range_check( input , range ):

    output = False

    if (input >= range[0]) and (input <= range[1]) :
        output = True

    return output

def pick_value_check( input , possible_values_list ):

    output = False
    lenght = len(possible_values_list)
    for loop in range(lenght):

        if input == possible_values_list[loop]:
            output = True
            break

    return output