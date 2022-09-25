'''
阿里巴巴商家节，用户，消费总金额，账户金额，优惠券
输入购买总购买金额，
如果金额0-500则是lv1级别，
如果500-2000元则是lv2级别，
2000以上是lv3级别

lv1：随机赠送3章1-10元的优惠券；
lv2：赠送2章50元优惠券，如果充值则送充值金额的10%；
lv3：赠送2张100元优惠券，如果充值则赠送15%的金额
'''

import random

buy_money = int(input('欢迎来到阿里巴巴商家节!请输入您的购买金额:'))
if buy_money < 500:
    r1 = random.randint(1, 10)
    r2 = random.randint(1, 10)
    r3 = random.randint(1, 10)
    print('恭喜您分别获得%d,%d,%d元的优惠券' % (r1, r2, r3))
elif 500 <= buy_money < 2000:
    recharge = input('是否选择充值（y/n）:')
    if recharge == 'n':
        print('恭喜您获得2张50元优惠券')
    elif recharge == 'y':
        recharge_money = int(input('请输入您要充值的金额：'))
        print('恭喜您额外获得%.2f元' % (recharge_money / 10))
    else:
        print('输入有误，请重新输入！')
elif buy_money >= 2000:
    recharge = input('是否选择充值（y/n）:')
    if recharge == 'n':
        print('恭喜您获得2张100元优惠券')
    elif recharge == 'y':
        recharge_money = int(input('请输入您要充值的金额：'))
        print('恭喜您额外获得%.2f元' % (recharge_money * 15 / 100))
    else:
        print('输入有误，请重新输入！')
else:
    print('您当前金额输入有误')
