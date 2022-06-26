from tkinter import *
from functools import partial
import tkinter.messagebox as msgbox
import time
import os

Id_list = []# Id 저장
class_list = []#Id 클래스 정보 저장
#두 개 리스트는 아이디의 특정 인덱스를 클래스 인덱스에 넣어주면 해당 클래스 주소가 나온다
title_list = []#글의 제목 저장
line_list = []#글의 클래스 정보 저장

class Account: #class_list
    def __init__(self,Id,Password,name,profile):
        self.Id = Id
        self.Password = Password
        self.name = name
        self.profile = profile


class Text_window: #line_list
    def __init__(self,title,text,time,reply,like,user_index):
        self.title = title#str
        self.text = text#str
        self.time = time#str
        self.reply = reply#list(쓴 사람의 index, text 내용)
        self.like = like#list(좋아요 누른 사람들의 index)
        self.user_index = user_index#int

def saving():
    f = open("Id_list.txt","w")#Id 리스트를 저장
    for i in range(len(Id_list)):
        f.write(Id_list[i]+"\n")
    f.close()

    f = open("class_list.txt","w")#class 리스트를 저장
    for i in range(len(class_list)):
        f.write(class_list[i].Id+"∮"+class_list[i].Password+"∮"+class_list[i].name+"∮"+class_list[i].profile+"∮")
    f.close()

    f = open("title_list.txt","w")#title 리스트를 저장
    for i in range(len(title_list)):
        f.write(title_list[i]+"\n")
    f.close()

    f = open("line_list.txt","w")#line list를 저장
    for i in range(len(line_list)):
        f.write(line_list[i].title+"∮")
        f.write(line_list[i].text+"∮")
        f.write(line_list[i].time+"∮")
        for j in range(len(line_list[i].reply)):
            f.write(str(line_list[i].reply[j][0])+"∃"+line_list[i].reply[j][1]+"∀")
        f.write("∮")
        for j in range(len(line_list[i].like)):
            f.write(str(line_list[i].like[j])+" ")
        f.write("∮")
        f.write(str(line_list[i].user_index)+"∮")
    f.close()
if(os.path.isfile("Id_list.txt")):
    f = open("Id_list.txt","r")#Id 리스트를 로드
    contents_Id = f.read().split("\n")
    if contents_Id[len(contents_Id)-1] =='':
        del(contents_Id[len(contents_Id)-1])
        for i in range(len(contents_Id)):
            Id_list.append(contents_Id[i])

    f = open("class_list.txt","r")#class 리스트를 로드
    contents_class = f.read().split("∮")
    if contents_class[len(contents_class)-1] =='':
        del(contents_class[len(contents_class)-1])
    length = int(len(contents_class)/4)
    class_list=[0 for i in range(length)]
    for i in range(length):
        class_list[i] = Account(contents_class[4*i],contents_class[4*i+1],contents_class[4*i+2],contents_class[4*i+3])

    f = open("title_list.txt","r")#title 리스틀를 로드
    contents_title = f.read().split("\n")
    if contents_title[len(contents_title)-1] =='':
        del(contents_title[len(contents_title)-1])
    for i in range(len(contents_title)):
        title_list.append(contents_title[i])

    f = open("line_list.txt","r")#line 리스트를 로드
    contents_line = f.read().split("∮")
    if contents_line[len(contents_line)-1] =='':
        del(contents_line[len(contents_line)-1])
    length = int(len(contents_line)/6)
    contents_line_reply = [0 for i in range(length)]
    contents_line_discriminate = [0 for i in range(length)]
    length_list = []

    for i in range(length):
        contents_line_reply=contents_line[6*i+3].split("∀")
        for j in range(len(contents_line_reply)):
            if contents_line_reply[len(contents_line_reply)-1] =='':
                del(contents_line_reply[len(contents_line_reply)-1])
        length_list.append(len(contents_line_reply))
    for i in range(len(length_list)):
        a = [[] for j in range(length_list[i])]
        contents_line_discriminate[i] = a
    for i in range(length):
        contents_line_reply=(contents_line[6*i+3].split("∀"))
        for j in range(len(contents_line_reply)):
            if contents_line_reply[len(contents_line_reply)-1] =='':
                del(contents_line_reply[len(contents_line_reply)-1])
        for k in range(len(contents_line_reply)):
            reply_id = int(contents_line_reply[k].split("∃")[0])
            reply_text = contents_line_reply[k].split("∃")[1]
            contents_line_discriminate[i][k] = contents_line_discriminate[i][k] + [reply_id,reply_text]

    list_like = [[] for i in range(length)]
    for i in range(length):
        contents_line_like = contents_line[6*i+4].split()
        contents_line_like = list(map(int,contents_line_like))
        list_like[i] = contents_line_like

    line_list = [0 for i in range(length)]
    for i in range(length):
        line_list[i] = Text_window(contents_line[6*i],contents_line[6*i+1],contents_line[6*i+2],contents_line_discriminate[i],list_like[i],int(contents_line[6*i+5]))
else:
    saving()

def main_title(index):
    main_screen = Tk()#메인 창
    main_screen.geometry("800x600")
    main_screen.title("SNS_Python  "+str(class_list[index].name))
    main_screen.option_add("*Font","맑은고딕15")

    def my_information():#내 정보를 확인하는 코드
        my_information_screen = Tk()
        my_information_screen.geometry("400x300")
        my_information_screen.title(str(class_list[index].Id)+"님의 정보")
        my_information_screen.option_add("*Font","맑은고딕20")

        label_my_Id=Label(my_information_screen,text = "아이디")
        label_my_Id.pack()
        label_my_Id.place(x=10,y=10)
        my_Id = Label(my_information_screen,text =class_list[index].Id,width=10)
        my_Id.pack()
        my_Id.place(x=130,y=10)

        label_my_name=Label(my_information_screen,text = "이름")
        label_my_name.pack()
        label_my_name.place(x=10,y=40)
        my_name = Label(my_information_screen,text =class_list[index].name, width=10)
        my_name.pack()
        my_name.place(x=130,y=40)

        label_my_profile=Label(my_information_screen,text = "프로필")
        label_my_profile.pack()
        label_my_profile.place(x=10,y=70)
        my_profile=Text(my_information_screen,width=35,height=5)
        my_profile.insert(1.0,class_list[index].profile)
        my_profile.pack()
        my_profile.place(x=10,y=100)

        def close_button():
            my_information_screen.destroy()

        btn_close = Button(my_information_screen, text="확인",command=close_button)
        btn_close.pack()
        btn_close.place(x=160,y=250)

    def edit_information():#내 정보를 수정하는 코드
        edit_information_screen = Tk()
        edit_information_screen.geometry("400x350")
        edit_information_screen.title(str(class_list[index].Id)+"님의 정보 수정")
        edit_information_screen.option_add("*Font","맑은고딕20")

        label_edit_name=Label(edit_information_screen,text = "이름")
        label_edit_name.pack()
        label_edit_name.place(x=10,y=10)
        edit_name = Entry(edit_information_screen,text =class_list[index].name, width=10)
        edit_name.pack()
        edit_name.place(x=120,y=10)
        edit_name.insert(0,class_list[index].name)

        label_edit_password=Label(edit_information_screen,text = "비밀번호")
        label_edit_password.pack()
        label_edit_password.place(x=10,y=40)
        edit_password = Entry(edit_information_screen,width=10)
        edit_password.pack()
        edit_password.place(x=120,y=40)

        label_edit_name=Label(edit_information_screen,text = "프로필")
        label_edit_name.pack()
        label_edit_name.place(x=10,y=70)
        edit_profile=Text(edit_information_screen,width=35,height=5)
        edit_profile.insert(1.0,class_list[index].profile)
        edit_profile.pack()
        edit_profile.place(x=10,y=100)

        label_confirm_password=Label(edit_information_screen,text ="현재 비밀번호")
        label_confirm_password.pack()
        label_confirm_password.place(x=10,y=270)
        confirm_password = Entry(edit_information_screen,width=10)
        confirm_password.pack()
        confirm_password.place(x=150,y=270)

        def close_button():
            edit_information_screen.destroy()
        def edit_button():
            if(confirm_password.get() != class_list[index].Password):
                msgbox.showwarning("실패!","현재 비밀번호가 틀립니다!")
            else:
                if(edit_name.get() == ""):
                    msgbox.showwarning("실패!","변경할 이름을 입력해주세요!")
                elif(edit_password.get() == ""):
                    msgbox.showwarning("실패!","변경할 비밀번호를 입력해주세요!")
                else:
                    if msgbox.askokcancel("확인","정말로 개인 정보를 변경하시겠습니까?"):
                        class_list[index].name = edit_name.get()
                        class_list[index].Password = edit_password.get()
                        class_list[index].profile = edit_profile.get("1.0",END)
                        saving()
                        msgbox.showinfo("성공!","변경 성공!!!")
                        edit_information_screen.destroy()
                        msgbox.showinfo("환영합니다!",str(class_list[index].name) +"님 어서오세요!")
                        main_screen.destroy()
                        main_title(index)

        btn_close = Button(edit_information_screen, text="취소", command = close_button)
        btn_close.pack()
        btn_close.place(x=190,y=300)

        btn_edit = Button(edit_information_screen, text="수정", command = edit_button)
        btn_edit.pack()
        btn_edit.place(x=120,y=300)

    def delete_account():#회원 탈퇴를 진행하는 코드
        delete_account_screen = Tk()
        delete_account_screen.geometry("630x130")
        delete_account_screen.title("회원 탈퇴")
        delete_account_screen.option_add("*Font","맑은고딕20")

        delete_label=Label(delete_account_screen,text = "회원 탈퇴를 원하시면 \'회원 탈퇴\'라고 적으시고 확인을 눌러주세요")
        delete_label.pack()
        delete_label.place(x=10,y=10)

        delete_confirm = Entry(delete_account_screen)
        delete_confirm.pack()
        delete_confirm.place(x=200,y=50)

        def delete_account_function():
            if (delete_confirm.get() == '회원 탈퇴'):
                if msgbox.askokcancel("회원 탈퇴","정말로 탈퇴하시겠습니까?"):
                        del Id_list[index]
                        del class_list[index]
                        for i in reversed(range(len(title_list))):
                            if(line_list[i].user_index == index):
                                del(line_list[i])
                                del(title_list[i])
                        for i in range(len(title_list)):
                            if(line_list[i].user_index >index):
                                line_list[i].user_index = line_list[i].user_index-1

                        for i in range(len(line_list)):
                            for j in reversed(range(len(line_list[i].reply))):
                                if (line_list[i].reply[j][0] == index):
                                    del(line_list[i].reply[j])
                        for i in range(len(line_list)):
                            for j in range(len(line_list[i].reply)):
                                if (line_list[i].reply[j][0] > index):
                                    line_list[i].reply[j][0] = line_list[i].reply[j][0]-1

                        for i in range(len(line_list)):
                            for j in reversed(range(len(line_list[i].like))):
                                if(line_list[i].like[j] == index):
                                    del(line_list[i].like[j])
                        for i in range(len(line_list)):
                            for j in range(len(line_list[i].like)):
                                if(line_list[i].like[j] > index):
                                    line_list[i].like[j] = line_list[i].like[j]-1
                        msgbox.showinfo("알림","탈퇴하셨습니다.")
                        saving()
                        delete_account_screen.destroy()
                        main_screen.destroy()
                        login_screen()

        btn_login = Button(delete_account_screen, text="탈퇴",command=delete_account_function)
        btn_login.pack()
        btn_login.place(x=280,y=80)

    def logout():#로그아웃 하는 코드
        main_screen.destroy()
        login_screen()

    def new_line():#새로운 글을 쓰는 코드

        def make_line():
            line_list_title = line_title.get()
            line_list_text = line_text.get("1.0",END)
            line_list_time = time.strftime('%m.%d.%p%I:%M',time.localtime(time.time()))
            if(line_list_title in title_list):
                line_list_title = line_list_title + '~'
            line = Text_window(line_list_title,line_list_text,line_list_time,[],[],index)
            title_list.append(line_list_title)
            line_list.append(line)
            msgbox.showinfo("작성 완료!","글을 작성하였습니다.")
            saving()
            line_screen.destroy()
            main_screen.destroy()
            main_title(index)


        line_screen = Tk()
        line_screen.geometry("600x400")
        line_screen.title("새로운 글")
        line_screen.option_add("*Font","맑은고딕15")

        line_title = Entry(line_screen,width=52)
        line_title.pack()
        line_title.place(x=10,y=5)

        line_text = Text(line_screen,width=52,height=14)
        line_text.pack()
        line_text.place(x=10,y=40)

        make_line_btn = Button(line_screen,text="작성",command=make_line)
        make_line_btn.pack()
        make_line_btn.place(x=270,y=340)

    #관리자 권한
    def observe():#회원 번호가 1일 때, 관리자 권한으로 모든 가입자의 정보를 볼 수 있는 코드
        observe_screen = Tk()
        observe_screen.geometry("430x500")
        observe_screen.title("회원 정보")
        observe_screen.option_add("*Font","맑은고딕20")

        observe_frame = Frame(observe_screen,width=36,height=24)
        observe_list = Text(observe_screen,width=36,height=23)
        for i in range(len(Id_list)):
            observe_list.insert(1.0,class_list[i].Id)
            observe_list.insert(1.0,"   ID:")
            observe_list.insert(1.0,class_list[i].name)
            observe_list.insert(1.0,"이름:")
            observe_list.insert(1.0,"\n")
        observe_list.pack()
        observe_list.place(x=10,y=10)

        scrollbar = Scrollbar(observe_frame)
        scrollbar.pack(side=RIGHT, fill=Y)
        scrollbar.config(command=observe_list.yview)
        observe_list.config(yscrollcommand=scrollbar.set)

        observe_frame.pack(side=RIGHT,fill=Y)

        for i in range(len(Id_list)):
            print(class_list[i].Id,class_list[i].Password,class_list[i].name,class_list[i].profile)
        saving()

    main_frame = Frame(main_screen,width=68,height=4)
    main_frame.pack()

    menu = Menu(main_screen)
    menu.option_add("*Font","맑은고딕10")

    menu_information = Menu(menu, tearoff=0)
    menu_information.add_command(label="내 정보 보기",command=my_information)
    menu_information.add_command(label="로그아웃",command=logout)

    menu_edit = Menu(menu, tearoff=0)
    menu_edit.add_command(label="내 정보 수정",command=edit_information)
    menu_edit.add_command(label="회원 탈퇴", command=delete_account)

    menu_line = Menu(menu,tearoff=0)
    menu_line.add_command(label="글 쓰기",command=new_line)

    menu.add_cascade(label="내 정보",menu=menu_information)
    menu.add_cascade(label="정보 수정",menu=menu_edit)
    menu.add_cascade(label="글",menu=menu_line)

    main_frame_left = Text(main_frame,width=69,height=30)

    if(index==0):#observe를 확인할 수 있는 유저의 index가 0인지 확인
        menu_observe = Menu(menu, tearoff=0)
        menu_observe.add_command(label="모든 회원 정보",command=observe)
        menu.add_cascade(label="관리자 권한",menu = menu_observe)

    def Id_info(index):
        Id_info_screen = Tk()
        Id_info_screen.geometry("400x290")
        Id_info_screen.title("작성자 정보")
        Id_info_screen.option_add("*Font","맑은고딕20")

        Id_info_screen_Id=Label(Id_info_screen,text = "아이디")
        Id_info_screen_Id.pack()
        Id_info_screen_Id.place(x=10,y=10)
        info_screen_Id = Label(Id_info_screen,text =class_list[index].Id,width=10)
        info_screen_Id.pack()
        info_screen_Id.place(x=130,y=10)

        info_screen_Id_name=Label(Id_info_screen,text = "이름")
        info_screen_Id_name.pack()
        info_screen_Id_name.place(x=10,y=40)
        info_screen_name = Label(Id_info_screen,text =class_list[index].name, width=10)
        info_screen_name.pack()
        info_screen_name.place(x=130,y=40)

        info_screen_Id_profile=Label(Id_info_screen,text = "프로필")
        info_screen_Id_profile.pack()
        info_screen_Id_profile.place(x=10,y=70)
        info_screen_profile=Text(Id_info_screen,width=35,height=5)
        info_screen_profile.insert(1.0,class_list[index].profile)
        info_screen_profile.pack()
        info_screen_profile.place(x=10,y=100)

        def close_button():
            Id_info_screen.destroy()

        btn_close = Button(Id_info_screen, text="확인",command=close_button)
        btn_close.pack()
        btn_close.place(x=160,y=250)

    def line_text_function(user_index,line_index):#유저가 쓴 글에서 실행하는 코드
        line_text_screen = Tk()
        line_text_screen.geometry("600x1050")
        line_text_screen.title("새로운 글")
        line_text_screen.option_add("*Font","맑은고딕15")

        line_Id = Label(line_text_screen,width=52,text= str(line_list[title_list.index(title_list[line_index])].time)+"에 쓰여진 "+class_list[user_index].Id+"님의 글")
        line_Id.grid(row=0,column=0)

        line_space = Label(line_text_screen)
        line_space.grid(row=1,column=0)

        line_title = Label(line_text_screen,width=52,text = title_list[line_index])
        line_title.grid(row=2,column=0)

        line_text = Text(line_text_screen,width=52,height=14)
        line_text.insert(1.0,str(line_list[title_list.index(title_list[line_index])].text))
        line_text.grid(row=3,column=0)

        def like(line_index_sub):#좋아요 관련 코드
            if index in line_list[line_index_sub].like:
                msgbox.showwarning("실패!","이미 좋아요를 누른 게시물입니다!")
                line_text_screen.focus_force()
            else:
                line_list[line_index].like.append(index)
                msgbox.showinfo("좋아요","좋아요!")
                saving()
                line_text_screen.destroy()
                line_text_function(user_index,line_index)

        def line_reply_input_function():#댓글과 관련된 코드

            def close_function():
                line_text_screen.destroy()

            def edit_line_text(line_index):
                if(msgbox.askokcancel("확인","정말로 수정하시겠습니까?")):
                    edit_line_text_screen = Tk()
                    edit_line_text_screen.geometry("600x400")
                    edit_line_text_screen.title("글 수정")
                    edit_line_text_screen.option_add("*Font","맑은고딕15")

                    edit_line_title = Entry(edit_line_text_screen,width=52)
                    edit_line_title.pack()
                    edit_line_title.place(x=10,y=5)
                    edit_line_title.insert(0,title_list[line_index])

                    edit_line_text = Text(edit_line_text_screen,width=52,height=14)
                    edit_line_text.pack()
                    edit_line_text.place(x=10,y=40)
                    edit_line_text.insert(1.0,line_list[line_index].text)

                    def edit_confirm():
                        edit_title = edit_line_title.get()
                        edit_text = edit_line_text.get(1.0,END)
                        title_list[line_index] = edit_title
                        line_list[line_index].title = edit_title
                        line_list[line_index].text = edit_text
                        msgbox.showinfo("성공!","수정 완료!")
                        saving()
                        edit_line_text_screen.destroy()
                        line_text_screen.destroy()
                        main_screen.destroy()
                        main_title(index)

                    edit_make_line_btn = Button(edit_line_text_screen,text="수정",command=edit_confirm)
                    edit_make_line_btn.pack()
                    edit_make_line_btn.place(x=210,y=340)

                    def delete_line_text(line_index):
                        if(msgbox.askokcancel("확인","정말로 삭제하시겠습니까?")):
                            msgbox.showinfo("성공","삭제 완료!")
                            line_text_screen.destroy()
                            del title_list[line_index]
                            del line_list[line_index]
                            saving()
                            main_screen.destroy()
                            main_screen.destory()
                            main_title(index)

                    edit_delete_line_btn = Button(edit_line_text_screen,text="글 삭제",command=partial(delete_line_text,title_list.index(title_list[line_index])))
                    edit_delete_line_btn.pack()
                    edit_delete_line_btn.place(x=280,y=340)

            text = line_reply_input.get("1.0",END)
            line_list[title_list.index(title_list[line_index])].reply = line_list[title_list.index(title_list[line_index])].reply + [[index,text]]

            for i in range(len(line_list[title_list.index(title_list[line_index])].reply)):
                line_reply_id = class_list[line_list[title_list.index(title_list[line_index])].reply[i][0]].Id
                line_reply_text = line_list[title_list.index(title_list[line_index])].reply[i][1]

                line_reply_id_label = Label(line_text_screen,text=line_reply_id+"님의 댓글",width=20)
                line_reply_id_label.grid(row=2*i+8,column=0)

                line_reply_text_text = Text(line_text_screen,width=42,height=4)
                line_reply_text_text.insert(1.0,line_reply_text)
                line_reply_text_text.grid(row=2*i+9,column=0)

                if( i == (len(line_list[title_list.index(title_list[line_index])].reply)) - 1):
                    if(user_index == index):
                        line_reply_edit_button = Button(line_text_screen,padx=3,pady=1,text="수정",command=partial(edit_line_text,title_list.index(title_list[line_index])))
                        line_reply_edit_button.grid(row=2*len(line_list[title_list.index(title_list[line_index])].reply)+9,column=0)
                    else:
                        line_reply_cancel_button = Button(line_text_screen,padx=3,pady=1,text="취소",command=close_function)
                        line_reply_cancel_button.grid(row=2*len(line_list[title_list.index(title_list[line_index])].reply)+9,column=0)


        line_like_button = Button(line_text_screen,padx=1,pady=1,text="♡"+str(len(line_list[title_list.index(title_list[line_index])].like)),command=partial(like,title_list.index(title_list[line_index])))
        line_like_button.grid(row=4,column=0)

        line_reply_Label = Label(line_text_screen,text="댓글 입력")
        line_reply_Label.grid(row=5,column=0)

        line_reply_input = Text(line_text_screen,width=42,height=4)
        line_reply_input.grid(row=6,column=0)

        line_reply_input_button = Button(line_text_screen,padx=3,pady=1,text="입력",command=line_reply_input_function)
        line_reply_input_button.grid(row=7,column=0)

        for i in range(len(line_list[title_list.index(title_list[line_index])].reply)):
            line_reply_id = class_list[line_list[title_list.index(title_list[line_index])].reply[i][0]].Id
            line_reply_text = line_list[title_list.index(title_list[line_index])].reply[i][1]

            line_reply_id_label = Label(line_text_screen,text=line_reply_id+"님의 댓글",width=20)
            line_reply_id_label.grid(row=2*i+8,column=0)

            line_reply_text_text = Text(line_text_screen,width=42,height=4)
            line_reply_text_text.insert(1.0,line_reply_text)
            line_reply_text_text.grid(row=2*i+9,column=0)

        def close_function():
            line_text_screen.destroy()

        if(user_index == index):
            def edit_line_text(line_index):
                if(msgbox.askokcancel("확인","정말로 수정하시겠습니까?")):
                    edit_line_text_screen = Tk()
                    edit_line_text_screen.geometry("600x400")
                    edit_line_text_screen.title("글 수정")
                    edit_line_text_screen.option_add("*Font","맑은고딕15")

                    edit_line_title = Entry(edit_line_text_screen,width=52)
                    edit_line_title.pack()
                    edit_line_title.place(x=10,y=5)
                    edit_line_title.insert(0,title_list[line_index])

                    edit_line_text = Text(edit_line_text_screen,width=52,height=14)
                    edit_line_text.pack()
                    edit_line_text.place(x=10,y=40)
                    edit_line_text.insert(1.0,line_list[line_index].text)

                    def edit_confirm():
                        edit_title = edit_line_title.get()
                        edit_text = edit_line_text.get(1.0,END)
                        title_list[line_index] = edit_title
                        line_list[line_index].title = edit_title
                        line_list[line_index].text = edit_text
                        msgbox.showinfo("성공!","수정 완료!")
                        saving()
                        edit_line_text_screen.destroy()
                        line_text_screen.destroy()
                        main_screen.destroy()
                        main_title(index)

                    edit_make_line_btn = Button(edit_line_text_screen,text="수정",command=edit_confirm)
                    edit_make_line_btn.pack()
                    edit_make_line_btn.place(x=210,y=340)

                    def delete_line_text(line_index):
                        if(msgbox.askokcancel("확인","정말로 삭제하시겠습니까?")):
                            msgbox.showinfo("성공","삭제 완료!")
                            line_text_screen.destroy()
                            del title_list[line_index]
                            del line_list[line_index]
                            saving()
                            main_screen.destroy()
                            main_title(index)

                    edit_delete_line_btn = Button(edit_line_text_screen,text="글 삭제",command=partial(delete_line_text,title_list.index(title_list[line_index])))
                    edit_delete_line_btn.pack()
                    edit_delete_line_btn.place(x=280,y=340)

            line_reply_edit_button = Button(line_text_screen,padx=3,pady=1,text="수정",command=partial(edit_line_text,title_list.index(title_list[line_index])))
            line_reply_edit_button.grid(row=2*len(line_list[title_list.index(title_list[line_index])].reply)+9,column=0)
        else:
            line_reply_cancel_button = Button(line_text_screen,padx=3,pady=1,text="취소",command=close_function)
            line_reply_cancel_button.grid(row=2*len(line_list[title_list.index(title_list[line_index])].reply)+9,column=0)

    line_number=0
    for i in range(len(title_list)-1,-1,-1):
        main_list_Id = Button(main_frame_left,width=9,height=1,text=str(class_list[line_list[i].user_index].Id),command=partial(Id_info,line_list[i].user_index))
        main_list_title =Button(main_frame_left,width=43,height=1,text=title_list[i]+"("+str(len((line_list[i].reply)))+","+"♡:"+str(len(line_list[i].like))+")",command=partial(line_text_function,line_list[i].user_index,i))
        main_list_info =Label(main_frame_left,width=12,height=1,text=str(line_list[i].time))
        main_list_Id.pack()
        main_list_title.pack()
        main_list_info.pack()
        main_list_Id.place(y=line_number*40,x=0)
        main_list_title.place(y=line_number*40,x=120)
        main_list_info.place(y=line_number*40,x=610)
        line_number = line_number+1

    main_frame_left.pack(side="left",fill="y")
    main_screen.config(menu=menu)
    main_screen.mainloop()

def login_screen():
    win = Tk()
    win.geometry("300x250")
    win.title("Login")
    win.option_add("*Font","맑은고딕25")

    label_ID = Label(win,text = "아이디를 입력하세요")
    label_ID.pack()

    Id = Entry(win,width=20)
    Id.pack()

    label_Password = Label(win,text = "비밀번호를 입력하세요")
    label_Password.pack()

    Password = Entry(win,width=20)
    Password.pack()

    def login_button():
        Id_check = Id.get()
        Password_check = Password.get()
        if (Id_check not in Id_list):
            msgbox.showwarning("알림","아이디가 존재하지 않습니다!")
        elif (class_list[Id_list.index(Id_check)].Password != Password.get()):
            msgbox.showwarning("알림","비밀번호가 맞지 않습니다!")
        else:
            msgbox.showinfo("환영합니다!",str(class_list[Id_list.index(Id_check)].name) +"님 어서오세요!")
            win.destroy()
            main_title(Id_list.index(Id_check))
            win.destroy()

    def make_account_def():#회원가입과 관련된 코드
        def make_account_check():
            new_Id = make_Id.get()
            new_password = make_password.get()
            new_name = make_name.get()
            new_profile = make_profile.get("1.0",END)
            if(new_Id == ""):
                msgbox.showwarning("실패!","아이디를 입력해주세요!")
            elif(new_password == ""):
                msgbox.showwarning("실패!","비밀번호를 입력해주세요!")
            elif(new_name == ""):
                msgbox.showwarning("실패!","이름을 입력해주세요!")
            else:
                if new_Id in Id_list:
                    msgbox.showwarning("알림","중복된 아이디입니다.")
                    return
                else:
                    Id_list.append(make_Id.get())
                    i = Id_list.index(new_Id)
                    class_list.append(0)
                    class_list[i] = Account(new_Id,new_password,new_name,new_profile)
                    saving()
                    msgbox.showinfo("회원가입 성공!","회원가입에 성공하였습니다.")
                    make_account.destroy()
                    return
            make_account.focus_force()

        make_account = Tk()
        make_account.geometry("600x320")
        make_account.title("회원가입")
        make_account.option_add("*Font","맑은고딕25")

        label_make_Id=Label(make_account,text = "아이디")
        label_make_Id.pack()
        label_make_Id.place(x=10,y=10)
        make_Id = Entry(make_account,width=15)
        make_Id.pack()
        make_Id.place(x=150,y=10)

        label_make_password=Label(make_account,text = "비밀번호")
        label_make_password.pack()
        label_make_password.place(x=10,y=40)
        make_password = Entry(make_account,width=15)
        make_password.pack()
        make_password.place(x=150,y=40)

        label_make_name=Label(make_account,text = "이름")
        label_make_name.pack()
        label_make_name.place(x=10,y=70)
        make_name = Entry(make_account,width=15)
        make_name.pack()
        make_name.place(x=150,y=70)

        label_make_profile=Label(make_account,text = "자기 소개")
        label_make_profile.pack()
        label_make_profile.place(x=10,y=100)
        make_profile = Text(make_account,width=35,height=5)
        make_profile.pack()
        make_profile.place(x=150,y=100)

        btn_account=Button(make_account,text="완료",command=make_account_check)
        btn_account.pack()
        btn_account.place(x=250,y=280)

    btn_login = Button(win, text="로그인",command=login_button)
    btn_login.pack()

    btn_login = Button(win, text="회원가입",command=make_account_def)
    btn_login.pack()

    login_status = Label(win,width=20)
    login_status.pack()
    win.mainloop()

login_screen()
