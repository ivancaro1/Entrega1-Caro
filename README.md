# Entrega1-Caro
First project delivery - Python CH

Esta primera entrega consiste en un ejemplo de e-commerce, con información para ver productos, agregar productos, chat para conversar con demás usuarios e información de los usuarios que han utilizado el chat.

### Navegación

* **AppCoder/inicio** página principal
*  **AppCoder/productos** información de los productos que están en la BD
*  **AppCoder/chat** centro de mensajes para agregar uno o ver los mensajes enviados
*  **AppCoder/cursoFormulario** para agregar un nuevo producto en la BD
*   **AppCoder/buscar** busca un producto
*   **AppCoder/infoUser** información de los usuarios que han utilizado el chat

### Configuración de folders
* __AppCoder__: la carpeta con la información de la aplicación

* __EntregaCoder__: carpeta con la información del proyecto

### EntregaCoder

* __urls__: - ***admin/*** ruta para acceder como admin
            - ***AppCoder/*** ruta de la aplicación

### AppCoder

* **models**: 
    - ***productos*** información del producto, donde:
        - title: es el nombre del producto
        - price: es el precio del producto
        - thumbnail: link con la imagen del producto, puedes buscar imagenes en https://www.iconfinder.com/

    - ***chat*** información del chat, donde:
        - user: nombre del usuario
        - message: mensaje del usuario
        - date: fecha de envío del mensaje

    - ***infoUsers*** información de usuarios que han utilizado el chat, donde:
        - user: nombre del usuario
        - lastmessagedate: fecha de envío del mensaje

* **forms**:
    - ***productoFormulario*** formulario para agregar un nuevo producto, donde:
        - title: es el nombre del producto
        - price: es el precio del producto
        - thumbnail: link con la imagen del producto, puedes buscar imagenes en https://www.iconfinder.com/
        
    - ***messageHub*** centro de mensajes, donde:
        - user: nombre del usuario
        - message: mensaje del usuario
