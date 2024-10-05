class TreeNode:
    def __init__(self, m_id,p_id, color, max_depth ):
        self.m_id = m_id
        self.max_depth = max_depth
        self.color = color
        self.color_subtree = [int(self.color)]
        self.children = []
        self.p_id = p_id
        self.parent = None

    def add_child(self,child):
        child.parent = self
        self.children.append(child)

    def search_parent_object(self, p_id):
        if self.m_id == p_id:
            return self
        else:
            if self.children:
                for child in self.children:
                    result = child.search_parent_object(p_id)
                    if result:
                        return result
        return None

    def subtree_color_sum(self, color):
        new_color = color
        current_node = self
        while current_node:
            current_node.color_subtree.append(int(new_color)) #self
            current_node = current_node.parent

    def change_color(self, color):
        self.color = color
        parent = self.parent
        parent.subtree_color_sum(color)


    def check_max_depth(self, p_id):
        parent = self.search_parent_object(p_id)
        if len(parent.children) + 1 < int(parent.max_depth):
            return True
        else:
            return False

    def print_tree(self):
        tree_value = len(set(self.color_subtree))
        data = [self.m_id, self.p_id, tree_value, self.color, self.max_depth]
        print(data)
        if self.children:
            for child in self.children:
                child.print_tree()



def identify_input(arr):
    root = None
    input_lines_number = int(arr[0])
    arr.pop(0)
    for i in range(input_lines_number):
        if arr[i][0] == '100':
            m_id = arr[i][1]
            p_id = arr[i][2]
            color = arr[i][3]
            max_depth = arr[i][4]
            if p_id == '-1':
                root = TreeNode(m_id, None, color, max_depth)
            else:
                    check_max_depth = root.check_max_depth(p_id)
                    if check_max_depth:
                        parent_found = root.search_parent_object(p_id)
                        parent_found.add_child(TreeNode(m_id, p_id, color, max_depth))
                        parent_found.subtree_color_sum(color)
                    else:
                        continue

        if arr[i][0] == '200':
            m_id = arr[i][1]
            color = arr[i][2]
            current_node = root.search_parent_object(m_id)
            current_node.change_color(color)

        # if arr[i][0] == '300':
        #     print("search color")
        # if arr[i][0] == '400':
        #     print("sum id")

    return root.print_tree()


def convert(string):
    li = string.split(" ")
    return li

def command_writer(arr):
    command = []
    for i in range(len(arr)-1):
        if arr[i] == '100':
            command_100 = []
            for count in range (0,5):
                command_100.append(arr[i+count])
            command.append(command_100)

        elif arr[i] == '200':
            command_200 = []
            for count in range(0, 3):
                command_200.append(arr[i + count])
            command.append(command_200)

        elif arr[i] == '300':
            command_300 = []
            for count in range(0, 3):
                command_300.append(arr[i + count])
            command.append(command_300)

        elif arr[i] == '400':
            command_400 = []
            for count in range(0, 1):
                command_400.append(arr[i + count])
            command.append(command_400)
    return command

#MAIN FUNCTION
no_of_lines = input()
lines = ""

for i in range(int(no_of_lines)+1):
    lines+=input() + " "

node_input = convert(no_of_lines + " " +lines)
node_input.remove('')
command = command_writer(node_input)
command.insert(0, no_of_lines)
identify_input(command)








