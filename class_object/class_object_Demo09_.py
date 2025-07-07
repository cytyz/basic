# 自定义 一进制 与 电影票订购系统
# 重载加（+）、减（-）、乘（*）、除（/）、地板除（//）五个运算符（为了简化实现逻辑，我们约定无论除法还是地板除，都统一采用地板除，即不考虑小数位）
from warnings import resetwarnings


class UnaryNumber:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        if self.value < 0:
            return '-' + '1' * abs(self.value)
        elif self.value == 0:
            return "没有"
        else:
            return '1' * self.value

    def __int__(self):
        return self.value

    def __add__(self, other):
        if isinstance(other, UnaryNumber):
            return UnaryNumber(self.value + other.value)
        else:
            raise ValueError("类型不同无法相加")

    def __sub__(self, other):
        if isinstance(other, UnaryNumber):
            return UnaryNumber(self.value - other.value)
        else:
            raise ValueError("类型不同无法相减")

    def __mul__(self, other):
        if isinstance(other, UnaryNumber):
            return UnaryNumber(self.value * other.value)
        else:
            raise ValueError("类型不同无法相乘")

    def __truediv__(self, other):
        if isinstance(other, UnaryNumber):
            if other.value != 0:
                return UnaryNumber(self.value // other.value)
            else:
                raise ValueError("除数不能为0")
        else:
            raise ValueError("类型不同无法相除")

    def __floordiv__(self, other):
        if isinstance(other, UnaryNumber):
            if other.value != 0:
                return UnaryNumber(self.value // other.value)
            else:
                raise ValueError("除数不能为0")
        else:
            raise ValueError("类型不同无法相除")

x = UnaryNumber(3)
y = UnaryNumber(5)
print(x, y) # 111 11111
print(x + y) # 11111111
print(x * y) # 111111111111111
print(x // y) # 没有


# ——————————————————————————————————————————————————
# 电影票订购系统
# 需要实现的功能：
# 查看信息
# 预订座位
# 查看预订
#
# 推荐实现方案（当然你也可以按照自己的思路来定义）：
# a. 电影院（Cinema）：用于管理电影的添加和信息呈现
# 添加电影和播放时间（add_movie）
# 显示所有电影及其播放时间（show_movies）
#
# b. 座位（Seat）：用于管理座位
# 管理座位是否被预定（reserve）
#
# c. 预订系统（MovieBookingSystem）：用于管理预定信息
# 预定座位操作（reserve_seat）
# 查看预订信息（view_reservation）

# 定义电影类
class Cinema:
    def __init__(self, movie_name):
        self.movie_name = movie_name
        self.movies = {}

    # 添加电影名，电影时间
    def add_movie(self, movie_name, schedule):
        self.movies[movie_name] = schedule

    #  展示电影时间
    def show_movies(self):
        for movie_name, schedule in self.movies.items():
            print(f"{movie_name}")
            for date, times in schedule:
                print(f"{date}: {', '.join(times)}")

# 定义座位类
class Seat:
    def __init__(self, row, number):
        self.row = row          # 座位所在的排数
        self.number = number    # 座位号
        self.reserved = False   # 标志一个座位是否被预定

    # 预定座位
    def reserve(self):
        if not self.reserved:
            self.reserved = True
        else:
            raise ValueError("该座位已被预定。")

class MovieBookingSystem:
    def __init__(self, cinema, rows, seats_per_row):
        self.cinema = cinema
        self.reservations = {}  # 存储预订信息的字典

        # 创建座位实例并存储到字典中
        self.seats = {f"{row + 1}-{seat + 1}": Seat(row + 1, seat + 1) for row in range(rows) for seat in range(seats_per_row)}

    # 预订座位
    def reserve_seat(self, movie_name, date, time, seat_id):
        key = (movie_name, date, time)
        seat = self.seats.get(seat_id)

        # 如果位置不存在抛出异常
        if not seat:
            raise ValueError("无效的座位号")

        # 如果预订信息不存在，创建新的预订信息
        if key not in self.reservations:
            self.reservations[key] = []

        # 如果座位未被预定，预定座位并添加到预定信息
        if seat not in self.reservations[key]:
            seat.reserve()
            self.reservations[key].append(seat)
        else:
            raise ValueError("该座位已被预定。")

    # 查看座位信息
    def view_reservation(self, movie_name, date, time):
        key = (movie_name, date, time)
        return self.reservations.get(key, [])

def dispaly_menu():
    print("欢迎来到电影票订购系统")
    print("1. 查看电影")
    print("2. 预订座位")
    print("3. 查看预订")
    print("4. 退出系统")

# 获取用户输入
def user_input(prompt):
    try:
        return input(prompt)
    except KeyboardInterrupt:
        print("\n谢谢使用！")
        exit(0)

def main():
    # 创建电影院实例并添加电影
    cinema = Cinema("鱼C影院")
    cinema.add_movie("《小甲鱼的救赎》", {"2023-07-20": ["14:00", "18:00"]})
    cinema.add_movie("《不二如是的假日》", {"2023-07-20": ["16:00", "20:00"]})

    # 创建预定实例
    booking_system = MovieBookingSystem(cinema, 10, 10)

    while True:
        dispaly_menu()
        choice = user_input("请输入操作指令：")

        # 查看电影
        if choice == "1":
            print("电影时间表 >>>")
            cinema.show_movies()

        # 预定座位
        elif choice == "2":
            movie_name = user_input("请输入电影名称")
            data = user_input("请输入日期（年-月-日）：")
            time = user_input("请输入时间（时：分）：")
            seat_id = user_input("请输入座位号（排数-座位号）")

            try:
                booking_system.reserve_seat(movie_name, data, time, seat_id)
                print("预定成功！\n")
            except ValueError as e:
                print(f"预定失败：{e}\n")

        # 查看预定
        elif choice == "3":
            movie_name = user_input("请输入电影名称")
            data = user_input("请输入日期（年-月-日）：")
            time = user_input("请输入时间（时：分）：")

            reserved_seat = booking_system.view_reservation(movie_name, data, time)
            if reserved_seat:
                print("预定的座位：")
                for seat in reserved_seat:
                    print(f"{seat.row}排，{seat.number}号")
            else:
                print("没有预定的座位。")
            print()

        # 退出系统
        elif choice == "4":
            print("谢谢使用！")
            break

        # 无效选择处理
        else:
            print("无效选择，请输入1~4之间的数字。\n")

if __name__ == "__main__":
    main()
