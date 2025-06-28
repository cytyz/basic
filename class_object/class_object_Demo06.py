# 企业员工管理程序
# a. 员工分类：普通员工（Employee）、组长（Teamleader）、经理（Manager）
# b. 员工属性：姓名（name）、职位（job）、级别（grade）、工龄（year）、工号（uid）
# c. 员工方法：
# get_uid() -- 获取工号
# get_name() -- 获取姓名
# get_job() -- 获取职位
# get_grade() -- 获取级别
# get_year() -- 获取工龄
# salary() -- 统计并返回工资（计算方法如下）
#
# d. 员工工资计算方法：
# 普通员工：3000 + 500 * 级别 + 50 * 工龄
# 组长：4000 + 800 * 级别 + 100 * 工龄
# 经理：5000 + 1000 * (级别 + 工龄)
#
# e. 程序功能：
# 录入员工数据功能（工号自动分配，由 10000 开始）
# 查询功能，分为员工查询和职位查询（见程序实现截图）
# 各类员工级别数量如下：
# 普通员工：10 级
# 组长：6 级
# 经理：3 级
# 升级功能：支持增加多级；当超过当前职位最高级别时，进行升职操作（无论增加多少个级别，只要发生升职，级别一律初始化为 1 级，见程序实现截图）.
# 降级功能：支持减少多级；当超过当前职位最高级别时，进行升职操作（无论减少多少个级别，只要发生降职，级别一律初始化为当前职位最高级别，见程序实现截图）
class Employee:
    def __init__(self, name, job, grade, year, uid):
        self.name = name
        self.job = job
        self.grade = grade
        self.year = year
        self.uid = uid

    def get_uid(self):
        return self.uid

    def get_name(self):
        return self.name

    def get_job(self):
        return self.job

    def get_grade(self):
        return self.grade

    def set_grade(self, grade):
        self.grade = grade

    def get_year(self):
        return self.year

    def salary(self):
        return 3000 + 500 * self.grade + 50 * self.year

class Teamleader(Employee):
    def salary(self):
        return 4000 + 800 * self.grade + 100 * self.year

class Manager(Employee):
    def salary(self):
        return 5000 + 1000 * (self.grade + self.year)

def main():
    mems = {}
    jobs = {'E': [], 'T': [], 'M': []}
    uid = 10000
    MAX_E_GRADE = 10
    MAX_T_GRADE = 6
    MAX_M_GRADE = 3

    while True:
        ins = input("\n1.录入;2.查询;3.升级;4.降级;5.退出：")

        # 主线功能：录入
        if ins == '1':
            name = input("姓名：")
            job = input("职位（E.普通员工;T.组长;M.经理）：")
            year = int(input("工龄："))
            grade = int(input("级别："))

            if job == 'E':
                while grade > MAX_E_GRADE:
                    grade = int(input(f"该职位最高级别为{MAX_E_GRADE}，请重新录入级别："))

                e = Employee(name, job, grade, year, uid)
                mems[uid] = e
                jobs['E'].append(e)

            if job == 'T':
                while grade > MAX_T_GRADE:
                    grade = int(input(f"该职位最高级别为{MAX_T_GRADE}，请重新录入级别："))

                e = Teamleader(name, job, grade, year, uid)
                mems[uid] = e
                jobs['T'].append(e)

            if job == 'M':
                while grade > MAX_M_GRADE:
                    grade = int(input(f"该职位最高级别为{MAX_M_GRADE}，请重新录入级别："))

                e = Manager(name, job, grade, year, uid)
                mems[uid] = e
                jobs['M'].append(e)

            print(f"录入成功！姓名：{name}，工号：{uid}，薪资：{e.salary()}")
            uid += 1

        # 主线功能：查询
        if ins == '2':
            op = input("1.员工查询;2.职位查询：")

            # 支线功能：员工查询
            if op == '1':
                uid = int(input("请输入工号："))

                if mems.get(uid):
                    e = mems[uid]
                    print(f"姓名：{e.get_name()}")
                    print(f"职位：{e.get_job()}")
                    print(f"级别：{e.get_grade()}")
                    print(f"工龄：{e.get_year()}")
                    print(f"薪资：{e.salary()}")
                else:
                    print("该工号不存在！")

            # 支线功能：职位查询
            if op == "2":
                job = input("职位（E.普通员工;T.组长;M.经理）：")

                if job == 'E':
                    if jobs["E"]:
                        print(f"目前普通员工共有{len(jobs['E'])}人")
                        for each in jobs['E']:
                            print(f"{each.get_uid() - each.get_name()}")
                    else:
                        print("目前公司没有普通员工！")

                if job == 'T':
                    if jobs['T']:
                        print(f"目前组长共有 {len(jobs['T'])} 人：")
                        for each in jobs['T']:
                            print(f"{each.get_uid()} - {each.get_name()}")
                    else:
                        print("目前公司没有组长！")

                if job == 'M':
                    if jobs['M']:
                        print(f"目前经理共有 {len(jobs['M'])} 人：")
                        for each in jobs['M']:
                            print(f"{each.get_uid()} - {each.get_name()}")
                    else:
                        print("目前公司没有经理！")

        if ins == "3":
            uid = int(input("请输入工号："))

            if mems.get(uid):
                e = mems[uid]
                print(f"{e.get_name}, 工号：{e.get_uid()}, 当前职位：{e.get_job()}{e.get_grade()}，当前薪资：{e.salary()}")

                name = e.get_name()
                job = e.get_job()
                grade = e.get_grade()
                year = e.get_year()
                old_salary = e.get_salary()

                n = int(input("请输入需要增加的级数："))

                if job == 'E':
                    if grade + n > MAX_M_GRADE:
                        job = "T"
                        grade = 1
                        jobs['E'].remove(e)
                        e = Employee(name, job, grade, year, uid)
                        jobs['T'].append(e)
                        mems[uid] = e
                    else:
                        grade = grade + n


                elif job == 'T':
                    if grade + n > MAX_T_GRADE:
                        job = "M"
                        grade = 1
                        jobs['T'].remove(e)
                        e = Employee(name, job, grade, year, uid)
                        jobs['M'].append(e)
                        mems[uid] = e
                    else:
                        e.set_grade(grade + n)

                elif job == 'M':
                    if grade + n > MAX_M_GRADE:
                        print("已达到最高级别")
                        grade = MAX_M_GRADE
                    else:
                        e.set_grade(grade + n)

                new_salary = e.salary()
                print(f"升级成功！\n{e.get_name}, 工号：{e.get_uid()}, 升级后职位：{e.get_job()}{e.get_grade()}，升级后薪资：{e.salary()}（+{new_salary - old_salary}）")
            else:
                print("该工号不存在！")

        if ins == "4":
            uid = int(input("请输入工号："))

            if mems.get(uid):
                e = mems[uid]
                print(
                    f"{e.get_name}, 工号：{e.get_uid()}, 当前职位：{e.get_job()}{e.get_grade()}，当前薪资：{e.salary()}")

                name = e.get_name()
                job = e.get_job()
                grade = e.get_grade()
                year = e.get_year()
                old_salary = e.get_salary()

                n = int(input("请输入需要减少的级数："))

                if job == 'M':
                    if grade - n <= 0:
                        job = "T"
                        grade = MAX_T_GRADE
                        jobs['M'].remove(e)
                        e = Employee(name, job, grade, year, uid)
                        jobs['T'].append(e)
                        mems[uid] = e
                    else:
                        grade = grade - n

                elif job == 'T':
                    if grade - n <= 0:
                        job = "E"
                        grade = MAX_E_GRADE
                        jobs['T'].remove(e)
                        e = Employee(name, job, grade, year, uid)
                        jobs['E'].append(e)
                        mems[uid] = e
                    else:
                        e.set_grade(grade - n)

                elif job == 'E':
                    if grade - n <= 0:
                        print("已达到最低级别")
                        grade = 1
                    else:
                        e.set_grade(grade - n)

                new_salary = e.salary()
                print(
                    f"升级成功！\n{e.get_name}, 工号：{e.get_uid()}, 升级后职位：{e.get_job()}{e.get_grade()}，升级后薪资：{e.salary()}（+{new_salary - old_salary}）")
            else:
                print("该工号不存在！")

        if ins == "5":
            break

main()
