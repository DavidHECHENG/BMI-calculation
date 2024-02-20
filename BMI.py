height = input('請輸入您的身高為多少公分：')
weight = input('請輸入您的體重為幾公斤：')
height = float(height)
weight = float(weight)
BMI = weight / (height * height / 10000)
if BMI>= 0 and BMI < 18.5 :
    print('您的BMI為' , BMI ,'，''體重過輕了！')
elif BMI >= 18.5 and BMI < 24 :
    print('您的BMI為' , BMI , '，''恭喜您體重在正常範圍')
elif BMI >= 24 and BMI < 27 :
    print('您的BMI為' , BMI ,'，','體重已經稍微超重了！')
elif BMI >= 27 and BMI < 30 :
    print('您的BMI為' , BMI ,'，','您已經達到輕度肥胖的邊準，要注意！')
elif BMI >= 30 and BMI < 35 :
    print('您的BMI為' , BMI ,'，','您已達到中度肥胖的標準，請更加注意自身體重或是尋求幫助！')
elif BMI >= 35 :
    print('您的BMI為' , BMI ,'，','您已達到重度肥胖的標準，建議您前往醫院尋求專業的幫助！')
else :
    print('請不要輸入不正常的數值！')     