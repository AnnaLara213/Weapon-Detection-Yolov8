from ultralytics import YOLO

def train_model():
    # Define o modelo YOLOv8
    model = YOLO('yolov8n.yaml')  # ou use o caminho para seu arquivo de configuração
    dataset = 'dataset.yaml'  # Caminho para o arquivo de configuração do dataset
    # Inicia o treinamento
    model.train(data=dataset, epochs=60, batch=6,amp=True,imgsz=320, device='cuda', project='/Users/annal/OneDrive/Documentos/Vai_dar_certo/runs/detect', name='train15')  # Ajuste os parâmetros conforme necessário

if __name__ == "__main__":
    import torch
    torch.multiprocessing.set_start_method('spawn', force=True)  # Configuração para ambiente Windows
    train_model()
