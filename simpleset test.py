# simpleset test

# 1. 사용시 simpleset 붙여줘야 함
# import simpleset

# # print(dir(simpleset))
# a=[1,2,3]
# b=[3,4,5]
# print(simpleset.union(a,b))

# 2. 사용시 simpleset 안 붙여줘도 함
# from simpleset import *

# # print(dir(simpleset))
# a=[1,2,3]
# b=[3,4,5]
# print(union(a,b))

# 3. 사용시 알리아스를 붙여줘야 함
import simpleset as sp

# print(dir(simpleset))
a=[1,2,3]
b=[3,4,5]
print(sp.union(a,b))
