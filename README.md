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
