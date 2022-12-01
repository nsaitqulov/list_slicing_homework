def main(list1,n):
    """
    A list of several elements is given. Return all elements in reverse order except n elements from the beginning.
    Args:
        list1(list): parameter
        n(int): parameter
    Returns:
        list: return answer.
    """
    w = list1[len(list1) - (len(list1) - n): : 1]
    return w[: : -1]
print(main(['a', 1, 'b', 2, 'c', 3, 'd', 4], 2))