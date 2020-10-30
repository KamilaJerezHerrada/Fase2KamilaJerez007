from django.contrib import admin
from .models import Categoria
from .models import Producto
from .models import Pedidos
from .models import DetallePedido
from .models import Cliente

admin.site.register(Categoria)
admin.site.register(Producto)
admin.site.register(Pedidos)
admin.site.register(DetallePedido)
admin.site.register(Cliente)