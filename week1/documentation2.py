
# 风格一：reStructuredText 格式（Sphinx 默认，PEP 287）
def add(a, b):
    """Return the sum of a and b.

    :param a: 第一个加数
    :param b: 第二个加数
    :return: 两数之和
    :rtype: int or float
    """
    return a + b


# 风格二：Google 风格（可读性强，被 Google 内部和众多开源项目采用）
def add(a, b):
    """Return the sum of a and b.

    Args:
        a: 第一个加数
        b: 第二个加数

    Returns:
        两数之和
    """
    return a + b


# 风格三：NumPy 风格（科学计算领域常用）
def add(a, b):
    """Return the sum of a and b.

    Parameters
    ----------
    a : int or float
        第一个加数
    b : int or float
        第二个加数

    Returns
    -------
    int or float
        两数之和
    """
    return a + b