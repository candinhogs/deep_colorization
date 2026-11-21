import os
import pandas as pd
from PIL import Image

DATASET_PATH = './dataset'

DIRECTORIES = {
    'Gray': os.path.join(DATASET_PATH, 'Gray'),
    'ColorfulOriginal': os.path.join(DATASET_PATH, 'ColorfulOriginal')
}

image_data = []

for dataset_type, directory in DIRECTORIES.items():
    for category in sorted(os.listdir(directory)):
        category_path = os.path.join(directory, category)

        for filename in sorted(os.listdir(category_path)):
            image_path = os.path.join(category_path, filename)
            try:
                with Image.open(image_path) as image:
                    width, height = image.size
                    image_data.append({
                        'dataset': dataset_type,
                        'category': category,
                        'filename': filename,
                        'format': image.format,
                        'width': width,
                        'height': height,
                        'resolution': f'{width}x{height}',
                        'channels': len(image.getbands()),
                        'color_mode': image.mode,
                        'file_size_kb': round(
                            os.path.getsize(image_path) / 1024, 2
                        ),
                        'aspect_ratio': round(width / height, 4)
                    })

            except Exception as error:
                print(f'Erro: {image_path}: {error}')

df = pd.DataFrame(image_data)

summary = df.groupby(['dataset', 'category']).agg(
    total_images=('filename', 'count'),
    avg_width=('width', 'mean'),
    avg_height=('height', 'mean'),
    avg_file_size=('file_size_kb', 'mean')
)

print(summary)
