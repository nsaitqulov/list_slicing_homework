def main(list1):
    """
    A list of several elements is given. Return this list by adding the reverse.
    Args:
        list1(list): parameter
    Returns:
        list: return answer.
    """
    w=list1[: : -1]
    return list1 + w
print(main(['a', 'b', 'c', 'd']))