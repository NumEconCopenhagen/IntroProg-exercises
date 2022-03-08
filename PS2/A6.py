import pickle

# a. create some data
my_data = {}
my_data['A'] = {'a': 1, 'b': 2}
my_data['B'] = np.array([1, 2, 3])
my_data['C'] = (1, 4, 2)

my_np_data = {}
my_np_data['D'] = np.array([1, 2, 3])
my_np_data['E'] = np.zeros((5, 8))
my_np_data['F'] = np.ones((7, 3, 8))

# c. save with pickle
with open(f'data.p', 'wb') as f:
    pickle.dump(my_data, f)

# d. save with numpy
np.savez(f'data.npz', **my_np_data)

# a. try


def load_and_print():
    with open(f'data.p', 'rb') as f:
        data = pickle.load(f)
        A = data['A']
        B = data['B']
        C = data['C']

    with np.load(f'data.npz') as data:
        D = data['D']
        E = data['E']
        F = data['F']

    print('variables loaded without error')


try:
    load_and_print()
except:
    print('an error is found')
