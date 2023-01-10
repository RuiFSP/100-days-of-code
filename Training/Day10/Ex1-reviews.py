# Functions with outputs
def format_name(f_name, l_name):
    name = f"{f_name} {l_name}".title()
    return name


print(format_name("ruI", "PiNtO"))


# functions with multiple returns
def format_name1(f_name, l_name):
    '''
    Take a first and last name and format it to return the title case version of the name
    :param f_name:
    :param l_name:
    :return:
    '''
    if f_name == "" or l_name == "":
        return "wrong input"
    name = f"{f_name} {l_name}".title()
    return name


print(format_name1("rui", ""))
