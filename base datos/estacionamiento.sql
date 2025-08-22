-- Tabla clientes (pensionados, residentes o normales)
CREATE TABLE clientes (
    id_cliente INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    telefono VARCHAR(20),
    correo VARCHAR(100),
    tipo_cliente ENUM('pensionado','residente','normal') NOT NULL,
    tipo_pension ENUM('dia','mes') NULL,
    fecha_inicio DATE NULL,
    fecha_fin DATE NULL
);

-- Tabla vehículos asociados a clientes
CREATE TABLE vehiculos (
    id_vehiculo INT AUTO_INCREMENT PRIMARY KEY,
    id_cliente INT NOT NULL,
    placa VARCHAR(10) NOT NULL UNIQUE,
    tipo_vehiculo ENUM('auto','moto') NOT NULL,
    FOREIGN KEY (id_cliente) REFERENCES clientes(id_cliente)
);

-- Tabla tickets que registra entradas y salidas
CREATE TABLE tickets (
    id_ticket INT AUTO_INCREMENT PRIMARY KEY,
    codigo_unico VARCHAR(50) NOT NULL UNIQUE,
    id_vehiculo INT NOT NULL,
    tipo_cliente ENUM('normal','pensionado','residente') DEFAULT 'normal',
    hora_entrada DATETIME NOT NULL,
    hora_salida DATETIME,
    precio DECIMAL(10,2),
    estado ENUM('abierto','cerrado') DEFAULT 'abierto',
    FOREIGN KEY (id_vehiculo) REFERENCES vehiculos(id_vehiculo)
);

-- Tabla tarifas para precios por tipo de vehículo y cliente (opcional)
CREATE TABLE tarifas (
    id_tarifa INT AUTO_INCREMENT PRIMARY KEY,
    tipo_vehiculo ENUM('auto','moto') NOT NULL,
    tipo_cliente ENUM('normal','pensionado','residente') NOT NULL,
    precio_hora DECIMAL(10,2) NOT NULL,
    precio_extrabio DECIMAL(10,2) NOT NULL,
    precio_dia DECIMAL(10,2),
    precio_mes DECIMAL(10,2)
);

-- Tabla usuarios para el login y control de acceso
CREATE TABLE usuarios (
    id_usuario INT AUTO_INCREMENT PRIMARY KEY,
    usuario VARCHAR(50) NOT NULL UNIQUE,
    contraseña VARCHAR(255) NOT NULL, -- almacenar hash seguro
    nombre_completo VARCHAR(100),
    rol ENUM('admin','empleado') DEFAULT 'empleado',
    fecha_creacion DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- Tabla papelera para tickets eliminados, guardando motivo de eliminación
CREATE TABLE papelera_tickets (
    id_papelera INT AUTO_INCREMENT PRIMARY KEY,
    id_ticket INT NOT NULL,
    codigo_unico VARCHAR(50) NOT NULL,
    id_vehiculo INT NOT NULL,
    tipo_cliente ENUM('normal','pensionado','residente') DEFAULT 'normal',
    hora_entrada DATETIME NOT NULL,
    motivo_eliminacion VARCHAR(255) NOT NULL,
    fecha_eliminacion DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- Tabla para registrar eventos (auditoría)
CREATE TABLE eventos_usuario (
    id_evento INT AUTO_INCREMENT PRIMARY KEY,
    id_usuario INT NOT NULL,
    accion VARCHAR(100) NOT NULL,
    descripcion TEXT,
    fecha_evento DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (id_usuario) REFERENCES usuarios(id_usuario)
);

-------------------------------------Procedimiento almacenados---------------------------------------------------------------------------------------------



-------------------------------------Dar de alta una tarifa o sobrescribir tarifa---------------------------------------------------------------------------------
DELIMITER //
CREATE PROCEDURE sp_guardar_tarifa(
    IN p_tipo_vehiculo VARCHAR(10),
    IN p_tipo_cliente VARCHAR(15),
    IN p_precio_hora DECIMAL(10,2),
    IN p_precio_extravio DECIMAL(10,2),
    IN p_precio_dia DECIMAL(10,2),
    IN p_precio_mes DECIMAL(10,2),
    IN p_id_usuario INT,
    OUT p_estado VARCHAR(30),
    OUT p_mensaje VARCHAR(100)
)
BEGIN
    DECLARE v_existente INT;

    SELECT COUNT(*) INTO v_existente
    FROM tarifas 
    WHERE tipo_vehiculo = p_tipo_vehiculo 
      AND tipo_cliente = p_tipo_cliente;

    IF v_existente > 0 THEN
        UPDATE tarifas 
        SET precio_hora = p_precio_hora, 
            precio_extrabio = p_precio_extravio,
            precio_dia = p_precio_dia,
            precio_mes = p_precio_mes
        WHERE tipo_vehiculo = p_tipo_vehiculo 
          AND tipo_cliente = p_tipo_cliente;

        SET p_estado = 'OK';
        SET p_mensaje = 'Tarifa actualizada correctamente.';
    ELSE
        INSERT INTO tarifas (tipo_vehiculo, tipo_cliente, precio_hora, precio_extrabio, precio_dia, precio_mes)
        VALUES (p_tipo_vehiculo, p_tipo_cliente, p_precio_hora, p_precio_extravio, p_precio_dia, p_precio_mes);

        SET p_estado = 'OK';
        SET p_mensaje = 'Tarifa insertada correctamente.';
    END IF;

    INSERT INTO eventos_usuario (id_usuario, accion, descripcion)
    VALUES (p_id_usuario, 'Guardar Tarifa', 'Se insertó o actualizó una tarifa');
END //
DELIMITER ;


------------------------------------------------------Dar de alta un cliente-----------------------------------------------------------------------------------
DELIMITER //
CREATE PROCEDURE sp_crear_cliente_con_ticket(
    IN p_nombre VARCHAR(100),
    IN p_telefono VARCHAR(20),
    IN p_correo VARCHAR(100),
    IN p_tipo_cliente ENUM('pensionado','residente','normal'),
    IN p_tipo_pension ENUM('dia','mes'),
    IN p_placa VARCHAR(10),
    IN p_id_usuario INT,
    IN p_tipo_vehiculo ENUM('auto','moto'),
    OUT p_estado VARCHAR(30),
    OUT p_mensaje VARCHAR(100)
)
proc_main: BEGIN
    DECLARE v_fecha_inicio DATETIME;
    DECLARE v_fecha_fin DATETIME;
    DECLARE v_id_cliente INT;
    DECLARE v_id_vehiculo INT;
    DECLARE v_precio DECIMAL(10,2);
    DECLARE v_codigo_unico VARCHAR(50);

    -- Asignar fechas
    SET v_fecha_inicio = NOW();
    IF p_tipo_pension = 'dia' THEN
        SET v_fecha_fin = DATE_ADD(v_fecha_inicio, INTERVAL 1 DAY);
    ELSEIF p_tipo_pension = 'mes' THEN
        SET v_fecha_fin = DATE_ADD(v_fecha_inicio, INTERVAL 1 MONTH);
    ELSE
        SET v_fecha_fin = NULL;
    END IF;

    -- Insertar cliente
    INSERT INTO clientes (nombre, telefono, correo, tipo_cliente, tipo_pension, fecha_inicio, fecha_fin)
    VALUES (p_nombre, p_telefono, p_correo, p_tipo_cliente, p_tipo_pension, v_fecha_inicio, v_fecha_fin);
    SET v_id_cliente = LAST_INSERT_ID();

    -- Verificar si vehículo ya existe
    SELECT id_vehiculo INTO v_id_vehiculo 
    FROM vehiculos 
    WHERE placa = p_placa 
    LIMIT 1;

    IF v_id_vehiculo IS NULL THEN
        -- Insertar vehículo nuevo
        INSERT INTO vehiculos (id_cliente, placa, tipo_vehiculo)
        VALUES (v_id_cliente, p_placa, p_tipo_vehiculo);
        SET v_id_vehiculo = LAST_INSERT_ID();
    ELSE
        -- Asociar vehículo existente al nuevo cliente si es necesario
        UPDATE vehiculos 
        SET id_cliente = v_id_cliente, tipo_vehiculo = p_tipo_vehiculo 
        WHERE id_vehiculo = v_id_vehiculo;
    END IF;

    -- Obtener tarifa
    SELECT 
        CASE 
            WHEN p_tipo_pension = 'dia' THEN precio_dia 
            WHEN p_tipo_pension = 'mes' THEN precio_mes 
            ELSE precio_hora 
        END
    INTO v_precio
    FROM tarifas
    WHERE tipo_vehiculo = p_tipo_vehiculo
      AND tipo_cliente = p_tipo_cliente
    LIMIT 1;

    IF v_precio IS NULL THEN
        SET p_estado = 'ERROR';
        SET p_mensaje = 'No existe tarifa para este tipo de cliente y vehículo.';
        LEAVE proc_main;
    END IF;

    -- Crear código único
    SET v_codigo_unico = CONCAT('T-', DATE_FORMAT(NOW(), '%Y%m%d%H%i%S'), '-', p_placa);

    -- Insertar ticket cerrado
    INSERT INTO tickets (codigo_unico, id_vehiculo, tipo_cliente, hora_entrada, hora_salida, precio, estado)
    VALUES (v_codigo_unico, v_id_vehiculo, p_tipo_cliente, v_fecha_inicio, v_fecha_fin, v_precio, 'cerrado');

    -- Mensaje de salida
    SET p_estado = 'OK';
    SET p_mensaje = 'Cliente y ticket creados correctamente.';

    
    INSERT INTO eventos_usuario (id_usuario, accion, descripcion)
    VALUES (p_id_usuario, 'Dar de alta Cliente', 'Se dio de alta un cliente');
END //
DELIMITER ;

-----------------------------------------------------Registrar un vehiculo normal---------------------------------------------------------------------------------------------
DELIMITER //
CREATE PROCEDURE registrar_ticket (
    IN p_placa VARCHAR(10),
    IN p_tipo_vehiculo VARCHAR(10),
    IN p_id_usuario INT,
    OUT p_estatus VARCHAR(30),
    OUT p_mensaje VARCHAR(255),
    OUT p_codigo VARCHAR(100)
)
BEGIN
    DECLARE v_id_vehiculo INT DEFAULT NULL;
    DECLARE v_id_cliente INT DEFAULT NULL;
    DECLARE v_tipo_cliente VARCHAR(20) DEFAULT 'normal';
    DECLARE v_fecha_fin DATE DEFAULT NULL;
    DECLARE v_ticket_abierto INT DEFAULT 0;
    DECLARE v_codigo VARCHAR(50) DEFAULT '';

    -- Validación inicial
    IF p_tipo_vehiculo NOT IN ('auto','moto') THEN
        SET p_estatus = "Error";
        SET p_mensaje = 'Tipo de vehículo inválido (debe ser auto o moto).';
    ELSE
        -- ¿El vehículo existe?
        SELECT id_vehiculo, id_cliente
        INTO v_id_vehiculo, v_id_cliente
        FROM vehiculos
        WHERE placa = p_placa;

        IF v_id_vehiculo IS NULL THEN
            INSERT INTO clientes (nombre, tipo_cliente)
            VALUES ('Cliente desconocido', 'normal');
            SET v_id_cliente = LAST_INSERT_ID();

            INSERT INTO vehiculos (id_cliente, placa, tipo_vehiculo)
            VALUES (v_id_cliente, p_placa, p_tipo_vehiculo);
            SET v_id_vehiculo = LAST_INSERT_ID();
            SET v_tipo_cliente = 'normal';
        ELSE
            SELECT tipo_cliente, fecha_fin
            INTO v_tipo_cliente, v_fecha_fin
            FROM clientes
            WHERE id_cliente = v_id_cliente;
        END IF;

        -- Ticket abierto
        SELECT COUNT(*) INTO v_ticket_abierto
        FROM tickets
        WHERE id_vehiculo = v_id_vehiculo AND estado = 'abierto';

        IF v_ticket_abierto > 0 THEN
            SET p_estatus = "Error";
            SET p_mensaje = 'Este vehículo ya tiene un ticket abierto.';
        ELSEIF v_tipo_cliente IN ('pensionado','residente') AND v_fecha_fin IS NOT NULL AND v_fecha_fin >= CURDATE() THEN
            SET p_estatus = "Error";
            SET p_mensaje = 'El vehículo cuenta con una pensión activa, no se genera ticket.';
        ELSE
            -- Generar código único
            SET v_codigo = CONCAT('T-', DATE_FORMAT(NOW(), '%Y%m%d%H%i%S'), '-', p_placa);

            INSERT INTO tickets (codigo_unico, id_vehiculo, tipo_cliente, hora_entrada, estado)
            VALUES (v_codigo, v_id_vehiculo, v_tipo_cliente, NOW(), 'abierto');

            SET p_estatus = "Exito";
            SET p_mensaje = CONCAT('Ticket generado exitosamente con código: ', v_codigo);
            SET p_codigo= v_codigo;
            INSERT INTO eventos_usuario (id_usuario, accion, descripcion)
VALUES (    p_id_usuario, 'registrar entrada vehiculo', 'Se realizo la entrada de un vehiculo');
        END IF;
    END IF;
END //
DELIMITER ;


---------------------------------------------------Checar Precio-----------------------------------------------------------------------------
DELIMITER //
CREATE PROCEDURE checar_precio_ticket (
    IN p_codigo VARCHAR(50),
    IN p_id_usuario INT,
    OUT p_estatus VARCHAR(30),
    OUT p_mensaje VARCHAR(255),
    OUT p_precio DECIMAL(10,2)
)
BEGIN
    DECLARE v_id_ticket INT;
    DECLARE v_id_vehiculo INT;
    DECLARE v_tipo_cliente VARCHAR(20);
    DECLARE v_tipo_vehiculo VARCHAR(10);
    DECLARE v_precio_hora DECIMAL(10,2);
    DECLARE v_horas INT;
    DECLARE v_estado VARCHAR(10);

    -- Buscar ticket
    SELECT id_ticket, id_vehiculo, tipo_cliente, estado, IFNULL(precio,0)
    INTO v_id_ticket, v_id_vehiculo, v_tipo_cliente, v_estado, p_precio
    FROM tickets
    WHERE codigo_unico = p_codigo;

    -- Validar existencia
    IF v_id_ticket IS NULL THEN
        SET p_estatus = 'Error';
        SET p_mensaje = 'Ticket no encontrado.';
    ELSE
        -- Si ya está cerrado
        IF v_estado = 'cerrado' THEN
            SET p_estatus = 'Aviso';
            SET p_mensaje = CONCAT('El ticket ya fue pagado. Total: $', p_precio);
        ELSE
            -- Obtener tipo de vehículo
            SELECT tipo_vehiculo
            INTO v_tipo_vehiculo
            FROM vehiculos
            WHERE id_vehiculo = v_id_vehiculo;

            -- Obtener tarifa por hora
            SELECT precio_hora
            INTO v_precio_hora
            FROM tarifas
            WHERE tipo_vehiculo = v_tipo_vehiculo
              AND tipo_cliente = v_tipo_cliente;

            IF v_precio_hora IS NULL THEN
                SET p_estatus = 'Error';
                SET p_mensaje = 'No existe tarifa configurada para este tipo de vehículo y cliente.';
            ELSE
                -- Calcular horas redondeando hacia arriba
                SELECT CEIL(TIMESTAMPDIFF(MINUTE, hora_entrada, NOW()) / 60.0)
                INTO v_horas
                FROM tickets
                WHERE id_ticket = v_id_ticket;

                SET p_precio = v_horas * v_precio_hora;
                SET p_estatus = 'Exito';
                SET p_mensaje = CONCAT('El precio calculado es $', p_precio);
                INSERT INTO eventos_usuario (id_usuario, accion, descripcion)
                VALUES (p_id_usuario, 'Checar Precio', 'Se checo el precio de un Ticket');

            END IF;
        END IF;
    END IF;
END //
DELIMITER ;

-------------------------------------------------------------Pagar Ticket ----------------------------------------------------------------------------

DELIMITER //
CREATE PROCEDURE pagar_ticket (
    IN p_codigo VARCHAR(50),
    IN p_id_usuario INT,
    OUT p_estatus VARCHAR(50),
    OUT p_mensaje VARCHAR(255),
    OUT p_precio DECIMAL(10,2)
)
BEGIN
    DECLARE v_id_ticket INT;
    DECLARE v_id_vehiculo INT;
    DECLARE v_tipo_cliente VARCHAR(20);
    DECLARE v_tipo_vehiculo VARCHAR(10);
    DECLARE v_precio_hora DECIMAL(10,2);
    DECLARE v_horas INT;
    DECLARE v_estado VARCHAR(10);

    -- Buscar ticket
    SELECT id_ticket, id_vehiculo, tipo_cliente, estado, IFNULL(precio,0)
    INTO v_id_ticket, v_id_vehiculo, v_tipo_cliente, v_estado, p_precio
    FROM tickets
    WHERE codigo_unico = p_codigo;

    -- Validar existencia
    IF v_id_ticket IS NULL THEN
        SET p_estatus = 'Error';
        SET p_mensaje = 'Ticket no encontrado.';
    ELSE
        -- Verificar si ya está cerrado
        IF v_estado = 'cerrado' THEN
            SET p_estatus = 'Aviso';
            SET p_mensaje = CONCAT('El ticket ya fue pagado. Total: $', p_precio);
        ELSE
            -- Obtener tipo de vehículo
            SELECT tipo_vehiculo
            INTO v_tipo_vehiculo
            FROM vehiculos
            WHERE id_vehiculo = v_id_vehiculo;

            -- Obtener tarifa por hora
            SELECT precio_hora
            INTO v_precio_hora
            FROM tarifas
            WHERE tipo_vehiculo = v_tipo_vehiculo
              AND tipo_cliente = v_tipo_cliente;

            IF v_precio_hora IS NULL THEN
                SET p_estatus = 'Error';
                SET p_mensaje = 'No existe tarifa configurada para este tipo de vehículo y cliente.';
            ELSE
                -- Calcular horas redondeando hacia arriba
                SELECT CEIL(TIMESTAMPDIFF(MINUTE, hora_entrada, NOW()) / 60.0)
                INTO v_horas
                FROM tickets
                WHERE id_ticket = v_id_ticket;

                SET p_precio = v_horas * v_precio_hora;

                -- Actualizar ticket: precio final, hora salida y estado cerrado
                UPDATE tickets
                SET precio = p_precio,
                    hora_salida = NOW(),
                    estado = 'cerrado'
                WHERE id_ticket = v_id_ticket;

                SET p_estatus = 'Exito';
                SET p_mensaje = CONCAT('Pago realizado con éxito. Total: $', p_precio);
                INSERT INTO eventos_usuario (id_usuario, accion, descripcion)
                VALUES (p_id_usuario, 'Pagar Ticket', 'Se realiso el pago del ticket');
            END IF;
        END IF;
    END IF;
END //
DELIMITER ;



--------------------------------------------------Pagar Ticket Extrabio-------------------------------------------------------
DELIMITER //
CREATE PROCEDURE pagar_ticket_extravio (
    IN p_codigo VARCHAR(50),
    IN p_id_usuario INT,
    OUT p_estatus VARCHAR(50),
    OUT p_mensaje VARCHAR(255),
    OUT p_precio DECIMAL(10,2)
)
BEGIN
    DECLARE v_id_ticket INT;
    DECLARE v_id_vehiculo INT;
    DECLARE v_tipo_cliente VARCHAR(20);
    DECLARE v_tipo_vehiculo VARCHAR(10);
    DECLARE v_precio_hora DECIMAL(10,2);
    DECLARE v_precio_extravio DECIMAL(10,2);
    DECLARE v_horas INT;
    DECLARE v_estado VARCHAR(10);

    -- Buscar ticket
    SELECT id_ticket, id_vehiculo, tipo_cliente, estado, IFNULL(precio,0)
    INTO v_id_ticket, v_id_vehiculo, v_tipo_cliente, v_estado, p_precio
    FROM tickets
    WHERE codigo_unico = p_codigo;

    -- Validar existencia
    IF v_id_ticket IS NULL THEN
        SET p_estatus = 'Error';
        SET p_mensaje = 'Ticket no encontrado.';
    ELSE
        -- Verificar si ya está cerrado
        IF v_estado = 'cerrado' THEN
            SET p_estatus = 'Aviso';
            SET p_mensaje = CONCAT('El ticket ya fue pagado. Total: $', p_precio);
        ELSE
            -- Obtener tipo de vehículo
            SELECT tipo_vehiculo
            INTO v_tipo_vehiculo
            FROM vehiculos
            WHERE id_vehiculo = v_id_vehiculo;

            -- Obtener tarifas (hora + extravío)
            SELECT precio_hora, precio_extrabio
            INTO v_precio_hora, v_precio_extravio
            FROM tarifas
            WHERE tipo_vehiculo = v_tipo_vehiculo
              AND tipo_cliente = v_tipo_cliente;

            IF v_precio_hora IS NULL THEN
                SET p_estatus = 'Error';
                SET p_mensaje = 'No existe tarifa configurada para este tipo de vehículo y cliente.';
            ELSE
                -- Calcular horas redondeando hacia arriba
                SELECT CEIL(TIMESTAMPDIFF(MINUTE, hora_entrada, NOW()) / 60.0)
                INTO v_horas
                FROM tickets
                WHERE id_ticket = v_id_ticket;

                -- Precio total con extravío
                SET p_precio = (v_horas * v_precio_hora) + v_precio_extravio;

                -- Actualizar ticket: precio final, hora salida y estado cerrado
                UPDATE tickets
                SET precio = p_precio,
                    hora_salida = NOW(),
                    estado = 'cerrado'
                WHERE id_ticket = v_id_ticket;

                SET p_estatus = 'Exito';
                SET p_mensaje = CONCAT('Pago realizado con éxito (incluye extravío). Total: $', p_precio);

                INSERT INTO eventos_usuario (id_usuario, accion, descripcion)
                VALUES (p_id_usuario, 'Pagar Ticket Extravio', 'Se realizó el pago del ticket con extravío');
            END IF;
        END IF;
    END IF;
END //
DELIMITER ;

------------------------------------------------------Check Precio Extrabio------------------------------------------------------
DELIMITER //

CREATE PROCEDURE calcular_ticket_extravio_por_placa (
    IN p_placa VARCHAR(10),
    OUT p_codigo VARCHAR(50),
    OUT p_estatus VARCHAR(50),
    OUT p_mensaje VARCHAR(255),
    OUT p_precio DECIMAL(10,2)
)
BEGIN
    DECLARE v_id_ticket INT;
    DECLARE v_id_vehiculo INT;
    DECLARE v_tipo_cliente VARCHAR(20);
    DECLARE v_tipo_vehiculo VARCHAR(10);
    DECLARE v_precio_hora DECIMAL(10,2);
    DECLARE v_precio_extravio DECIMAL(10,2);
    DECLARE v_horas INT;
    DECLARE v_estado VARCHAR(10);

    -- Buscar ticket abierto por placa
    SELECT t.id_ticket, t.id_vehiculo, t.tipo_cliente, t.estado, IFNULL(t.precio,0), t.codigo_unico
    INTO v_id_ticket, v_id_vehiculo, v_tipo_cliente, v_estado, p_precio, p_codigo
    FROM tickets t
    INNER JOIN vehiculos v ON t.id_vehiculo = v.id_vehiculo
    WHERE v.placa = p_placa
      AND t.estado = 'abierto'
    LIMIT 1;

    -- Validar existencia
    IF v_id_ticket IS NULL THEN
        SET p_estatus = 'Error';
        SET p_mensaje = 'No se encontró ticket abierto para esta placa.';
        SET p_codigo = NULL;
        SET p_precio = 0;
    ELSE
        -- Obtener tipo de vehículo
        SELECT tipo_vehiculo
        INTO v_tipo_vehiculo
        FROM vehiculos
        WHERE id_vehiculo = v_id_vehiculo;

        -- Obtener tarifas (hora + extravío)
        SELECT precio_hora, precio_extrabio
        INTO v_precio_hora, v_precio_extravio
        FROM tarifas
        WHERE tipo_vehiculo = v_tipo_vehiculo
          AND tipo_cliente = v_tipo_cliente;

        IF v_precio_hora IS NULL THEN
            SET p_estatus = 'Error';
            SET p_mensaje = 'No existe tarifa configurada para este tipo de vehículo y cliente.';
            SET p_precio = 0;
        ELSE
            -- Calcular horas redondeando hacia arriba
            SELECT CEIL(TIMESTAMPDIFF(MINUTE, hora_entrada, NOW()) / 60.0)
            INTO v_horas
            FROM tickets
            WHERE id_ticket = v_id_ticket;

            -- Precio total con extravío
            SET p_precio = (v_horas * v_precio_hora) + v_precio_extravio;

            SET p_estatus = 'Exito';
            SET p_mensaje = CONCAT('Cálculo realizado con éxito (incluye extravío). Total estimado: $', p_precio);
        END IF;
    END IF;
END //

DELIMITER ;

------------------------------------------------Eliminar ticket---------------------------------------------------------------
DELIMITER //
CREATE PROCEDURE eliminar_ticket (
    IN p_codigo VARCHAR(50),
    IN p_motivo VARCHAR(255),
    IN p_id_usuario INT,
    OUT p_estatus VARCHAR(30),
    OUT p_mensaje VARCHAR(255)
)
BEGIN
    DECLARE v_id_ticket INT;
    DECLARE v_id_vehiculo INT;
    DECLARE v_tipo_cliente VARCHAR(20);
    DECLARE v_hora_entrada DATETIME;
    DECLARE v_estado VARCHAR(10);

    -- Buscar ticket
    SELECT id_ticket, id_vehiculo, tipo_cliente, hora_entrada, estado
    INTO v_id_ticket, v_id_vehiculo, v_tipo_cliente, v_hora_entrada, v_estado
    FROM tickets
    WHERE codigo_unico = p_codigo;

    -- Validaciones
    IF v_id_ticket IS NULL THEN
        SET p_estatus = 'Error';
        SET p_mensaje = 'Ticket no encontrado.';
    ELSEIF v_estado = 'cerrado' THEN
        SET p_estatus = 'Error';
        SET p_mensaje = 'El ticket ya está cerrado y no puede eliminarse.';
    ELSE
        -- Insertar en la papelera
        INSERT INTO papelera_tickets
        (id_ticket, codigo_unico, id_vehiculo, tipo_cliente, hora_entrada, motivo_eliminacion)
        VALUES (v_id_ticket, p_codigo, v_id_vehiculo, v_tipo_cliente, v_hora_entrada, p_motivo);

        -- Eliminar el ticket original
        DELETE FROM tickets WHERE id_ticket = v_id_ticket;

        SET p_estatus = 'Exito';
        SET p_mensaje = CONCAT('Ticket ', p_codigo, ' movido a la papelera con motivo: ', p_motivo);
        INSERT INTO eventos_usuario (id_usuario, accion, descripcion)
        VALUES (p_id_usuario, 'Borrar Ticket', 'Se elimino Ticket');

    END IF;
END //
DELIMITER ;

------------------------------------------------Reporte Tickets--------------------------------------------------------------------------
DELIMITER //
CREATE PROCEDURE obtener_tickets_por_fechas (
    IN p_fecha_inicio DATE,
    IN p_fecha_fin DATE,
    IN p_id_usuario INT
)
BEGIN
    SELECT 
        id_ticket,
        codigo_unico,
        id_vehiculo,
        tipo_cliente,
        hora_entrada,
        hora_salida,
        precio,
        estado
    FROM tickets
    WHERE hora_entrada BETWEEN CONCAT(p_fecha_inicio, ' 00:00:00')
                           AND CONCAT(p_fecha_fin, ' 23:59:59')
    ORDER BY hora_entrada ASC;
    INSERT INTO eventos_usuario (id_usuario, accion, descripcion)
    VALUES (p_id_usuario, 'Se realizo un reporte', 'Se realizo un reporte');
END //
DELIMITER ;

------------------------------------------------add usuario-----------------------------------------------------------------------------------------
DELIMITER //

CREATE PROCEDURE CrearUsuario(
    IN p_usuario VARCHAR(50),
    IN p_contraseña VARCHAR(100),
    IN p_nombre_completo VARCHAR(100),
    IN p_id_usuario INT,
    IN p_rol ENUM('admin','empleado')
)
BEGIN
    DECLARE v_count INT;

    -- Verificar si el usuario ya existe
    SELECT COUNT(*) INTO v_count
    FROM usuarios
    WHERE usuario = p_usuario;

    IF v_count > 0 THEN
        SELECT 'El usuario ya existe' AS mensaje;
    ELSE
        -- Insertar usuario con contraseña segura
        INSERT INTO usuarios (usuario, contraseña, nombre_completo, rol)
        VALUES (p_usuario, SHA2(p_contraseña, 256), p_nombre_completo, p_rol);

        SELECT 'Usuario guardado con éxito' AS mensaje;
        INSERT INTO eventos_usuario (id_usuario, accion, descripcion)
        VALUES (p_id_usuario, 'Agregar usuario', 'Se agrego un usuario');

    END IF;
END //

DELIMITER ;


---------------------------------------------------Loggin validacion-----------------------------------------------------------------
DELIMITER //
CREATE PROCEDURE validar_login (
    IN p_usuario VARCHAR(50),
    IN p_contraseña VARCHAR(255),
    OUT p_id_usuario INT,
    OUT p_rol VARCHAR(20),
    OUT p_valido BOOLEAN
)
BEGIN
    DECLARE v_id_usuario INT;
    DECLARE v_rol VARCHAR(20);

    SELECT id_usuario, rol
    INTO v_id_usuario, v_rol
    FROM usuarios
    WHERE usuario = p_usuario AND contraseña = SHA2(p_contraseña,256);

    IF v_id_usuario IS NOT NULL THEN
        SET p_id_usuario = v_id_usuario;
        SET p_rol = v_rol;
        SET p_valido = TRUE;
    ELSE
        SET p_id_usuario = NULL;
        SET p_rol = NULL;
        SET p_valido = FALSE;
    END IF;
END //
DELIMITER ;
-----------------------------------------------------Obtener Precio Pension----------------------------------------------------------------------
DELIMITER //
CREATE PROCEDURE obtener_precio_pension (
    IN p_tipoCliente ENUM('pensionado','residente'),
    IN p_tipoVehiculo ENUM('auto','moto'),
    IN p_tipoPension ENUM('dia','mes'),
    OUT p_precio DECIMAL(10,2)
)
BEGIN
    IF p_tipoPension = 'dia' THEN
        SELECT precio_dia 
        INTO p_precio
        FROM tarifas
        WHERE tipo_cliente = p_tipoCliente
          AND tipo_vehiculo = p_tipoVehiculo
        LIMIT 1;
    ELSEIF p_tipoPension = 'mes' THEN
        SELECT precio_mes 
        INTO p_precio
        FROM tarifas
        WHERE tipo_cliente = p_tipoCliente
          AND tipo_vehiculo = p_tipoVehiculo
        LIMIT 1;
    ELSE
        SET p_precio = NULL; -- Por si pasa un valor no válido
    END IF;
END //
DELIMITER ;

----------------------------------------------------------------------Obtener ticket en estado avierto------------------------------------------------------------------------------
DELIMITER $$

CREATE PROCEDURE ObtenerTicketsAbiertos()
BEGIN
    SELECT 
        t.id_ticket,
        t.codigo_unico,
        v.placa,
        t.hora_entrada
    FROM tickets t
    INNER JOIN vehiculos v ON t.id_vehiculo = v.id_vehiculo
    WHERE t.estado = 'abierto'
    ORDER BY t.hora_entrada ASC;
END$$

DELIMITER ;