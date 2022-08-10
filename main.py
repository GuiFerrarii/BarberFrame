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

#frame0
fr0_img_1 = PhotoImage(file="imagens\\barber.png")



fr0_lab = Label(fr0, image=fr0_img_1,width=480).grid(row=0,column=0,sticky=W)


fr0_bt0 = Button(fr0,  text="Usuário",command=lambda: [fr0.grid_remove(),fr2.grid(),root.geometry("490x560+610+153"),root.title("User Barber")],bg='#1d1f21',font='arimo',highlightcolor='#1d1f21',
                    highlightbackground='#1d1f21',highlightthickness=0,bd='0',activebackground='#1d1f21',fg='#F6F9F8').place(width=118,height=14, x=183, y=419)


fr0_bt1 = Button(fr0,  text="Barbearia",command=lambda: [fr0.grid_remove(),fr3.grid(),root.geometry("490x560+610+153"),root.title("Janela Barber")],bg='#1d1f21',font='arimo',highlightcolor='#1d1f21',
                    highlightbackground='#1d1f21',highlightthickness=0,bd='0',activebackground='#1d1f21',fg='#F6F9F8').place(width=118,height=14, x=183, y=487)


#frame2
fr2_img_1 = PhotoImage(file="imagens\\cadast.png")
fr2_lab = Label(fr2,image=fr2_img_1,width=480).grid(row=0,column=0,sticky=W)
fr2_bt0 = Button(fr2,  text="Cadastrar",command=lambda: [fr2.grid_remove(),fr4.grid(),root.geometry("490x560+610+153"),root.title("Tela Agenda")],bg='#1d1f21',font='arimo',highlightcolor='#1d1f21',
                    highlightbackground='#1d1f21',highlightthickness=0,bd='0',activebackground='#1d1f21',fg='#F6F9F8').place(width=118,height=14, x=65, y=424)

#frame3
fr3_img_1 = PhotoImage(file="imagens\\cdsbarb.png")
fr3_lab = Label(fr3,image=fr3_img_1,width=480).grid(row=0,column=0,sticky=W)


fr0.grid()
root.mainloop()
