"""
The count-and-say sequence is the sequence of integers with the first five terms as following:

1.     1
2.     11
3.     21
4.     1211
5.     111221
1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.

Given an integer n where 1 ≤ n ≤ 30, generate the nth term of the count-and-say sequence.

Note: Each term of the sequence of integers will be represented as a string.

 

Example 1:

Input: 1
Output: "1"
Example 2:

Input: 4
Output: "1211"
"""

class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 0:
            return ""

        count = 0
        current_str = "1"
        for i in range(1,n):
            tmp = ""
            prev = current_str[0]
            for index in range(len(current_str)):
                
                if prev != current_str[index]:
                    tmp = tmp + str(count) + prev
                    prev = current_str[index]
                    count = 1
                else:    
                    count += 1   

            tmp = tmp + str(count) + prev  
            count = 0 
            current_str = tmp

        return current_str

class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        cur = "1"
        for i in range(1,n):
            tmp,prev,count = "",cur[0],0
            for char in cur:
                if char == prev:
                    count += 1
                else:
                    tmp = tmp + str(count) + prev
                    prev = char
                    count = 1
            tmp = tmp + str(count) + prev
            cur = tmp
        return cur

if __name__ == '__main__':
    print(Solution().countAndSay(6))            


                    















