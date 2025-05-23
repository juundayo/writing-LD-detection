import os
import cv2
import numpy as np
from torch.utils.data import Dataset
from PIL import Image, ImageEnhance
import random
from sklearn.model_selection import train_test_split

from class_renaming import class_mapping

# ----------------------------------------------------------------------------#

AUGMENTATIONS = 2000
SPACE_AUGMENTATIONS = 2500
AUGMENT = False

# ----------------------------------------------------------------------------#

'''
Data loading and preparation.

File layout:
    currentfolder/Data/GreekLetters/

    → Inside GreekLetters can be found two folders named CAPS and SMALL.
        →　Both folders contain two separate folders named SingleCharacters and
          DoubleCharacters.
          →　Inside each one of the folders can be found seperate folders, each
            containing a single letter or a combination of two letters - 
            depending on the folder.
'''

# ----------------------------------------------------------------------------#

def dataAugmentation(image_path, aug_number):
    """
    Augmentation function used to take each letter and create a new randomly
    augmented version of it through:
        → Random rotation (-7 to 7).
        → Random contrast (1 to 1.5).
    """
    try:
        original_img = Image.open(image_path).convert('L')
        
        for i in range(aug_number):
            ''' Random rotation (-7 to +7 degrees). '''
            angle = random.uniform(-7, 7)
            img_array = np.array(original_img)
            
            # Image center.
            height, width = img_array.shape[:2]
            image_center = (width/2, height/2)
            
            # Rotation matrix.
            rot_mat = cv2.getRotationMatrix2D(image_center, angle, 1.0)
            
            # Rotating.
            rotated_array = cv2.warpAffine(img_array, rot_mat, 
                                         (width, height),
                                         flags=cv2.INTER_LINEAR,
                                         borderMode=cv2.BORDER_REPLICATE)
            
            # Converting back to PIL Image!
            rotated_img = Image.fromarray(rotated_array)
            
            ''' Random contrast (1.0 to 1.5). '''
            contrast_factor = random.uniform(1.0, 1.5)
            contrast_enhancer = ImageEnhance.Contrast(rotated_img)
            contrast_img = contrast_enhancer.enhance(contrast_factor)
            
            # Saving the augmented image.
            base, ext = os.path.splitext(image_path)
            new_path = f"{base}_aug{i}{ext}"
            contrast_img.save(new_path)
            
    except Exception as e:
        print(f"Error augmenting image {image_path}: {str(e)}")

# ----------------------------------------------------------------------------#

class GreekLetterDataset(Dataset):
    def __init__(self, root_dir, transform=None):
        self.root_dir = root_dir
        self.transform = transform
        self.train_dataset = None
        self.test_dataset = None
        self.load_images()
        
        # Getting all unique classes!
        all_classes = sorted(list(set([img[1] for img in self.train_dataset + self.test_dataset])))
        
        self.classes = []
        for cls in all_classes:
            mapped_cls = class_mapping.get(cls, cls)
            self.classes.append(mapped_cls)
                
        self.class_to_idx = {cls: i for i, cls in enumerate(self.classes)}
        self.original_to_idx = {orig_cls: i for i, orig_cls in enumerate(all_classes)}
        

    def iterate_through(self):
        images_by_class = {}
        character_types = ['SMALL', 'CAPS', 'SPECIAL']
        sub_folders = ['SingleCharacters', 'Symbols']

        for char_type in character_types:
            char_type_dir = os.path.join(self.root_dir, char_type)
            if not os.path.exists(char_type_dir):
                continue
                
            for sub_folder in sub_folders:
                sub_folder_dir = os.path.join(char_type_dir, sub_folder)
                if not os.path.exists(sub_folder_dir):
                    continue
                
                for letter_folder in sorted(os.listdir(sub_folder_dir)):
                    letter_path = os.path.join(sub_folder_dir, letter_folder)
                    if not os.path.isdir(letter_path):
                        continue
                        
                    # Saving the letter as a class name.
                    class_name = letter_folder
                    images_by_class.setdefault(class_name, [])
                    
                    # Skipping to avoid duplicates!
                    for img_name in os.listdir(letter_path):
                        if '_aug' in img_name:
                            continue

                        img_path = os.path.join(letter_path, img_name)
                        images_by_class[class_name].append(img_path)

        return images_by_class

    def load_images(self):
        all_images = self.iterate_through()

        train_dataset = []
        test_dataset = []

        for class_name, image_paths in all_images.items():
            train_imgs, test_imgs = train_test_split(
                image_paths, test_size=0.3, random_state=1
            )

            train_dataset.extend([(path, class_name) for path in train_imgs])
            test_dataset.extend([(path, class_name) for path in test_imgs])
            
            '''Creating augmentations for the train and test dataset.'''
            if AUGMENT:
                aug_number = SPACE_AUGMENTATIONS if class_name == 'space' else AUGMENTATIONS

                # Augmentations in the train set.
                for path in train_imgs:
                    for i in range(aug_number):
                        dataAugmentation(path, 1)
                        base, ext = os.path.splitext(path)
                        aug_path = f"{base}_aug0{ext}"

                        if os.path.exists(aug_path):
                            renamed_path = f"{base}_augT{i}{ext}"
                            os.rename(aug_path, renamed_path)
                            train_dataset.append((renamed_path, class_name))

                # Augmentations in the test set.
                for path in test_imgs:
                    for i in range(aug_number):
                        dataAugmentation(path, 1)
                        base, ext = os.path.splitext(path)
                        aug_path = f"{base}_aug0{ext}"

                        if os.path.exists(aug_path):
                            renamed_path = f"{base}_augV{i}{ext}"
                            os.rename(aug_path, renamed_path)
                            test_dataset.append((renamed_path, class_name))

            
        if AUGMENT:
            print(f"Created augmentations successfully!")

        self.train_dataset = train_dataset
        self.test_dataset = test_dataset
        print("Loaded datasets successfully!")

    def __len__(self):
        return len(self.images)
    
    def __getitem__(self, idx):
        img_path, label = self.images[idx]
        image = Image.open(img_path).convert('L')
        
        if self.transform:
            image = self.transform(image)
            
        label_idx = self.original_to_idx[label]        
        return image, label_idx
    
    def get_datasets(self):
        return (
            GreekLetterSubDataset(self.train_dataset, self.transform,
                                   self.original_to_idx),
            GreekLetterSubDataset(self.test_dataset, self.transform, 
                                  self.original_to_idx)
        )
    
class GreekLetterSubDataset(Dataset):
    def __init__(self, samples, transform, original_to_idx):
        self.samples = samples
        self.transform = transform
        self.original_to_idx = original_to_idx

    def __len__(self):
        return len(self.samples)

    def __getitem__(self, idx):
        img_path, label = self.samples[idx]
        image = Image.open(img_path).convert('L')

        if self.transform:
            image = self.transform(image)
        label_idx = self.original_to_idx[label]

        return image, label_idx
    
# ----------------------------------------------------------------------------#

