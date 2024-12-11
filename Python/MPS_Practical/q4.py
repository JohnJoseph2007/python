# WAF to store zero for every repeated elements in the list.
# For example if the list contains [10, 7, 15, 7, 10]
# function should return [10, 7, 15, 0, 0]

def duplicator(list: list):
    checklist = []
    for i in range(len(list)):
        if list[i] in checklist:
            list[i] = 0
        else:
            checklist.append(list[i])
    print(list)
