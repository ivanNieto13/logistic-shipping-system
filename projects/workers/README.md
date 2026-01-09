
# Sistema distribuido de gestión de envíos

Este proyecto contiene un sistema de gestión de tareas construida con Python + FastAPI, que permite la creación de `shipments`, `shipment-events` y una simulación de datos de analítica llamado `data-analysis`. Incluye integración con Redis como broker para comunciación de mensajes y MongoDB para persistir los datos.

## Requisitos previos

Es requisito tener instalado Docker.

1. **Instalar Docker** (por si no lo tienes):
   ```bash
   https://docs.docker.com/desktop
   ```

## Configuración del proyecto

1. **Clonar el repositorio**:
   ```bash
   git clone <URL_DEL_REPOSITORIO>
   cd logistic-shipping-system/projects
   ```

2. **Configurar variables de entorno**:
   Crea un archivo `.env` en el directorio `logistic-shipping-system/projects` con las siguientes variables, agregar los valores proporcionados.

   ```dotenv
    DEBUG=True
    DATABASE_URL=mongodb://root:example@db:27017
    DATABASE_NAME=shipments_db
    REDIS_URL=redis://redis:6379
    CREATE_SHIPMENT_CHANNEL=shipment
    SHIPMENT_EVENT_CHANNEL=shipment_event
    SHIPMENT_FINAL_EVENT_CHANNEL=shipment_final_event
    SHIPMENTS_COLLECTION_NAME=shipments
    SHIPMENTS_EVENTS_COLLECTION_NAME=shipment_events
    DATA_ANALYSIS_COLLECTION_NAME=data_analysis
   ```

## Iniciar las APIs y Workers

1. **Levantar los contenedores**:
   ```bash
   docker-compose up
   ```

2. La API de `shipment` estará disponible en `http://localhost:8080`.

3. La API de `shipment-event` estará disponible en `http://localhost:8081`.

## Documentación Swagger

Para ver la documentación de la API en Swagger:

1. Asegúrate de que el servidor esté en ejecución.
2. Accede a `http://localhost:8080/docs` para ver la API de `shipment` en tu navegador.
3. Accede a `http://localhost:8081/docs` para ver la API de `shipment-event` en tu navegador.


## Información adicional

El sistema aplica una lógica de negocio para evitar la duplicidad en la persistencia de los datos.

