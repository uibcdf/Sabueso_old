
def is_file(molecular_system):

    from sabueso.forms import file_extensions_recognized

    output = False

    if type(molecular_system) is str:
        file_extension = molecular_system.split('.')[-1].lower()
        if file_extension in file_extensions_recognized:
            output = 'file:'+file_extension

    return output

