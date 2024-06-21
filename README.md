# Weapon-Detection-Yolov8
Um projeto para a disciplina de Inteligência Artificial que tem como objetivo detectar armas em vídeos ou web câmera.

Utilizamos um dataset que pode ser encontrado nesse repositório: https://github.com/MichelleCordeiro/weapon-detection.git

ATENÇÃO: Ao adicionarmos esse dataset modificamos o nome das pastas chamadas test dentro das pastas label e images para o nome val, pois dessa forma o código de treinamento funcionou de forma correta.
Utilizamos também o ambiente venv que não foi adicionado no diretório por ser um arquivo muito grande e conter dependências específicas do ambiente local que podem ser facilmente recriadas em outro ambiente usando um arquivo de requisitos como o "requirements.txt".
Também é importante lembrar que utilizamos a biblioteca ultralytics e importamos o yolov8 que pode ser encontrado também nesse repositório com mais instruções: https://github.com/ultralytics/ultralytics.git
