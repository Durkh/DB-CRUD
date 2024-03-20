#include "GerenciadorDeArquivo.h"


bool GerenciadorDeArquivo::AdicionaImoveis(std::string query. std::vector<Imoveis*> imoveis){
    try{
        if(conn.is_open()){
            pqxx::work txn(conn);

            std::string fields, values;

            pqxx::result r = txn.exec("INSERT INTO " + std::getenv("TABLE") + " " + fields + " VALUES " + values);
            txn.commit();

            //TODO use the values;

        }
    }catch(const std::exception& e){
        std::cout << "error connecting to the database on insert" << std::endl;
        return false;
    }

    return true;
}

std::vector<Imoveis*> GerenciadorDeArquivo::ListaImoveis(std::string query, std::string where){
    try{
        if(conn.is_open()){
            pqxx::work txn(conn);

            std::string fields, values;

            pqxx::result r = txn.exec("SELECT " + query + "FROM " std::getenv("TABLE") " WHERE " + where);
            txn.commit();
        }
    }catch(const std::exception& e){
        std::cout << "error connecting to the database on select" << std::endl;
        return false;
    }

    return true;
}

bool GerenciadorDeArquivo::ModificaImoveis(std::string update, std::string where){
    try{
        if(conn.is_open()){
            pqxx::work txn(conn);

            std::string fields, values;

            txn.exec("UPDATE " + std::getenv("TABLE") + "SET " + update + "WHERE " + where);
            txn.commit();
        }
    }catch(const std::exception& e){
        std::cout << "error connecting to the database on update" << std::endl;
        return false;
    }

    return true;
}

bool GerenciadorDeArquivo::RemoveImoveis(std::string where. std::vector<Imoveis*> imoveis){
    try{
        if(conn.is_open()){
            pqxx::work txn(conn);

            std::string fields, values;

            txn.exec("DELETE FROM " + std::getenv("table") + "WHERE" + where);
            txn.commit();
        }
    }catch(const std::exception& e){
        std::cout << "error connecting to the database on delete" << std::endl;
        return false;
    }

    return true;
}
