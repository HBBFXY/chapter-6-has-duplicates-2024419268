# 在这个文件中编写代码
def has_duplicates(lst):
    """
    检查列表中是否有重复元素
    参数: lst - 任意列表
    返回: bool - 如果有重复元素返回 True，否则返回 False
    """
    # 学生实现代码区域
   seen = set()
    for item in lst:
        if item in seen:
            return True
        seen.add(item)
    return False

# 主程序 - 测试函数
if __name__ == "__main__":
    # 学生需要提供测试用例
   test_cases = [
    [1, 2, 3, 4, 5],          
    [1, 2, 3, 2, 4],          
    ['a', 'b', 'c', 'a'],     
    [10, 20, 30, 40],         
    [5, 5, 5, 5],             
    []                        
]
    
    # 测试每个用例，编写具体测试代码
