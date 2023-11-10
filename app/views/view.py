from flask import (
    jsonify,
    render_template,
    request,
)

from app import app, db

from app.models.models import Usuario, Publicacion, Comentario, Categoria
from app.schemas.schema import UsuarioEsquema, PublicacionEsquema, ComentarioEsquema, CategoriaEsquema
from flask.views import MethodView


# Ruta principal de la aplicación
@app.route("/")
def inicio():
    return render_template("index.html")


# API para la entidad Usuario
class UsuarioApi(MethodView):
    def get(self, usuario_id=None):
        # Obtener todos los usuarios o uno específico por ID
        if usuario_id is None:
            usuarios = Usuario.query.all()
            usuarios_esquema = UsuarioEsquema().dump(usuarios, many=True)
            return jsonify(usuarios_esquema)
        usuario = Usuario.query.get(usuario_id)
        usuario_esquema = UsuarioEsquema().dump(usuario)
        return jsonify(usuario_esquema)

    def post(self):
        # Crear un nuevo usuario
        datos = request.get_json()
        nombre = datos.get("nombre")
        correo = datos.get("correo")
        contrasena = datos.get("contrasena")

        nuevo_usuario = Usuario(
            nombre=nombre,
            correo=correo,
            contrasena=contrasena,
        )
        db.session.add(nuevo_usuario)
        db.session.commit()

        return jsonify(MENSAJE=f"Se crea el usuario {nombre}")

    def put(self, usuario_id=None):
        # Actualizar información de un usuario por ID
        if usuario_id is None:
            return jsonify(MENSAJE=f"Retorna un ID para ver que se modificó")
        usuario = Usuario.query.get(usuario_id)

        datos = request.get_json()

        new_name_de_usuario = datos.get("new_name")
        new_user_password = datos.get("nueva_contrasena")

        usuario.nombre = new_name_de_usuario
        usuario.contrasena = new_user_password
        db.session.commit()

        usuario_esquema = UsuarioEsquema().dump(usuario)

        return jsonify(usuario_esquema)

    def delete(self, usuario_id=None):
        # Eliminar un usuario por ID
        if usuario_id is None:
            return jsonify(MENSAJE=f"Retorna un ID para saber qué eliminó.")
        usuario = Usuario.query.get(usuario_id)
        datos = request.get_json()

        # Elimino usuario
        db.session.delete(usuario)
        db.session.commit()
        return jsonify(Mensaje=f"El usuario {usuario_id} fue eliminado.")


# Registro URL para acceder a la clase
app.add_url_rule("/usuario", view_func=UsuarioApi.as_view("usuario"))
app.add_url_rule("/usuario/<usuario_id>", view_func=UsuarioApi.as_view("usuario_por_id"))


# API para la entidad Publicacion
class PublicacionApi(MethodView):
    def get(self, publicacion_id=None):
        # Obtener todas las publicaciones o una específica por ID
        if publicacion_id is None:
            publicaciones = Publicacion.query.all()
            publicaciones_esquema = PublicacionEsquema().dump(publicaciones, many=True)
            return jsonify(publicaciones_esquema)
        publicacion = Publicacion.query.get(publicacion_id)
        publicacion_esquema = PublicacionEsquema().dump(publicacion)
        return jsonify(publicacion_esquema)

    def post(self):
        # Crear una nueva publicación
        datos = request.get_json()
        titulo = datos.get("titulo")
        contenido = datos.get("contenido")
        usuario = datos.get("usuario")
        categoria = datos.get("categoria")

        nueva_publicacion = Publicacion(titulo=titulo, contenido=contenido, usuario=usuario, categoria=categoria)
        db.session.add(nueva_publicacion)
        db.session.commit()

        return jsonify(MENSAJE=f"Se hizo la publicación con el título: {titulo}")

    def put(self, publicacion_id=None):
        # Actualizar información de una publicación por ID
        if publicacion_id is None:
            return {"Mensaje": "Retorna un ID para saber qué actualizó."}
        publicacion = Publicacion.query.get(publicacion_id)

        datos = request.get_json()
        nuevo_titulo_de_publicacion = datos.get("titulo")
        nuevo_contenido_de_publicacion = datos.get("contenido")

        publicacion.titulo = nuevo_titulo_de_publicacion
        publicacion.contenido = nuevo_contenido_de_publicacion
        db.session.commit()

        publicacion_esquema = PublicacionEsquema().dump(publicacion)

        return jsonify(publicacion_esquema)

    def delete(self, publicacion_id=None):
        # Eliminar una publicación por ID
        if publicacion_id is None:
            return {"Mensaje": "Retorna un ID para saber qué eliminó."}
        publicacion = Publicacion.query.get(publicacion_id)
        # Elimino publicación
        db.session.delete(publicacion)
        db.session.commit()
        return jsonify(Mensaje=f"La publicación {publicacion_id} fue eliminada correctamente.")


# Registro URL para acceder a la clase
app.add_url_rule("/publicacion", view_func=PublicacionApi.as_view("publicacion"))
app.add_url_rule("/publicacion/<publicacion_id>", view_func=PublicacionApi.as_view("publicacion_por_id"))


# API para la entidad Comentario
class ComentarioApi(MethodView):
    def get(self, comentario_id=None):
        # Obtener todos los comentarios o uno específico por ID
        if comentario_id is None:
            comentarios = Comentario.query.all()
            comentarios_esquema = ComentarioEsquema().dump(comentarios, many=True)
            return jsonify(comentarios_esquema)
        comentario = Comentario.query.get(comentario_id)
        comentario_esquema = ComentarioEsquema().dump(comentario)
        return jsonify(comentario_esquema)

    def post(self):
        # Crear un nuevo comentario
        datos = request.get_json()
        contenido_comentario = datos.get("comentario")
        usuario = datos.get("usuario")
        publicacion = datos.get("publicacion")

        nuevo_comentario = Comentario(comentario=contenido_comentario, usuario=usuario, publicacion=publicacion)
        db.session.add(nuevo_comentario)
        db.session.commit()

        return jsonify(MENSAJE=f"Se hizo el comentario: {contenido_comentario}.")

    def put(self, comentario_id=None):
        # Actualizar contenido de un comentario por ID
        if comentario_id is None:
            return {"Mensaje": "Retorna un ID para saber qué actualizó."}
        comentario = Comentario.query.get(comentario_id)

        datos = request.get_json()
        nuevo_contenido_del_comentario = datos.get("comentario")

        comentario.comentario = nuevo_contenido_del_comentario
        db.session.commit()

        comentario_esquema = ComentarioEsquema().dump(comentario)

        return jsonify(comentario_esquema)

    def delete(self, comentario_id=None):
        # Eliminar un comentario por ID
        if comentario_id is None:
            return {"Mensaje": "Retorna un ID para saber qué eliminó."}
        comentario = Comentario.query.get(comentario_id)
        # Elimino comentario
        db.session.delete(comentario)
        db.session.commit()
        return jsonify(Mensaje=f"El comentario {comentario_id} fue eliminado correctamente.")


# Registro URL para acceder a la clase
app.add_url_rule("/comentario", view_func=ComentarioApi.as_view("comentario"))
app.add_url_rule("/comentario/<comentario_id>", view_func=ComentarioApi.as_view("comentario_por_id"))


# API para la entidad Categoria
class CategoriaApi(MethodView):
    def get(self, categoria_id=None):
        # Obtener todas las categorías o una específica por ID
        if categoria_id is None:
            categorias = Categoria.query.all()
            categorias_esquema = CategoriaEsquema().dump(categorias, many=True)
            return jsonify(categorias_esquema)
        categoria = Categoria.query.get(categoria_id)
        categoria_esquema = CategoriaEsquema().dump(categoria)
        return jsonify(categoria_esquema)

    def post(self):
        # Crear una nueva categoría
        datos = request.get_json()
        etiqueta = datos.get("etiqueta")

        nueva_categoria = Categoria(
            etiqueta=etiqueta,
        )
        db.session.add(nueva_categoria)
        db.session.commit()

        return jsonify(MENSAJE=f"Se hizo la categoría: {etiqueta}.")

    def put(self, categoria_id=None):
        # Actualizar contenido de una categoría por ID
        if categoria_id is None:
            return {"Mensaje": "Retorna un ID para saber qué actualizó."}
        categoria = Categoria.query.get(categoria_id)

        datos = request.get_json()
        nuevo_contenido_de_etiqueta = datos.get("etiqueta")

        categoria.etiqueta = nuevo_contenido_de_etiqueta
        db.session.commit()

        categoria_esquema = CategoriaEsquema().dump(categoria)

        return jsonify(categoria_esquema)

    def delete(self, categoria_id=None):
        # Eliminar una categoría por ID
        if categoria_id is None:
            return {"Mensaje": "Retorna un ID para saber qué eliminó"}
        categoria = Categoria.query.get(categoria_id)
        # Elimino categoría
        db.session.delete(categoria)
        db.session.commit()
        return jsonify(Mensaje=f"La categoría {categoria_id} fue eliminada correctamente.")


# Registro URL para acceder a la clase
app.add_url_rule("/categoria", view_func=CategoriaApi.as_view("categoria"))
app.add_url_rule(
    "/categoria/<categoria_id>", view_func=CategoriaApi.as_view("categoria_por_id")
)
