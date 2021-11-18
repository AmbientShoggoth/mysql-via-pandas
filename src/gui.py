import tkinter as tk
from sys import exit as sys_exit
import importlib



bgcol='#f7ca0d'
fgcol='black'

bwidth=30
bheight=5
bwidth_=int(bwidth*0.8)

class button_builder():
    def __init__(self,module_string,title,subtitle,uses_gui=False,width=bwidth,height=bheight):
        self.module_string=f"src.{module_string}"
        self.uses_gui=uses_gui
        
        self.title=title
        self.subtitle=subtitle
        
        self.width=width
        self.height=height
        
        
    def import_and_run_module(self):
        try:targetmodule=importlib.import_module(self.module_string)
        except ModuleNotFoundError:print(f"Module {self.module_string} not found.")
        
        if not self.uses_gui:self.root.withdraw()
        else:
            self.frame.pack_forget()
            try:
                targetmodule.main()
            except Exception as err:
                print(f"An error occured: {err}")
                self.root.deiconify()
            self.root.destroy()
        
    def create_button(self,frame,root):
        self.frame=frame
        self.root=root
        
        self.text=self.title+"\n\n"+self.subtitle
        
        self.button=tk.Button(self.frame,text=self.text,width=self.width,height=self.height,command=self.import_and_run_module)
        self.button.grid(row=main.row,column=main.col,padx=main.padx,pady=main.pady)
        
        main.col+=1
        if main.col>main.col_max:
            main.col=0
            main.row+=1
        
button_builder_list=[
    button_builder("encrypt","Encrypt","Generate encrypted credentials file and key.",True),
    button_builder("credentials","Temp","run credentials",True),
    
    ]

def main(sysargs=None):
    
    main.row,main.col=1,0
    main.col_max=5
    main.padx,main.pady=2,5
    
    root=tk.Tk()
    root.title("Various Scripts")
    
    root.tk_setPalette(foreground=fgcol,background=bgcol)
    
    # Override root close behaviour to quit script also
    def fullclose():root.destroy();sys_exit()
    root.protocol('WM_DELETE_WINDOW', fullclose)
    
    mainframe=tk.Frame(root)
    
    fullwidth=(bwidth+main.padx)*(main.col_max+1)
    
    greeting=tk.Label(mainframe,text="Select Script",width=fullwidth,height=3,bg=fgcol,fg=bgcol)
    greeting.grid(row=0,column=0,columnspan=main.col_max+1)
    
    #Build buttons
    for button in button_builder_list:button.create_button(frame=mainframe,root=root)
    
    mainframe.pack()
    
    root.mainloop()
    

if __name__ == '__main__':main()