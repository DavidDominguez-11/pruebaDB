-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 21-11-2023 a las 05:07:29
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
  `type` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `user`
--

INSERT INTO `user` (`ID`, `User`, `Password`, `type`) VALUES
(1, 'hola', 'como', ''),
(2, 'hola2', 'como', ''),
(3, 'kkk', 'kkk', ''),
(4, 'irisa', '1234', '');

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
