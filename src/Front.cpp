#include "Front.h"
#include "menu.h"

void Front::menu(Imobiliaria *imob)
{
    int opcao, subopcao, subsubopcao, verificacao;
    string name1, name2;
    Apartamento ap;
    Casa c1;
    Terreno t1;
    int disp;
    int tip;
    int num;

    std::string titulo;
    double valor;
    double area1;
    Endereco endereco;
    int andar;
    double valorCondominio;
    int numQuartos;
    int numVagas;
    string posicao;
    double area2;
    int numPavimentos;

    while (1)
    {
        limpaTela();
        ExibeMenu();
        printf("Digite a opcao desejada: ");
        cin >> opcao;
        if (opcao == 7)
        {
            break;
        }
        if(opcao>7 || opcao<0){
            puts("Opcao invalida");
            break;
        }
        switch (opcao)
        {
        case 1: //Cadastra imoveis
            limpaTela();
            while (1)
            {
                limpaTela();
                cabecalho();
                printf("Voce deseja adicionar um(a): \n"
                       "\t 1- Apartamento\n"
                       "\t 2- Casa\n"
                       "\t 3- Terreno\n"
                       "\t 4- Voltar\n");
                tip = inputInteiro();
                if (tip < 1 || tip > 4){
                    break;
                    puts("Opcao invalida");

                }
                puts("Opcao invalida");
            }
            switch (tip)
            {
            case APTO:

                
                titulo=inputStr("Digite o titulo: ");
                while (1)
                {
                    limpaTela();
                    cabecalho();
                    puts("O imovel esta disponivel para?");
                    puts("\t1 - Aluguel");
                    puts("\t2 - Venda");

                    printf("Digite um valor válido: ");
                    disp = inputInteiro();
                    if (disp == 1 || disp == 2)
                        break;
                    puts("Opcao invalida");
                }
                disp=(disp == 1 ? false : true);
                cout << "Digite o valor: " << endl;
                valor=inputValor();
                printf("Digite o numero de quartos: ");
                numQuartos=inputInteiro();
                printf("Digite a quantidade de vagas na garagem: ");
                numVagas=inputInteiro();
                printf("Digite o preco do condominio: ");
                valorCondominio=inputValor();
                posicao=inputStr("Digite a posicao do apartamento: ");
                printf("Digite a area do apartamento: ");
                area1=(inputValor());
                printf("Digite o andar: ");
                andar=inputInteiro();
                endereco.setCep(inputStr("Digite o cep: "));
                endereco.setCidade(inputStr("Digite a cidade: "));
                endereco.setBairro(inputStr("Digite o bairro: "));
                endereco.setLogradouro(inputStr("Digite a rua: "));
                printf("Digite o numero: ");
                num = inputInteiro();
                endereco.setNumero(num);

                imob->cadastraImovel(new Apartamento(endereco,disp,valor,titulo,andar,valorCondominio,area1,numQuartos,posicao,numVagas));
                break;
            case CASA:
                titulo=inputStr("Digite o titulo: ");
                while (1)
                {
                    limpaTela();
                    cabecalho();
                    puts("O imovel esta disponivel para?");
                    puts("\t1 - Aluguel");
                    puts("\t2 - Venda");
                    printf("Digite um valor válido: ");
                    cin >> disp;
                    cin.ignore();
                    if (disp == 1 || disp == 2)
                        break;
                    puts("Opcao invalida");
                }
                disp=(disp == 1 ? false : true);
                cout << "Digite o valor: " << endl;
                valor=inputValor();
                printf("Digite o numero de quartos: ");
                numQuartos=inputInteiro();
                printf("Digite o numero de pavimentos: ");
                numPavimentos=inputInteiro();
                printf("Digite a area do terreno: ");
                area1=inputValor();
                printf("Digite a area construida: ");
                area2=inputValor();

                endereco.setCep(inputStr("Digite o cep: "));
                endereco.setCidade(inputStr("Digite a cidade: "));
                endereco.setBairro(inputStr("Digite o bairro: "));
                endereco.setLogradouro(inputStr("Digite a rua: "));
                printf("Digite o numero: ");
                num = inputInteiro();
                endereco.setNumero(num);
                
                imob->cadastraImovel(new Casa(endereco,disp,valor,titulo,numPavimentos,numQuartos,area1,area2));
                break;
            case TERRENO:
                titulo = inputStr("Digite o titulo: ");
                while (1)
                {
                    limpaTela();
                    cabecalho();
                    puts("O imovel esta disponivel para?");
                    puts("\t1 - Aluguel");
                    puts("\t2 - Venda");
                    printf("Digite um valor válido: ");
                    cin >> disp;
                    cin.ignore();
                    if (disp == 1 || disp == 2)
                        break;
                    puts("Opcao invalida");
                }
                disp = (disp == 1 ? false : true);
                cout << "Digite o valor: " << endl;
                valor = inputValor();
                cout << "Digite a area do terreno: ";
                area1 = inputValor();
                endereco.setCidade(inputStr("Digite a cidade: "));
                endereco.setBairro(inputStr("Digite o bairro: "));
                endereco.setLogradouro(inputStr("Digite a rua: "));
                printf("Digite o numero: ");
                endereco.setNumero(inputInteiro());

                imob->cadastraImovel(new Terreno(endereco, disp, valor, titulo, area1));
                break;
            }
            break;

        case 2: //Listar imoveis
            limpaTela();
            exibeMenuListar();
            subopcao = inputInteiro();
            if (subopcao == 7){
                break;
            }
            switch (subopcao)
            {
            case 1:
                limpaTela();
                cabecalho();
                outputImoveis(imob->getImoveis(), 1);
                printf("Para voltar digite 1\n");
                verificacao = inputInteiro();
                if (verificacao == 1)
                    break;
            case 2: //Exibe imoveis por  tipo
                limpaTela();
                ExibeSubSubMenu();
                printf("Digite a opcao desejada: ");
                subsubopcao = inputInteiro();
                if (subsubopcao == 4)
                {
                    break;
                }
                switch (subsubopcao)
                {

                case 1: //Apartamento
                    limpaTela();
                    cabecalho();
                    outputImoveis(imob->getImoveis(imob->indexPorTipo('0')), 2);
                    break;
                case 2: //Casa
                    limpaTela();
                    cabecalho();
                    outputImoveis(imob->getImoveis(imob->indexPorTipo('1')), 2);
                    break;
                case 3: //Terreno
                    limpaTela();
                    cabecalho();
                    outputImoveis(imob->getImoveis(imob->indexPorTipo('2')), 2);
                    break;
                default:
                    puts("Opcao invalida");
                    break;
                }
                
                printf("Para voltar digite 1\n");
                verificacao = inputInteiro();
                if (verificacao == 1)
                    break;

            case 3: //Imoveis por Disponibilidade
                limpaTela();
                exibeMenuDisp();
                printf("Digite a opcao desejada: ");
                subsubopcao = inputInteiro();

                if (subsubopcao == 3)
                {
                    break;
                }
                else if (subsubopcao > 3 || subsubopcao < 1)
                {
                    puts("Opcao invalida");
                    break;
                }
                switch (subsubopcao)
                {
                case 1:
                    limpaTela();
                    cabecalho();
                    outputImoveis(imob->getImoveis(imob->indexPorDisponibilidade(true)), 2);
                    break;
                case 2:
                    limpaTela();
                    cabecalho();
                    outputImoveis(imob->getImoveis(imob->indexPorDisponibilidade(false)), 2);
                    break;
                default:
                    break;
                }
                printf("Para voltar digite 1\n");
                verificacao = inputInteiro();
                if (verificacao == 1){
                    break;
                }
            }
            break; 
        case 3: //Buscar imoveis
            limpaTela();
            buscar(imob, 0);
            printf("Para voltar digite 1\n");
            verificacao = inputInteiro();
            if (verificacao == 1){
                break;
            }
            break;
        case 4: //Remover Imovel
            limpaTela();
            buscar(imob, 1);
            printf("Para voltar digite 1\n");
            verificacao = inputInteiro();
            if (verificacao == 1)
                break;
        case 5: //Editar Imovel
            limpaTela();
            buscar(imob, 2);
            printf("Para voltar digite 1\n");
            verificacao = inputInteiro();
            if (verificacao == 1)
                break;
        case 6: //"Salvar"
            return;
        default:
            puts("Opcao invalida");
            break;
        }
    }
}

void Front::editarRemover(vector<int> index, int flag, Imobiliaria *imob)
{
    int verificacao = 0;
    int indexEditar;
    Imovel *ptrIm;

    std::string titulo;
    double valor;
    double area1;
    Endereco endereco;
    int andar;
    double valorCondominio;
    int numQuartos;
    int numVagas;
    string posicao;
    double area2;
    int numPavimentos;
    int num;
    int tip;
    int disp;

    outputImoveis(imob->getImoveis(index), 2);

    switch (flag)
    {
    case 1:
        cout << endl << "Confirma a remoção de todos estes imoveis?" << endl
                << " 1 - Sim" << endl
                << " 2 - Não" << endl;
        verificacao = inputInteiro();
        if(verificacao == 1){
            imob->removerImoveis(index);
            cout << "Remoção concluida." << endl;
        }else{
            cout << "Remoção cancelada." << endl;
        }
        break;

    case 2:
        cout << endl << "Qual destes imoveis você deseja editar?" << endl;
        indexEditar = inputInteiro();
        indexEditar = index[indexEditar-1];
        cout << endl << "Insira as informações do novo imovel:" << endl;

        //Cadastro do novo imovel
        while (1)
        {
            limpaTela();
            cabecalho();
            printf("Voce deseja adicionar um(a): \n"
                    "\t 1- Apartamento\n"
                    "\t 2- Casa\n"
                    "\t 3- Terreno\n"
                    "\t 4- Voltar\n");
            tip = inputInteiro();
            if (tip < 1 || tip > 4){
                break;
                puts("Opcao invalida");

            }
            puts("Opcao invalida");
        }
        switch (tip)
        {
        case APTO:

            
            titulo=inputStr("Digite o titulo: ");
            while (1)
            {
                limpaTela();
                cabecalho();
                puts("O imovel esta disponivel para?");
                puts("\t1 - Aluguel");
                puts("\t2 - Venda");

                printf("Digite um valor válido: ");
                disp = inputInteiro();
                if (disp == 1 || disp == 2)
                    break;
                puts("Opcao invalida");
            }
            disp=(disp == 1 ? false : true);
            cout << "Digite o valor: " << endl;
            valor=inputValor();
            printf("Digite o numero de quartos: ");
            numQuartos=inputInteiro();
            printf("Digite a quantidade de vagas na garagem: ");
            numVagas=inputInteiro();
            printf("Digite o preco do condominio: ");
            valorCondominio=inputValor();
            posicao=inputStr("Digite a posicao do apartamento: ");
            printf("Digite a area do apartamento: ");
            area1=(inputValor());
            printf("Digite o andar: ");
            andar=inputInteiro();
            endereco.setCep(inputStr("Digite o cep: "));
            endereco.setCidade(inputStr("Digite a cidade: "));
            endereco.setBairro(inputStr("Digite o bairro: "));
            endereco.setLogradouro(inputStr("Digite a rua: "));
            printf("Digite o numero: ");
            num = inputInteiro();
            endereco.setNumero(num);

            ptrIm = new Apartamento(endereco,disp,valor,titulo,andar,valorCondominio,area1,numQuartos,posicao,numVagas);
            break;
        case CASA:
            titulo=inputStr("Digite o titulo: ");
            while (1)
            {
                limpaTela();
                cabecalho();
                puts("O imovel esta disponivel para?");
                puts("\t1 - Aluguel");
                puts("\t2 - Venda");
                printf("Digite um valor válido: ");
                cin >> disp;
                cin.ignore();
                if (disp == 1 || disp == 2)
                    break;
                puts("Opcao invalida");
            }
            disp=(disp == 1 ? false : true);
            cout << "Digite o valor: " << endl;
            valor=inputValor();
            printf("Digite o numero de quartos: ");
            numQuartos=inputInteiro();
            printf("Digite o numero de pavimentos: ");
            numPavimentos=inputInteiro();
            printf("Digite a area do terreno: ");
            area1=inputValor();
            printf("Digite a area construida: ");
            area2=inputValor();

            endereco.setCep(inputStr("Digite o cep: "));
            endereco.setCidade(inputStr("Digite a cidade: "));
            endereco.setBairro(inputStr("Digite o bairro: "));
            endereco.setLogradouro(inputStr("Digite a rua: "));
            printf("Digite o numero: ");
            num = inputInteiro();
            endereco.setNumero(num);
            
            ptrIm = new Casa(endereco,disp,valor,titulo,numPavimentos,numQuartos,area1,area2);
            break;
        case TERRENO:
            titulo = inputStr("Digite o titulo: ");
            while (1)
            {
                limpaTela();
                cabecalho();
                puts("O imovel esta disponivel para?");
                puts("\t1 - Aluguel");
                puts("\t2 - Venda");
                printf("Digite um valor válido: ");
                cin >> disp;
                cin.ignore();
                if (disp == 1 || disp == 2)
                    break;
                puts("Opcao invalida");
            }
            disp = (disp == 1 ? false : true);
            cout << "Digite o valor: " << endl;
            valor = inputValor();
            cout << "Digite a area do terreno: ";
            area1 = inputValor();
            endereco.setCidade(inputStr("Digite a cidade: "));
            endereco.setBairro(inputStr("Digite o bairro: "));
            endereco.setLogradouro(inputStr("Digite a rua: "));
            printf("Digite o numero: ");
            endereco.setNumero(inputInteiro());

            ptrIm = new Terreno(endereco, disp, valor, titulo, area1);
            break;
        }

        imob->editarImovel(ptrIm, indexEditar);
        cout << "Edição concluida." << endl;

        break;
    
    default:
        break;
    }
}

void Front::buscar(Imobiliaria *imob, int flag)
{
    int opcao;
    double valor;
    bool disp;
    string name1;
    string name2;
    vector<int> index;
    vector<int>index1;
    vector<int>index2;

    exibeMenuBuscar();

    opcao = inputInteiro();
    if (opcao == 9)
        return;
    switch (opcao)
    {
    case 1:
        name1 = inputStr("Digite o titulo: ");
        index = imob->indexPorTitulo(name1);
        if (index.empty())
            cout << "Titulo nao encontrado!" << endl;
        else
            editarRemover(index, flag, imob);
        break;
    case 2:
        name1 = inputStr("Digite o Bairro: ");
        index=imob->indexPorBairro(name1);
        if (index.empty())
            cout << "Bairro nao encontrado!" << endl;
        else
            editarRemover(index, flag, imob);
        break;
    case 3:
        name1 = inputStr("Digite a cidade: ");
        index=imob->indexPorCidade(name1);
        if (index.empty())
            cout << "Cidade nao encontrada!" << endl;
        else
            editarRemover(index, flag, imob);
        break;
    case 4:
        cout << "Digite o valor: ";
        if (index.empty())
            cout << "Nao existem imoveis abaixo desse valor!" << endl;
        else
            editarRemover(index, flag, imob);
        break;
    case 5:
        name1 = inputStr("Digite o bairro:");
        index = imob->indexPorBairro(name1);
        cout << "Digite o valor: ";
        valor = inputValor();
        index1 = imob->indexPorValor(valor);
        index2 = imob->combinarFiltros(index,index1);

        if (index2.empty())
            cout << "Nao foi encontrado imoveis com esses parametros!" << endl;
        else
             outputImoveis(imob->getImoveis(index2), 2);
        break;
       
    case 6:
        name1 = inputStr("Digite a cidade");
        index =imob->indexPorCidade(name1);
        cout << "Digite o valor: ";
        valor = inputValor();
        index1=imob->indexPorValor(valor);
        index2=imob->combinarFiltros(index,index1);

        if (index2.empty())
            cout << "Nao foi encontrado imoveis com esses parametros!" << endl;
        else
             outputImoveis(imob->getImoveis(index2), 2);
        break;
    case 7:
        while (1)
        {
            exibeDisp();
            if (inputInteiro() != 1 || inputInteiro() != 2)
                cout << "Opcao invalida\n";
            else
            {
                disp = inputInteiro() == 1 ? true : false;
                printf("Digite o bairro: ");
                cin.ignore();
                getline(cin, name1);
                if (verificaStr(name1))
                    break;
            }
        }
        index=imob->indexPorDisponibilidade(disp);
        index1=imob->indexPorBairro(name1);
        index2=imob->combinarFiltros(index,index1);
        if (index2.empty())
            cout << "Nao foi encontrado imoveis com esses parametros!" << endl;
        else
             outputImoveis(imob->getImoveis(index2), 2);
        break;
    case 8:
        while (1)
        {
            exibeDisp();
            if (inputInteiro() != 1 || inputInteiro() != 2)
                cout << "Opcao invalida\n";
            else
            {
                disp = inputInteiro() == 1 ? true : false;
                printf("Digite a cidade: ");
                cin.ignore();
                getline(cin, name1);
                if (verificaStr(name1))
                    break;
            }
        }
        index=imob->indexPorDisponibilidade(disp);
        index1=imob->indexPorCidade(name1);
        index2=imob->combinarFiltros(index,index1);
        if (index2.empty())
            cout << "Nao foi encontrado imoveis com esses parametros!" << endl;
        else
             outputImoveis(imob->getImoveis(index2), 2);
        break;
    default:
        cout << "Escolha outra opcao" << endl;
    }
}

void Front::outputImovel(std::ostream &output, Imovel &imovel, int tipo)
{
    Imovel *ptr = &imovel;
    if (tipo == 1)
    {
        output << "Título: " << ptr->getTitulo() << "\n"
               << fixed << setprecision(2) << "Valor: " << ptr->getValor()<<"\n"
               << "Cidade: " << ptr->endereco.getCidade() << "\n"
               << "Bairro: " << ptr->endereco.getBairro() << "\n";
    }
    if (tipo == 2)
    {
        output << "Título: " << ptr->getTitulo() << "\n"
               << fixed << setprecision(2) << "Valor: " << ptr->getValor() << "\n"
               << "Disponibilidade: " << (ptr->getDisponiblidade() ? "Venda\n" : "Aluguel\n");
        if (ptr->getTipo() == '0')
        {
            output << "Numero de quartos: " << (((Apartamento *)ptr)->getNumQuartos()) << "\n"
                   << "Vagas na garagem: " << (((Apartamento *)ptr)->getNumVagas()) << "\n"
                   << "Andar: " << (((Apartamento *)ptr)->getAndar()) << "\n"
                   << "Area : " << (((Apartamento *)ptr)->getArea()) << "m²\n"
                   << "Posicao: " << (((Apartamento *)ptr)->getPosicao()) << "\n"
                   << "Preco do condominio: " << ((Apartamento *)ptr)->getValorCondominio() << "\n";
        }
        if (ptr->getTipo() == '1')
        {
            output << "Area construida: " << (((Casa *)ptr)->getAreaConstruida()) << "\n"
                   << "Area do terreno: " << (((Casa *)ptr)->getAreaTerreno()) << "\n"
                   << "Numero de pavimentos: " << (((Casa *)ptr)->getNumPavimentos()) << "\n"
                   << "Numero de quartos: " << (((Casa *)ptr)->getNumQuartos()) << "\n";
        }
        if (ptr->getTipo() == '2')
        {
            output << "Area: " << (((Terreno *)ptr)->getArea()) << "\n";
        }
        output << ptr->endereco.getAsString();
    }
}
void Front::outputImoveis(vector<Imovel *> lista, int tipo)
{
    cout << setw(15) << "Exibindo " << lista.size() << " imoveis\n";
    for (size_t i = 0; i < lista.size(); i++)
    {
        separador();
        cout << setw(15) << i + 1 << endl;
        separador();
        outputImovel(cout, *lista[i], tipo);
    }
}
