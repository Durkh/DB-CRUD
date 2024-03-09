#include "Terreno.h"
#include "Imovel.h"
#include <string>

Terreno::Terreno():Imovel(){
    tipo = '2';
    area = 0.0;
};

Terreno::Terreno(Endereco endereco, bool disponibilidade, double valor, std::string titulo, double area)
    :Imovel(endereco, disponibilidade, valor, titulo){
    tipo = '2';
    this -> area = area;
}

double Terreno::getArea(){
    return area;
};

void Terreno::setArea(double area){
    this-> area = area;
};

