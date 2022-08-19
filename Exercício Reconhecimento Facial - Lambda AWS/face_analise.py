import boto3
import json


s3 = boto3.resource('s3')
client = boto3.client('rekognition')


def detecta_faces():
    faces_detectadas = client.index_faces(
        CollectionID='faces',
        DetectionAttributes=['DEFAULT'],
        ExternalImageId='TEMPORARIA',
        Image={
            'S3Object': {
                'Bucket': 'fa-imagens-jnt',
                'Name': '_analise.png',
                }
            },
        )
    # print(json.dumps(faces_detectadas, indent=4))
    return faces_detectadas


def cria_lista_faceid_detectadas(faces_detectadas):
    faceid_detectadas = []
    for imagens in range(len(faces_detectadas['FaceRecords'])):
        faceid_detectadas.append(faces_detectadas['FaceRecords'][imagens]['Face']['FaceId'])
    return faceid_detectadas


def compara_imagens(faceid_detectadas):
    resultado_comparacao = []
    for ids in faceid_detectadas:
        resultado_comparacao.append(
            client.search_faces(
                CollectionId='faces',
                FaceId=ids,
                FaceMatchThreshold=80,
                MaxFaces=10,
                )
            )
    return resultado_comparacao


def gera_dados_json(resultado_comparacao):
    dados_json = []
    for face_matches in resultado_comparacao:
        if (len(face_matches.get('FaceMatches'))) >= 1:
            perfil = dict(nome=face_matches['FaceMatches'][0]['Face']['ExternalImageId'],
                          faceMatch=round(face_matches['FaceMatches'][0]['Similarity'], 2))
            dados_json.append(perfil)
    return dados_json


def publica_dados(dados_json):
    arquivo = s3.Object('fa-site-jnt', 'dados.json')
    arquivo.put(Body=json.dumps(dados_json))


def exclui_imagem_colecao(faceid_detectadas):
    client.delete_faces(
        CollectionID='faces',
        FaceIds='faceid_detectadas,'
    )


faces_detectadas = detecta_faces()
faceid_detectadas = cria_lista_faceid_detectadas(faces_detectadas)
resultado_comparacao = compara_imagens(faceid_detectadas)
dados_json = gera_dados_json(resultado_comparacao)
publica_dados(dados_json)

print(json.dumps(dados_json, indent=4))
