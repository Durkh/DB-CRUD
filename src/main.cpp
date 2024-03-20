#include <iostream>
#include <laserpants/dotenv/dotenv.h>
#include <sstream>

#include "Imobiliaria.h"
#include "GerenciadorDeTexto.h"
#include "GerenciadorDeArquivo.h"
#include "Front.h"

int main()
{

    dotenv::init("keys.env");

    std::stringstream URL;
    URL <<  "postgresql://" << std::getenv("USER") << ":" << std::getenv("PASSWD") << "@" << std::getenv("HOST") << "/" << std::getenv("DATABASE");

    Imobiliaria imob;
    try{
        GerenciadorDeArquivo f1;
    }catch (const std::exception &e) {
      cerr << "error connecting to database: " << e.what() << std::endl;
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
