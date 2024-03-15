"""Various validators"""

def validate_integer(
        arg_name: str, arg_value: object, min_value : int = None, max_value: int = None)-> None:
    """
        Validates that the provided argument is an integer within an optional range.

        **Args:**

        * `arg_name (str)`: The name of the argument being validated.
        * `arg_value (object)`: The value to be validated.
        * `min_value (int, optional)`: The minimum allowed value (inclusive). Defaults to None.
        * `max_value (int, optional)`: The maximum allowed value (inclusive). Defaults to None.

        **Raises:**

        * `TypeError`: If the argument value is not an integer.
        * `ValueError`: If the argument value is outside the specified range (if provided).

        **Returns:**

        * None

        **Example:**

        ```python
        def some_function(value):
        validate_integer("value", value, 0, 10)

        # Valid call
        some_function(5)

        # Invalid calls due to type mismatch
        try:
        some_function("hello")
        except TypeError as e:
        print(e)  # Output: value must be an integer

        # Invalid calls due to value being outside range
        try:
        some_function(15)
        except ValueError as e:
        print(e)  # Output: value can not be greather than 10
    """
    if not isinstance(arg_value, int):
        raise TypeError(f"{arg_name} must be an integer")
    
    if min_value is not None and arg_value < min_value:
        raise ValueError(f"{arg_name} can not be less than {min_value}")
        
    if max_value is not None and arg_value > max_value:
        raise ValueError(f"{arg_name} can not be greather than {max_value}")
    
    return True


    