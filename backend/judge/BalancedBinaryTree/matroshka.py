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

    def pre_order_travel(self, result=None):
        if result is None:
            result = {}
        if self.lChild is None or self.rChild is None or self is None:
            result["image_url"] = "http://47.110.134.247/numbers/num-inf.png"
            # del result
            # print("#", end=" ")
            return
        else:
            # print(self.val, end=" ")
            result["name"] = str(self.val)
            result["children"] = [{}, {}]
            result["image_url"] = "http://47.110.134.247/numbers/num" + str(self.val) + ".png"
            result["children"][0]["name"] = str(self.lChild.val)
            result["children"][1]["name"] = str(self.rChild.val)
            self.lChild.pre_order_travel((result["children"][0]))
            self.rChild.pre_order_travel((result["children"][1]))
            # print()
            # print(result)
            return result


# FamilyTree测试
def family_tree(pre_input_str: str):
    pre_input_str += ",#,#,#,#,#,#,#,#"
    pre_input_list = pre_input_str.split(",")
    bt = Tree()  # 建树根
    bt.pre_create(pre_input_list)  # 先序建树
    return bt.pre_order_travel()


# print(family_tree(pre_input_str="5,4,3,1,#,2,#,#,#,3,5,2,#,#,#,#,2,#,1,4,#,#,2,#,#"))
