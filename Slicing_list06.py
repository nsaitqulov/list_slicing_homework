def main(list1):
    """A list of several elements is given. Return all items from the beginning in three steps.
    Args:
        list1(list): parameter
    Returns:
        list: return answer.
    """
    w = list1[ : : 3]
    return w
print(main(['a', 'b', 'c', 'd', 'e', 'f']))