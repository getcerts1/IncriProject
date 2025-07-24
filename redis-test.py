import redis

r = redis.Redis(host='localhost', port=6379, decode_responses=True)


def user_input():
    name = input("name: ")
    age = input("age: ")


    r.set(name, age)
    output = r.get(name)

    return print(output)


user_input()