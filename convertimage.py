# Aplica um filtro preto e branco a uma imagem
from tkinter import *
from tkinter import filedialog

from PIL import Image
from PIL import ImageTk

# Inicializa o tkinter
root = Tk()
root.title('TextPad')

# Cria a barra de ferramentas
toolbar_frame = Frame(root)
toolbar_frame.pack()

# Função que abre a imagem
def open_file():
    global my_img
    global img
    global my_lbl2

    # Abre a janela para selecionar o caminho da imagem
    root.filename = filedialog.askopenfilename()
    
    # Cria as label's necessárias e exibe a imagem na tela
    my_lbl = Label(root).pack()
    img = Image.open(root.filename)
    my_img = ImageTk.PhotoImage(img)
    my_lbl2 = Label(image=my_img)
    my_lbl2.pack()


# função que aplica o filtro preto e branco a imagem
def convert():
    global my_img_bw

    # Verifica se a imagem está aberta e aplica o filtro
    if my_img:
        blackAndWhite = img.convert("L")
        my_img_bw = ImageTk.PhotoImage(blackAndWhite)
        my_lbl2.destroy()
        my_lbl3 = Label(image=my_img_bw).pack()

# Cria o menu
foolbar_menu = Menu(root)
root.config(menu=foolbar_menu)

# Adiciona as opções ao menu
file_menu = Menu(foolbar_menu, tearoff=False)
foolbar_menu.add_cascade(label="Arquivo", menu=file_menu)
file_menu.add_command(label="Abri Imagem", command=open_file)

# Cria o botão que chama a função convert()
bw_button = Button(toolbar_frame, text="Preto e Branco", command=convert)
bw_button.grid(row=0, column=0)

# Método que deixa o programa em loop
mainloop()