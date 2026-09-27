# Updated Table II: maximal-entanglement EA stabilizer codes

This is a working update of Table II in [Lai--Ashikhmin, arXiv:1602.00413](https://arxiv.org/abs/1602.00413).  An entry `a-b` means that the best published lower and upper bounds on the minimum distance are `a` and `b`; a single number is an exact value.  Every entry concerns a binary maximal-entanglement EA stabilizer code `[[n,k,d;n-k]]`.

The seven changes supported by the material in this repository are marked with `†` and listed below the tables.  All other entries are a transcription of the baseline Table II; they are not re-proved here.

## Dimensions `k=1` through `9`

| n \\ k | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 3 | 3 | 2 | — | — | — | — | — | — | — |
| 4 | 3 | 2 | 1 | — | — | — | — | — | — |
| 5 | 5 | 3 | 2 | 2 | — | — | — | — | — |
| 6 | 5 | 4 | 3 | 2 | 1 | — | — | — | — |
| 7 | 7 | 5 | 4 | 3 | 2 | 2 | — | — | — |
| 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | — | — |
| 9 | 9 | 6 | 6 | 5 | 4 | 3 | 2 | 2 | — |
| 10 | 9 | 7 | 6 | 6 | 5 | 4 | 3 | 2 | 1 |
| 11 | 11 | 8 | 7 | 6 | 6 | 5 | 4 | 3 | 2 |
| 12 | 11 | 9 | 8 | 7 | 6 | 5† | 4 | 4 | 3 |
| 13 | 13 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 4 |
| 14 | 13 | 10 | 10 | 8 | 7-8 | 6-7 | 6 | 5 | 4 |
| 15 | 15 | 11 | 10 | 9† | 8 | 7-8 | 6-7 | 6 | 5 |
| 16 | 15 | 12 | 11 | 10 | 9 | 8 | 7-8 | 6-7 | 6 |
| 17 | 17 | 13 | 12 | 11 | 9-10 | 8-9 | 7-8 | 7-8 | 6-7 |
| 18 | 17 | 14 | 13 | 11-12 | 10-11 | 9-10 | 9† | 8-9 | 8-9 |
| 19 | 19 | 14 | 13† | 12-13 | 11 | 10-11 | 9† | 8-9 | 8-9 |
| 20 | 19 | 15 | 14 | 13 | 12 | 11-12 | 10† | 8-10 | 8-9 |

## Dimensions `k=10` through `18`

| n \\ k | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 11 | 2 | — | — | — | — | — | — | — | — |
| 12 | 2 | 1 | — | — | — | — | — | — | — |
| 13 | 3 | 2 | 2 | — | — | — | — | — | — |
| 14 | 4 | 3 | 2 | 1 | — | — | — | — | — |
| 15 | 4 | 4 | 3 | 2 | 2 | — | — | — | — |
| 16 | 5 | 4 | 4 | 3 | 2 | 1 | — | — | — |
| 17 | 6 | 5 | 4 | 3† | 3 | 2 | 2 | — | — |
| 18 | 6-7 | 5-6 | 5 | 4 | 3 | 3 | 2 | 1 | — |
| 19 | 7 | 6-7 | 5-6 | 5 | 4 | 3 | 3 | 2 | 2 |
| 20 | 7-8 | 6-7 | 6-7 | 5-6 | 5 | 4 | 3 | 2 | 2 |

## Changes from the baseline Table II

| Parameter | Baseline entry | Updated entry | Justification |
|---|---:|---:|---|
| `[[12,6,d;6]]` | 5-6 | 5 | Classification of additive `[12,6,6]_4` codes plus the quadratic Gauss sum excludes distance 6. |
| `[[15,4,d;11]]` | 9-10 | 9 | Classification of binary `[45,8,20]` codes plus the quadratic Gauss sum excludes distance 10. |
| `[[17,13,d;4]]` | 3-4 | 3 | Classification of additive `[17,13,4]_4` codes excludes a nondegenerate symplectic restriction. |
| `[[18,7,d;11]]` | 8-9 | 9 | A checked Hermitian LCD `[18,7,9]_4` construction exists. |
| `[[19,3,d;16]]` | 13-14 | 13 | Distance 14 would give a binary LCD `[57,6,28]`, which is impossible. |
| `[[19,7,d;12]]` | 8-9 | 9 | A checked Hermitian LCD `[19,7,9]_4` construction exists. |
| `[[20,7,d;13]]` | 9-10 | 10 | A checked Hermitian LCD `[20,7,10]_4` construction exists. |

The entries for `[[18,7,9;11]]`, `[[19,7,9;12]]`, and `[[20,7,10;13]]` are verified by `verify_lcd_constructions.py`.  The reduction behind the `[[19,3,14;16]]` exclusion is explained in the repository README.

There are seven changed parameter families. The table has no claim that all unmarked gaps remain open today: it records only updates verified in this repository.
