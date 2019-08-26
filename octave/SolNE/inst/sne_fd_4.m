% Metodo M4 para encontrar el cero de una funcion
% :param str_funcion: string con la funcion que se debe evaluar
% :param xk: valor de x inicial con el cual aplicar el metodo
% :param y: constante que es un numero real, excepto cero.
% :param tol: tolerancia al fallo de debe tener el resultado final
% :returns: xk calculado y numero iteraciones
function [x_aprox, iter] = sne_fd_4(str_funcion, xk, y, tol, graph)
    if nargin == 4  % Si el numero de argumentos es igual a 3
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

            if abs(fxk) <= tol  % Se verifica la condicion de parada
                break;

            else
                wk = xk + (y * fxk)
                fwk=f(wk)
                yk=xk - (y * (fxk**2 / (fwk - fxk)))
                fyk=f(yk)
                y1 = ((wk - yk) / ((xk - yk) * y))
                y2 = ((xk - yk) / ((wk - yk) * y * fxk)) * fwk
                y3 = ((wk + xk - 2*yk) / ((xk - yk) * (wk - yk))) * fyk
                xk = yk - (fyk / (y1 - y2 - y3))
                itr += 1

            end  % abs(f(xk)) <= tol

        end  % while 1
    end

funcion1 = 'cos(2*x)^2 - x^2';
disp(funcion1);
[x_aprox1, iter1] = sne_fd_4(funcion1, 0,4, 10^-5);

funcion2 = 'x**3- x - 1';
disp(funcion2);
[x_aprox2, iter2] = sne_fd_4(funcion2, 3/4,1,5*10^-5);