import pymysql


# 将留言信息存入数据库
def mes_to_sql(f_name="unnamed", p_text="none_text", c_text="none_text"):
    # 连接数据库
    try:
        db = pymysql.connect(host="127.0.0.1", user="root", passwd="078406aaa", db="code_book", charset='utf8')
    except RuntimeError as err:
        db = None
        print("Could not connect to mysql server", err)
    cursor = db.cursor()
    value = (p_text, c_text, f_name)
    sql = "INSERT INTO messages(plain_text, encrypted_text, friend_name)VALUES(%s,%s,%s)"  # 数据个数要和 %s 个数一致
    cursor.execute(sql, value)  # 执行sql语句
    db.commit()
    cursor.close()
    mes_load()
    print("Message saved successfully!")


def mes_load():
    messages = []
    # 连接数据库
    try:
        db = pymysql.connect(host="127.0.0.1", user="root", passwd="078406aaa", db="code_book", charset='utf8')
    except RuntimeError as err:
        db = None
        print("Could not connect to mysql server", err)
    cursor = db.cursor()
    sql = "SELECT * FROM messages"
    cursor.execute(sql)
    results = cursor.fetchall()
    for item in results:
        messages.append({
            "id": item[0],
            "friend": item[3],
            "mes": item[2]
        })
    cursor.close()
    print("Message loaded successfully!")
    return messages
