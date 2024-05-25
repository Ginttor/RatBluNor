from tkinter import*
import http.server
import threading
import os
import cgi
import requests
import psutil
#----------------------------------------
#py install auto-py-to-exe

diip="";UPLOAD_DIR = 'uploa';cant=0;server=False
connections = psutil.net_connections();lb=[""]
for conn in connections:
    p, c=conn.laddr;t=True
    for i in lb:
        if i==p:t=False;break
    if t==True:lb.append(p);print(p)
for i in lb:
    if 0<i.count("192"):diip=i;break
HY="""
<!DOCTYPE html>
<html lang="es"></html>
<html>
    <head>
        <style>
            @font-face {
                font-family: MiFuente;
                src: url('reculs/Themundayfreeversion-Regular.ttf') format('truetype');
            }
            .cat{
                background-color:#daf87d;
            }
            .chi{
                background-color: #f9ab16;
            }
            .cha{
                background-color: #6bc5c6;
            }
            button, div, input, p{
                font-family: MiFuente, Arial, sans-serif;
            }
            summary{
                border-bottom: 3px double black;
            }
        </style>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>RBN</title>
        <h1 style="color: #ffffff;">R̟a̟t̟B̟l̟u̟N̟o̟r̟</h1>
    </head>
    <body bgcolor="#252850">
        <details class="cat">
            <summary><h1>ＣＡＴＡＬＯＧＯ</h1></summary> 
            <div id="CC" align="center" width="500" height="500">
                ...
            </div> 
            <p>NO HAY NADA</p><!--TB-->
        </details><br>
        <details class="chi">
            <summary><h1>ＣＨＩＳＭＥＳ</h1></summary> 
            <ol>
                <<<>>>
            </ol>
        </details><br>
        <details class="cha">
            <summary><h1>Ｅｎｖｉａ ｕｎ ｐａｑｕｅｔｅ</h1></summary> 
            <div id="CC" align="center" width="500" height="500">
                ..>>>
            </div> 
        </details><br>
    </body>
<script>
    let mode = []//LDR...
        function CC(N) {document.getElementById('CC').innerHTML=mode[N]}
</script>
</html>
"""
reg=open("faross.html", "w",encoding='utf-8')
reg.write(HY)
reg.close()
                         
class mask(http.server.BaseHTTPRequestHandler):#BaseHTTPRequestHandler/SimpleHTTPRequestHandler
    def do_GET(self):
        if self.path == '/':
            self.path = '/faross.html'
        try:
            # Abre el archivo solicitado para leerlo
            with open(self.path[1:], 'rb') as file:
                content = file.read()
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(content)
        except FileNotFoundError:
            self.send_error(404, 'Archivo no encontrado: {}'.format(self.path))

    
    def do_POST(self):
        global cant
        # Analizar la solicitud y obtener los datos del archivo
        form = cgi.FieldStorage(
            fp=self.rfile,
            headers=self.headers,
            environ={'REQUEST_METHOD': 'POST'}
        )
        
        # Verificar si hay un archivo en la solicitud
        
        if "file" in form:
            if cant>0:
                file_item = form["file"]
                # Guardar el archivo en el directorio de destino
                with open(os.path.join(UPLOAD_DIR, file_item.filename), 'wb') as f:
                    f.write(file_item.file.read())
                
                # Responder con un mensaje de éxito
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(b"""
                                 <!DOCTYPE html>
                                <html lang="es"></html>
                                <html>
                                    <head>
                                        <style>
                                            @font-face {
                                                font-family: MiFuente;
                                                src: url('reculs/Themundayfreeversion-Regular.ttf') format('truetype');
                                            }
                                            .cat{
                                                background-color:#daf87d;
                                            }
                                            .chi{
                                                background-color: #76f4ff;
                                            }
                                            button, div, input, p{
                                                font-family: MiFuente, Arial, sans-serif;
                                            }
                                            summary{
                                                border-bottom: 3px double black;
                                            }
                                        </style>
                                        <meta charset="UTF-8">
                                        <meta name="viewport" content="width=device-width, initial-scale=1.0">
                                        <title>RBN</title>
                                        <h1 style="color: #ffffff;">nameee</h1>
                                    </head>
                                 <body bgcolor="#252850">
                                 <p style="color: #ffffff;">Archivo subido exitosamente</p>
                                 </body>
                                 </html>
                                 """)
                cant-=1
            else:
                print("No as permitido mandar mas archibos")
        else:
            # Responder con un mensaje de error si no se proporciona ningún archivo
            self.send_response(400)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b'Error: No se proporciono ningun archivo')

class ServerApp:
    def __init__(self, P):
        self.P = P
        self.P.title("RatBluNor")
        self.iTi = PhotoImage(file="reculs/rat_icon-icons.com_56335.png")
        self.TiT=Label(P,image=self.iTi, bg="#252850", fg="#ffffff", font=("Roman SD",24)).place(x="100", y="50")
        self.TiT=Label(P, text="R̟a̟t̟B̟l̟u̟N̟o̟r̟",bg="#252850", fg="#ffffff", font=("Roman SD",24)).place(x="250", y="40")
        self.server_status = False
        self.cart=StringVar();self.cart.set("...")
        self.ctel=Entry(self.P, textvariable=self.cart, fg="#daf87d", bg="#6bc5c6", border=0).place(x="0", y="0")
        self.reg=Button(self.P, text="⇟R",fg="#daf87d", bg="#6bc5c6", command = self.rgl, border=0).place(x="122", y="0")
        self.lis=Listbox(self.P, fg="#daf87d", bg="#6bc5c6",  width="32", height="17", border=0);self.lis.place(x="0", y="60")
        self.exam=Button(self.P, text="<o> examine",bg="#daf87d", command = self.examin, border=0).place(x="54", y="39")
        self.cc=StringVar();self.cc.set(str(cant))
        self.Pc=Frame();self.Pc.config(bg="#6bc5c6", width="91", height="120");self.Pc.place(x="194", y="90")
        self.faro=Button(self.Pc, text="Port",bg="#daf87d", command = self.faross, border=0);self.faro.place(x="8", y="4")
        self.cct=Label(self.Pc, textvariable=self.cc, fg="#00ff00",bg="#daf87d", border=0).place(x="24", y="36")
        self.maz=Button(self.Pc, text="+", command=self.au, bg="#daf87d", border=0).place(x="50", y="34")
        self.mmi=Button(self.Pc, text="-", command=self.mi, bg="#daf87d", border=0).place(x="4", y="34")
        self.alm=Button(self.Pc, text="[warehouse O]", bg="#daf87d", command = self.bod, border=0).place(x="4", y="64")
        self.alm=Button(self.Pc, text="[warehouse I]", bg="#daf87d", command = self.pyu, border=0).place(x="4", y="94")
        self.listbox_datos = Text(self.P, bg="#f9ab16", width=24, height=10, border=0)
        self.listbox_datos.place(x="0", y="340")
        self.pef=Button(self.P, text="Save changes",fg="#daf87d", bg="#f9ab16", command = self.nau, border=0).place(x="194", y="340")
        self.pef=Button(self.P, text="See ads ⁑",fg="#daf87d", bg="#f9ab16", command = self.vla, border=0).place(x="194", y="370")
        self.P.protocol("WM_DELETE_WINDOW", self.close_s)

    def au(self):
        global cant
        if cant < 100:cant+=5
        self.cc.set(str(cant))

    def rgl(self):
        if 0<self.cart.get().count("http://"):
            if 0<self.cart.get().count("-<-"):
                with open("agenda.txt", "r",encoding='utf-8') as ren:
                    ge=ren.readlines()
                est=False;cop=False
                for i in ge:
                    c=(i.replace("\n","")).split("-<-")
                    a=(self.cart.get().replace("\n","")).split("-<-")
                    if c[0]==a[0]:cop=True
                    if c[1]==a[1]:est=True
                    print("c",c,"|a",a,"-------------",cop,est)
                if est==False:
                    with open("agenda.txt", "a",encoding='utf-8') as ren:
                        if cop==True:
                            a=(self.cart.get().replace("\n","")).split("-<-")
                            ren.write("\n"+a[0]+str(len(ge))+"-<-"+a[1])
                        else:ren.write("\n"+self.cart.get())
                    self.cart.set("Nueba ruta wardada")
                else:self.cart.set("Ya esta registrado")
            else:
                with open("agenda.txt", "r",encoding='utf-8') as ren:
                    ge=ren.readlines()
                self.cart.set("n"+str(len(ge))+"-<-"+self.cart.get())
        else:self.cart.set("No hay ruta")

    def vla(self):
        mm="*Titulo*\n-Contenido.\nlink:_http://direccion.com\n+----------------------+\n"
        with open("woodBox.txt", "r",encoding='utf-8') as ren:
            ge=ren.read()
        self.listbox_datos.delete("1.0", "end");mm+=ge
        self.listbox_datos.insert(END,mm)

    def nau(self):
        if 0<self.listbox_datos.get("1.0", "end").count("+----------------------+\n") and 2<=self.listbox_datos.get("1.0", "end").count("*"):
            with open("woodBox.txt", "w",encoding='utf-8') as file:
                file.write(self.listbox_datos.get("1.0", "end").replace("*Titulo*\n-Contenido.\nlink:_http://direccion.com\n+----------------------+\n",""))

    def mi(self):
        global cant
        cant-=1
        if cant < 1:cant=0
        self.cc.set(str(cant))
    
    def faross(self):
        mm="";fm="";lu=os.listdir("pos")
        reg=open("faross.html", "w",encoding='utf-8')
        for i in lu:
            if 0<i.count(".rar"):fm+="r";mm+='`'+i+'<br>...<a href="pos/'+i+'" download>DESCARGAR</a>`,'
            if 0<i.count(".html"):fm+="h";mm+='`'+i+'<br><a href="'+"pos/"+i+'">'+i+'</a>...<a href="pos/'+i+'" download>DESCARGAR</a>`,'
            if 0<i.count(".txt") :fm+="t";mm+='`'+i+'<br><a href="'+"pos/"+i+'">'+i+'</a>...<a href="pos/'+i+'" download>DESCARGAR</a>`,'
            if 0<i.count(".webp"):fm+="j";mm+='`'+i+'<br><img src="'+"pos/"+i+'" alt="WEBP can not load" width="500" height="500"></img>...<a href="pos/'+i+'" >VER</a>`,'
            if 0<i.count(".gif") :fm+="g";mm+='`'+i+'<br><img src="'+"pos/"+i+'" alt="GIF can not load" width="500" height="500"></img>...<a href="pos/'+i+'" >VER</a>`,'
            if 0<i.count(".png") :fm+="p";mm+='`'+i+'<br><img src="'+"pos/"+i+'" alt="PNG can not load" width="500" height="500"></img>...<a href="pos/'+i+'" >VER</a>`,'
            if 0<i.count(".jpeg"):fm+="j";mm+='`'+i+'<br><img src="'+"pos/"+i+'" alt="JPEG can not load" width="500" height="500"></img>...<a href="pos/'+i+'" >VER</a>`,'
            if 0<i.count(".jpg") :fm+="j";mm+='`'+i+'<br><img src="'+"pos/"+i+'" alt="JPG can not load" width="500" height="500"></img>...<a href="pos/'+i+'" >VER</a>`,'
            if 0<i.count(".mp3") :fm+="3";mm+='`'+i+'<br><audio controls src="'+"pos/"+i+'" alt="MP3 can not load" width="500" height="500"></audio>...<a href="pos/'+i+'" >VER</a>`,'
            if 0<i.count(".mp4") :fm+="4";mm+='`'+i+'<br><video src="'+"pos/"+i+'" alt="MP4 can not load" controls  width="500" height="500"></video>...<a href="pos/'+i+'" >VER</a>`,'
            if 0<i.count(".mkv") :fm+="4";mm+='`'+i+'<br><video src="'+"pos/"+i+'" alt="MKV can not load" controls  width="500" height="500"></video>...<a href="pos/'+i+'" >VER</a>`,'
            if 0<i.count(".pdf") :fm+="f";mm+='`'+i+'<br><embed src="'+"pos/"+i+'" alt="PDF can not load" width="500" height="500"></embed>...<a href="pos/'+i+'" >VER</a>`,'
        HY2=HY.replace('let mode = []//LDR...', 'let mode = ['+mm+']//LDR...')
        mm='<table border="0" align="center"><tr>';x=0
        while x<len(lu):
            if fm[x]=="r":mm+='<button onclick="CC('+str(x)+')"><a href="#CC"><img src="reculs/rar_filetype_icon_177520.png" alt="I cant load" width="170" height="170"></a><br>'+str(x+1)+'</button>'
            if fm[x]=="h":mm+='<button onclick="CC('+str(x)+')"><a href="#CC"><img src="reculs/html_filetype_icon_177535.png" alt="I cant load" width="170" height="170"></a><br>'+str(x+1)+'</button>'
            if fm[x]=="t":mm+='<button onclick="CC('+str(x)+')"><a href="#CC"><img src="reculs/txt_filetype_icon_177515.png" alt="I cant load" width="170" height="170"></a><br>'+str(x+1)+'</button>'
            if fm[x]=="j":mm+='<button onclick="CC('+str(x)+')"><a href="#CC"><img src="reculs/jpg_filetype_icon_177533.png" alt="I cant load" width="170" height="170"></a><br>'+str(x+1)+'</button>'
            if fm[x]=="g":mm+='<button onclick="CC('+str(x)+')"><a href="#CC"><img src="reculs/gif_filetype_icon_177536.png" alt="I cant load" width="170" height="170"></a><br>'+str(x+1)+'</button>'
            if fm[x]=="p":mm+='<button onclick="CC('+str(x)+')"><a href="#CC"><img src="reculs/png_filetype_icon_177523.png" alt="I cant load" width="170" height="170"></a><br>'+str(x+1)+'</button>'
            if fm[x]=="3":mm+='<button onclick="CC('+str(x)+')"><a href="#CC"><img src="reculs/filetype_mp_icon_177528.png" alt="I cant load" width="170" height="170"></a><br>'+str(x+1)+'</button>'
            if fm[x]=="4":mm+='<button onclick="CC('+str(x)+')"><a href="#CC"><img src="reculs/filetype_mp_icon_177527.png" alt="I cant load" width="170" height="170"></a><br>'+str(x+1)+'</button>'
            if fm[x]=="f":mm+='<button onclick="CC('+str(x)+')"><a href="#CC"><img src="reculs/pdf_filetype_icon_177525.png" alt="I cant load" width="170" height="170"></a><br>'+str(x+1)+'</button>'
            x+=1
        mm+='</tr></table>'
        HY2=HY2.replace('<p>NO HAY NADA</p><!--TB-->', mm)
        HY2=HY2.replace('..>>>','<form action="http://'+diip+':8030/upload" method="post" enctype="multipart/form-data"><input type="file" name="file" multiple><input type="submit" value="Subir"></form>')
        with open("woodBox.txt", "r",encoding='utf-8') as ren:
            ge=ren.readlines()
            cab=False;mm=""
            for i in ge:
                if cab==True and 0<i.count("+----------------------+\n"):cab=False;mm+="</details></li>"
                if cab==True:
                    if i.count(":_"):
                        c=i.split(":_")
                        mm+='<br><a href="'+c[1]+'" target="_blank">'+c[0]+'</a>'
                    else:mm+="<br>"+i
                if cab==False and 2<=i.count("*"):cab=True;mm+="<li><details><summary><h3>"+i+"</h3></summary>"
        HY2=HY2.replace('<<<>>>', mm)
        reg.write(HY2)
        reg.close()
        print("Reescrito el <html>")
        if server==False:
            self.start_server()
            self.faro.config(text=">o< | ↻")
    
    def bod(self):
        os.startfile("pos")

    def pyu(self):
        os.startfile("uploa")

    def examin(self):
        self.lis.delete(0, END)
        reg=open("agenda.txt", "r",encoding='utf-8')
        r=reg.readlines()
        reg.close()
        for i in r:
            drr=i.split("-<-")
            try:
                response = requests.get(drr[1].replace("\n", ""))
                if response.status_code == 200:
                    print("Servidor activo de ",drr[0])
                    self.lis.insert(END, i)
                else:
                    print("Servidor inactivo de ", drr[0])
            except requests.exceptions.RequestException as e:
                print("Server no conectable de ", drr[0])

    def start_server(self):
        self.server_status = True
        self.server_thread = threading.Thread(target=self.run_server)
        self.server_thread.start()

    def close_s(self):
        if server==True:
            self.httpd.shutdown()
            print("Servidor HTTP detenido")
        print("Servidor cerrado.")
        self.P.destroy()

    def run_server(self,server_class=http.server.HTTPServer, handler_class=mask, port=8030):
        global server
        server=True
        self.cart.set("http://"+diip+":"+str(port))
        #os.startfile("faross.html")
        server_address = (diip, port)
        self.httpd = server_class(server_address, handler_class)
        #-------------------------------------------------------------------------
        print("Sirviendo", self.httpd.server_address)
        self.httpd.serve_forever()

if __name__ == "__main__":
    if not os.path.exists(UPLOAD_DIR):
        os.makedirs(UPLOAD_DIR)
    if not os.path.exists("pos"):
        os.makedirs("pos")
    try:
        with open("woodBox.txt", "r",encoding='utf-8') as reg:
            r=reg.readlines()
    except FileNotFoundError:
        with open("woodBox.txt", "w",encoding='utf-8') as reg:
            reg.write("*Anuncio*\n-Contenido.")
    try:
        with open("agenda.txt", "r",encoding='utf-8') as reg:
            r=reg.readlines()
    except FileNotFoundError:
        with open("agenda.txt", "w",encoding='utf-8') as reg:
            reg.write("")
    P=Tk()
    P.title("RatBluNor")
    P.config(bg="#252850")
    P.geometry("400x500")
    P.iconbitmap("reculs/rat_icon-icons.com_56335.ico")
    P.resizable(0,0)
    app = ServerApp(P)
    P.mainloop()
