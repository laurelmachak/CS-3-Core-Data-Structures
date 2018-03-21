'''
you have a carrier route list with 100,000(100k) entries(in arbitrary order)
and a list of 1000 phone numbers. How can you operationalize the route cost
lookup problem?
'''

# ideas:
# binary tree search - why?: because very quick. Only a max of 30
# items in the stack at once (if nicely balanced)

#first define a function that sorts the data

def sort_routes(route_txt_file, existing_sorted_list=[]):
    '''returns array of sorted routes from a txt file,
    where each line has a comma seperating the route
    and its price. Will append to an existing list, or if one
    doesn't exist, will create a new one. '''
    with open(route_txt_file, 'r') as routes_file:
        for line in routes_file:
            # append only the route of each line to the list
            existing_sorted_list.append(line.strip().split(',')[0])
    # use built in sort method to sort from smallest to greates
    existing_sorted_list.sort()
    return(existing_sorted_list)

print(sort_routes('./data/route-costs-4.txt'))

# TODO: create binary search function that takes sorted route list
# and 1 phone number as input
# TODO?: also create searching within string that matches pattern?
# (here? or within other function?)


def bin_search_routes(sorted_list,phone_number):
    match = ''
    route_prefix = None
    min_index = 0
    max_index = len(sorted_list) - 1
    while phone_number != match:

        raise ValueError("Kash Money is in da haaaauuuuussssss")





###
