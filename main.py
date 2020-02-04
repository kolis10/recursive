import json

with open('users.json') as jfile:
    users = json.load(jfile)

#------------------------------
# obj = {
#     'one': 4,
#     'two': 2
# }

# x = [4,5,'one',7,'two']

# for key, values in obj.items():
#     # print(x[values])
#     print(obj[x[values]])
#-------------------------------
for user in users:
    print(user['last_name'])
    if user['first_name'] == 'Zion':
        user['last_name'] = 'Messed Up'
        print('why am I only printing one of these?')
# print(users)