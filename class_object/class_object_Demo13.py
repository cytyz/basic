# iPhone 提醒事项
# 编写一个类，模拟类似 iPhone 的提醒事项功能。
# 使用文件（如：reminders.pkl）来存储提醒事项
# 添加提醒事项
# 查看提醒事项列表
# 删除提醒事项
# 标记提醒事项为已完成
# 搜索提醒事项
# 按不同属性对提醒事项进行排序
import pickle
import time
from pathlib import Path


class Reminder:
    def __init__(self, storage_file='reminder.pkl'):
        self.storage_file = Path(storage_file)
        self.reminders = self.load_reminders()

    def __call__(self, action, *args, **kwargs):
        actions = {
            '添加': self.add_reminder,
            '查看': self.list_reminders,
            '删除': self.delete_reminder,
            '完成': self.complete_reminder,
            '搜索': self.search_reminders,
        }
        if action in actions:
            # 调用对应的函数，并传递 *args 和 **kwargs 作为参数
            actions[action](*args, **kwargs)
        else:
            print("无效操作，请使用'添加'、'查看'、'删除'、'完成'或'搜索'。")

    def __getitem__(self, index):
        return self.reminders[index]

    def __repr__(self):
        return f'Reminder(reminders={self.reminders})'

    def __str__(self):
        return f'提醒事项共有 {len(self.reminders)} 条'

    def load_reminders(self):
        if self.storage_file.exists():
            with self.storage_file.open('rb') as f:
                return pickle.load(f)
        return []

    def save_reminders(self):
        with self.storage_file.open('wb') as file:
            # pickle.dump() 函数用于将 Python 对象序列化为二进制数据，并写入到文件中
            pickle.dump(self.reminders, file)

    def add_reminder(self, reminder, category, color, priority=0, delay=0):
        reminder_item = {'text': reminder, 'category': category, 'color': color,
                         'completed': False, 'priority': priority}
        self.reminders.append(reminder_item)
        self.save_reminders()
        print(f'已添加提醒事项：{reminder}, 分类：{category}, 优先级：{priority}')
        if delay is not None:
            time.sleep(delay)
            self.show_reminders(reminder)

    def show_reminders(self, reminder):
        print(f'提醒：{reminder}')

    def list_reminders(self):
        print('提醒事项：')
        for i, reminder in enumerate(self.reminders):
            status = '已完成' if reminder['completed'] else '未完成'
            print(f'{i + 1}. {reminder["text"]} ({reminder["category"]}, {reminder["color"]})'
                  f' ({status})，优先级：{reminder["priority"]}')

    def delete_reminder(self, index):
        try:
            removed = self.reminders.pop(index - 1)
            self.save_reminders()
            print(f'已删除提醒事项：{removed["text"]}')
        except IndexError:
            print('索引无效，请检查提醒事项列表。')

    def complete_reminder(self, index):
        try:
            self.reminders[index - 1]['completed'] = True
            self.save_reminders()
            print(f'已完成提醒事项：{self.reminders[index - 1]["text"]}')
        except IndexError:
            print('索引无效，请检查提醒事项列表。')

    def search_reminders(self, keyword):
        results = [r for r in self.reminders if keyword.lower() in r['text'].lower()]
        if results:
            print('搜索结果：')
            for reminder in results:
                status = '已完成' if reminder['completed'] else '未完成'
                print(f'{reminder["text"]} ({reminder["category"]}, {reminder["color"]})'
                      f' ({status})，优先级：{reminder["priority"]}')
        else:
            print('未找到与关键词匹配的提醒事项。')

if __name__ == '__main__':
    # 添加路径
    p = Path.cwd() / "reminder.pkl"

    # 测试阶段为了防止数据重复添加
    # 在每次启动时自动删除pickle文件
    p.unlink(missing_ok=True)

    # 创建对象 __init__
    reminder = Reminder('reminders.pkl')

    # 添加提醒 __call__
    print("添加提醒 >>>")
    reminder('添加', '买牛奶', '购物', '黄色', 1)
    reminder('添加', '发邮件', '工作', '蓝色', 2)
    reminder('添加', '学编程', '学编程', '红色', 1)
    reminder('添加', '打游戏', '娱乐', '紫色', 4)
    reminder('添加', '谈恋爱', '娱乐', '粉色', 1)
    reminder('添加', '打酱油', '购物', '黄色', 3)

    # 删除提醒
    print('\n删除提醒 >>>')
    reminder.delete_reminder(6)

    # 列举提醒
    print('\n列举提醒 >>>')
    reminder.list_reminders()

    # 完成提醒
    print('\n完成提醒 >>>')
    reminder.complete_reminder(5)

    # 搜索提醒
    print('\n搜索提醒 >>>')
    reminder.search_reminders('编程')
