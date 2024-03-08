#include <iostream>
#include <pqxx/pqxx> 

using namespace std;
using namespace pqxx;

int main(int argc, char* argv[]) {
   try {
      pqxx::connection c{"postgresql://egidio:engcomp@localhost/ci_bd"};
      pqxx::work txn(c);
   } catch (const std::exception &e) {
      cerr << e.what() << std::endl;
      return 1;
   }
}
