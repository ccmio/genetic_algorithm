# 最优解在程序中以数字形式存储，再本函数中翻译成字符串形式的基因型用以输出结论
# dict1为一号位基因，1代表A11，2代表A12，5个字典对应5个位置的基因，以此类推
dict1 = {'1': 'A11',
        '2': 'A12',
        '3': 'A13',
        '4': 'A14',
        '5': 'A15'
        }
dict2 = {'1': 'A21',
        '2': 'A22',
        '3': 'A23',
        }
dict3 = {'1': 'A31',
        '2': 'A32',
        '3': 'A33',
        }
dict4 = {'1': 'T11',
        '2': 'T12',
        '3': 'T13',
        }
dict5 = {'1': 'T21',
        '2': 'T22',
        '3': 'T23',
        }
tran_list = [dict1, dict2, dict3, dict4, dict5]


def translate(list):
    num2char = []
    result = []
    i = 0
    for temp1 in list:
        num2char.append(str(temp1))
    for temp2 in num2char:
        tran = tran_list[i][temp2]
        result.append(tran)
        i += 1
    # 返回翻译好的最优解
    return result
