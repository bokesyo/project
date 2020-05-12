
# Read the tree object we generated before
from classRef.localCache import *

data = local_cache('dataStorge/primaryTreeObject')
tree_root = data['tree_root']

indent = 0
node_count = 0
countsm = 0
countbg = 0

# Open an empty python file
filehandle = open("output/generalExecute.py", "w")
filehandle.write('')  # clear the file
filehandle = open("output/generalExecute.py", "a")

# Write the header
filehandle.write('def classifier(data_list):\n')
filehandle.write('    fixed_acidity = data_list[0]\n')
filehandle.write('    volatile_acidity = data_list[1]\n')
filehandle.write('    citric_acid = data_list[2]\n')
filehandle.write('    residual_sugar = data_list[3]\n')
filehandle.write('    chlorides = data_list[4]\n')
filehandle.write('    free_sulfur_dioxide = data_list[5]\n')
filehandle.write('    total_sulfur_dioxide = data_list[6]\n')
filehandle.write('    density = data_list[7]\n')
filehandle.write('    pH = data_list[8]\n')
filehandle.write('    sulphates = data_list[9]\n')
filehandle.write('    alcohol = data_list[10]\n')


def grow(node):
    global countsm
    global countbg
    global indent
    global node_count

    if (node.type == 'terminal') or (not node):
        i = node.ID
        result = node.condition
        node_count += 1
        filehandle.write((' ' * 4 * (indent + 1) + 'return ' + str(result)) + '\n')
        # filehandle.write((' ' * 4 * (indent + 1) + 'ids' + str(i)) + '\n')
        return

    if node.left:
        node_count += 1
        result = node.condition
        indent += 1
        i = node.ID
        filehandle.write((' ' * 4 * indent + 'if ' + str(result) + ':') + '\n')
        grow(node.left)
    else:
        pass
        # filehandle.write((' ' * 4 * indent + 'fuck:left ') + '\n')

    if node.right:
        node_count += 1
        i = node.ID
        filehandle.write((' ' * 4 * indent + 'else: ') + '\n')
        grow(node.right)
        indent -= 1
    else:
        pass
        # filehandle.write((' ' * 4 * indent + 'fuck:right ') + '\n')


grow(tree_root)
