# Part-of-Speech-Tagging

## Overview
In this project, we tackled the challenge of part-of-speech (POS) tagging for multiple languages under constraints of limited computational resources and absence of training data for the target languages. Our innovative approach centered on the use of adapter modules, which are small, trainable components within a larger pre-trained model. These adapters allow for efficient model adaptation to new tasks without the need for extensive computational power or complete model retraining.

## Running the code
### Dependencies
Dependencies may be installed with pip:
```bash
pip install -r requirements.txt
```
### Data
The data can be downloaded via this command:
```bash
git clone https://github.com/masakhane-io/masakhane-pos.git
```
### Training
run the notebooks adapter_training_for_ibo, adapter_training_for_luo and adapter_training_for_tsn separately then the adapter_fusion notebook. We fuse only the adapters that are responsible for predicting on luo and tsn languages. Finally, run the notebook xlmroberta_train_adapter_pos to train the final adapter to make the model adapt the POS tagging task on ibo language. The inference is done on both luo and tsn languages.
