#include "Casa.h"
#include "Imovel.h"

Casa::Casa():Imovel(){
    tipo = '1';
    numPavimentos = 0;
    numQuartos = 0;
    areaTerreno = 0;
    areaConstruida = 0;
};

Casa::Casa( Endereco endereco
,  bool disponibilidade, double valor, std::string titulo, int numPavimentos, int numQuartos, double areaTerreno, double areaConstruida)
        :Imovel( endereco, disponibilidade, valor, titulo){
    tipo = '1';
    this -> numPavimentos = numPavimentos;
    this -> numQuartos = numQuartos;
    this -> areaTerreno = areaTerreno;
    this -> areaConstruida = areaConstruida;
};

int Casa::getNumPavimentos(){
    return numPavimentos;
};
int Casa::getNumQuartos(){
    return numQuartos;
};
double Casa::getAreaTerreno(){
    return areaTerreno;
};
double Casa::getAreaConstruida(){
    return areaConstruida;
};

void Casa::setNumPavimentos(int numPavimentos){
    this -> numPavimentos = numPavimentos;
};
void Casa::setNumQuartos(int numQuartos){
    this -> numQuartos = numQuartos;
};
void Casa::setArea(double areaTerreno){
    this -> areaTerreno = areaTerreno;
};
void Casa::setAreaConstruida(double areaConstruida){
    this -> areaConstruida = areaConstruida;
};

