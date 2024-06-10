import json
from bandas.models import Banda  # Substitua 'myapp' pelo nome do seu aplicativo Django

def importa(ficheiro):
    with open(ficheiro) as f:
        dados = json.load(f)
        for banda_data in dados:
            banda = Banda.objects.create(
                nome=banda_data['nome'],
                idade=banda_data['idade'],  # Se o campo idade não estiver presente nos dados, ajuste conforme necessário
                foto=banda_data['foto']
                # Adicione mais campos conforme necessário
            )
            print(f"Banda '{banda.nome}' importada com sucesso.")