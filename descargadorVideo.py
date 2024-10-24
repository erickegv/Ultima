import tkinter as tk
from PIL import Image, ImageTk
import yt_dlp
import subprocess

def descargar_video(url_video, carpeta_destino):
  if subprocess.call(['ffmpeg', '-version'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL) != 0:
        print("Instalando FFmpeg...")
        subprocess.call(['brew', 'install', 'ffmpeg'])

  ydl_opts = {
      'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
      'outtmpl': f'{carpeta_destino}/%(title)s.%(ext)s',
      'noplaylist': True,
      'nocheckcertificate': True,
      'ignoreerrors': True,
      'merge_output_format': 'mp4'
  }

  with yt_dlp.YoutubeDL(ydl_opts) as ydl:
      ydl.download([url_video])

def obtenerURL(): #Se hace una funcion antes de crear la ventana nose porque
    url_video = entrada.get() #desde antes de solicitar el dato ya se tiene planeado que se va hacer, obtenerlo
    descargar_video(url_video, carpeta_destino)
    nuevoValor= "Descarga completa"
    entrada.delete(0, tk.END) #ahora se elimina de inicio a fin lo que va haber en ña vañiable entrada
    entrada.insert(0, nuevoValor) #se inserta desde el inicio la variable que va decir lo que quieras

def limpiar():
    entrada.delete(0, tk.END)

carpeta_destino = "/Users/erickgonzalezvelazquez/Desktop/descargas_ytdlp/"

img = Image.open("/Users/erickgonzalezvelazquez/Desktop/descargadorVideo/meme.ico")
img = img.resize((32, 32))

ventana = tk.Tk()
icono = ImageTk.PhotoImage(img)
ventana.title("Descargador de Video")
ventana.wm_iconphoto(True, icono)
ventana.wm_attributes("-titlepath", "/Users/erickgonzalezvelazquez/Desktop/descargadorVideo/meme.ico")

miFrame= tk.Frame(ventana, width=50, height=50)
miFrame.pack()

entrada = tk.Entry(miFrame)
entrada.grid(row=0, column=1, pady=5, padx=5)

textoMostrado= tk.Label(miFrame, text="Pon tu URL")
textoMostrado.grid(row=0, column=0, pady=5, padx=5)

boton = tk.Button(miFrame, text="Descargar", command=obtenerURL)
boton.grid(row=1, column=1, pady=5, padx=5)

limpiarTexto = tk.Button(miFrame, text="limpiar", command=limpiar)
limpiarTexto.grid(row=1, column=0, pady=5, padx=5)

ventana.mainloop()