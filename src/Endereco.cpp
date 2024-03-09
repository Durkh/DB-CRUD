#include "Endereco.h"

//Endereco::Endereco(){};

Endereco::Endereco(std::string logradouro, int numero, std::string bairro, std::string cep, std::string cidade){
    setLogradouro(logradouro);
    setNumero(numero);
    setBairro(bairro);
    setCep(cep);
    setCidade(cidade);
};

    std::string Endereco::getLogradouro(){
        return logradouro;
    }
    int Endereco::getNumero(){
        return numero;
    }
    std::string Endereco::getBairro(){
        return bairro;
    }
    std::string Endereco::getCep(){
        return cep;
    }
    std::string Endereco::getCidade(){
        return cidade;
    };
    void Endereco::setEndereco(std::string logradouro, int numero, std::string bairro, std::string cep, std::string cidade){
        setLogradouro(logradouro);
        setNumero(numero);
        setBairro(bairro);
        setCep(cep);
        setCidade(cidade);
    };

    std::string Endereco::getAsString(){
        std::string parte1, parte2, parte3, parte4, parte5, saida1, saida2;
        parte1 = getLogradouro();
        parte2 = std::to_string(getNumero());
        parte3 = getBairro();
        parte4 = getCep();
        parte5 = getCidade();
        
        saida1 = parte1 + ", " + parte2 + ", " + parte3 + ", " + parte4 + ", " + parte5 + ".";
        saida2 = "Rua: " + parte1 + ", " + parte2 + "\n" + "Bairro: " + parte3 + "\n" + "Cep: " + parte4 + "\n" + "Cidade: " + parte5+"\n";


        return saida2;  
    };
    
    void Endereco::setLogradouro(std::string logradouro){
        const char *nameValue = logradouro.data();
        int length = logradouro.size();
        length = (length < MAX ? length : MAX - 1);
        strncpy(this -> logradouro, nameValue, length);
        this -> logradouro[length] = '\0';
        
    };
    void Endereco::setNumero(int numero){
        this -> numero = numero;
    };
    void Endereco::setBairro(std::string bairro){
        const char *nameValue = bairro.data();
        int length = bairro.size();
        length = (length < MAX ? length : MAX - 1);
        strncpy(this -> bairro, nameValue, length);
        this -> bairro[length] = '\0';
    };
    void Endereco::setCidade(std::string cidade){
        const char *nameValue = cidade.data();
        int length = cidade.size();
        length = (length < MAX ? length : MAX - 1);
        strncpy(this -> cidade, nameValue, length);
        this -> cidade[length] = '\0';
    };
    void Endereco::setCep(std::string cep)
    {
        const char *nameValue = cep.data();
        int length = cep.size();
        length = (length < MAX ? length : MAX - 1);
        strncpy(this -> cep, nameValue, length);
        this -> cep[length] = '\0';
    }

    /*char toString(string name){
        char str[MAX];
        const char *nameValue = name.data();
        int length = name.size();
        length = (length < MAX ? length : MAX - 1);
        strncpy(str, nameValue, length);
        str[length] = '\0';
        
        return str[length];
    }*/