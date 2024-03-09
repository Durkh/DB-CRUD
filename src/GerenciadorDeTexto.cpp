#include "GerenciadorDeTexto.h"

std::string GerenciadorDeTexto::strToLower(std::string str)
{
    for (int i = 0; i < str.length(); i++)
    {
        str[i] = tolower(str[i]);
    }
    return str;
}

std::string GerenciadorDeTexto::removeAcento(std::string str)
{ /*
    Para entender essa função, é preciso saber que para processar uma letra com acento c++ usa dois chars:
    um para indicar que o proximo char é um acento, e logo depois o acento em si.
    Por isso comAcentos.size() == 2*(semAcentos.size() - 1) + 1;
    */
    std::string comAcentos = "äáâàãéêëèíîïìöóôòõüúûùç";
    std::string semAcentos = "aaaaaeeeeiiiiooooouuuuc";
    char acento;

    for (int i = 0; i < str.length(); i++)
    {
        if (str[i] == comAcentos[0])
        {
            acento = str[i + 1];
            for (int j = 0; j < comAcentos.length(); j++)
            {
                if (comAcentos[j] == acento)
                {
                    str[i] = semAcentos[j / 2];
                    str.erase(str.begin() + i + 1);
                }
            }
        }
    }
    return str;
}