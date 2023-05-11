# explorer_services
Levantar el proyecto

```bash
docker-compose up --build
```

Al construir el contenedor se ejecutaran las migraciones y esto basta para que puedan usar la API y consumirla.

### Ejecutar tests

```bash
docker-compose run web python -m pytest
```