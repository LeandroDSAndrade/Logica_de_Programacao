#include <iostream>

using namespace std;



int main(){

    string nomeHeroi;
    string nivel;
    int XP;

    cout << "Digite o nome do Heroi" << endl;
    cin >> nomeHeroi;

    cout << "Digite a quantidade de XP que seu heroi possui" << endl;
    cin >> XP;

    if(XP <= 1000){nivel = "Ferro";
    }   else if (XP <= 2000){nivel = "Bronze";
        }   else if (XP <= 5000){nivel = "Prata";
            }   else if (XP <= 7000){nivel = "Ouro";
                }   else if (XP <= 8000){nivel = "Platina";
                    }   else if (XP <= 9000){nivel = "Ascendente";
                        }   else if (XP <= 10000){nivel = "Imortal";
                            }   else {nivel = "Radiante";
                                } 
    cout << "O heroi de nome " << nomeHeroi << " esta no nivel " << nivel << endl;

    return 0;
    

}