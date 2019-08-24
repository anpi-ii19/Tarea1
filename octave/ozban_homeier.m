%Carga del paquete simbólico
pkg load symbolic


function [x_aprox, iter] = ozban_homeier(func, xk, tol, graph)
  % Metodo de Ozban-Homeier para encontrar el cero de una funcion
  % :param func: string con la funcion que se debe evaluar
  % :param xk: valor de x inicial con el cual aplicar el metodo
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
  
  try
    # Variable que contiene la conversión de la ecuación simbólica
    ec = matlabFunction(sym(func))
    # Variable que contiene la derivada de la función
    dec = matlabFunction(diff(sym(func)))

    # Listas donde se guardan los valores para graficar el error
    lista_fxk = []
    lista_iter = []
    
    # Se inicializa el contador de iteraciones
    ite = 0
    
    while 1
      # Variable que contiene la imagen de xk en la función
      eval_ec = ec(xk)
      
      # Se guardan los valores para la grafica
      if graph == 1
        lista_fxk = [lista_fxk abs(eval_ec)]
        lista_iter = [lista_iter (ite)]
      endif
      
      # Verificar la condición de parada si la imagen del xk es menor o
      # igual que la tolerancia
      if abs(eval_ec) <= tol
        break
      # Si NO se cumple la condición de parada
      else
        # Variable que contiene la imagen de xk en la derivada de la función
        eval_dec = dec(xk)
        # Verificar que la imagen anterior no indefina el resultado
        if eval_dec == 0
          disp("La imagen de un xk en la derivada de la funcion se indefine")
          % Se finaliza la ejecucion
          return
        endif
        
        # Variable que contiene el resultado del metodo de Newton-Raphson
        nr = xk - (eval_ec / eval_dec)
        # Variable que contiene la imagen del nr en la derivada de la función
        eval_dec2 = dec(nr)
        # Verificar que la imagen anterior no indefina el resultado
        if eval_dec2 == 0
          disp("La imagen del Newton-Raphson en la derivada se indefine")
          % Se finaliza la ejecucion
          return
        endif
          
        # Se calcula el xk+1 para la siguiente iteración
        xk = xk - (1/2) * ((eval_ec / eval_dec) + (eval_ec / eval_dec2))
        # Se añade una iteración
        ite = ite + 1
      endif
    endwhile
    
    # Si termina el ciclo, grafica el error y retorna el resultado
    if graph == 1
      graficar_error(lista_iter, lista_fxk)
    endif
    
    x_aprox =  xk
    iter = ite
    
  catch
    disp("Sintaxis de la funcion es incorrecta")
    return
  end_try_catch
endfunction

# Ejemplo de prueba para el método de Ozban-Homeier
g = '(cos(2*x))**2 - (x**2)'
ozban_homeier(g, 3/4, 10**-5, 1)
