#include "header.h"
void ExibeMenu();
void exibeMenuListar();
void exibeMenuDisp();
void separador();
void limpaTela();
void ExibeSubSubMenu();
void cabecalho();
void escolha();
double inputValor();
int inputInteiro();
void cadatrarImoveis();
void TiraBarraN(char *str);
bool verificaStr(string nameStr);
vector<Imovel *> cadatrarImovel();
string inputStr(const string name);
//void cep(Apartamento &);
void buscaCep(char *, Apartamento &);
//void cep(int i);
void TiraBarraN(char *str)
{
    int i;
    for (i = 0; str[i] != '\0'; i++)
    {
        if (str[i] == '\n')
            str[i] = '\0';
    }
}
enum
{

    APTO = 1,
    CASA = 2,
    TERRENO = 3
};
int countC = 0, countD = 0, countE = 0;
void ExibeMenu()
{
    cabecalho();
    printf("\t 1- Cadastrar imovel\n"
           "\t 2- Listar Imoveis\n"
           "\t 3- Buscar imovel\n"
           "\t 4- Remover imovel\n"
           "\t 5- Editar registro\n"
           "\t 6- Salvar os dados\n"
           "\t 7- Sair\n");
}
void ExibeSubSubMenu()
{
    cabecalho();
    printf("Voce deseja adicionar um(a): \n"
           "\t 1- Apartamento\n"
           "\t 2- Casa\n"
           "\t 3- Terreno\n"
           "\t 4- Voltar\n");
}
void exibeMenuListar()
{
    cabecalho();
    printf("\t 1- Exibir todos imoveis\n"
           "\t 2- Exibir imoveis disponiveis por tipo\n"
           "\t 3- Exibir imoveis disponiveis para alugar ou vender\n"
           "\t 4- Voltar\n");
}
void exibeMenuBuscar()
{
    cabecalho();
    printf("\t 1- Buscar imovel por titulo\n"
           "\t 2- Buscar imovel por bairro\n"
           "\t 3- Buscar imovel por cidade\n"
           "\t 4- Buscar imovel por valor maximo\n"
           "\t 5- Buscar imovel por bairro e valor maximo\n"
           "\t 6- Buscar imovel por cidade e valor maximo\n"
           "\t 7- Buscar imovel por bairro e disponibilidade\n"
           "\t 8- Buscar imovel por cidade e disponibilidade\n"
           "\t 9- Voltar\n");
}
void exibeMenuDisp()
{
    cabecalho();
    printf("\t 1- Disponiveis para venda\n"
           "\t 2- Disponiveis para aluguel\n"
           "\t 3- Voltar\n");
}
void exibeDisp()
{
    printf("\t 1- Disponiveis para venda\n"
           "\t 2- Disponiveis para aluguel\n");
}
void escolha()
{
    puts("0- Nao");
    puts("1- Sim");
}
void limpaTela()
{
    printf("\e[H\e[2J");
}
void cabecalho()
{
    printf("==========================================================================\n"
           "||\t\t   Sistema de gerenciamento de imoveis       \t\t||"
           "==========================================================================\n");
}
void separador()
{
    printf("==========================================================================\n");
}

string inputStr(const string name)
{
    string str;
    while(1)
    {
        cout<<name;
        //cin.ignore();
        getline(cin,str);
        if(verificaStr(str))
            break;
    }
    return str;
}
int inputInteiro()
{
    int valor;
    char tempValor[MAX];
    while (1)
    {
        fgets(tempValor, MAX, stdin);
        valor = strtol(tempValor, NULL, 0);
        if (valor > 0)
        {
            break;
        }
        else
        {
            printf("Digite um valor válido: ");
        }
    }
    return valor;
}
double inputValor()
{
    float valor;
    char tempValor[MAX];
    char *ptNull;
    while (1)
    {
        fgets(tempValor, MAX, stdin);
        valor = strtod(tempValor, &ptNull);
        if (valor > 0)
        {
            break;
        }
        else
        {
            printf("Digite um Valor válido: ");
        }
    }
    return valor;
}
bool verificaStr(string strC)
{

    int j, count = 0;
    for (j = 0; j <= strC.size(); j++)
    {
        if (!(isspace(strC[j])) && strC[j] != '\0')
            count++;
    }
    if (count > 0)
        return 1;
    else
        return 0;
}