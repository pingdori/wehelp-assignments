#要求一：函式與流程控制
def calculate(min,max):
    sum=0
    for n in range(min,max+1):
            sum=sum+n
    print(sum)
calculate(1,3)
calculate(4,8)

#要求二：Python 字典與列表
def avg(data):
    lenght=data["count"]
    emp=data["employees"]
    money=emp[0]["salary"]
    sum=0
    for x in emp:
        sum=sum+x["salary"]
    sum=sum/lenght
    print(sum)
avg({
"count":3,
"employees":[
{
"name":"John",
"salary":30000
},
{
"name":"Bob",
"salary":60000
},
{
"name":"Jenny",
"salary":50000
}
]
})
 
 
 #要求三：演算法
def maxProduct(nums):
    m1=max(nums)
    x2=nums.copy()
    x2.remove(m1)
    m2=max(x2)

    x=m1
    y=m2
    p=x*y
    
    mi=min(nums)
    nums.remove(mi)
    mii=min(nums)
    
    t=mi
    r=mii
    s=mi*mii

    if (p>s):
        print(p)
    else:
        print(s)
# 請用你的程式補完這個函式的區塊
maxProduct([5, 20, 2, 6]) # 得到 120
maxProduct([10, -20, 0, 3]) # 得到 30
maxProduct([-1, 2]) # 得到 -2
maxProduct([-1, 0, 2]) # 得到 0
maxProduct([-1, -2, 0]) # 得到 2
#要求四 ( 請閱讀英文 )：演算法
def twoSum(nums, target):
    x2=nums.copy()
    for a,b in enumerate(nums):
        j=target-b
        for c,d in enumerate(x2):
            if (j==d):
                return [a,c] 
result=twoSum([2, 11, 7, 15], 9)
print(result) # show [0, 2] because nums[0]+nums[2] is 9