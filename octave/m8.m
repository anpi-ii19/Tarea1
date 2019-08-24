%Carga del paquete simbólico
pkg load symbolic


function [x_aprox, iter] = m8(func, xk, y, tol, graph)
  % Metodo M8 para encontrar el cero de una funcion
  % :param func: string con la funcion que se debe evaluar
  % :param xk: valor de x inicial con el cual aplicar el metodo
  % :param y: constante que es un numero real, excepto cero.
  % :param tol: tolerancia al fallo de debe tener el resultado final
  % :param graph: valor 0 para no graficar y 1 para graficar
  % :returns: xk calculado y numero iteraciones

  
  % Si el numero de argumento es igual a 3
  if nargin == 3
    % Se declara con el valor por defecto
    graph = 1
  endif
  
  % Verificar el tipo de dato de func
  if ~isa(func, 'char')
    disp("La funcion debe ser un string")
    % Se finaliza la ejecucion
    return
  endif
  
  % Verificar el tipo de dato de xk
  if ~isa(xk, 'double')
    disp("El xk debe ser un numero")
    % Se finaliza la ejecucion
    return
  endif
  
  % Verificar que y no sea cero
  if y == 0
    disp("La constante y no puede ser cero")
    % Se finaliza la ejecucion
    return
  endif

  % Verificar el tipo de dato de tol
  if ~isa(tol, 'double')
    disp("La tolerancia debe ser un numero")
    % Se finaliza la ejecucion
    return
  endif

  % Verificar que el valor de graph sea 0 o 1
  if graph ~= 1 && graph ~= 0
    disp("El graph debe ser 0 (desactivado) o 1 (activado)")
    % Se finaliza la ejecucion
    return
  endif
  
  
  % Variable que contiene la conversión de la ecuación simbólica
  ec = matlabFunction(sym(func))
  % Variable que contiene la derivada de la función
  dec = matlabFunction(diff(sym(func)))

  % Listas donde se guardan los valores para graficar el error
  lista_fxk = []
  lista_iter = []
  
  % Se inicializa el contador de iteraciones
  ite = 0
  
  while 1
    % Variable que contiene la imagen de xk en la función
    eval_ec = ec(xk)
    
    % Se guardan los valores para la grafica
    if graph == 1
      lista_fxk = [lista_fxk abs(eval_ec)]
      lista_iter = [lista_iter (ite)]
    endif
    
    % Verificar la condición de parada si la imagen del xk es menor o
    % igual que la tolerancia
    if abs(eval_ec) <= tol
      break
    % Si NO se cumple la condición de parada
    else
      % Se calcula el wk y su imagen en la función
      wk = xk + (y * eval_ec)
      eval_wec = ec(wk)

      % Verificar que no se indefina yk
      if (eval_wec - eval_ec) == 0
          disp("El yk se indefine")
          return
      endif
          
      % Se calcula el yk y su imagen en la función
      yk = xk - (y * (eval_ec ** 2 / (eval_wec - eval_ec)))
      eval_yec = ec(yk)

      % Se calcula el zk y su imagen en la función
      z1 = ((wk - yk) / ((xk - yk) * y))
      z2 = ((xk - yk) / ((wk - yk) * y * eval_ec)) * eval_wec
      z3 = ((wk + xk - 2 * yk) / ((xk - yk) * (wk - yk))) * eval_yec
      
      % Verificar que no se indefina zk
      if (z1 - z2 - z3) == 0
          disp("El zk se indefine")
          return
      endif
      
      zk = yk - (eval_yec / (z1 - z2 - z3))
      eval_zec = ec(zk)

      % Se calcula el xk+1 para la siguiente iteración
      h1 = (((yk - zk) * (wk - zk))) / ((xk - zk) * y * (xk - yk))
      h2 = ((((yk - zk) * (xk - zk)) / ((wk - zk) * (wk - yk) * (wk * xk)))
            * eval_wec)
      h3 = (((wk * xk) - (wk * xk) - (xk * zk) + zk ** 2) /
            ((yk - wk) * (yk - xk) * (yk - zk))) * eval_yec
      h4 = (((wk * xk) + (wk * yk) - (2 * wk * zk) + (xk * yk) - (2 * xk * zk) -
             (2 * yk * zk) + (3 * zk ** 2)) / ((zk - wk) * (zk - xk) * (zk - yk)) *
            eval_zec)
      % Verificar que no se indefina el zk
      if (h1 + h2 + h3 + h4) == 0
          disp("El xk+1 se indefine")
          return
      endif
      
      % Se calcula el xk+1 para la siguiente iteración
      xk = zk - (eval_zec / (h1 + h2 + h3 + h4))
      % Se añade una iteración
      ite = ite + 1
    endif
  endwhile
    
  % Si termina el ciclo, grafica el error y retorna el resultado
  if graph == 1
    graficar_error(lista_iter, lista_fxk)
  endif
  
  x_aprox =  xk
  iter = ite
    
endfunction

% Ejemplo de prueba para el método M8
g = '(cos(2*x))**2 - (x**2)'
m8(g, 3/4, 1, 10**-5, 1)
