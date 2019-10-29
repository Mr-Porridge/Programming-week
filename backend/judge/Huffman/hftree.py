"""
1、哈夫曼加密
2、哈夫曼解密
3、预防基于单词频度攻击
"""
import operator
import random
import pymysql


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
    # 之遍历一次就找到最小的两个值
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


def huffman_encode(code_book, plain: str, num: str = ""):
    ans = num
    try:
        for item in plain.split(" "):
            ans += code_book[item]  # 可以加修饰符
        return ans
    except KeyError as err:
        # 加入语料库学习区域
        learn = open('D:\\django_learning\\backend\\judge\\Huffman\\learning.txt', 'a+')
        learn.write(str(err) + " ")
        learn.close()
        return "对不起！我还在学习新词汇呢！\n\n" + str(err) + "这个单词我还不认识呢！试试其他的吧！"


# 解密直接使用已有的密码本解密
def huffman_decode(dic=None, encoded: str = "", ans=""):
    if dic is None:
        dic = {"Empty": "Code_book is empty!"}
        # print(dic)
    else:
        print(dic)

    while len(encoded) > 0:
        length = len(encoded)
        for x in range(0, len(encoded) + 1):
            segment = encoded[0:x]
            # print("Segment is: ", segment)
            if segment in dic.keys():
                # print(dic[segment])
                ans += dic[segment] + " "
                encoded = encoded[x:]
                break
        if len(encoded) == length:
            return "Error Huffman Code！"
    return ans


def dictionary_init():
    dic = {}
    # source = open('D:/porridge/playground/divide/washed_simplified.txt')
    source = open('D:\\django_learning\\backend\\judge\\Huffman\\washed_simplified.txt')
    words = source.read()
    for item in words.split(" "):
        dic[item] = round(random.random(), 2)
    # print(dic)
    return dic


def code_book_load(dic, method: int, num: str = "00"):
    # method 用于区分加密解密的密码本读取方法 调换 Key 和 Value 位置，方便进行加密解密
    # 1:加密
    # 0:解密
    try:
        db = pymysql.connect(host="127.0.0.1", user="root", passwd="078406aaa", db="code_book", charset='utf8')
    except RuntimeError as err:
        db = None
        print("Could not connect to mysql server", err)
    cursor = db.cursor()
    sql = "SELECT * FROM three_thousand" + num
    cursor.execute(sql)
    results = cursor.fetchall()
    if method == 0:
        for item in results:
            dic[item[2]] = item[1]
    if method == 1:
        for item in results:
            dic[item[1]] = item[2]
    print(dic)
    return dic


# 存储字典
def save_code_book(code_dic, table_name: str = "unnamed"):
    # 连接数据库
    try:
        db = pymysql.connect(host="127.0.0.1", user="root", passwd="078406aaa", db="code_book", charset='utf8')
    except RuntimeError as err:
        db = None
        print("Could not connect to mysql server", err)
    cursor = db.cursor()
    # 方便调试起见 每次建表时先删除已有表格
    # cursor.execute("DELETE FROM codes")
    sql = "CREATE TABLE IF NOT EXISTS `code_book`.`" + table_name + "` (`id` INT NOT NULL,`word` VARCHAR(255) NOT NULL,`code` VARCHAR(255) NULL,PRIMARY KEY (`id`));"
    cursor.execute(sql)
    i = 0
    for item in code_dic.keys():
        value = (i, code_dic[item], item)
        print(value)
        sql = "INSERT INTO " + table_name + "(id, word, code)VALUES(%s,%s,%s)"  # 数据个数要和 %s 个数一致
        cursor.execute(sql, value)  # 执行sql语句
        i += 1
        db.commit()
    cursor.close()  # 关闭连接


# 新建密码本建树封装
def initializing(name: str = "unnamed"):
    # 读取文本文件中的语料库
    dictionary = dictionary_init()
    code_book = {}  # 建树生成后的密码字典
    leafs = []  # 结点链表初始化
    # 根据语料库中的单词构造结点链表
    for word in dictionary:
        node = Tree(val=word, w=dictionary[word])
        leafs.append(node)
    # 用结点链表建树
    ht = create_huffman_tree(leafs)
    text = dictionary.keys()
    for word in text:
        code_book[huffman_encode_word(ht, word)] = word
    # 将密码本保存
    save_code_book(code_book, name)
    return ht


# 密码字典封装
def cipher_book(name: str = "00"):  # 已经使用数据库读取的方法
    code_book = code_book_load({}, 0, name)
    # print(code_book)
    return code_book


def show_cipher_book(name: str = "00"):
    book = code_book_load({}, 0, name)
    code_book = []
    i = 0
    for item in book.keys():
        code_book.append({
            "id": i,
            "code": item,
            "word": book[item]})
        i += 1
    print(code_book)
    return code_book


# 加密封装
def encode(user_input: str):  # 需要进行检查或者分词 再议
    num = str(round(random.random())) + str(round(random.random()))
    return huffman_encode(code_book_load({}, 1, num), user_input, num)


# 解密封装
def decode(user_input: str):
    return huffman_decode(cipher_book(user_input[0:2]), user_input[2:])

# 创立四张密码表
# for item in ["three_thousand00", "three_thousand01", "three_thousand10", "three_thousand11"]:
#    initializing(item)

# print(encode("THIS AFTERNOON I WILL FINISH IT LOVE YOU"))
# print(decode(encode("THIS AFTERNOON I WILL FINISH IT LOVE YOU")))
# print(cipher_book())
# code_book_load({})
# show_cipher_book()
