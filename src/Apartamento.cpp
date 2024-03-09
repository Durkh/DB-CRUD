#include "Apartamento.h"
#include "Imovel.h"

Apartamento::Apartamento() : Imovel()
{
    tipo = '0';
    andar = 0;
    valorCondominio = 0;
    area = 0;
    numQuartos = 0;
    posicao[0] = '\0';
    numVagas = 0;
};

Apartamento::Apartamento( Endereco endereco, bool disponibilidade, double valor, std::string titulo, int andar, double valorCondominio, double area, int numQuartos, std::string posicao, int numVagas) 
        : Imovel( endereco, disponibilidade, valor, titulo)
{
    tipo = '0';
    this->andar = andar;
    this->valorCondominio = valorCondominio;
    this->area = area;
    this->numQuartos = numQuartos;
    setPosicao(posicao);
    this->numVagas = numVagas;
};

int Apartamento::getAndar()
{
    return andar;
}
double Apartamento::getValorCondominio()
{
    return valorCondominio;
};
double Apartamento::getArea()
{
    return area;
};
int Apartamento::getNumQuartos()
{
    return numQuartos;
};
std::string Apartamento::getPosicao()
{
    return posicao;
};
int Apartamento::getNumVagas()
{
    return numVagas;
};

void Apartamento::setAndar(int andar)
{
    this->andar = andar;
};
void Apartamento::setValorCondominio(double valorCondominio)
{
    this->valorCondominio = valorCondominio;
};
void Apartamento::setArea(double area)
{
    this->area = area;
};
void Apartamento::setNumQuartos(int numQuartos)
{
    this->numQuartos = numQuartos;
};
void Apartamento::setPosicao(std::string posicao)
{
    const char *nameValue = posicao.data();
    int length = posicao.size();
    length = (length < MAX ? length : MAX - 1);
    strncpy(this->posicao, nameValue, length);
    this->posicao[length] = '\0';
};
void Apartamento::setNumVagas(int numVagas)
{
    this->numVagas = numVagas;
};
