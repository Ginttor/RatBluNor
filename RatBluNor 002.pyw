import random
import os
import shutil
import time
#----------------
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.clock import Clock
from kivy.uix.widget import Widget



def radi():
    m="";l="";mm="""
    <!DOCTYPE html>
<html lang="es"></html>
<html>
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>RBN</title>
        <style>
          body {
            background-color: #fffb005e;
            font-family: Arial, sans-serif;
          }
          h1,h3 {
            color: #7e7e7e;
          }
          
          /* Contenedor principal */
          .producto-container {
            display: flex;
            flex-wrap: wrap;
            justify-content: space-around;
            padding: 20px;
          }
          
          /* Estilo para cada tarjeta de video */
          .producto-card {
            background: #fff;
            border-radius: 8px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
            margin: 15px;
            width: 320px;
            transition: transform 0.3s ease;
          }
          
          .producto-card:hover {
            transform: scale(1.03);
          }
          
          /* Miniatura del video */
          .producto-thumbnail {
            width: 100%;
            height: 180px;
            border-top-left-radius: 8px;
            border-top-right-radius: 8px;
            object-fit: cover;
          }
          
          /* Título del video */
          .producto-title {
            background-color: #38c1eb;
            font-size: 18px;
            font-weight: bold;
            margin: 0 0 10px;
          }
          
          /* Descripción del video */
          .producto-description {
            font-size: 14px;
            color: #606060;
            margin: 0;
          }
          

        .search-container {
            text-align: center;
        }
        .search-bar {
            width: 300px;
            padding: 10px;
            margin-bottom: 15px;
        }
        .quick-buttons {
            display: flex;
            gap: 10px;
        }
        .quick-buttons button {
            padding: 10px 15px;
            cursor: pointer;
            background-color: #007BFF;
            border: none;
            color: white;
            border-radius: 5px;
            transition: background-color 0.3s ease;
        }
        .quick-buttons button:hover {
            background-color: #0056b3;
        }
          </style>
        <h1>RatBluNor</h1>
    </head>
    <body>
        <div style="background-color:#daf87d;"id="elemento">
            <h3>Productos</h3>
            <input type="text" id="search" class="search-bar" placeholder="Buscar..." onkeyup="filterList()">
            <button onclick="abrirEnlaceAleatorio()" color="#daf87d">SINTONIZAR</button>
            <div class="quick-buttons">
              <button onclick="setSearchText('');filterList();cambiarColor('#daf87d')">Borrar</button>
              <button onclick="setSearchText('img');filterList();cambiarColor('#ffffff')">Imagen</button>
              <button onclick="setSearchText('vid');filterList();cambiarColor('#000000')">Video</button>
              <button onclick="setSearchText('aud');filterList();cambiarColor('#38c1eb')">Audio</button>
              <button onclick="setSearchText('txt');filterList();cambiarColor('#f8d77d')">Texto</button>
          </div>
            <div id="item-list" class="producto-container">
<!--EEEEEEEEEEEEEEEEEEEEEEEE-->

            </div>,,,
        </div>
    </body>
    <script>
        // Obtener todos los elementos de video y audio
        const mediaElements = document.querySelectorAll('video, audio');
        // Añadir evento a cada elemento
        mediaElements.forEach(element => {
            element.addEventListener('play', () => {
                // Pausar todos los elementos excepto el que se está reproduciendo
                mediaElements.forEach(el => {
                    if (el !== element) {
                        el.pause();
                    }
                });
            });
        });
        function cambiarColor(color) {
              document.getElementById('elemento').style.backgroundColor = color;
          }
        function setSearchText(text) {
          document.getElementById('search').value = text;
          }
        function filterList() {
            // Obtener el valor del campo de búsqueda y convertirlo a minúsculas
            let searchInput = document.getElementById("search").value.toLowerCase();
            
            // Obtener la lista de elementos
            let items = document.getElementById("item-list").getElementsByTagName("div");

            // Iterar sobre cada elemento y mostrar/ocultar según coincida con la búsqueda
            for (let i = 0; i < items.length; i++) {
                let item = items[i].textContent || items[i].innerText;

                // Mostrar el elemento si coincide con la búsqueda
                if (item.toLowerCase().indexOf(searchInput) > -1) {
                    items[i].style.display = "";
                } else {
                    // Ocultar el elemento si no coincide
                    items[i].style.display = "none";
                }
            }
        }
    const checkboxes = document.querySelectorAll('input[name="opcion"]');

    // Limitar a 3 selecciones
    checkboxes.forEach(checkbox => {
      checkbox.addEventListener('change', function () {
        const checkedCount = document.querySelectorAll('input[name="opcion"]:checked').length;
        if (checkedCount > 100) {
          this.checked = false; // Desmarca el último seleccionado
        }
      });
    });
    // Array de enlaces
        const enlaces = [
            //--LINKKKKSSSS--//
        ];

        // Función para abrir un enlace aleatorio
        function abrirEnlaceAleatorio() {
            const indiceAleatorio = Math.floor(Math.random() * enlaces.length);
            window.location.href = enlaces[indiceAleatorio];
        }
    </script>
</html>
    """
    pa={
        "lin":"""<div class='producto-card'><h4 class='producto-title'><a href='{{DIRECCION}}'>{{NOMBRE}}</a></h4><p class='producto-thumbnail'>{{...}}</p></div>""",
    }
    bb=[]
    with open("radio.txt", "r",encoding='utf-8') as file:
        bb=file.readlines()
    for i in bb:
        l+="'"+i.split("!!")[0]+"',"
        m+=pa["lin"].replace("{{DIRECCION}}",i.split("!!")[0]).replace("{{NOMBRE}}",i.split("!!")[0]).replace("{{...}}",i.split("!!")[1])
    mm=mm.replace("//--LINKKKKSSSS--//",l).replace("<!--EEEEEEEEEEEEEEEEEEEEEEEE-->",m)
    with open("radio.html", "w",encoding='utf-8') as file:
        file.write(mm)
    print(mm)
    os.system("xdg-open radio.html")
def agrg(l,c):
    tl = os.path.getmtime(l)
    tc = os.path.getmtime(l)
    print("Última modificación:", time.ctime(tl), time.ctime(tc))
def reuv(k,b2,b1):
    for a in os.listdir(b1.replace('\n', '')):
        for i in k.split(","):
            if a.count("."+i):
                shutil.move(b1.replace('\n', '')+"/"+a.replace('\n', ''),b2.replace('\n', '')+"/"+a.replace('\n', ''))
                print("-Archibo ",a," reuvicado")
def prss(p,c):
    mm="""
    <!DOCTYPE html>
<html lang="es"></html>
<html>
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>RBN</title>
        <style>
          body {
            background-color: #fffb005e;
            font-family: Arial, sans-serif;
          }
          h1,h3 {
            color: #7e7e7e;
          }
          
          /* Contenedor principal */
          .producto-container {
            display: flex;
            flex-wrap: wrap;
            justify-content: space-around;
            padding: 20px;
          }
          
          /* Estilo para cada tarjeta de video */
          .producto-card {
            background: #fff;
            border-radius: 8px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
            margin: 15px;
            width: 320px;
            transition: transform 0.3s ease;
          }
          
          .producto-card:hover {
            transform: scale(1.03);
          }
          
          /* Miniatura del video */
          .producto-thumbnail {
            width: 100%;
            height: 180px;
            border-top-left-radius: 8px;
            border-top-right-radius: 8px;
            object-fit: cover;
          }
          
          /* Título del video */
          .producto-title {
            background-color: #38c1eb;
            font-size: 18px;
            font-weight: bold;
            margin: 0 0 10px;
          }
          
          /* Descripción del video */
          .producto-description {
            font-size: 14px;
            color: #606060;
            margin: 0;
          }
          

        .search-container {
            text-align: center;
        }
        .search-bar {
            width: 300px;
            padding: 10px;
            margin-bottom: 15px;
        }
        .quick-buttons {
            display: flex;
            gap: 10px;
        }
        .quick-buttons button {
            padding: 10px 15px;
            cursor: pointer;
            background-color: #007BFF;
            border: none;
            color: white;
            border-radius: 5px;
            transition: background-color 0.3s ease;
        }
        .quick-buttons button:hover {
            background-color: #0056b3;
        }
          </style>
        <h1>RatBluNor</h1>
    </head>
    <body>
        <div style="background-color:#daf87d;"id="elemento">
            <h3>Productos</h3>
            <input type="text" id="search" class="search-bar" placeholder="Buscar..." onkeyup="filterList()">
            <button id="descargarBtn" color="#daf87d">PEDIR</button>
            <div class="quick-buttons">
              <button onclick="setSearchText('');filterList();cambiarColor('#daf87d')">Borrar</button>
              <button onclick="setSearchText('img');filterList();cambiarColor('#ffffff')">Imagen</button>
              <button onclick="setSearchText('vid');filterList();cambiarColor('#000000')">Video</button>
              <button onclick="setSearchText('aud');filterList();cambiarColor('#38c1eb')">Audio</button>
              <button onclick="setSearchText('txt');filterList();cambiarColor('#f8d77d')">Texto</button>
          </div>
<!--EEEEEEEEEEEEEEEEEEEEEEEE-->

            </div>,,,
        </div>
    </body>
    <script>
        // Obtener todos los elementos de video y audio
        const mediaElements = document.querySelectorAll('video, audio');
        // Añadir evento a cada elemento
        mediaElements.forEach(element => {
            element.addEventListener('play', () => {
                // Pausar todos los elementos excepto el que se está reproduciendo
                mediaElements.forEach(el => {
                    if (el !== element) {
                        el.pause();
                    }
                });
            });
        });
        function cambiarColor(color) {
              document.getElementById('elemento').style.backgroundColor = color;
          }
        function setSearchText(text) {
          document.getElementById('search').value = text;
          }
        function filterList() {
            // Obtener el valor del campo de búsqueda y convertirlo a minúsculas
            let searchInput = document.getElementById("search").value.toLowerCase();
            
            // Obtener la lista de elementos
            let items = document.getElementById("item-list").getElementsByTagName("div");

            // Iterar sobre cada elemento y mostrar/ocultar según coincida con la búsqueda
            for (let i = 0; i < items.length; i++) {
                let item = items[i].textContent || items[i].innerText;

                // Mostrar el elemento si coincide con la búsqueda
                if (item.toLowerCase().indexOf(searchInput) > -1) {
                    items[i].style.display = "";
                } else {
                    // Ocultar el elemento si no coincide
                    items[i].style.display = "none";
                }
            }
        }
    const checkboxes = document.querySelectorAll('input[name="opcion"]');
    const descargarBtn = document.getElementById('descargarBtn');

    // Limitar a 3 selecciones
    checkboxes.forEach(checkbox => {
      checkbox.addEventListener('change', function () {
        const checkedCount = document.querySelectorAll('input[name="opcion"]:checked').length;
        if (checkedCount > 100) {
          this.checked = false; // Desmarca el último seleccionado
        }
      });
    });

    // Descargar archivo con opciones marcadas
    descargarBtn.addEventListener('click', function () {
      const selectedOptions = Array.from(document.querySelectorAll('input[name="opcion"]:checked'))
        .map(cb => cb.value);
      
      const blob = new Blob([selectedOptions.join('\\n')], { type: 'text/plain' });
      const url = URL.createObjectURL(blob);
      const a = document.createElement('a');
      a.href = url;
      a.download = '{{-<o>-}}.txt';
      a.click();
      URL.revokeObjectURL(url);
    });
    </script>
</html>
    """
    m="";n=c.split("/")[len(c.split("/"))-1].replace("\n","")
    pa={
        "cchh":"""<div class='producto-card'><li><label><input type="checkbox" name="opcion" value="{{NOMBRE}}">{{NOMBRE}}</label></li></div>""",
        ".txt":"""<div class='producto-card'><h4 class='producto-title'><a href='{{DIRECCION}}'>{{NOMBRE}}</a></h4><p class='producto-thumbnail'>{{...}}</p></div>""",
        ".png":"""<div class='producto-card'><h4 class='producto-title'><a href='{{DIRECCION}}'>{{NOMBRE}}</a></h4><img   class='producto-thumbnail'src='{{DIRECCION}}'/><p class='producto-description'>{{...}}</p></div>""",
        ".mp4":"""<div class='producto-card'><h4 class='producto-title'><a href='{{DIRECCION}}'>{{NOMBRE}}</a></h4><video class='producto-thumbnail'src='{{DIRECCION}}'type='video/mp4'controls></video><p class='producto-description'>{{...}}</p></div>""",
        ".mp3":"""<div class='producto-card'><h4 class='producto-title'><a href='{{DIRECCION}}'>{{NOMBRE}}</a></h4><audio src='{{DIRECCION}}'type='audio/mp3'controls></audio><p class='producto-description'>{{...}}</p></div>"""
    }
    bb=[];pp=p.split("/")
    x=0;ppp=""
    while x<len(pp)-1:
        ppp+=pp[x]+"/"
        x+=1
    try:
        os.mkdir(ppp+"/"+n)
        print("Directorio creado exitosamente")
    except FileExistsError:
        print("El directorio ya existe")
    if   os.path.isfile((ppp+"/"+n+"/"+n+".txt").replace("//","/")) and     os.path.isfile((ppp+"/"+n+"/"+n+" (1).txt").replace("//","/")):
        with open((ppp+"/"+n+"/"+n+" (1).txt").replace("//","/"), "r",encoding='utf-8') as file:
            bb=file.readlines()
        for i in os.listdir(ppp+"/"+n):
            os.remove(ppp+"/"+n+"/"+i)
        mimmmmm=""
        for i in bb:
            if i!="\n":mimmmmm+=i+"\n"
        with open((ppp+"/"+n+"/"+n+".txt").replace("//","/"), "w",encoding='utf-8') as file:
            file.write(mimmmmm)
        print("!!--borrando")
    elif os.path.isfile((ppp+"/"+n+"/"+n+".txt").replace("//","/")) and not os.path.isfile((ppp+"/"+n+"/"+n+" (1).txt").replace("//","/")):
        with open((ppp+"/"+n+"/"+n+".txt").replace("//","/"), "r",encoding='utf-8') as file:
            bb=file.readlines()

    for i in os.listdir(c.replace("\n","")):
        vl=False
        for y in bb:
            if i.count(y.replace("\n","")) and y!="\n":
                vl=True;break
        if vl:
            if i.count(".txt"):
                r=""
                with open(c.replace("\n","")+"/"+i, "r",encoding='utf-8') as file:
                    r=file.read()
                r=r.replace("\n","<br>")
                m+=pa[".txt"].replace("{{DIRECCION}}",i).replace("{{NOMBRE}}","txt_"+i.split(".")[0]).replace("{{...}}",r)
                print("archibo de texto: ",i)
                if not os.path.isfile((ppp+"/"+n+"/"+i).replace("//","/")):
                    shutil.copy(c.replace("\n","")+"/"+i, (ppp+"/"+n+"/"+i).replace("//","/"))
            if i.count(".gif") or i.count(".webp") or i.count(".jpeg") or i.count(".png"):
                m+=pa[".png"].replace("{{DIRECCION}}",i).replace("{{NOMBRE}}","img_"+i.split(".")[0])
                print("archibo de imagen: ",i)
                if not os.path.isfile((ppp+"/"+n+"/"+i).replace("//","/")):
                    shutil.copy(c.replace("\n","")+"/"+i, (ppp+"/"+n+"/"+i).replace("//","/"))
            if i.count(".mp4"):
                m+=pa[".mp4"].replace("{{DIRECCION}}",i).replace("{{NOMBRE}}","vid_"+i.split(".")[0])
                print("archibo de video: ",i)
                print("!!--",c.replace("\n","")+"/"+i," = ",(ppp+"/"+n+"/"+i).replace("//","/"))
                if not os.path.isfile((ppp+"/"+n+"/"+i).replace("//","/")):
                    shutil.copy(c.replace("\n","")+"/"+i, (ppp+"/"+n+"/"+i).replace("//","/"))
            if i.count(".mp3"):
                m+=pa[".mp3"].replace("{{DIRECCION}}",i).replace("{{NOMBRE}}","aud_"+i.split(".")[0])
                print("archibo de audio: ",i)
                if not os.path.isfile((ppp+"/"+n+"/"+i).replace("//","/")):
                    shutil.copy(c.replace("\n","")+"/"+i, (ppp+"/"+n+"/"+i).replace("//","/"))
        else:
            m+=pa["cchh"].replace("{{NOMBRE}}",i)
    mm=mm.replace("<!--EEEEEEEEEEEEEEEEEEEEEEEE-->",m)
    mm=mm.replace("{{-<o>-}}",n)
    with open(ppp+"/"+n+"/"+n+".html", "w",encoding='utf-8') as file:
        file.write(mm)
    print("<la presentasion",n,"se a creado>")
#------------------------------------------------
ctt=os.listdir("ctt")
print(ctt)
def rata():
    uv=""
    io=""
    ss=""
    md=""
    mc=""
    ma=""
    ms=""
    ct=""
    contttr=""
    for e in ctt:
        with open("ctt/"+e, "r",encoding='utf-8') as reg:
            r=reg.readlines()
            uv=r[0].replace("\n","").split("][");print("uvicasiones a revizar:",uv)
            io=r[1].replace("\n","").split("=")[0]
            ss=r[1].split("=")[1].replace("\n","").split("][");print("imbolucrados en el trato:",io," y ",ss)
            md=r[2].replace("\n","").split("][");print("marcadores de destinatarios:",md)
            mc=r[3].replace("\n","").split("][");print("marcadores de contenido:",mc)
            ma=r[4].replace("\n","").split("][");print("marcador de autor:",ma)
            ms=r[5].replace("\n","").split("][");print("marcador de separador:",ms)
            ct=int(r[6]);print("usos",r[6])
            contttr=r
        r=""
        y=0
        while y<len(uv):
            with open(uv[y], "r",encoding='utf-8') as reg:
                r=reg.read()
            x=0;b=True;md0="";mc0=""
            while x<len(r):
                if b:
                    for i in md:
                        if r[x]==i:md0=x;b=False
                x+=1
            x=md0+1;b=True
            while x<len(r):
                if b:
                    for i in mc:
                        if r[x]==i:mc0=x;b=False
                x+=1
            def cct(p,i,f):
                mm=""
                x=i+1
                while x<f:
                    mm+=p[x]
                    x+=1
                return mm
            destt=cct(r,md0,mc0)
            print("destinatario:",destt)
            x=mc0+1;b=True
            while x<len(r):
                if b:
                    for i in ma:
                        if r[x]==i:ma0=x;b=False
                x+=1
            cont=cct(r,mc0,ma0)
            print("contenido:",cont)
            x=ma0+1;b=True
            while x<len(r):
                if b:
                    for i in ma:
                        if r[x]==i:ma0=x;b=False
                x+=1
            blo=False
            if ss.count("t"):print("YO OIGO TODE DE TODOS");blo=True
            for i in ss:
                if destt==io and cct(r,ma0,ma0)==i:print("SI TE CONOSCO");blo=True
            if blo:
                for i in ms:
                    if cont.count(i):
                        cont=cont.split(i)
                        break
                print("cont:",cont)
                x=7
                while x<len(contttr):
                    for i in cont:
                        if contttr[x].count(":") and contttr[x].split(":")[0].count("*"+i):
                            print("operasion pedida:",contttr[x])
                            if   contttr[x].split(":")[1]=="prss":prss(uv[y],contttr[x].split(":")[2])
                            elif contttr[x].split(":")[1]=="agrg":agrg(contttr[x].split(":")[2],contttr[x].split(":")[3])
                            elif contttr[x].split(":")[1]=="reuv":reuv(contttr[x].split(":")[2],contttr[x].split(":")[3],contttr[x].split(":")[4])
                    x+=1
            y+=1
#------------------------------------------------

class ContadorApp(App):
    def build(self):
        radi()
        # Layout principal horizontal
        layout = BoxLayout(orientation='horizontal', padding=10, spacing=10)


        self.contador = 0
        self.contador_activo = False


        # Sección izquierda: mensaje
        left_layout = BoxLayout(orientation='vertical', size_hint=(0.7, 1))
        self.contador_label = Label(
            text="Hello World",
            font_size=48,
            halign='center',
            valign='middle'
        )
        self.contador_label.bind(size=self.contador_label.setter('text_size'))  # Ajustar texto al tamaño
        left_layout.add_widget(self.contador_label)
        left_layout.add_widget(Widget())  # Espaciador flexible
        layout.add_widget(left_layout)


        # Sección izquierda: mensaje
        right_layout = BoxLayout(orientation='vertical', size_hint=(0.7, 1))
        self.boton = Button(text="Iniciar/Reiniciar", font_size=32)
        self.boton.bind(size=self.boton.setter('text_size'))  # Ajustar texto al tamaño
        right_layout.add_widget(self.boton)
        self.pluss = Button(text="/\>", font_size=32,halign='center')
        self.pluss.bind(size=self.pluss.setter('text_size'))  # Ajustar texto al tamaño
        right_layout.add_widget(self.pluss)
        self.inf_label = Label(text="Hello World",font_size=20,halign='center',valign='middle')
        self.inf_label.bind(size=self.inf_label.setter('text_size'))  # Ajustar texto al tamaño
        right_layout.add_widget(self.inf_label)
        self.menou = Button(text="<\/", font_size=32,halign='center')
        self.menou.bind(size=self.menou.setter('text_size'))  # Ajustar texto al tamaño
        right_layout.add_widget(self.menou)
        right_layout.add_widget(Widget())  # Espaciador flexible
        layout.add_widget(right_layout)


        self.boton.bind(on_press=self.iniciar_reiniciar_contador)


        return layout

    def iniciar_reiniciar_contador(self, instance):
        if not self.contador_activo:
            self.contador_activo = True
            self.boton.text = "Detener"
            Clock.schedule_interval(self.actualizar_contador, 1)  # Actualiza cada segundo
        else:
            self.contador_activo = False
            self.boton.text = "Iniciar/Reiniciar"
            Clock.unschedule(self.actualizar_contador)
            self.contador = 0
            self.contador_label.text = str(self.contador)

    def actualizar_contador(self, dt):
        rata()
        self.contador += 1
        self.contador_label.text = str(self.contador)

if __name__ == '__main__':
    ContadorApp().run()   