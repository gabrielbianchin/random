# Projeto de adicionar filtros em tempo real pela WebCam

Para executar, digite:
```
python3 main.py **option**
```
No valor de **option**, as opções válidas são:
- cinza -> transforma o vídeo em tons de cinza
- negativo -> transforma o vídeo em negativo
- blur -> aplica filtro passa-baixa
- x -> aplica o operador de Sobel para detecção de bordas perpendiculares ao eixo X
- y -> aplica o operador de Sobel para detecção de bordas perpendiculares ao eixo Y
- realce -> aplica filtro passa-alta
- equalizado -> aplica a equalização do histograma da imagem
- cartoon -> aplica o filtro para tornar imagem como cartoon

Caso nenhuma opção informada seja válida, nenhum filtro será aplicado