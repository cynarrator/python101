def hashtag(function_to_hash):
    def print_hash_around():
        print('#' * 10)
        function_to_hash()
        print('#' * 10)
    return print_hash_around


def star(function_to_star):
    def print_star_around():
        print("*" * 10)
        function_to_star()
        print("*" * 10)
    return print_star_around

@hashtag
@star
def print_text():
    print("hello and bye")


print_text()

"""
star(hello)()
"""