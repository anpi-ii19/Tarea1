%{
Funcion para realizar la grafica de error, iteraciones vs | f(xk) |
:param lista_iter: lista con todos los valores que deben graficarse en el eje x
:param lista_xk: lista con todos los valores que deben graficarse en el eje y
%}

function graficarError(eje_x, lista_xk)
    % Lista iteraciones en el eje x
    % Lista fxk en el eje y
    plot(eje_x, eje_y);           % Se realiza la grafica
    grid on;                      % Se activa la malla
    xlabel("iteracion")           % Se nombra el eje x
    ylabel("| f(xk) | ")          % Se nombra el eje y

end % End graficar_error
