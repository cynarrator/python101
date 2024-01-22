a = 10
def first_layer():
    def second_layer():
        def third_layer():
            global a
            a = 11
            print(a)
        third_layer()
    second_layer()
first_layer()
print(a)

