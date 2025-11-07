# 在这个文件中编写代码
def has_duplicates(lst):
    """
    判断列表中是否存在重复元素
    :param lst: 输入的列表
    :return: 如果存在重复元素返回True，否则返回False
    """
    seen = set()
    for item in lst:
        if item in seen:
            return True
        seen.add(item)
    return False
# 测试用例
test_cases = [
    [1, 2, 3, 4, 5],          
    [1, 2, 3, 2, 4],          
    ['a', 'b', 'c', 'a'],     
    [10, 20, 30, 40],         
    [5, 5, 5, 5],             
    []                        
]

# 调用函数并输出结果
for i, test in enumerate(test_cases):
    result = has_duplicates(test)
    print(f"Test case {i+1}: {test} -> {result}")
