pkg load symbolic

% Metodo de Weerakoon-Fernando para encontrar el cero de una funcion
% :param str_funcion: string con la funcion que se debe evaluar
% :param xk: valor de x inicial con el cual aplicar el metodo
% :param tol: tolerancia al fallo de debe tener el resultado final
% :param graph: valor 0 para no graficar o 1 para graficar
% :returns: xk calculado y numero iteraciones
function [x_aprox, iter] = weerakoon_fernando(str_funcion, xk, tol, graph)
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

    % Se verifica que el valor de graph sea uno o cero
    if graph ~= 1 && graph ~= 0
        error("graph debe ser 0 (desactivado) o 1 (activado)")
    end

    funcion = matlabFunction(sym(str_funcion));   % Se obtiene la funcion
    df = matlabFunction(diff(sym(funcion)));  % Se calcula la derivada

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
            % Se calcula el valor de xk en la derivada de f
            df_xk = df(xk)

            if df_xk == 0  % Se verifica para evitar division entre cero
                break
            end  % df_xk == 0

            % Variable auxiliar para el calculo del denominador
            denominador_aux = df(xk - fxk / df_xk)

            % Se calcula el denominador entero
            denominador = df_xk + denominador_aux

            % Se verifica denominador para evitar division entre cero
            if denominador == 0
                break
            end  % denominador == 0

            % Se verifica que el nuevo xk no se indefina
            nuevo_xk = xk - ((2 * fxk) / denominador)
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

end  % weerakoon_fernando(str_funcion, xk, tol, graph)

%funcion1 = 'cos(2*x)^2 - x^2';
%disp(funcion1);
%[x_aprox1, iter1] = weerakoon_fernando(funcion1, 3/4, 10^-5);

%funcion2 = 'exp(x) - x^3 - x';
%disp(funcion2);
%[x_aprox2, iter2] = weerakoon_fernando(funcion2, 3/4, 10^-5);
