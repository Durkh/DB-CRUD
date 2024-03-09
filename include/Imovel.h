#pragma once
#include "header.h"
#include "Endereco.h"
#include <string>

class Imovel
{
protected:
    char tipo;
    bool disponibilidade;
    double valor;
    char titulo[MAX];

public:
    Endereco endereco; 

    Imovel();
    Imovel(Endereco endereco, bool disponibilidade, double valor, std::string titulo);

    //virtual void setArea()=0;
    char getTipo();
    bool getDisponiblidade();
    double getValor();
    std::string getTitulo();

    void setTipo(char tipo);
    void setDisponibilidade(bool disponibilidade);
    void setValor(double valor);
    void setTitulo(std::string titulo);
};