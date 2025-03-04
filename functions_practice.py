def make_pizza(*toppings, size = 16):
    '''
    strings of toppings, String
    rType: none
    '''
    print(f"size {size} pizza with {toppings}")

# make_pizza( "cheese", "sausage", "flour")

def build_profile(first, last, **user_info):
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

# print(build_profile('Chenyang', 'Li', age=35, look='great'))