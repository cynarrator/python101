def greet(data):
    print(f"Hello I am {data['name']}")
    print(f"I live in {data['city']}")

greet({
    "name": "Utsav",
    "city": "Ktm"
})