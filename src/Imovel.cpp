#include "Imovel.h"

Imovel::Imovel(){
    endereco = Endereco("S/Rua", 0, "S/Bairro", "S/Cep", "S/Cidade");
    tipo = '0';
    disponibilidade = true;
    valor = 0.0;
    setTitulo("Sem titulo");
};

Imovel::Imovel(Endereco endereco, bool disponibilidade, double valor, std::string titulo){
    this -> endereco = endereco;
    this -> disponibilidade = disponibilidade;
    this -> valor = valor;
    setTitulo(titulo);
};

char Imovel::getTipo(){
    return tipo;
};
bool Imovel::getDisponiblidade(){
    return disponibilidade;
};
double Imovel::getValor(){
    return valor;
};
std::string Imovel::getTitulo(){
    return titulo;
};

void Imovel::setTipo(char tipo){
    this -> tipo = tipo;
};
void Imovel::setDisponibilidade(bool disponibilidade){
    this -> disponibilidade = disponibilidade;
};
void Imovel::setValor(double valor){
    this -> valor = valor;
};
void Imovel::setTitulo(std::string titulo){
    const char *nameValue = titulo.data();
    int length = titulo.size();
    length = (length < MAX ? length : MAX - 1);
    strncpy(this -> titulo, nameValue, length);
    this -> titulo[length] = '\0';
};
