# def checklength(n):
#     n = n.split(" ")
#     for i in n:
#         a = len(i)
#         if a%2==0:
#             print(f"'{i}'", "is an even lettered word")
#         else:
#             print(f"'{i}'", "is an odd lettered word")


def checklength(n):
    n = n.split(" ")
    for i in n:
        if len(i)%2==0:
            print(i)



checklength("Hi my name is John.")