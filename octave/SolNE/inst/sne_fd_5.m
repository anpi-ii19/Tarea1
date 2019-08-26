%     Metodo  mejorado de Muller y Biseccion para encontrar el cero de una funcion
%     :param str_funcion: string con la funcion que se debe evaluar
%     :param a: limite inferior del dominio a resolver
%     :param b: limite superior del dominio a resolver
%     :param tol: tolerancia al fallo de debe tener el resultado final
%     :param graph: valor 0 para no graficar o 1 para graficar
%     :returns: lista con dos elementos, xk calculado y numero iteraciones
function [x_aprox, iter] = sne_fd_5(str_funcion, a,b, tol, graph)
    if nargin == 4  % Si el numero de argumentos es igual a 4
        graph = 1   % Se declara con el valor por defecto
    end

    % Se verifica el tipo de dato de str_funcion
    if ~isa(str_funcion, 'char')
        error("str_funcion debe ser un char, no %s.", class(str_funcion))
    end

    % Se verifica el tipo de dato de a
    if ~isa(a, 'double')
        error("a debe ser un double, no %s", class(a))
    end

    % Se verifica el tipo de dato de b
    if ~isa(a, 'double')
        error("b debe ser un double, no %s", class(b))
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
        c = a+(b-a)/2 # valor inicial de c (biseccion)
        xk=c
        while 1
            fxk = f(xk);  % Se evalua la funcion

            if graph == 1
                % Se guardan los valores para la grafica
                lista_fxk = [lista_fxk abs(fxk)]
                lista_iter = [lista_iter (iter)]
            end  % graph == 1

            if abs(fxk) <= tol  % Se verifica la condicion de parada
                break;

            else
                c_new =   aux_solve_cuadratic(a,b,c,f) % resolver la
                if (c_new>a & c_new<b) | (c_new<a & c_new>b)
                c = c_new

                else
                    c = a+(b-a)/2
                end
                iter += 1
                xk=c
                x_aprox=xk
            end

        end  % while 1
    end


  %     Metodo auxiliar para resolver una ecuacion cuadratica (Muller)
  %     :param x0: numero real
  %     :param x1: numero real
  %     :param x2: numero real
  %     :param f: funcion a evaluar
  %     :returns: cero de la funcion cuadratica
  function [x] = aux_solve_cuadratic(x0,x1,x2,func)
    f = matlabFunction(sym(func));
    f0 = f(x0)
    f1 = f(x1)
    f2 = f(x2)
    c =  f2
    b1 = (x0-x2)**2*(f1-f2)-( x1-x2)**2*(f0-f2)
    b2 = (x0-x1)*(x0-x2)*(x1-x2)
    b=b1/b2
    a1 =   (x1-x2)*(f0-f2)-((x0-x2)*(f1-f2) )
    a2 = (x0-x1)*(x0-x2)*(x1-x2)
    a=a1/a2
    if b<0
      signb=-1
    else
      signb=1
    end
    x=x2 - (2*c)/(b+signb*(b**2-4*a*c)**(1/2))
  end



funcion1 = 'cos(2*x)^2 - x^2';
disp(funcion1);
[x_aprox1, iter1] = sne_fd_5(funcion1, 0,3,5*10**-3,0);

funcion2 = 'x**3- x - 1';
disp(funcion2);
[x_aprox2, iter2] = sne_fd_5(funcion2, 0,3,5*10**-3,0);
