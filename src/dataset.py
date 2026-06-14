from pathlib import Path

from PIL import Image
from torch.utils.data import Dataset


class TrafficSignDataset(Dataset):
    def __init__(
        self,
        dataframe,
        root_dir,
        transform=None
    ):
        self.dataframe = dataframe.reset_index(drop=True)
        self.root_dir = Path(root_dir)
        self.transform = transform

    def __len__(self):
        return len(self.dataframe)

    def __getitem__(self, index):
        if index < 0 or index >= len(self.dataframe):
            raise IndexError(
                f"Index {index} is outside dataset range."
            )

        row = self.dataframe.iloc[index]
        image_path = self.root_dir / row["Path"]

        if not image_path.exists():
            raise FileNotFoundError(
                f"Image file not found: {image_path}"
            )

        with Image.open(image_path) as image:
            image = image.convert("RGB")

        label = int(row["ClassId"])

        if self.transform is not None:
            image = self.transform(image)

        return image, label