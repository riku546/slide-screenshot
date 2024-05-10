
    
# def sum_of_cubes(n):
#     result = 0
#     for i in range(1 ,n+1):
#         print(i)
#         result  +=  i**3
#     return result
# print(sum_of_cubes(10))


# def hit(a, b):
#     count = 0
#     for i in a:
#         for x in b:
#             if(i == x):
#                 count +=1
#     return count

# print(hit([1,2,3,4] , [1,2,3,4]))


# def avg(list):
#     total = 0
#     result = 0
#     for i in list:
#         total += i
#     result = total / len(list)
#     return result
# data = [172.8, 156.9, 175.9, 156.1, 166.8, 161.9, 166.9, 176, 159.8, 164, 160.3, 153.5, 174.1, 172.2, 172.7, 166.7, 173.7, 158, 172.7, 155.9]

# avg_num = avg(data)

# def variance(data):
#     cal = 0
#     for d in data:
#         cal += (d - avg_num) ** 2
#     cal /= len(data)
#     return cal


# print(variance(data))


# def sutoro(text):
#     result = ""
#     for t in text:
#         if t == "す":
#             pass
#         else:
#             result += t
#     return result

# print(sutoro("さしすせそ"))

def hit(a, b):
    count = 0
    for i in range(len(a)):
        if a[i] == b[i]:
            count += 1

    return count

print(hit([1,2,3,4],[1,4,3,2]))