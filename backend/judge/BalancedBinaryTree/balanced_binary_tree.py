"""
判断二叉树是否为平衡二叉树，数据结构采用二叉链表
1、二叉树的输入、打印
2、二叉树是否为二叉搜索树（平衡二叉树是二叉搜索树的一种）
3、二叉搜索树是否为二叉平衡树（平衡因子）
"""


class Tree:
    def __init__(self, val=float("-Inf"), left_child=None, right_child=None):
        self.val = val
        self.factor = -99
        self.lChild = left_child
        self.rChild = right_child

    def pre_create(self, user_input=None, i: int = 0):
        if user_input is None:
            user_input = []
        val = user_input[i]
        if val == "#":
            return i
        else:
            self.val = int(val)
            self.lChild = Tree()
            i = self.lChild.pre_create(user_input, i=i + 1)
            self.rChild = Tree()
            i = self.rChild.pre_create(user_input, i=i + 1)
            return i

    def pre_order_travel(self):
        if self.lChild is None or self.rChild is None or self is None:
            print("#", end=" ")
            return
        else:
            print(self.val, end=" ")
            self.lChild.pre_order_travel()
            self.rChild.pre_order_travel()

    def treeDepth(self):
        if (self.lChild is None) & (self.rChild is None):
            return 0
        leftDepth = self.lChild.treeDepth()
        rightDepth = self.rChild.treeDepth()
        return max(leftDepth, rightDepth) + 1


# 判断二叉树是否为二叉搜索树
def binary_search_tree(binary_tree: Tree):
    # 输入"#"的话没有参数传进来
    # binary_tree: NoneType
    # AttributeError raised
    # 所以直接捕获异常即可
    try:
        flag = True  # 是否为二叉搜索树的标志
        # 第一种情况：左右子树都未获取输入数据 -> 没有孩子 -> 叶子节点
        if (binary_tree.lChild.val == float("-Inf")) & (binary_tree.rChild.val == float("-Inf")):
            # print(binary_tree.lChild.val, binary_tree.val, binary_tree.rChild.val)
            # print("END!")
            return flag
        else:
            # 第二种情况：左子树存有输入数据集，右子树未获取输入 -> 一个孩子
            if (binary_tree.rChild.val == float("-Inf")) & (binary_tree.lChild.val != float("-Inf")):
                if binary_tree.lChild.val < binary_tree.val:
                    # print("Matched!")
                    binary_search_tree(binary_tree.lChild)
                    return flag
                else:
                    # print("Not a SBT!")
                    flag = False
                    return flag
            # 第三种情况：右子树存有输入数据集，左子树未获取输入 -> 一个孩子
            elif (binary_tree.lChild.val == float("-Inf")) & (binary_tree.rChild.val != float("-Inf")):
                if binary_tree.rChild.val > binary_tree.val:
                    # print("Matched!")
                    binary_search_tree(binary_tree.rChild)
                    return flag
                else:
                    # print("Not a SBT!")
                    flag = False
                    return flag
            # 第一种情况：左右子树数据与都存有输入数据 -> 两个孩子
            else:
                if binary_tree.lChild.val < binary_tree.val < binary_tree.rChild.val:
                    # print(binary_tree.lChild.val, binary_tree.val, binary_tree.rChild.val)
                    # print("Matched!")
                    binary_search_tree(binary_tree.lChild)
                    binary_search_tree(binary_tree.rChild)
                    return flag
                else:
                    # print(binary_tree.lChild.val, binary_tree.val, binary_tree.rChild.val)
                    # print("Not a SBT!")
                    flag = False
                    return flag
    except AttributeError as e:
        return True


# 判断二叉树（二叉搜索树）是否为二叉平衡树
def balanced_binary_tree(binary_tree: Tree):
    if binary_tree is None:
        return True
    flag = True
    if (binary_tree.lChild is None) & (binary_tree.rChild is None):
        return flag
    else:
        left_height = binary_tree.lChild.treeDepth()
        right_height = binary_tree.rChild.treeDepth()
        binary_tree.factor = left_height - right_height
        # print("At node ", binary_tree.val, "-> The result is: ", binary_tree.factor)
        if binary_tree.factor not in [-1, 0, 1]:
            print("The tree is a Binary Search Tree but not a Balanced Binary Tree! ")
            flag = False
            return flag
        else:
            balanced_binary_tree(binary_tree.lChild)
            balanced_binary_tree(binary_tree.rChild)
            return flag


# 判断二叉树是否为二叉平衡树
def is_bst_balanced(binary_tree: Tree):
    if binary_search_tree(binary_tree):
        # print("The tree is a Binary Search Tree! ")
        if balanced_binary_tree(binary_tree):
            # print("The Binary Search Tree is a Balanced Binary Tree! ")
            return True
        else:
            return False
    else:
        # print("The tree is not a Binary Search Tree! Nor a Balanced Binary Tree! ")
        return False


# 命令行版本封装
def B17040425():
    input_castle = [
        "4,1,0,#,#,#,2,#,#",
        "2,1,#,#,3,#,#",
        "6,4,2,#,#,#,8,#,#",
        "3,2,1,#,#,#,#"
    ]
    for i in range(len(input_castle)):
        pre_input_str = input_castle[i]  # 从前端获取输入即可
        pre_input_list = pre_input_str.split(",")
        bt = Tree()  # 建树根
        bt.pre_create(pre_input_list)  # 先序建树
        print()
        print("--------- The %d-th round begin !--------------------" % i)
        bt.pre_order_travel()  # 先序遍历打印树
        # print(binary_search_tree(bt))
        # print(bt.treeDepth())
        # balanced_binary_tree(bt)
        print()
        is_bst_balanced(bt)  # 判断输入的树是否为平衡二叉树
        print()


# 命令行版本测试
# B17040425()


def balanced(user_input: str) -> list:
    pre_input_list = user_input.split(",")
    bt = Tree()  # 建树根
    bt.pre_create(pre_input_list)  # 先序建树
    bt.pre_order_travel()  # 先序遍历打印树
    bst = binary_search_tree(bt)
    bal = is_bst_balanced(bt)  # 判断输入的树是否为平衡二叉树
    return [bst, bal]


# print(type("2,#,#"))
# print(balanced("2,#,#"))
