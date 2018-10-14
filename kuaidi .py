def choice_type():
    print('welcome to WSC pizza')
    the_type = input('\n' + '1.delivery；\n' + '2.pick up；' + '\n please choose:')
    try:
        the_type = int(the_type)
        all_info = []
        if the_type == 1:
            print('delivery')
            name = input("sbs name：")
            if name:
                all_info.append(name)
                address = input('sbs address：')
                if address:
                    all_info.append(address)
                    phone = input('sbs phone number：')
                    if phone:
                        all_info.append(phone)
                        return all_info
                    else:
                        print('must have phone number')
                else:
                    print('must have address')
            else:
                print('must have name')
        elif the_type == 2:
            print('pick up')
            name = input("name：")
            if name:
                return name
            else:
                print('must have name')
        else:
            print('The choose is wrong!')
            return None
    except:
        print ('The choose is wrong!!!')
        return None


def choice_number():
    number = input('pizza number(1~5)：')
    try:
        number = int(number)
        if number >= 1 and number <= 5:
            print('pizza number' + str(number))
            return number
        else:
            print('The number is not in the range.')
            return None
    except:
        print ("The number if wrong!!!")
        return None

def choice_pizza(num):
    print('we have 12 kinds of pizza please choose name ：')
    pizzas_dicts = {'1.Hot pizza': 8.50, '2.Fish pizza': 8.50, '3.Apple pizza': 8.50, '4.Salmon pizza': 8.50,
                    '5.Seafood pizza': 8.50,
                    '6.Sausage pizza': 8.50, '7.Fruit pizza': 8.50, '8.Beff pizza': 13.50, '9.Chicken pizza': 13.50,
                    '10.Lab pizza': 13.50, '11.Kiwi pizza': 13.50, '12.Rice pizza': 13.50}
    pizzas_key_list = []
    for key, value in pizzas_dicts.items():
        print(key + ':' + str(value))
        pizzas_key_list.append(key)
    pizzas = []
    for i in range(num):
        pizza_type = input("name" + str(i + 1) + "number：")
        try:
            pizza_type = int(pizza_type)
            if pizza_type >= 1 and pizza_type <= 12:
                pizzas.append(pizza_type)
            else:
                print('The pizza number is wrong!!')
                break
        except:
            print('The pizza number is wrong!!!')
            break
    return pizzas, pizzas_key_list


if __name__ == '__main__':
    sb_info = choice_type()
    num = choice_number()
    if num:
        pizzas, pizzas_list = choice_pizza(num)
        if isinstance(sb_info, str):
            print('sales message：')
            print('total sales' + str(len(pizzas)) + 'number')
            sums = 0
            for pizza in pizzas:
                if pizza <= 7:
                    sums += 8.5
                    print('piiza name：' + pizzas_list[pizza-1] + ",each：$8.5")
                else:
                    sums += 13.5
                    print('pizza kind：' + pizzas_list[pizza-1] + ",each：$13.5")
            print("total pirce：" + str(sums))
            print("sbs name：" + sb_info)
        else:
            print('message：')
            print('pizza name' + str(len(pizzas)) + 'number')
            sums = 0
            for pizza in pizzas:
                if pizza <= 7:
                    sums += 8.5
                    print('pizza name：' + pizzas_list[pizza-1] + ",each：$8.5")
                else:
                    sums += 13.5
                    print('pizza name：' + pizzas_list[pizza-1] + ",each：$13.5")
            print("total pirce：" + str(sums + 3) + "$3 for delivery")
            print("sbs name：" + sb_info[0])
            print("sbs address：" + sb_info[1])
            print("sbs phone number：" + sb_info[2])
        ex = input("cancel，1，or other ESC：")
        if ex:
            try:
                ex = int(ex)
                if ex == 1:
                    print('you have canceled！！')
                else:
                    pass
            except:
                pass
        else:
            pass

    else:
        pass

