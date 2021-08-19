#=====================================================#
#=========== Py pong by Edanzoung ====================#
#============== edanzoung@outlook.fr =================#
#=====================================================#


#=====================================================#
#==================== LICENSE ========================#

#************** THIS PROJECT IS FREE *****************#
#******* It means that the users have the freedom ****#
#***** *** to run, copy, distribute, study, change ***#
#*********** and improve the software  ***************#
#=====================================================#


from tkinter import Tk, Canvas, Entry, Label, Button, Frame
from PIL import Image, ImageTk, ImageGrab
import multitimer


class Tkinter_app():

    def __init__(self):
        self.window = Tk()
        self.window.geometry("800x500")
        self.window.configure(bg = "#000")
        self.window.resizable(False, False)
        
        #=== Logo Image
        self.logo_file = Image.open("assets/logo.png")
        self.logo_file = self.logo_file.resize((300,300), Image.ANTIALIAS)
        self.logo=ImageTk.PhotoImage(self.logo_file)
        
        #=== Player bar Image
        self.pad_file = Image.open("assets/pad2.png")
        self.pad_file = self.pad_file.resize((200,200), Image.ANTIALIAS)
        self.pad_=ImageTk.PhotoImage(self.pad_file)
        #=== Ball Image
        self.ball_file = Image.open("assets/ball.png")
        self.ball_file = self.ball_file.resize((30,30), Image.ANTIALIAS)
        self.ball_=ImageTk.PhotoImage(self.ball_file)
        
        
        #=== Start Button Image
        self.start_file = Image.open("assets/start.png")
        self.start_file = self.start_file.resize((150,50), Image.ANTIALIAS)
        self.start=ImageTk.PhotoImage(self.start_file)
        #=== Home Button Image
        self.home_file = Image.open("assets/home.png")
        self.home_file = self.home_file.resize((150,50), Image.ANTIALIAS)
        self.home=ImageTk.PhotoImage(self.home_file)
        #=== Start Loop Button Image
        self.start_loop_file = Image.open("assets/start_loop.png")
        self.start_loop_file = self.start_loop_file.resize((150,50), Image.ANTIALIAS)
        self.start_loop=ImageTk.PhotoImage(self.start_loop_file)
        #=== Stop Loop Button Image
        self.stop_loop_file = Image.open("assets/stop_loop.png")
        self.stop_loop_file = self.stop_loop_file.resize((150,50), Image.ANTIALIAS)
        self.stop_loop=ImageTk.PhotoImage(self.stop_loop_file)
        
        #==== Bar coordinates
        self.pad_coord_x=100
        self.pad_coord_y=100

        #==== Ball coordinates
        self.ball_coord_x=500
        self.ball_coord_y=100

        self.ball_direction_x=2
        self.ball_direction_y=2

        self.App()
        
        
        

    def App(self):
        
        def rgb(rgb):
            """translate an rgb tuple of int to a tkinter friendly color code"""
            return "#%02x%02x%02x" % rgb

        

        #=====================================================#
        #================= HOME PAGE    ======================#
        #=====================================================#
        self.frame1=Frame(self.window,bg = rgb((255,0,0)), height = 500, width = 800)
        self.frame1.place(x=0,y=0)
        self.canvas = Canvas(self.frame1,bg = "#fff",
            height = 500,
            width = 800,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge")

        self.canvas.place(x = 0, y = 0)

        #==== Logo Image
        self.canvas.create_image(400,200, image=self.logo)

        #=====================================================#
        #================= HOME PAGE  END  ===================#
        #=====================================================#
        

        #=====================================================#
        #================= GAME PAGE    ======================#
        #=====================================================#
        self.frame2=Frame(self.window,bg = rgb((100,100,100)), height = 500, width = 800)
        self.frame2.place(x=0,y=0)
        self.canvas2 = Canvas(self.frame2,bg = rgb((0,0,0)),
            height = 500,
            width = 800,
            bd = 0,
            highlightthickness = 0)
        self.canvas2.place(x = 0, y = 0)

        self.canvas2.create_rectangle(0,0,800,20,fill="#fff")
        self.canvas2.create_rectangle(0,440,800,500,fill="#fff")

        #==== pad Image
        self.pad_rect=self.canvas2.create_rectangle(self.pad_coord_x-5,self.pad_coord_y-60,self.pad_coord_x+15,self.pad_coord_y+10,fill="#000")
        self.pad=self.canvas2.create_image(self.pad_coord_x,self.pad_coord_y, image=self.pad_)
        #==== Ball Image
        self.ball=self.canvas2.create_image(self.ball_coord_x,self.ball_coord_y, image=self.ball_)     
        
        self.log=self.canvas2.create_text(120,10,text="",fill=rgb((255,255,255)),font=("Time",10,"bold"))
        self.pause=self.canvas2.create_text(420,250,text="PAUSE...",fill=rgb((255,255,255)),font=("Time",30,"bold"))
        
        #=====================================================#
        #================= GAME PAGE   END ===================#
        #=====================================================#
        

        #=====================================================#
        #================= PAGINATION FUNCTIONS ==============#
        #=====================================================#

        self.frame1.lift()
        
        def begin():
            self.frame2.lift()
            self.frame1.lower()
        def home():
            self.frame1.lift()
            self.frame2.lower()       

        #==== Button Start in Home Page        
        self.start_button = Button(self.canvas,image=self.start,compound = 'center',relief="flat",
                            highlightthickness = 0,text="",
                            bg=rgb((255,255,255)),borderwidth = 0,cursor="hand2",command=lambda : [begin()])
        self.start_button.place(x=320, y=400)
        
        #==== Button Home in ball Page
        self.home_button = Button(self.canvas2,image=self.home,compound = 'center',relief="flat",
                            highlightthickness = 0,text="",
                            bg=rgb((255,255,255)),borderwidth = 0,cursor="hand2",command=home)
        self.home_button.place(x=640, y=445)

        

        #=====================================================#
        #================= PAGINATION FUNCTIONS  END =========#
        #=====================================================#

        #=====================================================#
        #================= MOUSE EVENTS FUNCTIONS  ===========#
        #=====================================================#

        #==== When Mouse Enter and move over the snake
        def info(event):            
            self.canvas2.itemconfig(self.log,fill=rgb((0,0,0)),text='Mouse coordinates ==> x: '+str(event.x)+' / '+'y: '+str(event.y))
                

        #==== Function to move the pad
        def Pad_move(event):
            self.pad_coord_x=event.x
            self.pad_coord_y=event.y-60
            
            self.canvas2.coords(self.pad,(self.pad_coord_x,self.pad_coord_y))
            self.canvas2.coords(self.pad_rect,(event.x-5,event.y-120,event.x+15,event.y-50))

            

            #=== LEFT
            if self.canvas2.coords(self.pad)[0] <= 37:
                self.canvas2.coords(self.pad,(37,self.pad_coord_y))
                self.canvas2.coords(self.pad_rect,(37-5,self.pad_coord_y-60,37+15,self.pad_coord_y+10))

            #=== TOP
            if self.canvas2.coords(self.pad)[1] <= 85:
                self.canvas2.coords(self.pad,(self.pad_coord_x,85))
                self.canvas2.coords(self.pad_rect,(self.pad_coord_x-5,85-60,self.pad_coord_x+15,85+10))

            #=== BOTTOM
            if self.canvas2.coords(self.pad)[1] >= 420:
                self.canvas2.coords(self.pad,(self.pad_coord_x,420))
                self.canvas2.coords(self.pad_rect,(self.pad_coord_x-5,420-60,self.pad_coord_x+15,420+10))

            #=== LEFT/TOP
            if self.canvas2.coords(self.pad)[0] <= 37 and self.canvas2.coords(self.pad)[1] <= 85:
                self.canvas2.coords(self.pad,(37,85))
                self.canvas2.coords(self.pad_rect,(37-5,85-60,37+15,85+10))

            #=== LEFT/BOTTOM
            if self.canvas2.coords(self.pad)[0] <= 37 and self.canvas2.coords(self.pad)[1] >= 420:
                self.canvas2.coords(self.pad,(37,420))
                self.canvas2.coords(self.pad_rect,(37-5,420-60,37+15,420+10))

            

            

        #==== Function to move the ball

        #==== Timer to create a loop for ball move
        self.timer = multitimer.MultiTimer(interval=0.000000000000000000000000000000000000001,function=lambda:[ball_collisions()], count=-1)

        def start_loop():
            self.canvas2.itemconfig(self.pause,fill=rgb((255,255,255)),text="")
            self.timer.start()
        def stop_loop():
            self.canvas2.itemconfig(self.pause,fill=rgb((255,255,255)),text="PAUSE...")
            self.timer.stop()

        #==== Button Start loop in ball Page
        self.start_loop_button = Button(self.canvas2,image=self.start_loop,compound = 'center',relief="flat",
                            highlightthickness = 0,text="",
                            bg=rgb((255,255,255)),borderwidth = 0,cursor="hand2",command=start_loop)
        self.start_loop_button.place(x=250, y=445)
        #==== Button Stop loop in ball Page
        self.stop_loop_button = Button(self.canvas2,image=self.stop_loop,compound = 'center',relief="flat",
                            highlightthickness = 0,text="",
                            bg=rgb((255,255,255)),borderwidth = 0,cursor="hand2",command=stop_loop)
        self.stop_loop_button.place(x=440, y=445)
        
        
        def ball_collisions():

            self.width_pad = self.canvas2.winfo_width()-(self.canvas2.winfo_x()+self.canvas2.coords(self.pad)[0])
            
            #print(self.canvas2.coords(self.ball))
            
            self.canvas2.move(self.ball,self.ball_direction_x,self.ball_direction_y)

            #=== CANVAS RIGHT SIDE DETECTION BY THE BALL
            if self.canvas2.coords(self.ball)[0] >= self.canvas2.winfo_width()-20:
                self.ball_direction_x *= -1
            #=== CANVAS BOTTOM SIDE DETECTION BY THE BALL
            if self.canvas2.coords(self.ball)[1] >= self.canvas2.winfo_height()-80:
                self.ball_direction_y *= -1
            #=== CANVAS LEFT SIDE DETECTION BY THE BALL
            if self.canvas2.coords(self.ball)[0] <= self.canvas2.winfo_x()+20:
                self.ball_direction_x *= -1
            #=== CANVAS TOP SIDE DETECTION BY THE BALL
            if self.canvas2.coords(self.ball)[1] <= self.canvas2.winfo_y()+40:
                self.ball_direction_y *= -1

            #=== PAD AND BALL COLLISION
            if (self.canvas2.coords(self.ball)[0] <= self.canvas2.winfo_x()+self.canvas2.coords(self.pad_rect)[0] and
                self.canvas2.coords(self.ball)[1] >= self.canvas2.winfo_y()+self.canvas2.coords(self.pad_rect)[1] and
                self.canvas2.coords(self.ball)[1] <= self.canvas2.winfo_y()+self.canvas2.coords(self.pad_rect)[3]):
                self.ball_direction_x *=1
            elif (self.canvas2.coords(self.ball)[0] <= self.canvas2.winfo_x()+self.canvas2.coords(self.pad_rect)[2] and
                self.canvas2.coords(self.ball)[1] >= self.canvas2.winfo_y()+self.canvas2.coords(self.pad_rect)[1] and
                self.canvas2.coords(self.ball)[1] <= self.canvas2.winfo_y()+self.canvas2.coords(self.pad_rect)[3]) :
                
                self.ball_direction_x *= -1

            
                
                


        #=====================================================#
        #================= MOUSE EVENTS FUNCTIONS  END =======#
        #=====================================================#


        #=====================================================#
        #============= ITEMS BINDING =========================#
        #=====================================================#
        self.canvas2.tag_bind(self.pad,"<B1-Motion>",Pad_move)
        self.canvas2.bind("<Motion>",info)
        #=====================================================#
        #============= ITEMS BINDING  END ====================#
        #=====================================================#
        


if __name__=='__main__':
    app=Tkinter_app()
    app.window.mainloop()
