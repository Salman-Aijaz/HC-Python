def custom_sort(s):
    # Sort the string based on the custom order
    sorted_string = sorted(s, key=lambda x: (x
        x.isdigit(),               # Digits go last
        x.isdigit() and int(x) % 2 == 0,  # Even digits after odd digits
        x.isupper(),               # Uppercase letters after lowercase
        x                          # Natural order
    ))
    return ''.join(sorted_string)

input_str = "Sorting1234"
output_str = custom_sort(input_str)
print(output_str)
