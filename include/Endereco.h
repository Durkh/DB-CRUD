#pragma once
#include "header.h"
#include <string>
#include <iostream>

class Endereco
{    
protected:
    char logradouro[MAX];
    int numero;
    char bairro[MAX];
    char cep[MAX];
    char cidade[MAX];
public:
    //Endereco();
    Endereco(std::string = "", int = 0, std::string = "", std::string = "", std::string = "");
    std::string getAsString();
    std::string getLogradouro();
    int getNumero();
    std::string getBairro();
    std::string getCep();
    std::string getCidade();

    void setLogradouro(std::string logradouro);
    void setNumero(int numero);
    void setBairro(std::string bairro);
    void setCep(std::string cep);
    void setCidade(std::string cidade);

    void setEndereco(std::string logradouro, int numero, std::string bairro, std::string cep, std::string cidade);

};