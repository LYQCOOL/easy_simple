def choice_type():
    print('欢迎来到披萨饼订单管理系统')
    the_type = input('订单类型，如下：\n' + '1.快递；\n' + '2.面取；' + '\n请选择:')
    try:
        the_type = int(the_type)
        all_info = []
        if the_type == 1:
            print('您选择的是类型是快递')
            name = input("请输入客户姓名：")
            if name:
                all_info.append(name)
                address = input('请输入客户地址：')
                if address:
                    all_info.append(address)
                    phone = input('请输入客户电话：')
                    if phone:
                        all_info.append(phone)
                        return all_info
                    else:
                        print('客户电话不能为空')
                else:
                    print('客户地址不能为空')
            else:
                print('客户姓名不能为空')
        elif the_type == 2:
            print('您选择的是类型是面取')
            name = input("请输入客户姓名：")
            if name:
                return name
            else:
                print('客户姓名不能为空')
        else:
            print('只能输入1或2，请从新输入！')
    except:
        print('输入格式错误，只能输入1或则2！')
    return None


def choice_number():
    number = input('请输入披萨个数(1到5个)：')
    try:
        number = int(number)
        if number >= 1 and number <= 5:
            print('您输入的披萨数是' + str(number) + '个')
            return number
        else:
            print('披萨数不对，请输入1到5之间的数字！！')
    except:
        print('输入格式错误，请输入1-5之间的数字！！')
    return None


def choice_pisha(num):
    print('披萨类型有1到12共十二种，如下，购买请输入对应序号：')
    pishas_dicts = {'1.Hot pizza': 8.50, '2.Fish pizza': 8.50, '3.Apple pizza': 8.50, '4.Salmon pizza': 8.50,
                    '5.Seafood pizza': 8.50,
                    '6.Sausage pizza': 8.50, '7.Fruit pizza': 8.50, '8.Beff pizza': 13.50, '9.Chicken pizza': 13.50,
                    '10.Lab pizza': 13.50, '11.Kiwi pizza': 13.50, '12.Rice pizza': 13.50}
    pishas_key_list = []
    for key, value in pishas_dicts.items():
        print(key + ':' + str(value))
        pishas_key_list.append(key)
    pishas = []
    for i in range(num):
        pisha_type = input("请选择您购买的第" + str(i + 1) + "个披萨：")
        try:
            pisha_type = int(pisha_type)
            if pisha_type >= 1 and pisha_type <= 12:
                pishas.append(pisha_type)
            else:
                print('披萨个数输入错误！！')
                break
        except:
            print('输入格式错误！！')
            break
    return pishas, pishas_key_list


if __name__ == '__main__':
    kehu_info = choice_type()
    num = choice_number()
    pishas, pishas_list = choice_pisha(num)
    if isinstance(kehu_info, str):
        print('客户买取的披萨信息如下：')
        print('共买取' + str(len(pishas)) + '个披萨，详细信息如下')
        sums = 0
        for pisha in pishas:
            if pisha <= 7:
                sums += 8.5
                print('类别：' + pishas_list[pisha] + ",单价：8.5美元")
            else:
                sums += 13.5
                print('类别：' + pishas_list[pisha] + ",单价：13.5美元")
        print("披萨总价：" + str(sums) + "美元,客户面取，无快递费！")
        print("客户姓名：" + kehu_info)
    else:
        print('客户买取的披萨信息如下：')
        print('共买取' + str(len(pishas)) + '个披萨，详细信息如下')
        sums = 0
        for pisha in pishas:
            if pisha <= 7:
                sums += 8.5
                print('类别：' + pishas_list[pisha] + ",单价：8.5美元")
            else:
                sums += 13.5
                print('类别：' + pishas_list[pisha] + ",单价：13.5美元")
        print("披萨总价：" + str(sums + 3) + "美元,加收快递费3美元！")
        print("客户姓名：" + kehu_info[0])
        print("客户地址：" + kehu_info[1])
        print("客户电话：" + kehu_info[2])
    ex = input("若要取消订单，请输入1，否则按任意键（除1外）退出：")
    if ex:
        try:
            ex = int(ex)
            if ex == 1:
                print('您已经取消订单！！')
            else:
                pass
        except:
            pass
    else:
        pass
