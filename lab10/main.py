from myqueue import MyQueue, Dot


def main():
    q = MyQueue()
    dot_list = [Dot("A", 1, 2),
                Dot("B", 2, 1),
                Dot("C", 4, 7),
                Dot("D", 31, 2)]
    for dot in dot_list:
        q.push(dot)

    q.print_queue()
    print(q.size())
    print(q.get_range())

    print(q.search_element(4, 7))
    q.pop()
    q.pop()
    q.pop()
    q.print_queue()

    q.delete_queue()
    q.print_queue()


if __name__ == '__main__':
    main()
