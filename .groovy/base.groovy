//$引用
name = "xuhongchuan" 
println("my name is $name")//my name is xuhongchuan
// 集合在结尾添加元素的两种写法
demoList.add(100) 
demoList << 100
//闭包
// 打印奇数
def getOdd = {
    if (it % 2 != 0)  //it是隐式变量
        println it
}