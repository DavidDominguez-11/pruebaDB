-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 22-11-2023 a las 05:19:38
-- Versión del servidor: 10.4.28-MariaDB
-- Versión de PHP: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `proyecto_2`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `chatbot`
--

CREATE TABLE `chatbot` (
  `ID` int(11) NOT NULL,
  `entrada` text NOT NULL,
  `salida` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `chatbot`
--

INSERT INTO `chatbot` (`ID`, `entrada`, `salida`) VALUES
(3, 'hola', '¡Hola! ¿En qué puedo ayudarte hoy?'),
(3, 'dime un chiste corto', 'Claro, aquí tienes uno:\n\n¿Por qué los pájaros no usan Facebook?\n\nPorque ya tienen Twitter.'),
(3, 'hola', '[34m¡Hola! ¿En qué puedo ayudarte hoy?'),
(3, 'como estas', '[34m¡Hola! Como soy una inteligencia artificial, no tengo emociones, pero estoy aquí para ayudarte. ¿En qué puedo asistirte hoy?');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `traducciones`
--

CREATE TABLE `traducciones` (
  `ID` int(11) NOT NULL,
  `Idioma1` text NOT NULL,
  `Idioma2` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `user`
--

CREATE TABLE `user` (
  `ID` int(11) NOT NULL,
  `User` varchar(20) NOT NULL,
  `Password` varchar(20) NOT NULL,
  `Type` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `user`
--

INSERT INTO `user` (`ID`, `User`, `Password`, `Type`) VALUES
(1, 'hola', 'como', 'chat'),
(2, 'hola2', 'como', 'traslate'),
(3, 'kkk', 'kkk', 'super'),
(4, 'irisa', '1234', 'chat'),
(5, 'hola3', 'como', 'super'),
(6, 'hola4', 'como', 'traslate'),
(7, 'user7', 'pass7', 'chat'),
(8, 'user8', 'pass8', 'traslate'),
(9, 'user9', 'pass9', 'super'),
(10, 'user10', 'pass10', 'chat'),
(11, 'user11', 'pass11', 'traslate'),
(12, 'user12', 'pass12', 'super'),
(13, 'user13', 'pass13', 'chat'),
(14, 'user14', 'pass14', 'traslate'),
(15, 'user15', 'pass15', 'super'),
(16, 'user16', 'pass16', 'chat'),
(17, 'user17', 'pass17', 'traslate'),
(18, 'user18', 'pass18', 'super'),
(19, 'user19', 'pass19', 'chat'),
(20, 'user20', 'pass20', 'traslate'),
(21, 'user21', 'pass21', 'super'),
(22, 'user22', 'pass22', 'chat'),
(23, 'user23', 'pass23', 'traslate'),
(24, 'user24', 'pass24', 'super'),
(25, 'user25', 'pass25', 'chat'),
(26, 'user26', 'pass26', 'traslate'),
(27, 'user27', 'pass27', 'super'),
(28, 'user28', 'pass28', 'chat'),
(29, 'user29', 'pass29', 'traslate'),
(30, 'user30', 'pass30', 'super'),
(31, 'user31', 'pass31', 'chat'),
(32, 'user32', 'pass32', 'traslate'),
(33, 'user33', 'pass33', 'super'),
(34, 'user34', 'pass34', 'chat'),
(35, 'user35', 'pass35', 'traslate'),
(36, 'user36', 'pass36', 'super');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `traducciones`
--
ALTER TABLE `traducciones`
  ADD KEY `ID` (`ID`);

--
-- Indices de la tabla `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`ID`);

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `traducciones`
--
ALTER TABLE `traducciones`
  ADD CONSTRAINT `traducciones_ibfk_1` FOREIGN KEY (`ID`) REFERENCES `user` (`ID`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
