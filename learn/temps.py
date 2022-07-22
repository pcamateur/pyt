shengxiao='猴鸡狗猪鼠牛虎兔龙蛇马羊'                     

xz_name=['摩羯座','水瓶座','双鱼座','白羊座','金牛座','双子座','巨蟹座','狮子座','处女座','天秤座','天蝎座','射手座'] 

xz_date = ((1,20),(2,19),(3,21),(4,21),(5,21),(6,22),(7,23),(8,23),(9,23),(10,23),(11,23),(12,23))

year,month,day = eval(input("请输入出生年月日，用逗号分隔："))  

u_shengxiao =shengxiao[year%12]                               

u_xz_name =xz_name[len(list(filter(lambda x:x<(month,day),xz_date)))%12]

print("属：%s  星座：%s"%(u_shengxiao,u_xz_name))
