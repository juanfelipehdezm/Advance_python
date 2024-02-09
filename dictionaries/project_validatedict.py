"""
In this project our goal is to validate one dictionary structure against a template dictionary.

A typical example of this might be working with JSON data inputs in an API. You are trying to validate this received JSON against some kind of 
template to make sure the received JSON conforms to that template (i.e. all the keys and structure are identical - value types being important, 
but not the value itself - so just the structure, and the data type of the values).

To keep things simple we'll assume that values can be either single values (like an integer, string, etc), or a dictionary, itself only containing single values or other dictionaries, recursively. 
In other words, we're not going to deal with lists as possible values. Also, to keep things simple, we'll assume that all keys are **required**, and that no extra keys are permitted.

In practice we would not have these simplifying assumptions, and although we could definitely write this ourselves, there are many 3rd party libraries that already exist to do this (such as `jsonschema`, `marshmallow`, and many more, 
some of which I'll cover lightly in some later videos.)

"""

template = {
    'user_id': int,
    'name': {
        'first': str,
        'last': str
    },
    'bio': {
        'dob': {
            'year': int,
            'month': int,
            'day': int
        },
        'birthplace': {
            'country': str,
            'city': str
        }
    }
}

def extract_keys(some_dict: dict) -> list:
    list_of_keys = []
    for k, v in some_dict.items():
        list_of_keys.append(k)
        if isinstance(v, dict):
            nested_keys = extract_keys(some_dict[k])
            list_of_keys.extend(iter(nested_keys))
    return list_of_keys


def match_keys(data, template):
    data_keys, template_keys = set(extract_keys(data)), set(extract_keys(template))

    missing_error_msg = " "
    extra_error_msg = " "
    #keys that are missing and should be present
    if missing_keys := template_keys - data_keys:
        missing_error_msg = ("Missing Keys = " +
                      ",".join(str(key) for key in missing_keys))

    #keys that are extra and should not be present
    elif extra_keys:= data_keys - template_keys:
        extra_error_msg = ("Extra Keys = " +
                      ",".join(str(key) for key in extra_keys))


    final_error_msg = ""
    if missing_error_msg and extra_error_msg:
        final_error_msg = f"{missing_error_msg}  {extra_error_msg}"
    elif missing_error_msg:
        final_error_msg = missing_error_msg
    else:
        final_error_msg = extra_error_msg

    return final_error_msg or True


def compare_value_data_types(data, template):
    

eric = {
    'user_id': 101,
    'name': {
        'first': 'Eric',
        'last': 'Idle'
    },
    'bio': {
        'dob': {
            'year': 1943,
            'month': 3,
            'day': 29
        },
        'birthplace': {
            'country': 'United Kingdom'
        }
    }
}

print(match_keys(eric, template))
print(compare_value_data_types(eric,template))