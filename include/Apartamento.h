#pragma once

#include "Imovel.h"

#include <string>

class Apartamento : public Imovel
{
private:
    int andar;
    double valorCondominio;
    double area;
    int numQuartos;
    char posicao[MAX];
    int numVagas;

public:
    Apartamento();
    Apartamento(Endereco endereco, bool disponibilidade, double valor, std::string titulo, int andar, double valorCondominio, double area, int numQuartos, std::string posicao, int numVagas);
    int getAndar();
    double getValorCondominio();
    double getArea();
    int getNumQuartos();
    std::string getPosicao();
    int getNumVagas();

    void setAndar(int andar);
    void setValorCondominio(double valorCondominio);
    void setArea(double area);
    void setNumQuartos(int numQuartos);
    void setPosicao(std::string posicao);
    void setNumVagas(int numVagas);
};