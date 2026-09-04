# Auditoría de Seguridad del Proyecto

## Fase 1 – Auditoría

Para realizar la auditoría de seguridad del código se utilizó **Bandit**, una herramienta de análisis estático de seguridad para aplicaciones Python.

La auditoría se ejecutó de forma local sobre el proyecto mediante el siguiente comando:

```bash
bandit -r . -x ./venv -f txt -o auditoria_bandit.txt

## Tabla de auditoría

| ID | Vulnerabilidad | Descripción | Severidad | Confianza | Ubicación | Recomendación |
|---|---|---|---|---|---|---|
| B105 | Contraseña codificada en el código | Se detectó una contraseña escrita directamente en `app.py`. Esto puede exponer las credenciales. | Baja | Media | `app.py:10` | Utilizar variables de entorno o un sistema seguro de gestión de secretos. |
| B608 | Construcción de consulta SQL mediante cadenas | La consulta SQL utiliza concatenación con un parámetro recibido desde la solicitud, lo que puede generar una inyección SQL. | Media | Baja | `app.py:25` | Utilizar consultas SQL parametrizadas u ORM. |
| B311 | Uso de generador pseudoaleatorio no seguro | Se utiliza `random.random()`. Este generador no debe utilizarse para operaciones que requieran seguridad criptográfica. | Baja | Alta | `app.py:30` | Utilizar un generador criptográficamente seguro cuando sea necesario. |
| B201 | Flask con `debug=True` | La aplicación Flask está ejecutándose con el modo de depuración activado, lo que puede exponer información sensible. | Alta | Media | `app.py:35` | Desactivar `debug=True` en producción y utilizar `debug=False`. |
| B104 | Aplicación enlazada a todas las interfaces | Se utiliza `host='0.0.0.0'`, permitiendo que la aplicación escuche en todas las interfaces de red. | Media | Media | `app.py:35` | Restringir la interfaz de escucha cuando no sea necesario exponer el servicio externamente. |
| B101 | Uso de `assert` | Se detectó el uso de `assert` en las pruebas. Estas instrucciones pueden eliminarse al ejecutar Python con optimizaciones. | Baja | Alta | `test_app.py:7` | Utilizar las aserciones propias del framework de pruebas. |


## Resumen de la auditoría

| Severidad | Cantidad |
|---|---:|
| Alta | 1 |
| Media | 2 |
| Baja | 3 |
| **Total** | **6** |

## Resumen por confianza

| Confianza | Cantidad |
|---|---:|
| Alta | 2 |
| Media | 3 |
| Baja | 1 |
| **Total** | **6** |

## Resultado Final 

| Herramienta | Resultado                   | Problemas encontrados |
| ----------- | --------------------------- | --------------------: |
| Bandit      | Sin problemas identificados |                     0 |


## Auditoría de Seguridad

| Hallazgo | Severidad | Herramienta | Ubicación | Estado | Justificación |
|---|---|---|---|---|---|
| Binding a todas las interfaces (0.0.0.0) | Media | Bandit (B104) | app.py:45 | Aceptado con excepción | Necesario para exponer el servicio desde el contenedor Docker al host; el acceso real se controla vía mapeo de puertos y configuración de red/firewall |