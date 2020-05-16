from regGrow import *
from regAsses import *
from regPrune import *
from readData import *
from M5 import *


data_dict = readCSV('inputData/partial_train.csv')

"""

print('The tree is growing, please wait a few seconds. (About 5 seconds on MacBook Pro)')
# Growing
T = regGrow('inputData/partial_train.csv', 'tmp/reg/treeObj')
tree = T.tree
print('Grown up!')

print('Start pruning')
# Pruning
stop = False
n = 1

while tree.size > 1:
    this = regPrune(tree, data_dict)
    tree = this.tree
    print('This is the', str(n), 'th pruning.')
    data = local_cache('tmp/reg/forest/' + str(n))
    data['tree'] = tree
    n = n + 1

print('Pruning is finished.')


print('Cross validation starts.')


# Filtering
m = 1
tup_list = []
for i in range(1, n - 1):
    data = local_cache('tmp/reg/forest/' + str(m))
    tree = data['tree']
    A = regAsses('inputData/remain_train.csv', tree)
    print('This is the ', m, 'th candidate tree, MSE is', A.mse, 'R2 is', A.R2, 'Cor', A.cor)
    tup = (m, A.mse, A.R2, A.cor, A.nmse)
    tup_list.append(tup)
    m = m + 1


optimal = None
for tup in tup_list:
    if not optimal:
        optimal = tup
    else:
        if tup[1] < optimal[1]:
            optimal = tup


print(optimal[0], 'th candidate is the optimized tree with a MSE of ', optimal[1], 'R2 is', str(optimal[2]),
      'Correlation Coefficient is', optimal[3])

print('Cross validation ends.')


# Testing
print('Testing begins.')


print('Here is the best tree.')
data = local_cache('tmp/reg/forest/' + str(optimal[0]))
tree = data['tree']

A = regAsses('inputData/test.csv', tree)
print(optimal[0], 'th tree is the optimal tree, MSE is', A.mse, 'R2 is', A.R2, 'Cor is', A.cor)


print('Testing finished.')
"""

print('Now we use M5 algorithm to optimize our model!')
m5 = M5(data_dict, 1)

m5.tree = local_cache('tmp/reg/forest/' + str(591))['tree']
node = m5.tree.root
# Process
m5.main(node)
# Evaluate
m5.evaluate()

print(m5.getMSE())
# Write File
local_cache('tmp/reg/forest/' + str(591))['tree'] = m5.tree

"""


result_list = m5.mse_list

print(result_list)

min_mse = None
for tup in result_list:
    if not min_mse:
        min_mse = tup
    else:
        if tup[1] <= min_mse[1]:
            min_mse = tup

optimal_tree_id = min_mse[0]

data = local_cache('tmp/reg/forest/' + str(optimal_tree_id))
tree = data['tree']

A = regAsses('inputData/test.csv', tree)

print('By using M5 algorithm,', optimal_tree_id, 'th tree is the optimal tree, MSE is', A.mse)

"""