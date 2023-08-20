# Face-Verification
A face verification software created with TensorFlow and Python is used to disable the keyboard and mouse when the user is either not detected in the webcam or if it is a different person.

# Technique
![download](https://github.com/NateTheGreat7117/Face-Verification/assets/71854770/968c13d7-35bc-4548-9f08-3f8b1e0fb632)

This model was created using pairwise training. This compares two samples from a dataset and outputs the probability that they come from the same class. Theoretically, the model should be able to distinguish between any two faces, although there is still a lot of error in the model. It could be improved by increasing the size of the dataset, using different algorithms, or increasing augmentation and image preprocessing.

# Update
![triplet-loss-w-keras-and-tf-featured](https://github.com/NateTheGreat7117/Face-Verification-Security/assets/71854770/0fd7c442-5bbf-47ed-96a3-ba14579e50d3)

After realizing that pairwise training may not be the best solution, I realized that I should switch to a Siamese neural network with a triplet loss. This model takes an anchor image(my face for this project) and two input images(one image of my face and one of a random person). The model learns to distinguish between my face and other people's faces over time as it takes the difference in the loss of each input image.
