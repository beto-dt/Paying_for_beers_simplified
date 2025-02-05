# Backend - Python
# Paying_for_beers_simplified

### 🚀 Funcionalidad Principal

El  objetivo del endpoint  es obtener el estatus completo de la orden simulada:

1. **Cálculo de Totales del Pedido (`calculate_order_totals`)**:

       - Se calculan el **subtotal**, los **impuestos** y el **total final**.
       - Es compatible con descuentos configurables según los datos del inventario simulado y reglas de promoción.
       - Se valida que las cantidades pedidas no excedan la disponibilidad de inventario.


2. **Aplicación de Descuentos Dinámicos (`calculate_discount`)**:

       - Descuento basado en el monto mínimo de compra (`min_amount`) y el porcentaje aplicado (`discount_percentage`).
       - Compatible con reglas personalizables que pueden definirse en el sistema.

### 🛠️ Arquitectura
El sistema sigue una estructura modular para mantener la claridad y facilitar el mantenimiento.

1. **Components**:

       - Core: Contiene las entidades principales (`Order`, `Stock`, etc.) y lógica principal como `calculate_order_totals`.
       - Infrastructure: Se encarga de manejar los datos de entrada como inventario (`stock_data`) y pedidos (`order_data`).
       - Interfaces: Capa para controladores y comunicación entre capas (como `order_controller.py`).

2. **Flujo del Cálculo de Pedido**:

       - Los datos del inventario (`stock_data`) y del pedido (`order_data`) se envían al caso de uso de cálculo.
       - Los valores de subtotal, impuestos, y descuento se calculan dinámicamente y se integran en el pedido.
       - Los resultados procesados incluyen los detalles con los totales.

### 🌟 Lógica Principal de Negocios

#### 1. Cálculo del Total del Pedido

    El cálculo del pedido utiliza la función `calculate_order_totals`, que recibe los datos del pedido y del inventario para calcular:

    - Subtotal: Calculado como la suma total del precio de cada artículo multiplicado por la cantidad solicitada.
    - Impuestos: Un valor fijo calculado como el 15% del subtotal.
    - Descuento: Calculado según las reglas configuradas en la función `calculate_discount`.
    - Total (final): La suma del subtotal, impuestos y descuentos aplicados.

#### 2. Función de Descuentos Dinámicos

    La función `calculate_discount` se encarga de calcular descuentos basados en las siguientes reglas:

    - Monto mínimo (`min_amount`): Si el subtotal del pedido no alcanza este monto, no se aplica descuento.
    - Porcentaje de descuento (`discount_percentage`): Se aplica al subtotal solo si este cumple con el monto mínimo.

### 🔧 Instalación

1. **Clonar el repositorio:**

       git clone git@github.com:beto-dt/Paying_for_beers_simplified.git

2. **Instalar dependencias:** Asegúrate de tener Python 3.10+ y usa `pip` para instalar las dependencias.

       pip3 install -r requirements.txt

3. **Ejecutar pruebas:** Usa `pytest` para verificar que todo esté funcionando correctamente:
    
       pytest

4.  **Ejecutar pruebas:** :  
 
        uvicorn backend.app.main:app --reload

