1,2,3,4,5,7,8,

2,4,6 ,9 



#1. SELECT * FROM data;

 
2. SELECT * FROM data LIMIT(10);
 
3. SELECT id FROM data;  //id 是 data 表的特定一列
 
4. SELECT COUNT(id) FROM ttt;
 
5. SELECT * FROM data WHERE id<1000 AND age>30;
 
6. SELECT id,COUNT(DISTINCT order_id) FROM table1 GROUP BY id;
 
7. SELECT * FROM table1 t1 INNER_JOIN table2 t2 ON t1.id = t2.id;
 
8. SELECT * FROM table1 UNION SELECT * FROM table2;

 
9. DELETE FROM table1 WHERE id=10;

 
10. ALTER TABLE table1 DROP COLUMN column_name;



"""
from pathlib import Path
pwd= Path.cwd()
print(pwd)

print(0)


def scope_test():
    def do_local():
        spam = "local spam"
    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"
    def do_global():
        global spam
        spam = "global spam"

    spam = "test spam"
    do_local()
    print("After local assignment:", spam)
    do_nonlocal()
    print("After nonlocal assignment:", spam)
    do_global()
    print("After global assignment:", spam)
print(dir())
scope_test()
print("In global scope:", spam)
print(dir())

class Solution:
    def ff(self, arr, ll, r, kk):
        if ll == r: return arr[r]
        q = self.pp(arr, ll, r)
        w = q - ll + 1

        if w == kk:
            return arr[q]
        elif w > kk:
            return self.ff(arr, ll, q - 1, kk)
        elif w < kk:
            return self.ff(arr, q + 1, r, kk - w)

    def pp(aa, start, end):
        key = aa[end]
        s = start

        for i in range(start, end + 1):
            if aa[i] > key:
                aa[i], aa[s] = aa[s], aa[i]
                s += 1
        aa[s], aa[end] = aa[end], aa[s]

        return s

    def findKthLargest(self, nums: List[int], k: int) -> int:
        return self.ff(nums, 0, len(nums) - 1, k)



a = [1, 3, 2, 4, 5, 6, 7, 8, 9, 33, 44, 55, 22, 11]


def kk(arr, l, r):
    if l < r:
        q = pp(arr, l, r)
        kk(arr, l, q - 1)
        kk(arr, q + 1, r)


kk(a, 0, 13)
print(333, a)

class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        if not nums:
            return 0

        n = len(nums)
        ans = n
        start, end, total = 0, 0, 0
        for end in range(n):
            total += nums[end]
            while total >= s:
                ans = min(ans, end - start)
                total -= nums[start]
                start += 1

        return 0 if ans == n else ans + 1


class Solution:
    def minSubArrayLen(self, s, nums):
        if max(nums) >= s:
            return 1
        dp = [0]

        k = len(nums)
        now = 0
        for i in range(k):
            now += nums[i]
            dp.append(now)
        print(dp)
        diff = k + 2
       
        if now < s: return 0
        

        slow = fast = 0
        for slow in range(k + 1):
            while fast <= k and dp[fast] - dp[slow] < s:
                fast += 1
            print(fast)
        '''
        '''
            if fast == k + 1:
                break
            else:
                t = fast - slow
                if t == 1: return 1
                if t < diff: diff = t
            '''
        return diff


cc = Solution()
cc.minSubArrayLen(7, [2, 3, 1, 2, 4, 3, 8])

dd=input("input the nums in the list:")

astr = "ai=" + dd
exec(astr)  #去掉括号并执行它，其实是执行了 ai=(33,44,55,66)
print(ai,"我是元组",type(ai))
ke = list(ai)  #把元组类型转换为列表
print(ke,"我就是一个列表",type(ke))


class Solution:
    def threeSumClosest(self, nums, target):
        nums.sort()
        absdis = float("inf")  # record abs
        diff = 0  # save sum3-target
        k = len(nums)
        n, t = nums, target
        rr = k - 2
        for i in range(k - 2):
            j = i + 1
            r = k - 1
            # 两种边界判断
            j2 = i + 2
            small = n[i] + n[j] + n[j2]
            if small == t:
                return t
            elif small > t:  # n[i] 已经很大了，不用再循环了。
                if small - t < absdis:
                    return small
                else:
                    return t + diff
            elif small < t:
                # check the big from this n[i]
                big = n[i] + n[rr] + n[r]
                if big == t:
                    return t
                elif big < t:
                    # 尝试更新
                    temp = t - big
                    if temp < absdis:
                        absdis = temp
                        diff = -temp
                elif big > t:
                    # 需要双指针查找，并更新absdis
                    while j < r:
                        a = n[i] + n[j] + n[r]
                        if a == t:
                            return a
                        elif a > t:
                            # refresh absdis and diff if need
                            if a - t < absdis:
                                absdis = a - t
                                diff = absdis
                            # r -= 1  add slide when two nums are same
                            k0 = r - 1
                            while j < k0 and n[k0] == n[r]:
                                k0 -= 1
                            r = k0

                        elif a < t:
                            if t - a < absdis:
                                absdis = t - a
                                diff = -absdis

                            jj = j + 1
                            while jj < r and n[jj] == n[j]:
                                jj += 1
                            j = jj

        return t + diff"""
