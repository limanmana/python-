#  (了解) 重载
# 面试题；重写与重载的区别？



#三个数比大小
class G(object):
    @staticmethod
    def y(n1 , n2, n3):
        if n1 < n2 > n3:
            return n2
        if n1 < n3 > n2:
            return n3
        if n2 < n1 > n3:
            return n1

    # 第二个方法
    def n(n1,n2,n3):
        y = n1
        if n2 > y:
            y = n2
        if n3 > y:
            y = n3
        return y



    # 列表比大小
    def n1(n2):
        y = n2[0]
        for i in range(0 ,len(n2)):
            if i < n2[i]:
                y = n2[i]
        return y


print('最大值', G.y(1,2,3))
print('最大值', G.n(1,3,4))
print('最大值', G.n1([1,3,4,5]))








