
def check_route_data(phone_number):
    ''' return the price '''
    price = 0
    prefix_matches = []
    with open('./data/route-costs-4.txt', 'r') as routes_file:
        for line in routes_file:
            #remove the new line char, then split the line into an array
            route_with_price = line.strip().split(',')

            print('route', route_with_price[0][0:6])
            if phone_number[0:5] == route_with_price[0][0:5]:
                prefix_matches.append(route_with_price)
    for each_match in prefix_matches:
        # TODO for each match check longest pattern match
        pass

    return prefix_matches

test = check_route_data('+15124156620')
print(test)

# with open('./data/route-costs-4.txt', 'r') as routes_file:
#     matches = []
#     for line in routes_file:
#         route = line.split(',')
#         print(route[0])
#         print('0:6', route[0][0:6])
