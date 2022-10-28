# Modul11
import unittest
import random

list_num = []

n=7
for i in range(n):
    list_num.append(random.randint(0, 99))
print("Случайно заданный список чисел:", list_num)

def sorting(nums): 

    if len(nums) > 1: 
        mid = len(nums)//2
        left = nums[:mid] 
        right = nums[mid:]
        sorting(left) 
        sorting(right) 
        i = j = k = 0

        while i < len(left) and j < len(right): 
            if left[i] < right[j]: 
                nums[k] = left[i] 
                i+=1
            else: 
                nums[k] = right[j] 
                j+=1
            k+=1

        while i < len(left): 
            nums[k] = left[i] 
            i+=1
            k+=1

        while j < len(right): 
            nums[k] = right[j] 
            j+=1
            k+=1

    return nums


print ("Упорядоченный список чисел:", sorting(list_num))


class TestSort(unittest.TestCase):

    def test1(self):
        b = [992, 74, 661, 40, 282, 497]
        c = sorted(b)
        print ("Результат теста №1:",c)
        self.assertEqual(sorting(b), c)

    def test2(self):
        b =  [-35, 9, -91, 13, 53, 76, 0, 23, -1]
        c = sorted(b)
        print ("Результат теста №2:",c)
        self.assertEqual(sorting(b), c)

    def test3(self):
        b = [331, 830, 79, 894, 463, 271, 353]
        c = sorted(b)
        print ("Результат теста №3:",c)
        self.assertEqual(sorting(b), c)



suite = unittest.TestLoader().loadTestsFromTestCase(TestSort)
unittest.TextTestRunner(verbosity=2).run(suite)
