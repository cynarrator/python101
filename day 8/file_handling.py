try:
    f = open('myfile.txt', 'r')

except Exception as e:
    print(f"Error occured: {e}")