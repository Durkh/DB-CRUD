#include <iostream>
#include <pqxx/pqxx> 
#include <laserpants/dotenv/dotenv.h>
#include <sstream>

#include "Imobiliaria.h"
#include "GerenciadorDeTexto.h"
#include "GerenciadorDeArquivo.h"
#include "Front.h"


//#include "menu.h"
void outputImovel(std::ostream &output, Imovel &imovel, int tipo);
void outputImoveis(vector<Imovel *> lista, int tipo);
void buscar(vector<Imovel *> listaPtr, Imobiliaria imob);
void menu(vector<Imovel *> listaPtr, Imobiliaria &imob);
//vector<Imovel *> cadatrarImovel(Imobiliaria imob);
//bool leArquivo(Imobiliaria &imob);
//bool SalvaArquivo(vector<Imovel *> lista);

int main()
{
    Imobiliaria imob;
    GerenciadorDeArquivo f1;

    dotenv::init("keys.env");

    std::stringstream URL;
    URL <<  "postgresql://" << std::getenv("USER") << ":" << std::getenv("PASSWD") << "@" << std::getenv("HOST") << "/" << std::getenv("DATABASE");

    try {
      pqxx::connection c{URL.str()};
      pqxx::work txn(c);
    } catch (const std::exception &e) {
      cerr << e.what() << std::endl;
      return 1;
    }

    Front exibe;
    exibe.menu(&imob);

    f1.setLista(imob.getImoveis());
    if ( f1.SalvaArquivo() )
        cout << "Arquivo Salvo" << endl;
    else
        cout << "Continue tentando" << endl;

    return 0;
} 
