all_student = []
def menu():
    print('1,添加学生信息')
    print('2,删除学习信息')
    print('3,修改学生信息')
    print('4,显示所有学生信息')
    print('0,退出系统')
def add_info():
    new_name = input('新学生名字:')
    new_sex = input('新学生性别:')
    new_phone = input('新学生手机:')
    new_student = {}
    new_student['name'] = new_name
    new_student['sex'] = new_sex
    new_student['phone'] = new_phone
    all_student.append(new_student)
def del_info(student):
    def_number = int(input('请输入要删除的序号:'))
    del student[def_number]
def change_info():
    student_id = int(input('要修改的学生的序号:'))
    new_name = input('新名字:')
    new_sex = input('新性别:')
    new_phone = input('新电话:')
    all_student[student_id-1]['name'] = new_name
    all_student[student_id-1]['sex'] = new_sex
    all_student[student_id-1]['phone'] = new_phone
def show_info():
    print('学生信息如下:')
    print('序号  姓名  性别  手机号')
    i = 1
    for temp in all_student:
        print(('{},{},{},{}').format(i,temp['name'],temp['sex'],temp['phone']))
        i += 1
def main():
    while True:
        menu()
        key = input('请输入对应的序号:')
        if key == '1':
            add_info()
        elif key == '2':
            del_info()
        elif key == '3':
            change_info()
        elif key == '4':
            show_info()
        elif key == '0':
            print('退出系统')
            break
        else:
            print('输入有误，重新输入')

main()
