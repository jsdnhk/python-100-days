"""
另一種創建類的方式

Version: 0.1
Author: 駱昊
Date: 2018-03-08
"""


def bar(self, name):
    self._name = name


def foo(self, course_name):
    print('%s正在學習%s.' % (self._name, course_name))


def main():
    Student = type('Student', (object,), dict(__init__=bar, study=foo))
    stu1 = Student('駱昊')
    stu1.study('Python程序設計')


if __name__ == '__main__':
    main()  
