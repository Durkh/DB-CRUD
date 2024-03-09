#pragma once
#include "GerenciadorDeArquivo.h"

class Front
{
private:
    Imobiliaria *imob;
    /*Imovel imovel;
    Imobiliaria imob;
    vector<Imovel *> listaImoveis;
    vector<int> indices;
    GerenciadorDeArquivo arquivo;*/
public:
    
    void menu(Imobiliaria *);
    void buscar(Imobiliaria *, int);
    void outputImovel(std::ostream &output, Imovel &imovel, int);
    void outputImoveis(vector<Imovel *> lista, int);
    void editarRemover(vector<int> index, int flag, Imobiliaria*);
    //vector<Imovel *> getLista();
};
