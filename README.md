# Task Manager (Entrega Final)

## Requisitos
- Python 3.11+
- pip

## Rutas principales
- Home: `/`
- About: `/about/`
- Auth: `/cuentas/login/`, `/cuentas/signup/`, `/cuentas/logout/`
- Perfil: `/cuentas/profile/` y edición `/cuentas/profile/editar/`
- Task Manager: Proyectos `/proyectos/`, Etiquetas `/etiquetas/`, Tareas `/tareas/`, Búsqueda `/tareas/buscar/`
- Demo CBV (projects): `/projects/`

## Flujo de prueba sugerido (usuario común)
1. Registro y login
- Ir a `/cuentas/signup/` y crear usuario (solicita username, email y password)
- Queda logueado automáticamente. Alternativa: `/cuentas/login/`

2. Perfil
- Ir a `/cuentas/profile/`
- Editar perfil en `/cuentas/profile/editar/` (subir avatar, bio, link y fecha de nacimiento)
- Probar cambiar contraseña desde el botón “Cambiar contraseña”

3. Proyectos y Etiquetas
- Crear un proyecto en `/proyectos/` → “Nuevo”
- Crear etiquetas en `/etiquetas/` → “Nueva”
- En móvil, verás menú de “Acciones” como dropdown (Editar/Eliminar)

4. Tareas
- Crear tarea en `/tareas/` → “Nueva” (seleccionar proyecto y etiquetas si corresponde)
- Listado `/tareas/`: botones Ver/Editar/Eliminar; en móvil, dropdown “Acciones”
- Cambiar estado desde el listado con el badge (Pendiente / En progreso / Finalizado)
- Búsqueda avanzada en `/tareas/buscar/` por texto, estado, proyecto y etiqueta
- Confirmar que cada usuario solo ve sus propios proyectos/etiquetas/tareas (prueba con dos cuentas)

5. Borrado con confirmación
- Al eliminar un Proyecto o una Etiqueta se muestra confirmación y un checkbox para borrar también las tareas relacionadas

6. Demo CBV (projects)
- Navegar a `/projects/` (requiere login)
- Crear/Editar/Eliminar tareas de la demo (cada usuario ve solo las suyas)

7. Admin (opcional)
- `/admin/` con el superusuario creado para ver y gestionar modelos

8. UI/UX
- Probar toggle de tema en la navbar (☀️/🌙) — persiste en el navegador
- Ver layout responsive: en móvil se ocultan columnas no esenciales para evitar overflow

## Notas de implementación
- No se incluye `db.sqlite3` ni la carpeta `media/` en el repo (.gitignore)
- Las imágenes de interfaz (favicon y avatar por defecto) están en `static/img/`

## Pruebas rápidas en 2 usuarios (aislamiento)
1) Usuario A crea proyecto, etiquetas y tareas
2) Usuario B inicia sesión en el mismo navegador (otra sesión/incógnito) y verifica que no ve los datos de A