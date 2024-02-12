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
    """
        Extracts all keys from a dictionary, including nested dictionaries.

        Args:
            some_dict (dict): The dictionary from which to extract keys.

        Returns:
            list: A list of all keys extracted from the dictionary.

        Examples:
            >>> my_dict = {'a': 1, 'b': {'c': 2, 'd': {'e': 3}}}
            >>> extract_keys(my_dict)
            ['a', 'b', 'c', 'd', 'e']
    """
    list_of_keys = []
    for k, v in some_dict.items():
        list_of_keys.append(k)
        if isinstance(v, dict):
            nested_keys = extract_keys(v)
            list_of_keys.extend(iter(nested_keys))
    return list_of_keys



def extract_values(some_dict:dict) -> list:
    """
        Extracts all values from a dictionary, including nested dictionaries.

        Args:
            some_dict (dict): The dictionary from which to extract values.

        Returns:
            list: A list of all values extracted from the dictionary.

        Examples:
            >>> my_dict = {'a': 1, 'b': {'c': 2, 'd': {'e': 3}}}
            >>> extract_values(my_dict)
            [1, 2, 3]
    """
    values = []
    stack = [some_dict]
    #print(stack)

    while stack:
        current_dict = stack.pop()
        for value in current_dict.values():
            if isinstance(value, dict):
                stack.append(value)
            else:
                values.append(value)
    return values
        


def match_keys(data, template):
    """
        Checks if the keys in a given data dictionary match the keys in a template dictionary.

        Args:
            data: The data dictionary to be checked.
            template: The template dictionary containing the expected keys.

        Returns:
            Union[str, bool]: If the keys match, returns True. If there are missing or extra keys, returns an error message as a string.

        Examples:
            >>> data = {'a': 1, 'b': 2}
            >>> template = {'a': 1, 'b': 2, 'c': 3}
            >>> match_keys(data, template)
            'Missing Keys = c'
            >>> data = {'a': 1, 'b': 2, 'c': 3}
            >>> template = {'a': 1, 'b': 2}
            >>> match_keys(data, template)
            'Extra Keys = c'
            >>> data = {'a': 1, 'b': 2}
            >>> template = {'a': 1, 'b': 2}
            >>> match_keys(data, template)
            True
    """

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


    if len(final_error_msg) < 5:
        return True, "None missing keys"
    else: return final_error_msg




def match_values_types(data, template):
    """
        Compares the data types of corresponding values in two dictionaries.

        Args:
            data: The first dictionary for comparison.
            template: The second dictionary for comparison.

        Returns:
            Union[str, List[str]]: If the number of values in the dictionaries is different, returns a string indicating a missing key. Otherwise, returns a list of strings indicating data type mismatches for corresponding values.

        Examples:
            >>> data = {'a': 1, 'b': 'two', 'c': [1, 2, 3]}
            >>> template = {'a': int, 'b': str, 'c': list}
            >>> match_values_types(data, template)
            ['Data type mismatch at value two: expected <class 'int'>, got <class 'str'>', 'Data type mismatch at value [1, 2, 3]: expected <class 'str'>, got <class 'list'>']
            >>> data = {'a': 1, 'b': 'two', 'c': [1, 2, 3]}
            >>> template = {'a': int, 'b': str, 'c': dict}
            >>> match_values_types(data, template)
            ['Data type mismatch at value [1, 2, 3]: expected <class 'dict'>, got <class 'list'>']
            >>> data = {'a': 1, 'b': 'two', 'c': [1, 2, 3]}
            >>> template = {'a': int, 'b': str, 'c': list}
            >>> match_values_types(data, template)
            'There is a missing key so no comparison is being made'
    """

    data_values, template_types = extract_values(data), extract_values(template)

    print("values: ",data_values)
    print("expected types: ", template_types)

    if len(data_values) != len(template_types):
        return "There is a missing key so no comparison is being made"
    else:
        return [
            f"Data type mismatch at value {data_values[i]}: expected {expected_type}, got {type(value)}"
            for i, (value, expected_type) in enumerate(
                zip(data_values, template_types)
            )
            if not isinstance(value, expected_type)
        ]




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

michael = {
    'user_id': 102,
    'name': {
        'first': 'Michael',
        'last': 'Palin'
    },
    'bio': {
        'dob': {
            'year': 1943,
            'month': 'May',
            'day': 5
        },
        'birthplace': {
            'country': 'United Kingdom',
            'city': 'Sheffield'
        }
    }
}

print(match_keys(eric, template))

print(match_values_types(eric,template))



