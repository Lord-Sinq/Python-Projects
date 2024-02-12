import itertools

def generate_subsets(a): # function to make subsets
    subsets = []
    for i in range(len(a)+1):
        for subset in itertools.combinations(a, i):
            subsets.append(subset)
    return subsets

def generate_binary_sets(subsets): # function to make binary sets
    bin_sets = []
    for subset in subsets:
        bin_set = [0] *len(a)
        for i in subset:
            bin_set[i-1] = 1
            bin_sets.append(bin_set)
    return bin_sets


a = {1, 2, 3, 4}
subsets = generate_subsets(a)
bin_sets = generate_binary_sets(subsets)
print('Name: Sinclair DeYoung')
print('Size of sets:',len(a))
print('Number of Subsets:',len(subsets))
print('') # added for a space

for bin_set, subset in zip(bin_sets, subsets): # printing the compination of Bin_sets and Subsets
    print('{} ----> {}'.format(bin_set, subset))