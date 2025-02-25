import matplotlib.pyplot as plt
from numpy import ones,diag,c_,zeros
from scipy.optimize import linprog

# 设置matplotlib的参数使其支持LaTeX文本和字体大小
plt.rc('text',usetex=True)
plt.rc('font',size=16)

c=[-0.05,-0.27,-0.19,-0.185,-0.185]

# 使用c_来合并数组，
A=c_[zeros(4),diag([0.025,0.015,0.055,0.026])]
# diag 创建对角线矩阵
# A=hstack((zeros(4),diag([0.025,0.015,0.055,0.026])))

Aeq=[[1,1.01,1.02,1.045,1.065]]
beq=[1]

a=0

aa=[]
ss=[]

while a<0.05:
    b=ones(4)*a

    res=linprog(c,A,b,Aeq,beq,bounds=[(0,None),(0,None),(0,None),(0,None),(0,None)])

    x=res.x

    Q=-res.fun

    aa.append(a)

    ss.append(Q)

# 绘制结果 a值和最优值Q之间的关系图
plt.plot(aa,ss,'r*')

# 设置坐标轴的标签
plt.xlabel('$a$')
plt.ylabel('$Q$',rotation=90)

plt.show()

