from bandas.models import Banda, Album, Musica
import json

# Limpando os objetos existentes
Banda.objects.all().delete()
Musica.objects.all().delete()
Album.objects.all().delete()

# Carregando os dados das bandas
with open('bandas/json/bandas.json') as f:
    bandas_data = json.load(f)
    for banda_info in bandas_data:
        # Adicionando instrução de depuração
        print("Ano de criação da banda:", banda_info.get('ano_criacao', 0))

        # Verifica se a banda já existe antes de criar uma nova
        ano_criacao = int(banda_info.get('ano_criacao', 0))  # Convertendo para inteiro
        banda, created = Banda.objects.get_or_create(
            nome=banda_info.get('nome', 'Nome desconhecido'),
            defaults={'ano_criacao': ano_criacao,
                      'nacionalidade': banda_info.get('nacionalidade', 'Desconhecido')}
        )

# Carregando os dados dos álbuns e músicas
with open('bandas/json/musicas.json') as f:
    albuns_data = json.load(f)
    for album_info in albuns_data:
        # Busca a banda pelo nome
        banda = Banda.objects.get(nome=album_info['banda'])

        # Cria o objeto Album
        album, created = Album.objects.get_or_create(
            titulo=album_info['titulo'],
            ano_lancamento=album_info['ano_lancamento'],
            banda=banda
        )

        # Cria os objetos Música
        for musica_info in album_info['musicas']:
            Musica.objects.create(
                titulo=musica_info['titulo'],
                duracao=musica_info['duracao'],
                album=album
            )
