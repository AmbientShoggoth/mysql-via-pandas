def config_type_string_to_dict(in_string):
    """Convert contents of ini files to dict"""
    string_list=in_string.split("\n")
    string_list=[i.split("#")[0].replace(" ","").split("=",maxsplit=1) for i in string_list if i and "=" in i]
    return({pair[0]:pair[1] for pair in string_list})