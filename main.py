def print_hi(name):
    # 在下面的代码行中使用断点来调试脚本。
    print(f'Hi, {name}')  # 按 Ctrl+F8 切换断点。
    b = 10
    a = b
    a = 20
    print(a, b)
    print(a is b)
    if True:
        print("neo")
    else:
        print("smile")
    total = 'item_one' + \
            'item_two' + \
            'item_three'
    print(total)
    word = 'word'
    sentence = "This is a sentence."
    paragraph = """This is a paragraph. It is
    made up of multiple lines and sentences."""
    print(paragraph)
    print(sentence)
    print(word)
    print(type(paragraph))
    print(type(sentence))
    print(type(word))

if __name__ == '__main__':
    print_hi('PyCharm')
