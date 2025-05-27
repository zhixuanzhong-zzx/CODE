def check_age(age):
    """
    计算两个数字的和。

    Parameters
    ----------
    a : int
        第一个数字。
    b : int
        第二个数字。

    Returns
    -------
    int
        a 和 b 的和。
    """
    if age >= 18:
        return "SUCCESS"  # 成年返回 "SUCCESS"
    else:
        return None       # 未成年返回 None

result = check_age(18)    # 传入年龄 16
if not result:            # 如果 result 是 None（即 False）
    print("未成年，不可以进入")  # 输出提示