from cProfile import label
from tkinter import *

root = Tk()
root.title("Barber Shop")
root.geometry("490x560+610+153")
root.resizable(height=False, width=False)

fr0 = Frame()
fr1 = Frame()
fr2 = Frame()
fr3 = Frame()
fr4 = Frame()
fr5 = Frame()
fr6 = Frame()
fr7 = Frame()


#caps primeira letra cad user
var1=StringVar()
def caps(*args):
    var1.set(var1.get().title())
var1.trace("w", caps)

#caps primeira letra cad BArbeiro
var2=StringVar()
def caps(*args):
    var2.set(var2.get().title())
var2.trace("w", caps)

#Nome user não inserir numero
def nome(event=None):
    x=fr2_in0.get()
    y=''
    if event.keysym.lower() == "backspace": return
    for i in range(len(x)):
        if x[i] not in '0123456789':
            y+=x[i]
    fr2_in0.delete(0, 'end')
    fr2_in0.insert(0, y)

#Nome barbeiro não inserir numero
def nome1(event=None):
    x=fr3_in0.get()
    y=''
    if event.keysym.lower() == "backspace": return
    for i in range(len(x)):
        if x[i] not in '0123456789':
            y+=x[i]
    fr3_in0.delete(0, 'end')
    fr3_in0.insert(0, y)



fr0_img_1 = PhotoImage(file="imagens\\barber.png")



fr0_lab = Label(fr0, image=fr0_img_1,width=480).grid(row=0,column=0,sticky=W)


fr0_bt0 = Button(fr0,  text="Usuário",command=lambda: [fr0.grid_remove(),fr2.grid(),root.geometry("490x560+610+153"),root.title("User Barber")],bg='#1d1f21',font='arimo',highlightcolor='#1d1f21',
                    highlightbackground='#1d1f21',highlightthickness=0,bd='0',activebackground='#1d1f21',fg='#F6F9F8').place(width=118,height=14, x=183, y=419)


fr0_bt1 = Button(fr0,  text="Cadastro Barbeiro",command=lambda: [fr0.grid_remove(),fr3.grid(),root.geometry("490x560+610+153"),root.title("Janela Barberia")],bg='#1d1f21',font='arimo',highlightcolor='#1d1f21',
                    highlightbackground='#1d1f21',highlightthickness=0,bd='0',activebackground='#1d1f21',fg='#F6F9F8').place(width=150,height=14, x=172, y=487)



#frame2
fr2_img_1 = PhotoImage(file="imagens\\cadast.png")
fr2_lab = Label(fr2,image=fr2_img_1,width=480).grid(row=0,column=0,sticky=W)
fr2_bt0 = Button(fr2,  text="Cadastrar",command=lambda: [fr2.grid_remove(),fr4.grid(),root.geometry("490x560+610+153"),root.title("Tela Serviços")],bg='#1d1f21',font='arimo',highlightcolor='#1d1f21',
                    highlightbackground='#1d1f21',highlightthickness=0,bd='0',activebackground='#1d1f21',fg='#F6F9F8').place(width=118,height=14, x=65, y=424)

fr2_bt1 = Button(fr2,  text="Entrar",command=lambda: [fr2.grid_remove(),fr4.grid(),root.geometry("490x560+610+153"),root.title("Tela Serviços")],bg='#1d1f21',font='arimo',highlightcolor='#1d1f21',
                    highlightbackground='#1d1f21',highlightthickness=0,bd='0',activebackground='#1d1f21',fg='#F6F9F8').place(width=118,height=14, x=299, y=424)

fr2_in0 = Entry(fr2, bd=0,bg='#1D1F21',fg='white',textvariable=var1, font=("Calibri", 15), justify=CENTER)
fr2_in0.place(width=230, height=39, x=130, y=125)
fr2_in0.bind('<KeyRelease>', nome)

fr2_in1 = Entry(fr2, bd=0,bg='#1D1F21',fg='white', font=("Calibri", 15), justify=CENTER)
fr2_in1.place(width=230, height=39, x=130, y=203)


#frame3
fr3_img_1 = PhotoImage(file="imagens\\cdsbarb.png")
fr3_lab = Label(fr3,image=fr3_img_1,width=480).grid(row=0,column=0,sticky=W)
fr3_bt0 = Button(fr3,  text="Cadastrar",command=lambda: [fr3.grid_remove(),fr6.grid(),root.geometry("490x560+610+153"),root.title("Tela Final")],bg='#1d1f21',font='arimo',highlightcolor='#1d1f21',
                    highlightbackground='#1d1f21',highlightthickness=0,bd='0',activebackground='#1d1f21',fg='#F6F9F8').place(width=118,height=14, x=65, y=424)

fr3_bt1 = Button(fr3,  text="Entrar",command=lambda: [fr3.grid_remove(),fr6.grid(),root.geometry("490x560+610+153"),root.title("Tela Final")],bg='#1d1f21',font='arimo',highlightcolor='#1d1f21',
                    highlightbackground='#1d1f21',highlightthickness=0,bd='0',activebackground='#1d1f21',fg='#F6F9F8').place(width=118,height=14, x=299, y=424)

fr3_in0 = Entry(fr3, bd=0,bg='#1D1F21',textvariable=var2,fg='white', font=("Calibri", 15), justify=CENTER)
fr3_in0.place(width=230, height=39, x=130, y=125)
fr3_in0.bind('<KeyRelease>', nome1)




#frame4
fr4_img = PhotoImage(file="imagens\\serviço.png")
fr4_lab = Label(fr4, image=fr4_img,width=480).grid(row=0,column=0,sticky=W)

#buttons serviço

fr4_bt = Button(fr4, text="corte na tesoura", command=lambda: [fr4.grid_remove(),fr5.grid(),root.geometry("490x560+610+153"),root.title("Agendamento")]
                ,bg='#1d1f21',font='arimo 8',highlightcolor='#1d1f21', highlightbackground='#1d1f21',highlightthickness=0,bd='0',activebackground='#1d1f21',fg='#F6F9F8').place(width=111,height=15, x=8, y=435)

fr4_bt1 = Button(fr4, text="pezinho", command=lambda: [fr4.grid_remove(),fr5.grid(),root.geometry("490x560+610+153"),root.title("Agendamento")]
                ,bg='#1d1f21',font='arimo 8',highlightcolor='#1d1f21', highlightbackground='#1d1f21',highlightthickness=0,bd='0',activebackground='#1d1f21',fg='#F6F9F8').place(width=111,height=15, x=130, y=435)

fr4_bt2 = Button(fr4, text="corte moderno", command=lambda: [fr4.grid_remove(),fr5.grid(),root.geometry("490x560+610+153"),root.title("Agendamento")]
                ,bg='#1d1f21',font='arimo 8',highlightcolor='#1d1f21', highlightbackground='#1d1f21',highlightthickness=0,bd='0',activebackground='#1d1f21',fg='#F6F9F8').place(width=111,height=15, x=240, y=435)

fr4_bt3 = Button(fr4, text="lavagem", command=lambda: [fr4.grid_remove(),fr5.grid(),root.geometry("490x560+610+153"),root.title("Agendamento")]
                ,bg='#1d1f21',font='arimo 8',highlightcolor='#1d1f21', highlightbackground='#1d1f21',highlightthickness=0,bd='0',activebackground='#1d1f21',fg='#F6F9F8').place(width=111,height=15, x=355, y=435)

fr4_bt4 = Button(fr4, text="barba", command=lambda: [fr4.grid_remove(),fr5.grid(),root.geometry("490x560+610+153"),root.title("Agendamento")]
                ,bg='#1d1f21',font='arimo 8',highlightcolor='#1d1f21', highlightbackground='#1d1f21',highlightthickness=0,bd='0',activebackground='#1d1f21',fg='#F6F9F8').place(width=111,height=15, x=185, y=540)


#frame5 tela agenda

fr5_image = PhotoImage(file="imagens\\agenda.png")
fr5_lab = Label(fr5,image=fr5_image,width=480).grid(row=0,column=0,sticky=W)

#buttons agenda

fr5_bt_1 = Button(fr5, text="9:00 am", command=lambda: [fr5.grid_remove(),fr7.grid(),root.geometry("490x560+610+153"),root.title("Tela Final")]
                ,bg='#FFFFFF',font='arimo 15',highlightcolor='#FFFFFF', highlightbackground='#FFFFFF',highlightthickness=0,bd='0',activebackground='#ffffff',fg='#1D1F21').place(width=111,height=15, x=33, y=293)

r5_bt_2 = Button(fr5, text="10:00 am", command=lambda: [fr5.grid_remove(),fr7.grid(),root.geometry("490x560+610+153"),root.title("Tela Final")]
                ,bg='#FFFFFF',font='arimo 15',highlightcolor='#FFFFFF', highlightbackground='#FFFFFF',highlightthickness=0,bd='0',activebackground='#ffffff',fg='#1D1F21').place(width=111,height=15, x=173, y=293)

r5_bt_3 = Button(fr5, text="11:00 am", command=lambda: [fr5.grid_remove(),fr7.grid(),root.geometry("490x560+610+153"),root.title("Tela Final")]
                ,bg='#FFFFFF',font='arimo 15',highlightcolor='#FFFFFF', highlightbackground='#FFFFFF',highlightthickness=0,bd='0',activebackground='#ffffff',fg='#1D1F21').place(width=111,height=15, x=320, y=293)

r5_bt_4 = Button(fr5, text="13:00 am", command=lambda: [fr5.grid_remove(),fr7.grid(),root.geometry("490x560+610+153"),root.title("Tela Final")]
                ,bg='#FFFFFF',font='arimo 15',highlightcolor='#FFFFFF', highlightbackground='#FFFFFF',highlightthickness=0,bd='0',activebackground='#ffffff',fg='#1D1F21').place(width=111,height=15, x=33, y=385)

r5_bt_5 = Button(fr5, text="14:00 am", command=lambda: [fr5.grid_remove(),fr7.grid(),root.geometry("490x560+610+153"),root.title("Tela Final")]
                ,bg='#FFFFFF',font='arimo 15',highlightcolor='#FFFFFF', highlightbackground='#FFFFFF',highlightthickness=0,bd='0',activebackground='#ffffff',fg='#1D1F21').place(width=111,height=15, x=173, y=385)

#cadastrado

fr6_img = PhotoImage(file="imagens\\cdsfuncionario.png")
fr6_lab = Label(fr6, image=fr6_img,width=480).grid(row=0,column=0,sticky=W)

#fr7
fr7_img = PhotoImage(file="imagens\\hora_marc.png")
fr7_lab = Label(fr7, image=fr7_img,width=480).grid(row=0,column=0,sticky=W)

fr0.grid()
root.mainloop()
