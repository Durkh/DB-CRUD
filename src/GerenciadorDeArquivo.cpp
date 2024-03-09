#include "GerenciadorDeArquivo.h"

string toStringApartamento(Imovel *);
string toStringCasa(Imovel &);
string toStringTerreno(Imovel &);
void outputLine(std::ostream &output, Imovel &record);

bool GerenciadorDeArquivo::SalvaArquivo()
{
    bool disponibilidade;
    double valor;
    string titulo;
    double area1;
    Endereco endereco;
    int andar;
    double valorCondominio;
    double area2;
    string posicao;
    int numVagas;
    int numPavimentos;
    int numQuartos;
    
    Apartamento ap;
    Terreno t1;
    Casa c1;

    ofstream outputFile;
    outputFile.open("imoveis.dat", ios::binary);

    if (!outputFile.is_open())
    {
        cerr << "Erro ao tentar abrir o arquivo" << endl;
        outputFile.close();
        exit(1);
    }



    cout << "Salvando " << lista.size() << " imoveis." << endl;

    for (int i = 0; i < lista.size(); i++)
    {
        if (lista[i]->getTipo() == '0')
        {
            titulo = lista[i]->getTitulo();
            valor = lista[i]->getValor();
            disponibilidade = lista[i]->getDisponiblidade();
            area1 = ((Apartamento *)lista[i])->getArea();
            andar = ((Apartamento *)lista[i])->getAndar();
            numVagas = ((Apartamento *)lista[i])->getNumVagas();
            valorCondominio = ((Apartamento *)lista[i])->getValorCondominio();
            posicao = ((Apartamento *)lista[i])->getPosicao();
            endereco.setCidade(((Apartamento *)lista[i])->endereco.getCidade());
            endereco.setBairro(((Apartamento *)lista[i])->endereco.getBairro());
            endereco.setLogradouro(((Apartamento *)lista[i])->endereco.getLogradouro());
            endereco.setNumero(((Apartamento *)lista[i])->endereco.getNumero());
            endereco.setCep(((Apartamento *)lista[i])->endereco.getCep());

            ap = Apartamento(endereco, disponibilidade, valor, titulo, andar, valor, area1, numQuartos, posicao, numVagas);
            outputFile.write(reinterpret_cast<const char *>(&ap),
                                sizeof(Apartamento));
        }

        if (lista[i]->getTipo() == '1')
        {
            titulo = lista[i]->getTitulo();
            valor = lista[i]->getValor();
            disponibilidade = lista[i]->getDisponiblidade();
            area1 = ((Casa *)lista[i])->getAreaTerreno();
            area2 = ((Casa *)lista[i])->getAreaConstruida();
            numPavimentos = ((Casa *)lista[i])->getNumPavimentos();
            numQuartos = ((Casa *)lista[i])->getNumQuartos();
            endereco.setCidade(((Casa *)lista[i])->endereco.getCidade());
            endereco.setBairro(((Casa *)lista[i])->endereco.getBairro());
            endereco.setLogradouro(((Casa *)lista[i])->endereco.getLogradouro());
            endereco.setNumero(((Casa *)lista[i])->endereco.getNumero());
            endereco.setCep(((Casa *)lista[i])->endereco.getCep());

            c1 = Casa(endereco, disponibilidade, valor, titulo, numPavimentos, numQuartos, area1, area2);
            outputFile.write(reinterpret_cast<const char *>(&c1),
                                sizeof(Casa));
        }
        if (lista[i]->getTipo() == '2')
        {
            titulo = lista[i]->getTitulo();
            valor = lista[i]->getValor();
            disponibilidade = lista[i]->getDisponiblidade();
            area1 = ((Terreno *)lista[i])->getArea();
            endereco.setCidade(((Terreno *)lista[i])->endereco.getCidade());
            endereco.setBairro(((Terreno *)lista[i])->endereco.getBairro());
            endereco.setLogradouro(((Terreno *)lista[i])->endereco.getLogradouro());
            endereco.setNumero(((Terreno *)lista[i])->endereco.getNumero());
            endereco.setCep(((Terreno *)lista[i])->endereco.getCep());

            t1 = Terreno(endereco, disponibilidade, valor, titulo, area1);
            outputFile.write(reinterpret_cast<const char *>(&t1),
                                sizeof(Terreno));
        }
    }

    outputFile.close();
    return true;
}

bool GerenciadorDeArquivo::leArquivo(Imobiliaria *imob)
{
    vector<Imovel *> lista;
    char tipo;
    //Imovel i;

    Apartamento ap;
    Terreno terreno;
    Casa casa;
    ifstream inFile("imoveis.dat", ios::in);
    if (!inFile)
    {
        cerr << "Erro ao tentar abrir o arquivo" << endl;
        return 1;
    }
    inFile.read(reinterpret_cast<char *>(&tipo), sizeof(char));
    inFile.seekg(-1, inFile.cur);
    while (inFile && !inFile.eof())
    {

        if (tipo == '0')
        {
            inFile.read(reinterpret_cast<char *>(&ap), sizeof(Apartamento));
            //outputLine(cout, ap);
            Apartamento *tempAp = new Apartamento;
            *tempAp = ap;
            imob->cadastraImovel(tempAp);
        }
        if (tipo == '1')
        {
            inFile.read(reinterpret_cast<char *>(&casa), sizeof(Casa));
            //outputLine(cout, casa);
            Casa *tempC = new Casa();
            *tempC = casa;
            imob->cadastraImovel(tempC);
        }
        if (tipo == '2')
        {
            inFile.read(reinterpret_cast<char *>(&terreno), sizeof(Terreno));
            //outputLine(cout, terreno);
            Terreno *tempT = new Terreno();
            *tempT = terreno;
            imob->cadastraImovel(tempT);
        }
        inFile.read(reinterpret_cast<char *>(&tipo), sizeof(char));
        inFile.seekg(-1, inFile.cur);
    }

    inFile.close();

    return 0;
}
void outputLine(std::ostream &output, Imovel &record)
{
    Imovel *ptr = &record;
    output << record.getTitulo() << "\n"
           << setprecision(2) << fixed << record.getValor() << "\n"
           << record.getTipo() << "\n"
           << record.getDisponiblidade() << "\n"
           <<(((Apartamento*)ptr)->getAndar())<<"\n"
           << (((Apartamento*)ptr)->getPosicao())
           << endl;
}

