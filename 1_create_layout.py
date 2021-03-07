from tkinter import *
import tkinter.ttk as ttk

root=Tk()
root.title("Merge Pictures")

# file
fileFrame=Frame(root)
fileFrame.pack(fill='x',padx=5,pady=5)
btnAddFile=Button(fileFrame,text='Add File')
btnAddFile.pack(side='left')
btnDelFile=Button(fileFrame,text='Del. File')
btnDelFile.pack(side='right')

#list box
listFrame=Frame(root)
listFrame.pack(fill='both',padx=5,pady=5)
sb=Scrollbar(listFrame)
sb.pack(side='right',fill='y')
listFile=Listbox(listFrame,selectmode='extended',height=15,yscrollcommand=sb.set)
listFile.pack(side='left',fill='both',expand=True)
sb.config(command=listFile.yview)

#path
pathFrame=LabelFrame(root,text='Saving Path')
pathFrame.pack(fill='x',padx=5,pady=5)
pathSaving=Entry(pathFrame)
pathSaving.pack(side='left',fill='x',expand=True,ipady=3,padx=5,pady=5)
btnSearchPath=Button(pathFrame,text='Search Path',width=10)
btnSearchPath.pack(side='right',padx=5,pady=5)

#options
optFrame=LabelFrame(root,text='Option...')
optFrame.pack(padx=5,pady=5)
 # Width
lbPicWidth=Label(optFrame,text='Width',width=8)
lbPicWidth.pack(side='left',padx=5,pady=5)
optPicWidth=['Origin','1024','800','640']
cbPicWidth=ttk.Combobox(optFrame,state='readonly',values=optPicWidth,width=8)
cbPicWidth.current(0)
cbPicWidth.pack(side='left',padx=5,pady=5)

 # Gap
lbPicGap=Label(optFrame,text='Gap',width=8)
lbPicGap.pack(side='left',padx=5,pady=5)
optPicGap=['None','Narrow','Normal','Wide']
cbPicGap=ttk.Combobox(optFrame,state='readonly',values=optPicGap,width=8)
cbPicGap.current(0)
cbPicGap.pack(side='left',padx=5,pady=5)

 # Pic Format
lbPicFormat=Label(optFrame,text='Format',width=8)
lbPicFormat.pack(side='left',padx=5,pady=5)
optPicFormat=['PNG','JPG','BMP']
cbPicFormat=ttk.Combobox(optFrame,state='readonly',values=optPicFormat,width=8)
cbPicFormat.current(0)
cbPicFormat.pack(side='left',padx=5,pady=5)

# Progree Bar
pbFrame=LabelFrame(root,text='Saving Progress')
pbFrame.pack(fill='x',padx=5,pady=5)
statusPB=DoubleVar()
pbMerging=ttk.Progressbar(pbFrame,maximum=100,variable=statusPB)
pbMerging.pack(fill='x',padx=5,pady=5)

# Execute Frame
runFrame=Frame(root)
runFrame.pack(fill='x',padx=5,pady=5)
btnRun=Button(runFrame,text='Run',width=10)
btnRun.pack(side='left',padx=5,pady=5)
btnQuite=Button(runFrame,text='Quit',width=10,command=root.quit)
btnQuite.pack(side='right',padx=5,pady=5)

root.resizable(False,False)
root.mainloop()