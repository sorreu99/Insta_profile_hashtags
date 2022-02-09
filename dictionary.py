details = {
    "name" : "ayush",
    "age" : 23,
    "gender": "male"
}
print(details[0])
# details["name"] = "vijay"
# print(details.get("name"))
# print(details)
# for x in details:
#     print(details[x])
# for x, y in details.items():
#     print(x, y)
# print(len(details))
# if "age" in details:
#     print("Key exist")
# del details["name"]
# print(details)
family = {
    "member1" : {
        "name" : "ayush",
        "age":23,
        "gender":"male"
    },
    "member2" : {
        "name" : "vijay",
        "age":"22",
        "gender" :"female"
    },
    "member3": {
        "name": "sumit",
        "age": False,

    }
}
# family["member1"] = None
# print(family)
# for x in details:
#     print(x)
# for x in details:
#     print(details[x])
# for x,y in details.items():
#     print(x,y)
# for x,y in enumerate(details):
#     print(x,y)

#  to access the particular index key
key = list(details)[0]
print(details[key])
a="{'member1': {'name': 'ayush', 'age': 23, 'gender': 'male'}, 'member2': {'name': 'vijay', 'age': '22', 'gender': 'female'}, 'member3': {'name': 'sumit', 'age': False}}"

