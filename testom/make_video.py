import cv2
import numpy as np


# Создаем пустое изображение размером 100 на 100 пикселей
def make_video_from_text(text, time_video, fps, red, green, blue):
    image = np.full((100, 100, 3), (255, 255, 255), np.uint8)
    # Устанавливаем параметры текста
    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 1
    font_color = (red, green, blue)  # Белый цвет текста
    line_type = cv2.LINE_AA

    # Определяем параметры видео
    video_length = time_video  # Длина видео в секундах
    total_frames = fps * video_length

    # Создаем объект записи видео
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    video_writer = cv2.VideoWriter('./media/running_text.mp4', fourcc, fps, (100, 100))

    # Генерируем видео
    text_width, text_height = cv2.getTextSize(text, font, font_scale, 1)[0]
    text_width -= 100
    dx = text_width / total_frames
    dx = int(-1 * dx // 1 * -1)
    x = 0
    for frame_number in range(total_frames):
        # Очищаем изображение
        image.fill(255)
        # image = np.full((100, 100, 3), (255, 0, 0), np.uint8)
        x = x - dx
        y = (100 + text_height) // 2

        # Рисуем текст на изображении
        cv2.putText(image, text, (x, y), font, font_scale, font_color, 1, line_type)

        # Записываем кадр в видео
        video_writer.write(image)

    # Закрываем объект записи видео
    video_writer.release()