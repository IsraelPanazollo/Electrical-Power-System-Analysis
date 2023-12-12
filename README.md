# Electrical-Power-System-Analysis
Este repositório contém o que desenvolvi como bolsista na UFSM em Python e que resultou no meu trabalho de conclusão do curso, intitulado "Metodologia para Modelagem e Análise Integrada de Redes de Transmissão e Distribuição no Software OpenDSS"

Importante ressaltar que na época que o trabalho foi desenvolvido o ANAREDE se encontrava na versão 11.0.1, o OpenDSS na versão 9.0.0.3. e o Python na versão 3.7.9.

O código "conversor_pwf_to_py" serve para converter o cartão .pwf, utilizado pelo ANAREDE, para um formato de dados usado no ambiente Python.

O código "conversor_py_to_dss" serve para converter os dados obtidos da primeira conversão em um formato .dss para ser lido pelo OpenDSS

Vale destacar que o código aqui foi usado com um cartão exemplo e foi desenvolvido para finalidades acadêmicas, no sentido de descobrir se seria possível realizar uma análise integrada das redes de transmissão e de distribuição em um só programa. 

O conversor não foi projetado para converter qualquer cartão do ANAREDE e o OpenDSS não trabalha de forma identica ao ANARDE, incluindo na modelagem dos elementos da rede. Portanto, este trabalho está longe de ser utilizado numa aplicação comercial. Por outro lado, ele indica que uma análise integrada não é impossível.
