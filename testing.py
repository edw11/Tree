import sys

class TreeNode:
    def __init__(self, m_id, p_id, color, max_depth):
        self.m_id = m_id
        self.max_depth = max_depth
        self.color = color
        self.color_subtree = [int(self.color)]
        self.children = []
        self.p_id = p_id
        self.parent = None

    def add_child(self, child):
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
            current_node.color_subtree.append(int(new_color))
            current_node = current_node.parent

    def change_color(self, color):
        current_node = self
        parent = current_node.parent
        while parent:
            parent.color_subtree.remove(int(current_node.color))
            parent = parent.parent
        current_node.color_subtree.remove(int(current_node.color))
        current_node.color = color
        current_node.subtree_color_sum(color)
        for child in current_node.children:
            child.change_color(color)

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

    def sum_all(self):
        tree_value = len(set(self.color_subtree))
        total = (tree_value * tree_value)
        if self.children:
            for child in self.children:
                total = total + child.sum_all()
        return total

    def search_color(self, m_id):
        current_node = self.search_parent_object(m_id)
        return int(current_node.color)

# MODIFY THIS FUNCTION TO HANDLE MULTIPLE ROOTS
def identify_input(arr):
    roots = []  # List to hold multiple roots

    input_lines_number = int(arr[0])
    arr.pop(0)

    for i in range(input_lines_number):
        if arr[i][0] == '100':
            m_id = arr[i][1]
            p_id = arr[i][2]
            color = arr[i][3]
            max_depth = arr[i][4]

            if p_id == '-1':  # It's a root node
                root = TreeNode(m_id, None, color, max_depth)
                roots.append(root)  # Add this root to the list of roots
            else:
                # Search all roots to find the correct parent
                parent_found = None
                for root in roots:
                    parent_found = root.search_parent_object(p_id)
                    if parent_found:
                        break

                if parent_found and parent_found.check_max_depth(p_id):
                    new_node = TreeNode(m_id, p_id, color, max_depth)
                    parent_found.add_child(new_node)
                    parent_found.subtree_color_sum(color)

        elif arr[i][0] == '200':
            m_id = arr[i][1]
            color = arr[i][2]

            # Search all roots to find the node
            current_node = None
            for root in roots:
                current_node = root.search_parent_object(m_id)
                if current_node:
                    break

            if current_node:
                current_node.change_color(color)

        elif arr[i][0] == '300':
            m_id = arr[i][1]

            # Search all roots to find the node
            current_node = None
            for root in roots:
                current_node = root.search_parent_object(m_id)
                if current_node:
                    break

            if current_node:
                print(root.search_color(m_id))

        elif arr[i][0] == '400':
            total_sum = 0
            for root in roots:
                total_sum += root.sum_all()
            print(total_sum)



#MAIN FUNCTION
no_of_lines = input()  # First input is the number of lines
lines = sys.stdin.read()  # Read the rest of the input at once
lines_array = []
lines_new = lines.split("\n")
for command in lines_new:
    lines_array.append(command.split(" "))
lines_array.insert(0, no_of_lines)
identify_input(lines_array)