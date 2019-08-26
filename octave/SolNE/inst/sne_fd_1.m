% Metodo de Steffensen para encontrar el cero de una funcion
% :param str_funcion: string con la funcion que se debe evaluar
% :param xk: valor de x inicial con el cual aplicar el metodo
% :param tol: tolerancia al fallo de debe tener el resultado final
% :param graph: valor 0 para no graficar o 1 para graficar
% :returns: xk calculado y numero iteraciones
function [x_aprox, iter] = sne_fd_1(str_funcion, xk, tol, graph)
    if nargin == 3  % Si el numero de argumentos es igual a 3
        graph = 1   % Se declara con el valor por defecto
    end

    % Se verifica el tipo de dato de str_funcion
    if ~isa(str_funcion, 'char')
        error("str_funcion debe ser un char, no %s.", class(str_funcion))
    end

    % Se verifica el tipo de dato de xk
    if ~isa(xk, 'double')
        error("xk debe ser un double, no %s", class(xk))
    end

    % Se verifica el tipo de dato de la tolerancia
    if ~isa(tol, 'double')
        error("tol debe ser un double, no un %s", class(tol))
    end

    % Se verifica que la tolerancia sea un numero positivo
    if tol < 0
        error("tol debe ser un numero positivo")
    end

    % Se verifica que el valor de graph sea uno o cero
    if graph ~= 1 && graph ~= 0
        error("graph debe ser 0 (desactivado) o 1 (activado)")
    end

    funcion = matlabFunction(sym(str_funcion));   % Se obtiene la funcion

    % Listas donde se guardaran los valores para la grafica de error
    lista_fxk = [];
    lista_iter = [];

    itr = 0;  % Se inicializa el contador de iteraciones

    while 1
        fxk = funcion(xk);  % Se evalua la funcion

        if graph == 1
            % Se guardan los valores para la grafica
            lista_fxk = [lista_fxk abs(fxk)]
            lista_iter = [lista_iter (itr)]
        end  % graph == 1

        if abs(fxk) <= tol % Se verifica la condicion de parada
            break;

        else
            % Variable auxiliar para el calculo del denominador
            denominador_aux = funcion(xk + fxk)

            % Se calcula el denominador entero
            denominador = denominador_aux - fxk

            % Se verifica denominador para evitar division entre cero
            if denominador == 0
                break
            end  % denominador == 0

            % Se verifica que el nuevo xk no se indefina
            nuevo_xk = xk - ((fxk ^ 2) / denominador)
            if isnan(nuevo_xk) || isinf(nuevo_xk)
                error('Este metodo no es apto para la funcion ingresada')
            end  % isnan(nuevo_xk) || isinf(nuevo_xk)

            xk = nuevo_xk
            itr = itr + 1

        end  % abs(f(xk)) <= tol

    end  % while 1

    if graph == 1
        graficar_error(lista_iter, lista_fxk)
    end  % graph == 1

    x_aprox = xk
    iter = itr

end  % steffensen(str_funcion, xk, tol, graph)

