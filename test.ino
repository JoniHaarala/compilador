#include <nombreDeLibreria.extension>
int MD1;
int MD2;
int MD3;
int MD4;
MD4 = 2;
MD3 = 2;
MD2 = 2;
MD1 = 2;

void setup(){
    pinMode(MD1, INPUT);
    pinMode(MD2, INPUT);
    pinMode(MD3, INPUT);
    pinMode(MD4, OUTPUT);
}

loop setup(){
    avanzar();
    giro_izquierda();
    parar();
}
