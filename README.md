# GaitUpStepUp
MC@MSD 2nd International StepUP Competition for Biometric Footstep Recognition.

The team is composed of [Maxime Devanne](https://github.com/maxwell1503) and myself [Cyril Meyer](https://github.com/Cyril-Meyer).

We are both member of the [MSD](https://msd-irimas.github.io/) team within the [IRIMAS](https://www.irimas.uha.fr/) research institute.


## TLDR I want to see the best submission method only

* [PrepData](PrepData.ipynb)
  * use export 1 for image video preprocessing
  * export 4 `XId` dict is used during trainning for custom batches
* [TrainV4](TrainV4.ipynb) with `X_AllStepsR_f32_norm` and concat on series channel (V8 area) 
* PredMax (TODO)


## Notebooks explained

* [PrepData](PrepData.ipynb) : from original data to easy to load numpy array
  * Export 1 : export with log norm
  * Export 2 : export with minmax norm
  * Export 3 : 1 with metadata dictionary for custom batches
  * Export 4 : export with L/R pairs and more metadata dictionary for custom batches
  * Export 5 : export with gaussian filter try 1
  * Export 6 : export with gaussian filter try 2
* Train : train model
  * [TrainV1](TrainV1.ipynb) : 1D model train with single foot
  * [TrainV2](TrainV2.ipynb) : contrastive loss / gradient reversal try
  * [TrainV3](TrainV3.ipynb) : contrastive loss with custom batches
  * [TrainV4](TrainV4.ipynb) : 1D model with pairs of feet + contrastive loss + custom batches
* Pred : from trained model to scores
  * [PredV1](PredV1.ipynb) : prediction for 1D models which process 1 foot (merge embedding by averaging)
  * [PredV2](PredV2.ipynb) : prediction for 1D models which process pairs of feet
  * PredMax (TODO)
* inception*.py : models
  * [inception.py](inception.py) : inception model
  * [inceptionembed.py](inceptionembed.py) : inception model + embeding output
  * [inceptiongradreverse.py](inceptiongradreverse.py) : inception model + gradient reversal
  * [inceptionviz.py](inceptionviz.py) : inception model + input in 2D CNN


# More details

Almost everything we have done and try is documented.
If something is missing, do not hesitate to contact us for more informations.

## History

### Best submissions

| Submission | Score | Idea |
|:-|:-|:-|
| 047 | **8.88** | model 082 50, method maxime 4 |
| 037 | *9.20* | model 082 50, method 014 |
| 049 | 9.18 | model 082 50, method maxime 4.1 |
| 048 | 9.64 | model 082 50, method maxime ??? |
| 036 | 10.16 | model 082 100, method 014 |
| 043 | 10.44 | model 091 100, method 014 |

### All submissions

| Submission | Score | Idea |
|:-|:-|:-|
| 028-2 | bug | model 081 200, method 014, platform score bug |
| 029 | 22.36 | model 081 200, method 014 but reverted foots |
| 030 | 13.92 | model 081 200, method 014 but reverted foots 2nd version (flip footstep + also revert reference) |
| 031 | 12.20 | model 081 150, method 014 |
| 028-2 | 13.15 | model 081 200, method 014 |
| 032 | 12.59 | maxime 1, model 071 : baseline distances |
| 033 | 11.39 | maxime 2, model 071 : online distances |
| 034 | 12.93 | maxime 3, model 071 : baseline full manifold distances |
| 035 | 12.03 | model 082 150, method 014 |
| 036 | 10.16 | model 082 100, method 014 |
| 037 | *9.20* | model 082 50, method 014 |
| 038 | 10.51 | maxime 4, model 071 + ??? |
| 039 | 11.93 | maxime 5, model 071 + ??? |
| 040 | 12.80 | model 072 200, method 014 |
| 041 | 12.32 | maxime 6, model 071 + ??? |
| 042 | 11.68 | model 091 50, method 014 |
| 043 | 10.44 | model 091 100, method 014 |
| 044 | 10.89 | model 101 50, method 014 |
| 045 | 10.83 | model 101 25, method 014 |
| 046 | 11.32 | model 102 50, method 014 |
| 047 | **8.88** | model 082 50, method maxime 4 |
| 048 | 9.64 | model 082 50, method maxime ??? |
| 049 | 9.18 | model 082 50, method maxime 4.1 |

| Submission | Score | Idea |
|:-|:-|:-|
| 001   | | error |
| 002   | | error |
| 002-1 | 43.40 | use pretrained on train classification inception as embeding, l2 normalize then cosine similarity between ref / emb and keep using threshold |
| 003   | 41.96 | alternative to 002-1 where left and right foot are merged earlier than cosine |
| 004   | 21.08 | add check between ref and probe pair instead of just probe to all ref |
| 005   | 22.03 | as 004 but different ref/probe checking not using average embed but best match |
| 006   | 22.87 | 004 with minmax-normalization (best model) |
| 007   | 23.40 | 005 with minmax-normalization (best model) |
| 008   | 21.92 | 004 with minmax-normalization (last model) |
| 009   | 21.75 | 004 with model 021 (ref data) |
| 010   | 21.69 | 004 with model 031 |
| 011   | 22.16 | 004 with model 041 best |
| 012   | 21.15 | 004 with model 041 last |
| 013   | 17.89 | model 001 but norm on claim per class |
| 014   | 17.00 | 013 mais medoid + filtre valeur "aberantes" sur les proto |
| 015   | 18.92 | model 001 like 013 but zt-norm |
| 016   | 17.28 | 014 with model 002 last |
| 017   | 19.09 | 014 with model 003 800 |
| 017-2 | 19.09 | 017 with different threshold (checking threshold useless for EER) |
| 018   | 13.20 | model 052, method 014 |
| 019   | 12.27 | model 053, method 014 |
| 020   | 16.64 | model 054, method 014 |
| 021   | 14.52 | model 055 best, method 014 |
| 022   | 14.48 | model 055 last, method 014 |
| 023   | 19.48 | model 061 last, method 014 |
| 024   | 11.53 | model 071 last (300), method 014 |
| 025   | 11.32 | model 071 200, method 014 |
| 026   | 11.53 | model 071 100, method 014 |
| 027   | 12.31 | model 071 best, method 014 |
| 028   | 47.36 | error in code |


## Models

| N°  | Architecture | Input shape      | BatchSize | Norm | More ? |
|:----|:-------------|:-----------------|:----------|:-----|:-------|
| 001 | Inception 1D | None, None, 3000 | 32        | log  | |
| 002 | Inception 1D | None, None, 3000 | 32        | log  | same as 001 but know have best and last |
| 003 | Inception 1D | None, None, 3000 | 32        | log  | same as 002 but with much more epoch (+/- 800 epochs with checkpoint every 100 epoch, it crashed between 800 and 900) |
| 011 | Inception 1D | None, None, 3000 | 32        | minmax  | |
| 021 | Inception 1D | None, None, 3000 | 32        | log  | use ref for train |
| 031 | Conv2D encoder + Inception 1D | None, None, 75, 40, 1 | 32 | log | |
| 041 | Conv2D encoder + Inception 1D | None, None, 75, 40, 1 | 32 | log | other encoder see src |
| 051 | Inception 1D | None, None, 3000 | 32        | log  | triplet loss (not good batch generated, fast try) |
| 052 | Inception 1D | None, None, 3000 | 32        | log  | 051 with a fixed lambda |
| 053 | Inception 1D | None, None, 3000 | 32        | log  | contrastive loss |
| 054 | Inception 1D | None, None, 3000 | 512       | log  | contrastive loss best of 83 epochs (crashes / reboot ?) |
| 055 | Inception 1D | None, None, 3000 | 256       | log  | contrastive loss |
| 061 | Inception 1D | None, None, 3000 | 32        | log  | gradient reversal |
| 071 | Inception 1D | None, None, 3000 | 32        | log  | contrastive loss with 4 class batches |
| 072 | Inception 1D | None, None, 3000 | 32        | log  | contrastive loss with 4 class batches, larger lambda weight 0.5, 200 epochs |
| 081 | Inception 1D | None, None, 6000 | 32        | log  | 071 but use pairs (pairs on channel), 200+ epochs |
| 082 | Inception 1D | None, None, 6000 | 32        | log  | 071 but use pairs (pairs on channel), use all right foot 260 epochs |
| 091 | Inception 1D | None, None, 3000 | 32        | log  | 071 but use pairs (pairs on series length), use all right foot |
| 101 | Inception 1D | None, None, 6000 | 32        | log  | 082 with Gaussian filter on the input (sigma = 0.5) |
| 102 | Inception 1D | None, None, 6000 | 32        | log  | 082 with Gaussian filter on the input (sigma = (0.1, 0.25, 0.25)) |


## Notes

* normalization
  * lognorm seems to work a little better than minmax
* model selection
  * last model seems to perform better than best model for probing
  * 50 epochs seems like a sweet spot, especially for model 071 (or maybe a lucky train)
* model architecture
  * surprisingly, model with image encoder do not perform better than simple 1D model with flatten image input
* loss
  * contrastive loss with custom batches improve performances
