import cv2
from ultralytics import YOLO

# Carrega o modelo treinado
model = YOLO('/Users/annal/OneDrive/Documentos/Vai_dar_certo/runs/detect/train15/weights/last.pt')

# Define os nomes das classes
class_names = ['pistol', 'smartphone', 'knife', 'monedero', 'billete', 'tarjeta']

# Abre a webcam
cap = cv2.VideoCapture(0)

while True:
    # Captura frame-by-frame
    ret, frame = cap.read()
    if not ret:
        break

    # Realiza a detecção no frame
    results = model(frame)

    # Itera sobre os resultados e desenha as caixas de detecção
    for result in results:
        for bbox in result.boxes:
            # Obtém as coordenadas da caixa de detecção
            x1, y1, x2, y2 = map(int, bbox.xyxy[0])
            confidence = bbox.conf[0]
            class_id = int(bbox.cls[0])
            class_name = class_names[class_id]

            # Desenha a caixa no frame
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            label = f'{class_name} {confidence:.2f}'
            cv2.putText(frame, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

    # Exibe o frame com as detecções
    cv2.imshow('Detecção de Armas', frame)

    # Sai do loop se a tecla 'q' for pressionada
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Libera a webcam e fecha as janelas
cap.release()
cv2.destroyAllWindows()
