### código inspirado no tutorial https://www.youtube.com/watch?v=NI9LXzo0UY0&ab_channel=developedbyed ###

# bibliotecas que foram utilizadas
import tkinter
import customtkinter
from pytube import YouTube

# função para fazer o download
def Dowloading(media):
    media.download()
    finishLabel.configure(text="Download foi concluido!", text_color="green")

def startDownload():
    try:
        # sabendo qual é a escolha do usuario
        current_state = combobox.get()
        
        # pegando o link  e criando objeto da biblioteca pytube
        ytLink = link.get()
        ytObject = YouTube(ytLink, on_progress_callback=on_progress)
        
        # comparando com cada estado
        match current_state:
            case "Video: Highest Quality":
                media = ytObject.streams.get_highest_resolution()
                Dowloading(media)
            case "Music: Highest Quality":
                media = ytObject.streams.get_audio_only(subtype="mp4")
                Dowloading(media)
            case _:
                print("Escolha uma opção")
    except:
        finishLabel.configure(text="Invalid link!", text_color="red")

# calculos muito doidos para ter a porcentagem da barra de progresso 🤓
def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_of_completion = bytes_downloaded / total_size * 100
    per = str(int(percentage_of_completion))
    pPercentage.configure(text=per + '%')
    pPercentage.update()
    # barra de progresso
    progressBar.set(float((percentage_of_completion) / 100))


# defininfo a cor da interface
customtkinter.set_appearance_mode("System")

# criando objeto do ctk
app = customtkinter.CTk()
app.geometry("720x480")
app.title("Pirataria não é crime, crime é coisa de carioca!")

# adicionando titulo e outros elementos de UI
title = customtkinter.CTkLabel(app, text="Insira a url do vídeo")
title.pack(padx=10, pady=10)

# link inputs
url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=500, height=40, textvariable=url_var)
link.focus()
link.pack()

# texto de feedback, se o download foi efetuado ou falhou
finishLabel = customtkinter.CTkLabel(app, text="")
finishLabel.pack()

# Caixa de escolha
combobox = customtkinter.CTkComboBox(app,
                                     values=["Video: Highest Quality",
                                             "Music: Highest Quality"],
                                     width=200)
combobox.pack()

# porcentagem de progresso
pPercentage = customtkinter.CTkLabel(app, text="0%")
pPercentage.pack()

# mostrando a barra de progresso
progressBar = customtkinter.CTkProgressBar(app, width=400)
progressBar.set(0)
progressBar.pack(padx=10, pady=10)

# botao de download
download = customtkinter.CTkButton(app, text="Download", command=startDownload)
download.pack(padx=10, pady=10)

# loop para o aplicativo ficar aberto
app.mainloop()