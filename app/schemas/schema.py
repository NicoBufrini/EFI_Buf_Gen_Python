from app import ma
from marshmallow import fields


class PublicacionEsquema(ma.Schema):
    id =  fields.Integer(dump_only=True)
    title = fields.String()
    content = fields.String()
    fechacreacion = fields.DateTime()
    user = fields.Integer()
    category = fields.Integer()

class ComentarioEsquema(ma.Schema):
    id =  fields.Integer(dump_only=True)
    coment =fields.String()
    fechacreacion = fields.DateTime()
    user = fields.Integer()
    post = fields.Integer()

class UsuarioEsquema(ma.Schema):
    id =  fields.Integer(dump_only=True)
    name = fields.String()
    correo = fields.String()
    password = fields.String()
    posts = fields.Nested(PublicacionEsquema, many=True)
    coments = fields.Nested(ComentarioEsquema,many=True)

class CategoriaEsquema(ma.Schema):
    id =  fields.Integer(dump_only=True)
    etiqueta = fields.String()
    posts =posts = fields.Nested(PublicacionEsquema, many=True)