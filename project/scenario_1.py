
def check_route_data(phone_number):
    ''' return the phone_number(string) and a comma with the price(string) '''
    price = '0'
    prefix_matches = []
    longest = ''
    with open('./data/route-costs-4.txt', 'r') as routes_file:
        for line in routes_file:
            #remove the new line char, then split the line into an array
            route_with_price = line.strip().split(',')

            # assuming US prefix, and includes the +
            # move longest_match check to in this loop and get rid of prefix array
            if phone_number[0:5] == route_with_price[0][0:5]:
                prefix_matches.append(route_with_price)

    # if no matches were found return 0
    if prefix_matches == []:
        return phone_number + ', 0'

    else:
        longest_match = phone_number[0:5]
        for each_match in prefix_matches:
            # TODO for each match check longest pattern match
            pass
    #longest match[1] is just the string it matches, fix this
    return phone_number + ',' + longest_match[1]



test = check_route_data('+15124156620')
print(test)

# with open('./data/route-costs-4.txt', 'r') as routes_file:
#     matches = []
#     for line in routes_file:
#         route = line.split(',')
#         print(route[0])
#         print('0:6', route[0][0:6])
