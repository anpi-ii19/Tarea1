% Metodo de Chun-Kim para encontrar el cero de una funcion
% :param func: string con la funcion que se debe evaluar
% :param xk: valor de x inicial con el cual aplicar el metodo
% :param tol: tolerancia al fallo de debe tener el resultado final
% :param graph: valor 0 para no graficar y 1 para graficar
% :returns: xk calculado y numero iteraciones
function [x_aprox, iter] = sne_ud_2(func, xk, tol, graph)
  % Si el numero de argumento es igual a 3
  if nargin == 3
    % Se declara con el valor por defecto
    graph = 1
  endif
  
  % Verificar el tipo de dato de func
  if ~isa(func, 'char')
    error("La funcion debe ser un string")
  endif
  
  % Verificar el tipo de dato de xk
  if ~isa(xk, 'double')
    error("El xk debe ser un numero")
  endif

  % Verificar el tipo de dato de tol
  if ~isa(tol, 'double')
    error("La tolerancia debe ser un numero")
  endif

      % Se verifica que la tolerancia sea un numero positivo
    if tol < 0
        error("tol debe ser un numero positivo")
    end

  % Verificar que el valor de graph sea 0 o 1
  if graph ~= 1 && graph ~= 0
    error("El graph debe ser 0 (desactivado) o 1 (activado)")
  endif
  
  % Variable que contiene la conversi�n de la ecuaci�n simb�lica
  ec = matlabFunction(sym(func))
  % Variable que contiene la derivada de la funci�n
  dec = matlabFunction(diff(sym(func)))

  % Listas donde se guardan los valores para graficar el error
  lista_fxk = []
  lista_iter = []
  
  % Se inicializa el contador de iteraciones
  ite = 0
  
  while 1
    % Variable que contiene la imagen de xk en la funci�n
    eval_ec = ec(xk)
    
    % Se guardan los valores para la grafica
    if graph == 1
      lista_fxk = [lista_fxk abs(eval_ec)]
      lista_iter = [lista_iter (ite)]
    endif
    
    % Verificar la condici�n de parada si la imagen del xk es menor o
    % igual que la tolerancia
    if abs(eval_ec) <= tol
      break
    % Si NO se cumple la condici�n de parada
    else
      % Variable que contiene la imagen de xk en la derivada de la funci�n
      eval_dec = dec(xk)
      % Verificar que la imagen anterior no indefina el resultado
      if eval_dec == 0
        error("La imagen de un xk en la derivada de la funcion se indefine")
      endif
      
      % Variable que contiene el resultado del metodo de Newton-Raphson
      nr = xk - (eval_ec / eval_dec)
      % Variable que contiene la imagen del nr en la derivada de la funci�n
      eval_dec2 = dec(nr)
        
      % Se calcula el xk+1 para la siguiente iteraci�n
      xk = xk - (1/2) * (3 - (eval_dec2 / eval_dec)) * (eval_ec / eval_dec)
      % Se a�ade una iteraci�n
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

%Ejemplo de prueba para el metodo de Chun-Kim
g = '(cos(2*x))**2 - (x**2)'
sne_ud_2(g, 3/4, 10**-5, 0)