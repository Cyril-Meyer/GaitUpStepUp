# GaitUpStepUp
MC@MSD 2nd International StepUP Competition for Biometric Footstep Recognition

## History

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

## Models

| N°  | Architecture | Input shape      | BatchSize | Norm | More ? |
|:----|:-------------|:-----------------|:----------|:-----|:-------|
| 001 | Inception 1D | None, None, 3000 | 32        | log  | |
| 011 | Inception 1D | None, None, 3000 | 32        | minmax  | |
| 021 | Inception 1D | None, None, 3000 | 32        | log  | use ref for train |
| 031 | Conv2D encoder + Inception 1D | None, None, 75, 40, 1 | 32 | log | |

### Next things
* Less dumb architecture...
* Classif pairs ?
* Use ref in train ?
* Check par candidat ++ ?

### Uncertainty

For submission 001 to 005, model should be best on the valid set but not sure 100% it was not the last epoch model.
