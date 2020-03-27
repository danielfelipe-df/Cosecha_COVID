#include <iostream>
#include <string>
#include <vector>
#include <fstream>
#include "other_CSV.h"

int main(void)
{
  std::vector<std::string> files;
  read_directory("Data_2", files);
  files.erase(files.begin() + 0);
  files.erase(files.begin() + 0);

  std::cout << files.size() << std::endl;

  std::vector<std::vector<double> > values, aux;

  csv_d(values, "Data_2/"+files[0]);

  std::cout << values.size() << std::endl;

  for(unsigned int i=1; i<files.size(); i++){
    std::cout << i << std::endl;
    csv_d(aux, "Data_2/"+files[i]);
    for(unsigned int j=0; j<aux.size(); j++){
      values[j][0] += aux[j][0];
      values[j][1] += aux[j][1];
      values[j][2] += aux[j][2];
      values[j][3] += aux[j][3];
    }
    aux.clear();
  }

  std::ofstream fout("data_2.csv");
  for(unsigned int i=0; i<values.size(); i++){
    fout << std::to_string(values[i][0]) << '\t';
    fout << std::to_string(values[i][1]) << '\t';
    fout << std::to_string(values[i][2]) << '\t';
    fout << std::to_string(values[i][3]) << '\n';
  }
  fout.close();

  return 0;
}

