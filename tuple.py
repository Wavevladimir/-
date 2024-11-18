# my_fruits = ('apple', 'banana', 'lime')
# posts_ids = (151, 245, 762, 167)
#user_inputs = (True, 'hi', '=)', 10.5)

#other_fruits = ('banana', 'lime', 'apple')

#print(my_fruits == other_fruits)

#print(posts_ids[0])
#print(posts_ids[-1])

#my_nums = (10, 4, 8, 0)
#print(type(my_nums))
#my_nums[1] = 7
#del my_nums[3]
#error

users = (
    {
        'user_id': 134,
        'user_name': 'Alice'
    },
    {
        'user_id': 831,
        'user_name': 'Bob'
    }
)
print(users[1]['user_id']) 
users[1]['user_id'] = 100
print(users[1]['user_id'])

my_fruit = 'apple'
other_fruit = 'banana'
new_fruit = 'lime'

all_fruits = (my_fruit, other_fruit, new_fruit)
print(all_fruits)
