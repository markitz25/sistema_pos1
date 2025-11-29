"""
Patrón Singleton para la configuración del Sistema POS
Gestiona configuraciones globales del sistema de forma centralizada
"""
from decimal import Decimal


class ConfiguracionSistema:
    """
    Singleton para gestionar la configuración global del sistema POS
    
    Responsabilidades:
    - Gestionar tasa de IVA
    - Configurar moneda y formato
    - Definir límites y validaciones
    - Almacenar información del negocio
    """
    
    _instance = None
    _initialized = False
    
    def __new__(cls):
        """
        Implementación del patrón Singleton
        Garantiza una única instancia de configuración
        """
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def __init__(self):
        """Inicializar configuración solo una vez"""
        if not self._initialized:
            self._cargar_configuracion_default()
            ConfiguracionSistema._initialized = True
    
    def _cargar_configuracion_default(self):
        """Cargar valores por defecto de configuración"""
        # Configuración de impuestos
        self.tasa_iva = Decimal('0.19')  # 19% IVA en Colombia
        self.incluir_iva = True
        
        # Configuración de moneda
        self.moneda = 'COP'
        self.simbolo_moneda = '$'
        self.separador_miles = ','
        self.separador_decimales = '.'
        self.decimales = 2
        
        # Información del negocio
        self.nombre_negocio = 'Sistema POS'
        self.nit = '900.123.456-7'
        self.direccion = 'Calle Principal #123'
        self.telefono = '+57 300 123 4567'
        self.email = 'ventas@sistemapos.com'
        self.sitio_web = 'www.sistemapos.com'
        
        # Configuración de ventas
        self.descuento_maximo_porcentaje = Decimal('50.00')
        self.stock_minimo_alerta = 5
        self.permitir_ventas_sin_stock = False
        
        # Configuración de facturación
        self.prefijo_factura = 'FAC'
        self.resolucion_dian = '18764001234567'
        self.fecha_resolucion = '2024-01-01'
        self.rango_inicial = 1
        self.rango_final = 10000
        
        # Configuración de reportes
        self.formato_fecha = '%d/%m/%Y'
        self.formato_hora = '%I:%M %p'
        self.formato_fecha_hora = '%d/%m/%Y %I:%M %p'
    
    # ==================== MÉTODOS DE IMPUESTOS ====================
    
    def calcular_iva(self, subtotal):
        """
        Calcular IVA sobre un subtotal
        
        Args:
            subtotal: Valor base para calcular IVA
            
        Returns:
            Decimal: Valor del IVA
        """
        if not self.incluir_iva:
            return Decimal('0.00')
        return subtotal * self.tasa_iva
    
    def calcular_total_con_iva(self, subtotal):
        """
        Calcular total incluyendo IVA
        
        Args:
            subtotal: Valor base
            
        Returns:
            Decimal: Total con IVA incluido
        """
        iva = self.calcular_iva(subtotal)
        return subtotal + iva
    
    def cambiar_tasa_iva(self, nueva_tasa):
        """
        Cambiar la tasa de IVA del sistema
        
        Args:
            nueva_tasa: Nueva tasa de IVA (ejemplo: 0.19 para 19%)
        """
        if not isinstance(nueva_tasa, Decimal):
            nueva_tasa = Decimal(str(nueva_tasa))
        
        if nueva_tasa < 0 or nueva_tasa > 1:
            raise ValueError("La tasa de IVA debe estar entre 0 y 1")
        
        self.tasa_iva = nueva_tasa
        return True
    
    # ==================== MÉTODOS DE FORMATO ====================
    
    def formatear_moneda(self, valor):
        """
        Formatear valor como moneda
        
        Args:
            valor: Valor numérico a formatear
            
        Returns:
            str: Valor formateado como moneda
        """
        if not isinstance(valor, Decimal):
            valor = Decimal(str(valor))
        
        # Formatear con separadores
        valor_str = f"{valor:,.{self.decimales}f}"
        
        # Reemplazar separadores según configuración
        if self.separador_miles == '.':
            valor_str = valor_str.replace(',', 'TEMP')
            valor_str = valor_str.replace('.', ',')
            valor_str = valor_str.replace('TEMP', '.')
        
        return f"{self.simbolo_moneda}{valor_str}"
    
    def formatear_numero(self, valor, decimales=None):
        """
        Formatear número con separadores
        
        Args:
            valor: Número a formatear
            decimales: Cantidad de decimales (usa default si es None)
            
        Returns:
            str: Número formateado
        """
        if decimales is None:
            decimales = self.decimales
        
        return f"{float(valor):,.{decimales}f}"
    
    # ==================== MÉTODOS DE VALIDACIÓN ====================
    
    def validar_descuento(self, descuento, subtotal):
        """
        Validar si un descuento es válido
        
        Args:
            descuento: Valor del descuento
            subtotal: Subtotal de la venta
            
        Returns:
            tuple: (es_valido, mensaje)
        """
        if descuento < 0:
            return False, "El descuento no puede ser negativo"
        
        if descuento > subtotal:
            return False, "El descuento no puede ser mayor al subtotal"
        
        porcentaje = (descuento / subtotal) * 100
        if porcentaje > self.descuento_maximo_porcentaje:
            return False, f"El descuento máximo permitido es {self.descuento_maximo_porcentaje}%"
        
        return True, "Descuento válido"
    
    def validar_stock(self, producto, cantidad_solicitada):
        """
        Validar disponibilidad de stock
        
        Args:
            producto: Objeto Producto
            cantidad_solicitada: Cantidad que se desea vender
            
        Returns:
            tuple: (es_valido, mensaje)
        """
        if cantidad_solicitada <= 0:
            return False, "La cantidad debe ser mayor a cero"
        
        if producto.stock < cantidad_solicitada:
            if not self.permitir_ventas_sin_stock:
                return False, f"Stock insuficiente. Disponible: {producto.stock}"
        
        if producto.stock - cantidad_solicitada < self.stock_minimo_alerta:
            return True, f"⚠️ Alerta: Stock quedaría por debajo del mínimo"
        
        return True, "Stock disponible"
    
    # ==================== MÉTODOS DE CONFIGURACIÓN ====================
    
    def actualizar_info_negocio(self, **kwargs):
        """
        Actualizar información del negocio
        
        Args:
            **kwargs: Campos a actualizar (nombre_negocio, nit, direccion, etc.)
        """
        campos_permitidos = [
            'nombre_negocio', 'nit', 'direccion', 'telefono', 
            'email', 'sitio_web'
        ]
        
        for campo, valor in kwargs.items():
            if campo in campos_permitidos:
                setattr(self, campo, valor)
        
        return True
    
    def obtener_configuracion_completa(self):
        """
        Obtener toda la configuración como diccionario
        
        Returns:
            dict: Configuración completa del sistema
        """
        return {
            'impuestos': {
                'tasa_iva': float(self.tasa_iva),
                'incluir_iva': self.incluir_iva,
            },
            'moneda': {
                'codigo': self.moneda,
                'simbolo': self.simbolo_moneda,
                'decimales': self.decimales,
            },
            'negocio': {
                'nombre': self.nombre_negocio,
                'nit': self.nit,
                'direccion': self.direccion,
                'telefono': self.telefono,
                'email': self.email,
            },
            'ventas': {
                'descuento_maximo': float(self.descuento_maximo_porcentaje),
                'stock_minimo_alerta': self.stock_minimo_alerta,
                'permitir_ventas_sin_stock': self.permitir_ventas_sin_stock,
            },
        }
    
    def __repr__(self):
        """Representación del objeto"""
        return f"<ConfiguracionSistema: {self.nombre_negocio}>"
    
    def __str__(self):
        """String representation"""
        return f"Configuración del Sistema POS - {self.nombre_negocio}"


# Crear instancia global (Singleton)
config_sistema = ConfiguracionSistema()