import boto3


s3 = boto3.resource('s3')
client = boto3.client('rekognition')


def lista_imagens():
    imagens = []
    bucket = s3.Bucket('fa-imagens-jnt')  # variável = usa função pra buscar elementos no bucket (s3) AWS
    for imagem in bucket.objects.all():  # laço for, normal...
        imagens.append(imagem.key)  # adicionando cada imagem.key na lista imagens (criada no começo da função.

    print(imagens)
    return imagens


def indexa_colecao(imagens):
    for i in imagens:
        response=client.index_faces(
            CollectionID='faces',
            DetectionAttributes=[],
            ExternalImageId=i[:-4],
            Image={
                'S3Object': {
                    'Bucket': 'fa-imagens-jnt',
                    'Name': i,
                    }
                },
            )


# imagens = lista_imagens()
