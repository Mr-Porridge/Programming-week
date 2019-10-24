"""
1、哈夫曼加密
2、哈夫曼解密
3、预防基于单词频度攻击
"""
import operator


class Tree:
    def __init__(self, val: str = float("-Inf"), w: float = -1, left_child=None, right_child=None):
        self.val = val
        self.weight = w
        self.lChild = left_child
        self.rChild = right_child

    def merge_two_trees(self, left_child=None, right_child=None):
        self.lChild = left_child
        self.rChild = right_child

    def pre_order_travel(self):
        if self.lChild is None or self.rChild is None or self is None:
            # print(self.val, "->", self.weight, end="|")
            # print("#", end=" ")
            return
        else:
            # print(self.val, self.weight, end="|")
            self.lChild.pre_order_travel()
            self.rChild.pre_order_travel()

    def is_leaf(self) -> bool:
        if self.lChild is None and self.rChild is None:
            return True
        else:
            return False


def quick_sort(maples: list):
    # print("To be sorted: ")
    # print_nodes(maples)
    compare_fun = operator.attrgetter('weight', 'val')
    maples.sort(key=compare_fun)
    # print("After sorted: ")
    # print_nodes(leafs)


def print_nodes(nodes: list):
    print("[", end="")
    for item in nodes:
        item.pre_order_travel()
    print("]", end="")
    print()


def create_huffman_tree(leaves: list):
    while len(leaves) > 1:
        quick_sort(leaves)
        # print_nodes(leaves)
        # 选权重最小的两个结点
        # min1, min2 = Tree("min1", float('inf')), Tree("min2", float('inf'))
        # for item in leaves:
        #     if item.weight < min1.weight:
        #         min2.weight = min1.weight
        #         min1.weight = item.weight
        #     elif item.weight < min2.weight:
        #         min2.weight = item.weight
        min1, min2 = leaves[0], leaves[1]
        # print(min1.val, "->", min1.weight, min2.val, "->", min2.weight)
        combined = Tree("sum", min1.weight + min2.weight, min1, min2)
        del leaves[0]
        del leaves[0]
        leaves.append(combined)
        # print_nodes(leaves)
        # print("---------------------------")
    return leaves[0]


def huffman_encode_word(huffman_tree: Tree, item: str, codes: str = "", ans=""):
    if item == huffman_tree.val:
        # print(codes)
        # print("Success!")
        return codes
    else:
        if huffman_tree.lChild is not None:
            ans = huffman_encode_word(huffman_tree.lChild, item, codes=codes + "0", ans=ans)
        if huffman_tree.rChild is not None:
            ans = huffman_encode_word(huffman_tree.rChild, item, codes=codes + "1", ans=ans)
        return ans


def huffman_encode(huffman_tree: Tree, plain: str):
    ans = ""
    for item in plain.split(" "):
        ans += huffman_encode_word(huffman_tree, item)  # 可以加修饰符
    return ans


def huffman_decode(huffman_tree: Tree = None, dic=None, encoded: str = "", ans=""):
    if dic is None:
        dic = {"Empty": "Code_book is empty!"}
        # print(dic)
    else:
        print(dic)
    while len(encoded) > 0:
        for x in range(0, len(encoded) + 1):
            segment = encoded[0:x]
            # print("Segment is: ", segment)
            if segment in dic.keys():
                # print(dic[segment])
                ans += dic[segment] + " "
                encoded = encoded[x:]
                break
    return ans


# 建树封装
def initializing():
    dictionary = {
        "I": 8,
        "LOVE": 12,
        "YOU": 4,
        "BABY": 15,
        "MY": 7,
    }
    code_book = {}  # 建树生成后的密码字典
    leafs = []  # 结点链表初始化
    # 根据语料库中的单词构造结点链表
    for word in dictionary:
        node = Tree(val=word, w=dictionary[word])
        leafs.append(node)
    ht = create_huffman_tree(leafs)  # 用结点链表建树
    text = dictionary.keys()
    for word in text:
        code_book[huffman_encode_word(ht, word)] = word
    return ht


# 密码字典封装
def cipher_book():  # 之后使用数据库读取的方法
    dictionary = {
        "I": 8,
        "LOVE": 12,
        "YOU": 4,
        "BABY": 15,
        "MY": 7,
    }
    code_book = {}  # 建树生成后的密码字典
    text = dictionary.keys()
    for word in text:
        code_book[huffman_encode_word(initializing(), word)] = word
    return code_book


# 加密封装
def encode(user_input: str):  # 需要进行检查或者分词 再议
    return huffman_encode(initializing(), user_input)


# 解密封装
def decode(user_input: str):
    return huffman_decode(initializing(), cipher_book(), user_input)


# print(encode("BABY I LOVE YOU"))
# print(decode("110010010"))
# print(cipher_book())
