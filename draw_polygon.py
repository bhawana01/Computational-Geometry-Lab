from matplotlib import pyplot as plt


def get_point():
    p = input('Enter x and y coordinates as x, y :')
    p = p.split(',')
    x = int(p[0])
    y = int(p[1])
    return [x,y]


def user_input():
    input_str = []
    ask = int(input('How many vertices you wanna take?'))
    for i in range(ask):
        input_str.append(get_point())
    input_str.append(input_str[0])  # repeat the first point to create a 'closed loop'
    xs, ys = zip(*input_str)  # create lists of x and y values
    plt.figure()
    plt.plot(xs, ys)
    plt.show()




def main():
    user_input()
