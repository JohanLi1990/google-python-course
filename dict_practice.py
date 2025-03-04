alien_0 = {'color': 'green', 'points': 5}
alien_0['eye'] = 3
print(alien_0)
if 'eye' in alien_0:
    print(alien_0['eye'])

alien_0.clear()
print(alien_0)
alien_0['color'] = 'blue'
alien_0['name'] = 'Shuai Chenyang'
print(alien_0)

new_dict = {k: v for k, v in alien_0.items() if k != 'name'}
print(new_dict)
new_dict[5] = 6
for k, v in new_dict.items():
    print(f"{k} : {v}")
del new_dict[5]
print(new_dict)
print(new_dict.get('name', 'Chenyang'))
new_dict['name'] = new_dict.get('name', 'Chenyang') + 'shuai'
print(new_dict)
for key, value in new_dict.items():
    print(key, value)

new_dict['wife'] = 'Rona'
new_dict['son'] = 'Em'
print(new_dict)
