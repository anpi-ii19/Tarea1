pkg load symbolic

funcion1 = 'cos(2*x)^2 - x^2'
funcion2 = 'exp(x) - x - 2'
funcion3 = 'cos(x) - x'

%% Ejemplo de prueba para el metodo de Weerakoon_Fernando
%sne_ud_1(funcion1, 3/4, 10^-5, 0)
%sne_ud_1(funcion2, 3/4, 10^-5, 0)
%sne_ud_1(funcion3, 3/4, 10^-5, 0)
%
%
%% Ejemplo de prueba para el metodo de Chun-Kim
%sne_ud_2(funcion1, 3/4, 10^-5, 0)
%sne_ud_2(funcion2, 3/4, 10^-5, 0)
%sne_ud_2(funcion3, 3/4, 10^-5, 0)
%
%
%% Ejemplo de prueba para el metodo de Ozban-Homeier
%sne_ud_3(funcion1, 3/4, 10^-5, 0)
%sne_ud_3(funcion2, 3/4, 10^-5, 0)
%sne_ud_3(funcion3, 3/4, 10^-5, 0)
%
%% Ejemplo de prueba para el metodo de Darvishi - Barati
%sne_ud_4(funcion1, 2/4, 10^-5, 0)
%sne_ud_4(funcion2, 2/4, 10^-5, 0)
%sne_ud_4(funcion3, 3/4, 10^-5, 0)
%
%
%% Ejemplo de prueba para el metodo de Ostrowski de cuarto orden
%sne_ud_5(funcion1, 2/4, 10^-5, 0)
%sne_ud_5(funcion2, 2/4, 10^-5, 0)
%sne_ud_5(funcion3, 3/4, 10^-5, 0)
%
%
%% Ejemplo de prueba para el metodo de Traub
%sne_ud_6(funcion1, 2/4, 10^-5, 0)
%sne_ud_6(funcion2, 2/4, 10^-5, 0)
%sne_ud_6(funcion3, 3/4, 10^-5, 0)
%
%
%% Ejemplo de prueba para el metodo de Steffensen
%sne_fd_1(funcion1, 5/7, 10^-5, 0)
%sne_fd_1(funcion1, 5/7, 10^-5, 0)
%sne_fd_1(funcion1, 5/7, 10^-5, 0)
%
%
%% Ejemplo de prueba para el metodo M8
%sne_fd_2(funcion1, 5/7, 3/4, 10^-5, 0)
%sne_fd_2(funcion1, 5/7, 3/4, 10^-5, 0)
%sne_fd_2(funcion1, 5/7, 3/4, 10^-5, 0)
%
%
%% Ejemplo de prueba para el metodo IODF
%sne_fd_3(funcion1, 5/7, 3/4, 10^-5, 0)
%sne_fd_3(funcion1, 5/7, 3/4, 10^-5, 0)
%sne_fd_3(funcion1, 5/7, 3/4, 10^-5, 0)
%

%% Ejemplo de prueba para el metodo de M4
% sne_fd_4(funcion1, 3/4,1,5*10**-5,1)
% sne_fd_4(funcion2, 3/4,1,5*10**-5,1)
% sne_fd_4(funcion3, 3/4,1,5*10**-5,1)

%
%% Ejemplo de prueba para el metodo de Muller-Biseccion
% sne_fd_5(funcion1, 0,3,5*10**-3,0);
% sne_fd_5(funcion2, 0,3,5*10**-3,0);
% sne_fd_5(funcion3, 0,3,5*10**-3,0);

%% Ejemplo de prueba para el metodo parametrico de Ostrowski-Chun
% sne_fd_6(funcion1, 0.99, 0.9,2,2.8,2.5,1,5*10**-5,0,200);
% sne_fd_6(funcion2, 0.99, 0.9,2,2.8,2.5,1,5*10**-5,0,200);
% sne_fd_6(funcion3, 0.99, 0.9,2,2.8,2.5,1,5*10**-5,0,200);
