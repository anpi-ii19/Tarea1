pkg load symbolic

function [x_aprox, iter] = darvishi_barati(str_funcion, xk, tol, graph)
    % Metodo de Darvishi-Barati para encontrar el cero de una funcion
    % :param str_funcion: string con la funcion que se debe evaluar
    % :param xk: valor de x inicial con el cual aplicar el metodo
    % :param tol: tolerancia al fallo de debe tener el resultado final
    % :returns: xk calculado y numero iteraciones

    if nargin == 3  % Si el numero de argumento es igual a 3
        graph = 1   % Se declara con el valor por defecto
    end

    % Se verifica el tipo de dato de str_funcion
    if ~isa(str_funcion, 'char')
        disp("La funcion debe estar en un char")
        return  % Se finaliza la ejecucion
    end

    % Se verifica el tipo de dato de xk
    if ~isa(xk, 'double')
        disp("xk debe ser un numero")
        return  % Se finaliza la ejecucion
    end

    % Se verifica el tipo de dato de la tolerancia
    if ~isa(tol, 'double')
        disp("La tolerancia debe ser un numero")
        return  % Se finaliza la ejecucion
    end

    % Se verifica que el valor de graph sea uno o cero
    if graph ~= 1 && graph ~= 0
        disp("graph debe ser cero (desactivado) o uno (activado)")
        return  % Se finaliza la ejecucion
    end

    try
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

            if abs(fxk) <= tol  % Se verifica la condicion de parada
                break;

            else
                % Se calcula el valor de xk en la derivada de f
                df_xk = df(xk)

                if df_xk == 0  % Se verifica para evitar division entre cero
                    break
                end  % df_xk == 0

                % Calculo del numerador
                numerador = funcion(xk - fxk / df_xk)

                xk = xk - (fxk / df_xk) - (numerador / df_xk)
                itr = itr + 1

            end  % abs(f(xk)) <= tol

        end  % while 1

    catch
        disp("Sintaxis de la funcion es incorrecta")
        return  % Se finaliza la ejecucion

    end  % try / catch


    if graph == 1
        graficar_error(lista_iter, lista_fxk)
    end  % graph == 1

    x_aprox = xk
    iter = itr

end  % darvishi_barati(str_funcion, xk, tol, graph)