def main(list1,n,k):
    """
    A list of several elements is given. Return the value from n index to k index.
    Args:
        list1(list): parameter
        n(int): parameter
        k(int): parameter
    Returns:
        list: return answer.
    """
    w = list1[n: k: 1]
    return w

print(main(['a', 1, 'b', 2, 'c', 3, 'd', 4], 1, 3))