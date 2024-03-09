#include "Imobiliaria.h"

void Imobiliaria::cadastraImovel(Imovel *imovelParaCadastro)
{
    listaImoveis.push_back(imovelParaCadastro);
}

void Imobiliaria::removerImoveis(std::vector<int> indexes)
{
    int j = 0;
    for (int i : indexes)
    {
        delete listaImoveis[i-j];
        listaImoveis.erase(listaImoveis.begin() + i-j);
        j++;
    }
}

void Imobiliaria::editarImovel(Imovel *novoImovel, int index)
{
    delete listaImoveis[index];
    listaImoveis.erase(listaImoveis.begin() + index);
    listaImoveis.insert(listaImoveis.begin() + index, novoImovel);
}
std::vector<Imovel *> Imobiliaria::getImoveis()
{
    return listaImoveis;
}

std::vector<Imovel *> Imobiliaria::getImoveis(std::vector<int> indexes)
{
    std::vector<Imovel *> imoveisRetorno;
    for (int i : indexes)
    {
        imoveisRetorno.push_back(listaImoveis[i]);
    }
    return imoveisRetorno;
}

std::vector<int> Imobiliaria::indexPorTipo(char tipo)
{
    std::vector<int> indexes;
    for (int i = 0; i < listaImoveis.size(); i++)
    {
        if (listaImoveis[i]->getTipo() == tipo)
        {
            indexes.push_back(i);
        }
    }
    return indexes;
}

std::vector<int> Imobiliaria::indexPorDisponibilidade(bool disp)
{
    std::vector<int> indexes;
    for (int i = 0; i < listaImoveis.size(); i++)
    {
        if (listaImoveis[i]->getDisponiblidade() == disp)
        {
            indexes.push_back(i);
        }
    }
    return indexes;
}

std::vector<int> Imobiliaria::indexPorBairro(std::string bairroBuscado)
{
    std::vector<int> indexes;
    std::string bairroExistente;

    bairroBuscado = format.strToLower(bairroBuscado);
    bairroBuscado = format.removeAcento(bairroBuscado);
    
    for (int i = 0; i < listaImoveis.size(); i++)
    {
        bairroExistente = listaImoveis[i]->endereco.getBairro();

        bairroExistente = format.strToLower(bairroExistente);
        bairroExistente = format.removeAcento(bairroExistente);

        if (bairroExistente.find(bairroBuscado) < bairroExistente.length())
        {
            indexes.push_back(i);
        }
    }
    return indexes;
}

std::vector<int> Imobiliaria::indexPorCidade(std::string cidadeBuscada)
{
    std::vector<int> indexes;
    std::string cidadeExistente;

    cidadeBuscada = format.strToLower(cidadeBuscada);
    cidadeBuscada = format.removeAcento(cidadeBuscada);

    for (int i = 0; i < listaImoveis.size(); i++)
    {
        cidadeExistente = listaImoveis[i]->endereco.getCidade();

        cidadeExistente = format.strToLower(cidadeExistente);
        cidadeExistente = format.removeAcento(cidadeExistente);

        if (cidadeExistente.find(cidadeBuscada) < cidadeExistente.length())
        {
            indexes.push_back(i);
        }
    }
    return indexes;
}

std::vector<int> Imobiliaria::indexPorTitulo(std::string tituloBuscado)
{
    std::vector<int> indexes;
    std::string tituloExistente;

    tituloBuscado = format.strToLower(tituloBuscado);
    tituloBuscado = format.removeAcento(tituloBuscado);

    for (int i = 0; i < listaImoveis.size(); i++)
    {
        tituloExistente = listaImoveis[i]->getTitulo();

        tituloExistente = format.strToLower(tituloExistente);
        tituloExistente = format.removeAcento(tituloExistente);

        if (tituloExistente.find(tituloBuscado) < tituloExistente.length())
        {
            indexes.push_back(i);
        }
    }
    return indexes;
}

std::vector<int> Imobiliaria::indexPorValor(double valor)
{
    std::vector<int> indexes;
    for (int i = 0; i < listaImoveis.size(); i++)
    {
        if (listaImoveis[i]->getValor() <= valor)
        {
            indexes.push_back(i);
        }
    }
    return indexes;
}

std::vector<int> Imobiliaria::combinarFiltros(std::vector<int> indexes1, std::vector<int> indexes2)
{
    std::vector<int> indexesEmAmbos;

    for (int i = 0; i < indexes1.size(); i++)
    {
        for (int j = 0; j < indexes2.size(); j++)
        {
            if (indexes1[i] == indexes2[j])
            {
                indexesEmAmbos.push_back(indexes1[i]);
                //Passa pro proximo de indexes1
                i++;
                j = 0;
            }
        }
    }
    return indexesEmAmbos;
}