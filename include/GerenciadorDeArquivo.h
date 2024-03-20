#pragma once

#include "Imobiliaria.h"
#include "Imovel.h"
#include "Apartamento.h"
#include "Casa.h"
#include "Terreno.h"
#include <pqxx/pqxx>

class GerenciadorDeArquivo
{
private:
    pqxx::connection conn;

public:
    GerenciadorDeArquivo(std::string URL){
        this->conn = pqxx::connection(URL);
    }

    bool AdicionaImoveis(std::string query. std::vector<Imoveis*> imoveis);
    std::vector<Imoveis*> ListaImoveis(std::string query);
    bool ModificaImoveis(std::string query);
    bool RemoveImoveis(std::string where. std::vector<Imoveis*> imoveis);


    ~GerenciadorDeArquivo();
};


