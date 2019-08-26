% Metodo parametrico de Ostrowski-Chun para encontrar el cero de una funcion
%   :param str_funcion: string con la funcion que se debe evaluar
%   :param x0: valor de x inicial con el cual aplicar el metodo
%   :param a1:  constante que es un numero real, excepto cero.
%   :param a2: constante que es un numero real, excepto cero.
%   :param b1: constante que es un numero real, excepto cero.
%   :param b2: constante que es un numero real, excepto cero.
%   :param alpha: constante que es un numero real, excepto cero.
%
%   :param tol: tolerancia al fallo de debe tener el resultado final
%   :param graph: valor 0 para no graficar o 1 para graficar
%   :returns: lista con dos elementos, xk calculado y numero iteraciones
    function [x_aprox, iter] = sne_fd_6(str_funcion, xk,a1,a2,b1,b2, alpha, tol, graph, max_iter)
    if nargin == 4  % Si el numero de argumentos es igual a 4
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


    % Se verifica el tipo de dato de a1
    if ~isa(a1, 'double')
        error("a1 debe ser un double, no %s", class(a1))
    end
    % Se verifica el tipo de dato de a2
    if ~isa(a2, 'double')
        error("a2 debe ser un double, no %s", class(a2))
    end
    % Se verifica el tipo de dato de b1
    if ~isa(b1, 'double')
        error("b1 debe ser un double, no %s", class(b1))
    end
    % Se verifica el tipo de dato de b2
    if ~isa(b2, 'double')
        error("b2 debe ser un double, no %s", class(b2))
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

    f = matlabFunction(sym(str_funcion));   % Se obtiene la funcion

        % Listas donde se guardaran los valores para la grafica de error
        lista_fxk = [];
        lista_iter = [];

        iter = 0;  % Se inicializa el contador de iteraciones

        w  = @(x1,x2) (f(x1)-f(x2))/(x1-x2);
        while 1
            fxk = f(xk);  % Se evalua la funcion

            if graph == 1
                % Se guardan los valores para la grafica
                lista_fxk = [lista_fxk abs(fxk)]
                lista_iter = [lista_iter (iter)]
            end  % graph == 1

            if abs(fxk) <= tol || iter >=max_iter  % Se verifica la condicion de parada
                break;

            else
                zk= xk+f(xk)**2
                yk=xk-alpha*(f(xk)/w(zk,xk))
                xk= yk - (f(yk)/w(zk,xk))*(  f(xk)/(a1*f(xk)+a2*f(yk)) +  (b1*f(xk)+b2*f(yk))/f(xk))
                iter+=1
                x_aprox=xk
            end  % abs(f(xk)) <= tol

        end  % while 1
    end

funcion1 = 'cos(2*x)^2 - x^2';
disp(funcion1);
[x_aprox1, iter1] = sne_fd_6(funcion1, 0.99, 0.9,2,2.8,2.5,1,5*10**-5,0,200);

funcion2 = 'x**3- x - 1';
disp(funcion2);
[x_aprox2, iter2] = sne_fd_6(funcion2, 2, 1,2,3,4,1,5*10**-5,0,200);
