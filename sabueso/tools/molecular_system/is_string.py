def is_string(molecular_system):

    from sabueso.forms import string_names_recognized
    from sabueso.tools.string import guess_form

    output = False

    if type(molecular_system) is str:
        if ':' in molecular_system:
            string_name = molecular_system.split(':')[0]
            if string_name in string_names_recognized:
                output = 'string:'+string_name
        if output==False:
            output = guess_form(molecular_system)
            if output is None:
                output = False

    return output

