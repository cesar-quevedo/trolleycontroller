from tkinter import *
import customtkinter  # python UI-library based on Tkinter.
# To install do: pip3 install customtkinter. To update do: pip3 install customtkinter --upgrade
from PIL import Image, ImageTk
import time
import serial  # This allows python to connect to serial. NAME: pyserial
# To install do: pip install pyserial
from tkinter import messagebox

customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("blue")


class Ap(customtkinter.CTk):

    def __init__(self):
        super().__init__()
        self.title("")
        self.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        # self.attributes('-fullscreen', True) # This command is to make the screen full-screen
        self.iconbitmap('C:\\Users\\quevedo\\PycharmProjects\\Trolleytrolley\\images\\hp.ico')  # Almost every device
        # will have a different file PATH so change if needed
        self.state('zoomed')  # This command maximizes the screen

        """
        Mostly evey device would have a different screen resolution(eg. 1920x1080) so every frame, label, widget, etc 
        width and height 
        would most likely need to be change in order to make this GUI fit on the screen
        """

        """ one frame """
        self.one_frame = customtkinter.CTkFrame(master=self, corner_radius=0)
        self.one_frame.place(relx=.5, rely=.5, anchor="center", width=2000, height=960)
        self.one_frame.configure(fg_color="white")
        """ two frame """
        self.two_frame = customtkinter.CTkFrame(master=self.one_frame, corner_radius=0)
        self.two_frame.place(relx=.5, rely=0, anchor="center", width=2000, height=150)
        self.two_frame.configure(fg_color="white")
        """ label """
        self.twv = customtkinter.CTkLabel(master=self.one_frame, text_font=("rono", 30, "bold"), bg_color='white',
                                          text="TWV Trolley Controller", text_color='black')
        self.twv.place(relx=.5, rely=0.04, anchor=CENTER)
        """ three frame """
        self.three_frame = customtkinter.CTkFrame(master=self.one_frame, corner_radius=0)
        self.three_frame.place(relx=.5, rely=.27, anchor="center", width=2000, height=370)
        self.three_frame.configure(fg_color="white")

        """ This code is for the connect button """
        def connect_pressed():
            ser = serial.Serial()
            ser.port = 'COM1'  # This serial port has to be changed to the device serial port
            # (eg. /dev/ttyS0,/dev/tty1(for linux)...COM2, COM3(for windows)
            ser.baudrate = 9600                 # Change this settings if needed
            ser.bytesize = serial.EIGHTBITS
            ser.parity = serial.PARITY_NONE
            ser.xonxoff = 1
            ser.rtscts = 0
            ser.dsrdtr = 0
            ser.stopbits = 1
            ser.timeout = 1
            ser.open()
            if ser.isOpen():
                while True:
                    time.sleep(1)
                    ser.write(str.encode('root\n'))  # Trolley controller username(host name)
                    time.sleep(1)
                    ser.write(str.encode('socorro!\n'))  # Trolley controller password
                    time.sleep(2)
                    ser.write(str.encode('tl\n'))  # Command that connects and controls trolleys
                    out = ser.readline().decode('utf-8', 'ignore').strip()  # There's a lot of print because it allows
                    # to read data faster and makes everything run better
                    print(str(out))
                    out = ser.readline().decode('utf-8', 'ignore').strip()
                    print(str(out))
                    out = ser.readline().decode('utf-8', 'ignore').strip()
                    print(str(out))
                    out = ser.readline().decode('utf-8', 'ignore').strip()
                    print(str(out))
                    out = ser.readline().decode('utf-8', 'ignore').strip()
                    print(str(out))
                    # self.controllerbutton.configure(state=customtkinter.NORMAL) # 
                    if 'Login incorrect' in out:
                        messagebox.showerror("", "Please Try Again")
                        formattercheckbox = customtkinter.CTkCheckBox(master=self.four_frame, text="", height=130,
                                                                      width=130)
                        formattercheckbox.place(relx=.055, rely=.4)
                        formattercheckbox.select()
                        formattercheckbox.configure(border_color='black', highlightcolor='red', fg_color='red',
                                                    hover_color='white',
                                                    state=customtkinter.DISABLED)
                        tclcheckbox = customtkinter.CTkCheckBox(master=self.four_frame, text="", height=130, width=130)
                        tclcheckbox.place(relx=.45, rely=.4)
                        tclcheckbox.select()
                        tclcheckbox.configure(border_color='black', highlightcolor='red', fg_color='red',
                                              hover_color='white',
                                              state=customtkinter.DISABLED)
                        trolleycheckbox = customtkinter.CTkCheckBox(master=self.four_frame, text=".",
                                                                    text_color="white",
                                                                    height=130, width=130)
                        trolleycheckbox.place(relx=.861, rely=.4)
                        trolleycheckbox.select()
                        trolleycheckbox.configure(border_color='black', highlightcolor='red', fg_color='red',
                                                  hover_color='white',
                                                  state=customtkinter.DISABLED)
                        break
                    time.sleep(1)
                    ser.write(str.encode('Zeus start GpioArm2\n'))
                    ser.write(str.encode('GpioArm2 setLevel FUSION2_CAN_A_12V_CTRL 1\n'))
                    ser.write(str.encode('GpioArm2 setLevel FUSION2_CAN_B_12V_CTRL 1\n'))
                    ser.write(str.encode('Zeus start TrolleyPlatforms\n'))
                    time.sleep(1.5)
                    ser.write(str.encode('Trolley connect\n'))
                    time.sleep(.1)
                    # self.connectbutton.configure(state=customtkinter.DISABLED)
                    out = ser.readline().decode('utf-8', 'ignore').strip()
                    print(str(out))
                    out = ser.readline().decode('utf-8', 'ignore').strip()
                    print(str(out))
                    out = ser.readline().decode('utf-8', 'ignore').strip()
                    print(str(out))
                    out = ser.readline().decode('utf-8', 'ignore').strip()
                    print(str(out))
                    out = ser.readline().decode('utf-8', 'ignore').strip()
                    print(str(out))
                    out = ser.readline().decode('utf-8', 'ignore').strip()
                    print(str(out))
                    out = ser.readline().decode('utf-8', 'ignore').strip()
                    print(str(out))
                    out = ser.readline().decode('utf-8', 'ignore').strip()
                    print(str(out))
                    out = ser.readline().decode('utf-8', 'ignore').strip()
                    print(str(out))
                    out = ser.readline().decode('utf-8', 'ignore').strip()
                    print(str(out))
                    out = ser.readline().decode('utf-8', 'ignore').strip()
                    print(str(out))
                    out = ser.readline().decode('utf-8', 'ignore').strip()
                    print(str(out))
                    out = ser.readline().decode('utf-8', 'ignore').strip()
                    print(str(out))
                    out = ser.readline().decode('utf-8', 'ignore').strip()
                    print(str(out))
                    out = ser.readline().decode('utf-8', 'ignore').strip()
                    print(str(out))
                    out = ser.readline().decode('utf-8', 'ignore').strip()
                    print(str(out))
                    out = ser.readline().decode('utf-8', 'ignore').strip()
                    print(str(out))
                    out = ser.readline().decode('utf-8', 'ignore').strip()
                    print(str(out))
                    out = ser.readline().decode('utf-8', 'ignore').strip()
                    print(str(out))
                    out = ser.readline().decode('utf-8', 'ignore').strip()
                    print(str(out))
                    out = ser.readline().decode('utf-8', 'ignore').strip()
                    print(str(out))
                    out = ser.readline().decode('utf-8', 'ignore').strip()
                    print(str(out))
                    out = ser.readline().decode('utf-8', 'ignore').strip()
                    print(str(out))
                    out = ser.readline().decode('utf-8', 'ignore').strip()
                    print(str(out))
                    out = ser.readline().decode('utf-8', 'ignore').strip()
                    print(str(out))
                    out = ser.readline().decode('utf-8', 'ignore').strip()
                    print(str(out))
                    out = ser.readline().decode('utf-8', 'ignore').strip()
                    print(str(out))
                    out = ser.readline().decode('utf-8', 'ignore').strip()
                    print(str(out))
                    out = ser.readline().decode('utf-8', 'ignore').strip()
                    print(str(out))
                    out = ser.readline().decode('utf-8', 'ignore').strip()
                    print(str(out))
                    """
                    if "[ " in out:
                        messagebox.showerror("", "Please Press The 'connect' Button Again")
                        formattercheckbox = customtkinter.CTkCheckBox(master=self.four_frame, text="", height=130,
                                                                      width=130)
                        formattercheckbox.place(relx=.055, rely=.4)
                        formattercheckbox.select()
                        formattercheckbox.configure(border_color='black', highlightcolor='green', fg_color='green',
                                                    hover_color='white', state=customtkinter.DISABLED)
                        tclcheckbox = customtkinter.CTkCheckBox(master=self.four_frame, text="", height=130,
                                                                width=130)
                        tclcheckbox.place(relx=.45, rely=.4)
                        tclcheckbox.select()
                        tclcheckbox.configure(border_color='black', highlightcolor='green', fg_color='green',
                                              hover_color='white',
                                              state=customtkinter.DISABLED)
                        trolleycheckbox = customtkinter.CTkCheckBox(master=self.four_frame, text=".",
                                                                    text_color="white",
                                                                    height=130, width=130)
                        trolleycheckbox.place(relx=.861, rely=.4)
                        trolleycheckbox.select()
                        trolleycheckbox.configure(border_color='black', highlightcolor='red', fg_color='red',
                                                  hover_color='white', state=customtkinter.DISABLED)
                        ser.close()
                        break
                    if "-bash: Zeus: command not found" in out:
                        messagebox.showerror("", "Please Press The 'connect' Button")
                        formattercheckbox = customtkinter.CTkCheckBox(master=self.four_frame, text="", height=130,
                                                                      width=130)
                        formattercheckbox.place(relx=.055, rely=.4)
                        formattercheckbox.select()
                        formattercheckbox.configure(border_color='black', highlightcolor='green', fg_color='green',
                                                    hover_color='white', state=customtkinter.DISABLED)
                        tclcheckbox = customtkinter.CTkCheckBox(master=self.four_frame, text="", height=130,
                                                                width=130)
                        tclcheckbox.place(relx=.45, rely=.4)
                        tclcheckbox.select()
                        tclcheckbox.configure(border_color='black', highlightcolor='red', fg_color='red',
                                              hover_color='white',
                                              state=customtkinter.DISABLED)
                        trolleycheckbox = customtkinter.CTkCheckBox(master=self.four_frame, text=".",
                                                                    text_color="white",
                                                                    height=130, width=130)
                        trolleycheckbox.place(relx=.861, rely=.4)
                        trolleycheckbox.select()
                        trolleycheckbox.configure(border_color='black', highlightcolor='red', fg_color='red',
                                                  hover_color='white', state=customtkinter.DISABLED)
                        ser.close()
                        break
                        """
                    if '1' in out:
                        messagebox.showerror("", "No Connection To Trolley")
                        formattercheckbox = customtkinter.CTkCheckBox(master=self.four_frame, text="", height=130,
                                                                      width=130)
                        formattercheckbox.place(relx=.055, rely=.4)
                        formattercheckbox.select()
                        formattercheckbox.configure(border_color='black', highlightcolor='green', fg_color='green',
                                                    hover_color='white',
                                                    state=customtkinter.DISABLED)
                        tclcheckbox = customtkinter.CTkCheckBox(master=self.four_frame, text="", height=130, width=130)
                        tclcheckbox.place(relx=.45, rely=.4)
                        tclcheckbox.select()
                        tclcheckbox.configure(border_color='black', highlightcolor='green', fg_color='green',
                                              hover_color='white',
                                              state=customtkinter.DISABLED)
                        trolleycheckbox = customtkinter.CTkCheckBox(master=self.four_frame, text=".",
                                                                    text_color="white",
                                                                    height=130, width=130)
                        trolleycheckbox.place(relx=.861, rely=.4)
                        trolleycheckbox.select()
                        trolleycheckbox.configure(border_color='black', highlightcolor='red', fg_color='red',
                                                  hover_color='white',
                                                  state=customtkinter.DISABLED)
                        # self.controllerbutton.configure(state=customtkinter.DISABLED)
                    else:
                        messagebox.showinfo("", "Trolley Controller Is Ready")
                        # self.connectbutton.configure(state=customtkinter.NORMAL)
                        formattercheckbox = customtkinter.CTkCheckBox(master=self.four_frame, text="", height=130,
                                                                      width=130)
                        formattercheckbox.place(relx=.055, rely=.4)
                        formattercheckbox.select()
                        formattercheckbox.configure(border_color='black', highlightcolor='green', fg_color='green',
                                                    hover_color='white',
                                                    state=customtkinter.DISABLED)
                        tclcheckbox = customtkinter.CTkCheckBox(master=self.four_frame, text="", height=130, width=130)
                        tclcheckbox.place(relx=.45, rely=.4)
                        tclcheckbox.select()
                        tclcheckbox.configure(border_color='black', highlightcolor='green', fg_color='green',
                                              hover_color='white',
                                              state=customtkinter.DISABLED)
                        trolleycheckbox = customtkinter.CTkCheckBox(master=self.four_frame, text=".",
                                                                    text_color="white",
                                                                    height=130, width=130)
                        trolleycheckbox.place(relx=.861, rely=.4)
                        trolleycheckbox.select()
                        trolleycheckbox.configure(border_color='black', highlightcolor='green', fg_color='green',
                                                  hover_color='white',
                                                  state=customtkinter.DISABLED)
                        ser.close()
                        break

                    ser.close()
                    break

        """ This code is for the connect button"""
        image_size1_x = 600
        image_size1_y = 290
        self.connect_image = ImageTk.PhotoImage(
            Image.open('C:\\Users\\quevedo\\PycharmProjects\\Trolleytrolley\\images\\connect.PNG').resize(
                (image_size1_x, image_size1_y)))
        self.connectbutton = customtkinter.CTkButton(master=self.one_frame, image=self.connect_image,
                                                     text_font=("Arial", 1), text=".", width=400, height=200,
                                                     border_width=0, corner_radius=20, command=connect_pressed)
        self.connectbutton.configure(bg_color="white", fg_color="white", hover_color='green', text_color="white")
        self.connectbutton.place(relx=.7, rely=.27, anchor=CENTER)
        # self.connectbutton.configure(state=customtkinter.DISABLED)

        ##############################################################################################################
        """ This code is for the disconnect button """

        def disconnect_pressed():
            ser = serial.Serial()
            ser.port = 'COM1'
            ser.baudrate = 9600
            ser.bytesize = serial.EIGHTBITS
            ser.parity = serial.PARITY_NONE
            ser.xonxoff = 1
            ser.rtscts = 0
            ser.dsrdtr = 0
            ser.stopbits = 1
            ser.timeout = 2
            ser.open()
            # self.controllerbutton.configure(state=customtkinter.DISABLED)
            ser.write(str.encode('\x03'))  # \x03 is equivalent as ctrl + c
            out = ser.readline().decode('utf-8', 'ignore').strip()
            print(str(out))
            formattercheckbox = customtkinter.CTkCheckBox(master=self.four_frame, text="", height=130, width=130)
            formattercheckbox.place(relx=.055, rely=.4)
            formattercheckbox.select()
            formattercheckbox.configure(border_color='black', highlightcolor='red', fg_color='red', hover_color='white',
                                        state=customtkinter.DISABLED)
            tclcheckbox = customtkinter.CTkCheckBox(master=self.four_frame, text="", height=130, width=130)
            tclcheckbox.place(relx=.45, rely=.4)
            tclcheckbox.select()
            tclcheckbox.configure(border_color='black', highlightcolor='red', fg_color='red', hover_color='white',
                                  state=customtkinter.DISABLED)
            trolleycheckbox = customtkinter.CTkCheckBox(master=self.four_frame, text=".", text_color="white",
                                                        height=130, width=130)
            trolleycheckbox.place(relx=.861, rely=.4)
            trolleycheckbox.select()
            trolleycheckbox.configure(border_color='black', highlightcolor='red', fg_color='red', hover_color='white',
                                      state=customtkinter.DISABLED)
            # self.connectbutton.configure(state=customtkinter.NORMAL)
            print("DISCONNECTED")
            ser.close()

        image_size1_x = 600
        image_size1_y = 290
        self.disconnect_image = ImageTk.PhotoImage(
            Image.open("C:\\Users\\quevedo\\PycharmProjects\\Trolleytrolley\\images\\disconnect.PNG").resize(
                (image_size1_x, image_size1_y)))
        self.disconnectbutton = customtkinter.CTkButton(master=self.one_frame, image=self.disconnect_image,
                                                        text_font=("Arial", 1), text=".", width=400, height=200,
                                                        border_width=0, corner_radius=20, command=disconnect_pressed)
        self.disconnectbutton.configure(bg_color="white", fg_color="white", hover_color='red', text_color="white")
        self.disconnectbutton.place(relx=.3, rely=.27, anchor=CENTER)
        ###############################################################################################################
        """ line """
        self.horizontal_line = customtkinter.CTkFrame(master=self.three_frame, corner_radius=0)
        self.horizontal_line.place(relx=.5, rely=.95, anchor="center", width=2000, height=10)
        self.horizontal_line.configure(fg_color="black")
        """ four frame """
        self.four_frame = customtkinter.CTkFrame(master=self.one_frame, corner_radius=0)
        self.four_frame.place(relx=.5, rely=.65, anchor="center", width=2000, height=370)
        self.four_frame.configure(fg_color="white")
        """ status label """
        self.status = customtkinter.CTkLabel(master=self.four_frame, text_font=("rono", 30, "bold"), bg_color='white',
                                             text="STATUS:", text_color='black')
        self.status.place(relx=.5, rely=.09, anchor=CENTER)
        """ Formatter label """
        self.formatter = customtkinter.CTkLabel(master=self.four_frame, text_font=("Arial", 25), bg_color='white',
                                                text="Formatter:", text_color='black')
        self.formatter.place(relx=.1035, rely=.3, anchor=CENTER)
        """ This code is for the Formatter connection checkbox """
        formattercheckbox = customtkinter.CTkCheckBox(master=self.four_frame, text="", height=130, width=130)
        formattercheckbox.place(relx=.055, rely=.4)
        formattercheckbox.configure(border_color='black', highlightcolor='green', fg_color='green', hover_color='white',
                                    state=customtkinter.DISABLED)
        """ TCL label """
        self.tcl = customtkinter.CTkLabel(master=self.four_frame, text_font=("Arial", 25), bg_color='white',
                                          text="TCL:", text_color='black')
        self.tcl.place(relx=.5, rely=.3, anchor=CENTER)
        """ This code is for the TCL connection checkbox """
        tclcheckbox = customtkinter.CTkCheckBox(master=self.four_frame, text="", height=130, width=130)
        tclcheckbox.place(relx=.45, rely=.4)
        tclcheckbox.configure(border_color='black', highlightcolor='green', fg_color='green', hover_color='white',
                              state=customtkinter.DISABLED)
        """ Trolley label """
        self.trolley = customtkinter.CTkLabel(master=self.four_frame, text_font=("Arial", 25), bg_color='white',
                                              text="Trolley:", text_color='black')
        self.trolley.place(relx=.91, rely=.3, anchor=CENTER)
        """ trolley connection """
        trolleycheckbox = customtkinter.CTkCheckBox(master=self.four_frame, text=".", text_color="white", height=130,
                                                    width=130)
        trolleycheckbox.place(relx=.861, rely=.4)
        trolleycheckbox.configure(border_color='black', highlightcolor='green', fg_color='green', hover_color='white',
                                  state=customtkinter.DISABLED)
        """ bottom line """
        self.vertical_line = customtkinter.CTkFrame(master=self.four_frame, corner_radius=0)
        self.vertical_line.place(relx=.5, rely=1, anchor="center", width=2000, height=20)
        self.vertical_line.configure(fg_color="black")
        """ five frame """
        self.five_frame = customtkinter.CTkFrame(master=self.one_frame, corner_radius=0)
        self.five_frame.place(relx=.5, rely=.9221, anchor="center", width=2000, height=150)
        self.five_frame.configure(fg_color="white")
        ###############################################################################################################
        """ This code is for the controller button """
        image_size1_x = 850
        image_size1_y = 120
        self.control_image = ImageTk.PhotoImage(
            Image.open("C:\\Users\\quevedo\\PycharmProjects\\Trolleytrolley\\images\\controltrolley.PNG").resize(
                (image_size1_x, image_size1_y)))
        self.controllerbutton = customtkinter.CTkButton(master=self.five_frame, image=self.control_image,
                                                        text_font=("Arial", 1), text=".", width=500,
                                                        height=90, border_width=0, corner_radius=20)
        self.controllerbutton.configure(bg_color="white", fg_color="white", hover_color='light blue',
                                        text_color="white", command=self.tc_pressed)
        self.controllerbutton.place(relx=.5, rely=.5, anchor=CENTER)
        # self.controllerbutton.configure(state=customtkinter.DISABLED)

    def on_closing(self):
        self.destroy()

    def tc_pressed(self):
        main = customtkinter.CTkToplevel(self)
        self.iconify()
        main.title("")
        main.geometry("700x500")
        main.protocol("WM_DELETE_WINDOW")
        main.grid_columnconfigure(0, weight=1)
        main.grid_rowconfigure(0, weight=1)
        main.iconbitmap('C:\\Users\\quevedo\\PycharmProjects\\Trolleytrolley\\images\\hp.ico')
        main.state('zoomed')
        """ main frame """
        main.one_frame = customtkinter.CTkFrame(master=main, corner_radius=0)
        main.one_frame.place(relx=.5, rely=.5, anchor="center", width=2000, height=960)
        main.one_frame.configure(fg_color="white")
        """ horizontal line """
        main.horizontal_line = customtkinter.CTkFrame(master=main, corner_radius=0)
        main.horizontal_line.place(relx=.63, rely=.33, anchor="center", width=1500, height=10)
        main.horizontal_line.configure(fg_color="black")
        """ vertical line """
        main.vertical_line = customtkinter.CTkFrame(master=main, corner_radius=0)
        main.vertical_line.place(relx=.24, rely=.5, anchor="center", width=10, height=960)
        main.vertical_line.configure(fg_color="black")
        ###############################################################################################################
        """ This code is for the down button """

        def active_downbutton():
            main.downbutton.configure(state=NORMAL)

        def down_pressed():
            global ser
            n = 1
            while n == 1:
                # add ui/window that tells user that the trolley controller is currently moving
                ser = serial.Serial()
                ser.port = 'COM1'
                ser.baudrate = 9600
                ser.bytesize = serial.EIGHTBITS
                ser.parity = serial.PARITY_NONE
                ser.xonxoff = 1
                ser.rtscts = 0
                ser.dsrdtr = 0
                ser.stopbits = 1
                ser.timeout = 1
                ser.open()
                ser.write(str.encode('[Distance_get [PowderPlatformFront getPosition] 1]\n'))
                out = ser.readline().decode("utf-8").strip()
                print(str(out))
                out = ser.readline().decode("utf-8").strip()
                print(str(out))
                num = out
                distance = (int((''.join(filter(str.isdigit, num)))))
                print(int(distance))
                main.after(2000)
                if int(distance) < 200:
                    ser.write(str.encode(
                        "PowderPlatformFront  move [new_Distance 10 1] [new_Speed 2 1] $IBuildPlatform_RISING_EDGE\n"))
                    print('moving Down')
                    time.sleep(.01)
                    ser.write(str.encode(
                        "PowderPlatformRear  move [new_Distance 10 1] [new_Speed 2 1] $IBuildPlatform_RISING_EDGE\n"))
                    main.after(3000)
                    ser.close()
                else:
                    print("done")
                    main.frontpos_1 = customtkinter.CTkLabel(master=main.second_frame,
                                                             text_font=("Buffalo", 25, "bold"),
                                                             text=str(distance) + '' + ' mm')
                    main.frontpos_1.configure(fg="green", bg_color='white')
                    main.frontpos_1.place(relx=.17, rely=.6, anchor=CENTER)

                    main.rearpos_2 = customtkinter.CTkLabel(master=main.second_frame,
                                                            text_font=("Buffalo", 25, "bold"),
                                                            text=str(distance) + '' + ' mm')
                    main.rearpos_2.configure(fg="green", bg_color='white')
                    main.rearpos_2.place(relx=.83, rely=.6, anchor=CENTER)
                    ser.write(str.encode('[Distance_get [BuildPlatform getPosition] 1]\n'))
                    out = ser.readline().decode("utf-8").strip()
                    print(str(out))
                    out = ser.readline().decode("utf-8").strip()
                    print(str(out))
                    num = out
                    build_distance = (int((''.join(filter(str.isdigit, num)))))
                    print(int(distance))
                    main.buildpos_3 = customtkinter.CTkLabel(master=main.second_frame,
                                                             text_font=("Buffalo", 25, "bold"),
                                                             text=str(build_distance) + '' + ' mm')
                    main.buildpos_3.configure(fg="green", bg_color='white')
                    main.buildpos_3.place(relx=.5, rely=.6, anchor=CENTER)
                    n = 2
                    ser.close()
                    break

        image_size1_x = 550
        image_size1_y = 550
        main.downbutton_image = ImageTk.PhotoImage(
            Image.open("C:\\Users\\quevedo\\PycharmProjects\\Trolleytrolley\\images\\arrowdown.PNG").resize(
                (image_size1_x, image_size1_y)))
        main.downbutton = customtkinter.CTkButton(master=main.one_frame, image=main.downbutton_image,
                                                  text_font=("Arial", 1), text="", height=50, border_width=0,
                                                  corner_radius=0, command=down_pressed, width=50)
        main.downbutton.configure(bg_color="white", fg_color="white", hover_color='black', text_color="white")
        main.downbutton.place(relx=.47, rely=.665, anchor=CENTER)

        ###############################################################################################################
        """ This code is for the up button """

        def active_upbutton():
            main.upbutton.configure(state=NORMAL)

        def up_pressed():
            ser = serial.Serial()
            ser.port = 'COM1'
            ser.baudrate = 9600
            ser.bytesize = serial.EIGHTBITS
            ser.parity = serial.PARITY_NONE
            ser.xonxoff = 1
            ser.rtscts = 0
            ser.dsrdtr = 0
            ser.stopbits = 1
            ser.timeout = 2
            ser.open()
            if ser.isOpen():
                while True:
                    time.sleep(.01)
                    ser.write(str.encode('[Distance_get [BuildPlatform getPosition] 1]\n'))
                    out = ser.readline().decode("utf-8").strip()
                    print(str(out))
                    out = ser.readline().decode("utf-8").strip()
                    print(str(out))
                    numthree = out
                    j = ''.join(x for x in numthree if x.isdigit())
                    print(int(j))
                    main.buildpos_3 = customtkinter.CTkLabel(master=main.second_frame,
                                                             text_font=("Buffalo", 25, "bold"),
                                                             text=j + '' + ' mm')
                    main.buildpos_3.configure(fg="green", bg_color='white')
                    main.buildpos_3.place(relx=.83, rely=.6, anchor=CENTER)
                    if int(j) == 0:
                        main.upbutton.configure(state=customtkinter.DISABLED)
                        messagebox.showinfo("", "MAX Distance")
                        break
                    else:
                        ser.write(str.encode(
                            "BuildPlatform  move [new_Distance -5 1] [new_Speed 2 1] $IBuildPlatform_RISING_EDGE\n"))
                        out = ser.readline().decode("utf-8").strip()
                        print(str(out))
                        out = ser.readline().decode("utf-8").strip()
                        print(str(out))
                        out = ser.readline().decode("utf-8").strip()
                        print(str(out))
                        ser.close()
                        break
            main.downbutton.after(1500, active_downbutton)
            ser.close()

        image_size1_x = 550
        image_size1_y = 550
        main.upbutton_image = ImageTk.PhotoImage(
            Image.open("C:\\Users\\quevedo\\PycharmProjects\\Trolleytrolley\\images\\arrowup.PNG").resize(
                (image_size1_x, image_size1_y)))
        main.upbutton = customtkinter.CTkButton(master=main.one_frame, image=main.upbutton_image,
                                                text_font=("Arial", 1), text="", height=50, border_width=0,
                                                corner_radius=0, command=up_pressed, width=50)
        main.upbutton.configure(bg_color="white", fg_color="white", hover_color='black', text_color="white")
        main.upbutton.place(relx=.763, rely=.665, anchor=CENTER)
        ##############################################################################################################
        """ second frame """
        main.second_frame = customtkinter.CTkFrame(master=main, corner_radius=0, width=970, height=205)
        main.second_frame.place(relx=.6215, rely=.1685, anchor=CENTER)
        main.second_frame.configure(fg_color="white")
        """ vertical line """
        main.vertical_line = customtkinter.CTkFrame(master=main, corner_radius=0)
        main.vertical_line.place(relx=.5, rely=.166, anchor="center", width=10, height=307)
        main.vertical_line.configure(fg_color="black")
        """ vertical line """
        main.vertical_line = customtkinter.CTkFrame(master=main, corner_radius=0)
        main.vertical_line.place(relx=.7455, rely=.166, anchor="center", width=10, height=307)
        main.vertical_line.configure(fg_color="black")
        """ label """
        main.plabel_1 = customtkinter.CTkLabel(master=main.second_frame, text_font=("Buffalo", 20, "bold"),
                                               text="Front Platform Position")
        main.plabel_1.configure(fg="black", bg_color='white')
        main.plabel_1.place(relx=.17, rely=.2, anchor=CENTER)
        """ label """
        main.plabel_2 = customtkinter.CTkLabel(master=main.second_frame, text_font=("Buffalo", 20, "bold"),
                                               text="Build Platform Position")
        main.plabel_2.configure(fg="black", bg_color='white')
        main.plabel_2.place(relx=.5, rely=.2, anchor=CENTER)
        """ label """
        main.plabel_3 = customtkinter.CTkLabel(master=main.second_frame, text_font=("Buffalo", 20, "bold"),
                                               text="Rear Platform Position")
        main.plabel_3.configure(fg="black", bg_color='white')
        main.plabel_3.place(relx=.83, rely=.2, anchor=CENTER)
        ##############################################################################################################
        """ This code is for the position button """

        def update_position():
            ser = serial.Serial()
            ser.port = 'COM1'
            ser.baudrate = 9600
            ser.bytesize = serial.EIGHTBITS
            ser.parity = serial.PARITY_NONE
            ser.xonxoff = 1
            ser.rtscts = 0
            ser.dsrdtr = 0
            ser.stopbits = 1
            ser.timeout = None
            ser.open()
            if ser.isOpen():
                while True:
                    time.sleep(.01)
                    ser.write(str.encode('[Distance_get [PowderPlatformFront getPosition] 1]\n'))
                    out = ser.readline().decode("utf-8").strip()
                    print(str(out))
                    out = ser.readline().decode("utf-8").strip()
                    print(str(out))
                    num = out
                    k = ''.join(x for x in num if x.isdigit())
                    print(int(k))

                    main.frontpos_1 = customtkinter.CTkLabel(master=main.second_frame,
                                                             text_font=("Buffalo", 25, "bold"),
                                                             text=k + '' + ' mm')
                    main.frontpos_1.configure(fg="green", bg_color='white')
                    main.frontpos_1.place(relx=.17, rely=.6, anchor=CENTER)
                    time.sleep(.01)
                    ser.write(str.encode('[Distance_get [PowderPlatformRear getPosition] 1]\n'))
                    out = ser.readline().decode("utf-8").strip()
                    print(str(out))
                    out = ser.readline().decode("utf-8").strip()
                    print(str(out))
                    numtwo = out
                    l = ''.join(x for x in numtwo if x.isdigit())
                    print(int(l))

                    main.rearpos_2 = customtkinter.CTkLabel(master=main.second_frame,
                                                            text_font=("Buffalo", 25, "bold"),
                                                            text=l + '' + ' mm')
                    main.rearpos_2.configure(fg="green", bg_color='white')
                    main.rearpos_2.place(relx=.83, rely=.6, anchor=CENTER)
                    time.sleep(.01)
                    ser.write(str.encode('[Distance_get [BuildPlatform getPosition] 1]\n'))
                    out = ser.readline().decode("utf-8").strip()
                    print(str(out))
                    out = ser.readline().decode("utf-8").strip()
                    print(str(out))
                    numthree = out
                    j = ''.join(x for x in numthree if x.isdigit())
                    print(int(j))
                    main.buildpos_3 = customtkinter.CTkLabel(master=main.second_frame,
                                                             text_font=("Buffalo", 25, "bold"),
                                                             text=j + '' + ' mm')
                    main.buildpos_3.configure(fg="green", bg_color='white')
                    main.buildpos_3.place(relx=.5, rely=.6, anchor=CENTER)
                    ser.close()
                    break
                ser.close()

        image_size1_x = 300  # Image size
        image_size1_y = 200
        main.position_image = ImageTk.PhotoImage(
            Image.open("C:\\Users\\quevedo\\PycharmProjects\\Trolleytrolley\\images\\position.PNG").resize
            ((image_size1_x, image_size1_y)))
        main.positionbutton = customtkinter.CTkButton(master=main.one_frame, image=main.position_image,
                                                      text_font=("Arial", 1),
                                                      text=".", width=10,
                                                      height=100, border_width=0, corner_radius=20,
                                                      command=update_position)
        main.positionbutton.configure(bg_color="white", fg_color="white", hover_color='red', text_color="white")
        main.positionbutton.place(relx=.13, rely=.535, anchor=CENTER)

        ###############################################################################################################
        """ This code is for the exit button """

        def exit_pressed():
            # self.controllerbutton.configure(state=customtkinter.DISABLED)
            main.destroy()
            self.state('zoomed')
            formattercheckbox = customtkinter.CTkCheckBox(master=self.four_frame, text="", height=130,
                                                          width=130)
            formattercheckbox.place(relx=.055, rely=.4)
            formattercheckbox.select()
            formattercheckbox.configure(border_color='black', highlightcolor='green', fg_color='green',
                                        hover_color='white', state=customtkinter.DISABLED)
            tclcheckbox = customtkinter.CTkCheckBox(master=self.four_frame, text="", height=130, width=130)
            tclcheckbox.place(relx=.45, rely=.4)
            tclcheckbox.select()
            tclcheckbox.configure(border_color='black', highlightcolor='green', fg_color='green',
                                  hover_color='white',
                                  state=customtkinter.DISABLED)
            trolleycheckbox = customtkinter.CTkCheckBox(master=self.four_frame, text=".", text_color="white",
                                                        height=130, width=130)
            trolleycheckbox.place(relx=.861, rely=.4)
            trolleycheckbox.select()
            trolleycheckbox.configure(border_color='black', highlightcolor='red', fg_color='red',
                                      hover_color='white', state=customtkinter.DISABLED)

        image_size1_x = 350
        image_size1_y = 140
        main.exit_image = ImageTk.PhotoImage(
            Image.open("C:\\Users\\quevedo\\PycharmProjects\\Trolleytrolley\\images\\exit.PNG").resize(
                (image_size1_x, image_size1_y)))
        main.exitbutton = customtkinter.CTkButton(master=main.one_frame, image=main.exit_image,
                                                  text_font=("Arial", 1),
                                                  text=".",
                                                  width=10, height=100, border_width=0, corner_radius=20,
                                                  command=exit_pressed)
        main.exitbutton.configure(bg_color="white", fg_color="white", hover_color='white', text_color="white")
        main.exitbutton.place(relx=.13, rely=.88, anchor=CENTER)
        ###############################################################################################################
        """ This code is for the Home Button """
        image_size1_x = 300  # Size image
        image_size1_y = 200
        main.home_image = ImageTk.PhotoImage(
            Image.open("C:\\Users\\quevedo\\PycharmProjects\\Trolleytrolley\\images\\home.PNG").resize
            ((image_size1_x, image_size1_y)))
        # add your image^
        main.homebutton = customtkinter.CTkButton(master=main.one_frame, image=main.home_image,
                                                  text_font=("Arial", 1),
                                                  text=".", width=10,
                                                  height=100, border_width=0, corner_radius=20,
                                                  command=self.home_pressed)
        main.homebutton.configure(bg_color="white", fg_color="white", hover_color='green', text_color="white")
        main.homebutton.place(relx=.13, rely=.15, anchor=CENTER)

    def home_pressed(self):
        confirm = customtkinter.CTkToplevel()
        confirm.geometry(f'{500}x{400}+{600}+{50}')
        confirm.resizable(False, False)
        confirm.title("")
        confirm.iconbitmap('C:\\Users\\quevedo\\PycharmProjects\\Trolleytrolley\\images\\hp.ico')

        def button_pressed(a):
            start_time = time.time()

            def button_release(b):
                end_time = time.time()
                seconds = round(end_time - start_time, 1)
                if seconds > 5:
                    ser = serial.Serial()
                    ser.port = 'COM1'
                    ser.baudrate = 9600
                    ser.bytesize = serial.EIGHTBITS
                    ser.parity = serial.PARITY_NONE
                    ser.xonxoff = 1
                    ser.rtscts = 0
                    ser.dsrdtr = 0
                    ser.stopbits = 1
                    ser.timeout = 2
                    ser.open()
                    time.sleep(.1)
                    ser.write(str.encode('PowderPlatformFront home\n'))
                    time.sleep(.1)
                    ser.write(str.encode('PowderPlatformRear home\n'))
                    time.sleep(.1)
                    ser.write(str.encode('BuildPlatform home\n'))
                    time.sleep(.01)
                    text1 = customtkinter.CTkTextbox(confirm)
                    text1.insert('end', 'Moving Platforms to Home Position...')
                    text1.configure(state='disabled', font='Arial 15', bg_color='black', border_color='black',
                                    fg_color='black', bd=0)
                    text1.set_dimensions(335, 35)
                    text1.place(relx=.5, rely=.28, anchor=CENTER)
                    confirm.after(2000, lambda: confirm.destroy())
                    ser.close()

                else:
                    text2 = customtkinter.CTkTextbox(confirm)
                    text2.insert('end', 'Try again: ' + str(seconds) + "/" + str(5) + ' ' + 'Seconds')
                    text2.configure(state='disabled', font='Arial 15', bg_color='black', border_color='black',
                                    fg_color='black', bd=0)
                    text2.set_dimensions(335, 35)
                    text2.place(relx=.6, rely=.28, anchor=CENTER)

            confirm.bind('<ButtonRelease>', button_release)

        confirm.bind('<Button-1>', button_pressed)
        # Home frame
        home_frame = customtkinter.CTkFrame(master=confirm, corner_radius=0)
        home_frame.place(relx=.5, rely=.5, anchor="center", width=750, height=600)
        home_frame.configure(fg_color="black")
        """ This code is for the red Button """
        image_size1_x = 400
        image_size1_y = 300
        confirm.home_image = ImageTk.PhotoImage(
            Image.open("C:\\Users\\quevedo\\PycharmProjects\\Trolleytrolley\\images\\redred1.PNG").resize(
                (image_size1_x, image_size1_y)))
        confirm.button = customtkinter.CTkButton(master=confirm, image=confirm.home_image, text="", width=300,
                                                 text_color="red",
                                                 border_width=0, corner_radius=8, height=200)
        confirm.button.configure(fg_color="black", hover_color='red', text_color='black', bg_color='black')
        confirm.button.place(relx=.5, rely=.6, anchor=CENTER)
        # Home label
        homebutton_label = customtkinter.CTkLabel(master=home_frame, text_font=("Arial", 30, "bold"),
                                                  bg_color='black',
                                                  text="Home Position Button: ", text_color='red')
        homebutton_label.place(relx=.5, rely=0.1, anchor=CENTER)

        homebutton_label2 = customtkinter.CTkLabel(master=home_frame, text_font=("Arial", 12, "bold"),
                                                   bg_color='black',
                                                   text="Hold Button For 5 Seconds", text_color='red')
        homebutton_label2.place(relx=.5, rely=0.91, anchor=CENTER)

        confirm.mainloop()


app = Ap()
app.mainloop()
