# Soluciones a retos de Codember.dev

## Reto 01

CHALLENGE_01.txt

El reto
Un espía está enviando mensajes encriptados.

Tu misión es crear un programa que nos ayude a buscar patrones...

Los mensajes son palabras separadas por espacios como este:
gato perro perro coche Gato peRRo sol

Necesitamos que el programa nos devuelva el número de veces que aparece cada palabra en el mensaje, independientemente de si está en mayúsculas o minúsculas.

El resultado será una cadena de texto con la palabra y el número de veces que aparece en el mensaje, con este formato:
gato2perro3coche1sol1

¡Las palabras son ordenadas por su primera aparición en el mensaje!

Más ejemplos:
    llaveS casa CASA casa llaves -> llaves2casa3
    taza ta za taza -> taza2ta1za1
    casas casa casasas -> casas1casa1casas1

Cómo resolverlo 
    1. Resuelve el mensaje que encontrarás en este archivo: https://codember.dev/data/message_01.txt

    2. Envía tu solución con el comando "submit" en la terminal, por ejemplo así:
    submit perro3gato3coche1sol1



## Reto 02

CHALLENGE_02.txt

Mini Compiler Challenge
En el mundo del espionaje, se utiliza un lenguaje de codificación con símbolos que realizan operaciones matemáticas simples.

Tu tarea es crear un mini compilador que interprete y ejecute programas escritos en este lenguaje de símbolos.

Las operaciones del lenguaje son las siguientes:

"#" Incrementa el valor numérico en 1.
"@" Decrementa el valor numérico en 1.
"*" Multiplica el valor numérico por sí mismo.
"&" Imprime el valor numérico actual.
El valor numérico inicial es 0 y las operaciones deben aplicarse en elorden en que aparecen en la cadena de símbolos.

Ejemplos de entrada:
    Entrada: "##*&"
    Salida esperada: "4"
    Explicación: Incrementa (1), incrementa (2), multiplica (4), imprime (4).

Entrada: "&##&*&@&"
Salida esperada: "0243"
Explicación: Imprime (0), incrementa (1), incrementa (2), imprime (2), multiplica (4), imprime (4), decrementa (3), imprime (3).

Tu desafío:
    Desarrolla un mini compilador que tome una cadena de texto y devuelva otra cadena de texto con el resultado de ejecutar el programa.

Cómo resolverlo
    1. Resuelve el mensaje que encontrarás en este archivo: https://codember.dev/data/message_02.txt

    2. Crea un programa al que le pases como entrada el mensaje anterior. Envía la salida con el comando "submit" en la terminal, por ejemplo así:
    submit 024899488

solucion= 024899455

## Reto 03

CHALLENGE_03.txt

El Desafío del Cifrado Espía

    Un grupo de espías ha descubierto que su sistema de cifrado de mensajes está comprometido.

    Han encontrado algunas contraseñas que no cumplen con laPolítica de Seguridad de Cifrado que tenían establecida cuando fueron creadas.

    Para solucionar el problema, han creado una lista (tu entrada al desafío) de contraseñas (según la base de datos corrupta) y la política de seguridad cuando esa clave fue establecida.

Ejemplo de la lista:

    2-4 f: fgff
    4-6 z: zzzsg
    1-6 h: hhhhhh
    Cada línea indica, separado por :, la política de la clave y la clave misma.

    La política de la clave especifica el número mínimo y máximo de veces que un carácter dado debe aparecer para que la clave sea válida. Por ejemplo, 2-4 f significa que la clave debe contener f al menos 2 veces y como máximo 4 veces.

    Sabiendo esto, en el ejemplo anterior, hay 2 claves válidas:

    La segunda clave, zzzsg, no lo es; contiene 3 veces la letra z, pero necesita al menos 4. Las primeras y terceras claves son válidas: contienen la cantidad adecuada de f y h, respectivamente, según sus políticas.

Tu desafío:

    Determina cuántas claves de cifrado son válidas según sus políticas.

Cómo resolverlo

    1. Analiza la lista de políticas y claves de cifrado que encontrarás en este archivo: https://codember.dev/data/encryption_policies.txt

    2. Crea un programa que devuelva la clave inválida número 42 (de todas las claves inválidas, la 42ª en orden de aparición). Por ejemplo:
    submit bqamidgewtbuz

resultado:

##