pkg load symbolic

%Weerakoon_Fernando
funcion1 = 'cos(2*x)^2 - x^2';
%sne_ud_1(funcion1, 3/4, 10^-5);

funcion2 = 'exp(x) - x^3 - x';
%sne_ud_1(funcion2, 3/4, 10^-5);


%Ejemplo de prueba para el metodo de Chun-Kim
%sne_ud_2(funcion1, 3/4, 10^-5, 0)
%sne_ud_2(funcion2, 3/4, 10^-5, 0)


% Ejemplo de prueba para el metodo de Ozban-Homeier
%sne_ud_3(funcion1, 3/4, 10^-5, 1)
%sne_ud_3(funcion2, 3/4, 10^-5, 1)

%Darvishi - Barati
%sne_ud_4(funcion1, 1, 10 ^ -5)
%sne_ud_4(funcion2, 2 / 4, 10 ^ -5);
