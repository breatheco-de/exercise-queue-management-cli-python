# ![alt text](https://assets.breatheco.de/apis/img/images.php?blob&random&cat=icon&tags=breathecode,32) Queue Management System CLI


Creemos un sistema de espera: Los sistemas de espera o queue system son muy usados en las Instituciones Gubernamentales, aeropuertos, bancos y muchos otros lugares que buscan organizar el táfico entrante.

Los sistemas de espera también pueden usarse para equiparar la carga en varias aplicaciones como:
- Establecer prioridades en las solicitudes entrantes de los servidores web
- Inmigración y aplicaciones a visas que requieren de prioridad.
- Paquetes Network.
- etc.

Una cola es solo una lista de elementos que debe ser procesada en un orden en particular: FIFO o FILO

Hoy vamos a construir un Sistema de cola (o espera) con enfoque FIFO para los restaurantes: Si llega un nuevo cliente al restaurante, se añade su teléfono a la cola, cuando se hora se sentarse a la mesa, el cliente será notificado por email.


## 🌱  Cómo iniciar este proyecto

Este proyecto viene con los archivos necesarios para empezar a trabajar, pero tienes dos opciones para empezar:

a) Abrir este link con Gitpod (recomendada) en tu navegador: https://gitpod.io#https://github.com/breatheco-de/exercise-queue-management-cli-python

b) Clonar este repositorio localmente en tu computador:
```sh
$ git clone https://github.com/breatheco-de/exercise-queue-management-cli-python
```

2. Intalar las dependencias de los paquetes con el comando`$ pipenv install`

3. Ingresar al entorno con el comando `$ pipenv shell`

4. Puedes ejecutar tu proyecto con el comando `$ python src/app.py`

💡 Importante: Recuerda actualizar el `remote` del proyecto con el de tu repositorio usando `git remote set-url origin <your new url>`, y luego guardar tu código en tu nuevo repositorio usando `add`, `commit` y `push`.
 
## 📝 Instrucciones

 ¡Empieza a codificar! Actualiza el archivo app.py para que el usuario pueda gestionar o manejar un cola simple: 
 
 - Añadir a una persona, 
 - Eliminar a una persona, de quien es el turno (cola):
 - La aplicación también tiene que exportar la cola a un archivo llamado `queue.json`.
 - La aplicación debe integrar la API twilio para enviarle un un SMS cada vez que un número de teléfono salga de la lista de espera (cola)
 - Usa la siguiente estructura de datos para implementar la cola:

```python
class Queue:

    def __init__(self, mode, current_queue=[]):
        self.queue = current_queue
        # dependiendo del the _mode, la cola debe comportarse FIFO o FILO
        if mode is None:
            raise "Please specify a queue mode FIFO or LIFO"
        else:
            self.mode = mode
    
    def enqueue(self, item):
        pass
    def dequeue(self):
        pass
    def get_queue(self):
        pass
    def size(self):
        return len(self.queue) 
```
## Ejemplo de flujo de trabajo

1. La CLI muestra el menú y el usuario selecciona la opción para agregar "Bob" a la cola.
2. La aplicación anuncia a Bob y notifica la confirmación en la terminal y debe decir cuántas personas hay frente a él en la línea.
3. El sistema ahora muestra el menú (comienza de nuevo) esperando que el usuario elija otra opción.
4. Si el usuario elige la opción de eliminar de la cola, la siguiente persona en la cola se elimina y se muestra un mensaje de confirmación.
5. El usuario debe recibir un SMS a la hora de comer.
6. Si el usuario elige ver el estado completo de la cola, se imprime una lista de todos con su posición respectiva en la cola.
7. Si el usuario elige exportar la cola completa, se crea un archivo JSON con una lista de todos.


## 📖 Fundamentos

Este ejercicio te hará practicar los siguientes fundamentos:

- Ejecución de archivos de Python desde la línea de comandos.
- Obtenga la entrada del usuario desde la línea de comando.
- Loops, condicionales y funciones.
- Uso de archivos de texto sin formato para almacenar datos.
- Estructuras de datos complejas.
- Cola (FIFO vs FILO)
- SMS.
