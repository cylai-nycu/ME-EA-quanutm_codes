# Maximal-entanglement EA stabilizer-code notes

Reproducible notes on several open entries in Table II of
[Lai and Ashikhmin, *Linear Programming Bounds for Entanglement-Assisted Quantum Error-Correcting Codes by Split Weight Enumerators*](https://arxiv.org/abs/1602.00413).

The full working table, with every supported update marked and explained, is in [UPDATED_TABLE_II.md](UPDATED_TABLE_II.md).

The parameters use the convention `[[n,k,d;n-k]]` for binary maximal-entanglement EA stabilizer codes.

## Results currently established here

| Parameter | Result | Method |
|---|---|---|
| `[[12,6,6;6]]` | does not exist | Classification of additive `[12,6,6]_4` codes and the quadratic Gauss-sum condition |
| `[[15,4,10;11]]` | does not exist | Classification of binary `[45,8,20]` codes and the quadratic Gauss-sum condition |
| `[[17,13,4;4]]` | does not exist | Classification of additive `[17,13,4]_4` codes; the unique dual has a nontrivial radical |
| `[[19,3,14;16]]` | does not exist | Reduction to a binary LCD `[57,6,28]` code, known not to exist |
| `[[18,7,9;11]]` | exists | Independently checked Hermitian LCD construction |
| `[[19,7,9;12]]` | exists | Independently checked Hermitian LCD construction |
| `[[20,7,10;13]]` | exists | Independently checked Hermitian LCD construction |

The scripts do **not** prove nonexistence merely when a linear/integer program returns `sat`: that only gives a feasible formal weight enumerator. This distinction is deliberate.

## The new exclusion: `[[19,3,14;16]]`

Let `C` be the additive quaternary code associated with a maximal-entanglement EA stabilizer code.  Its binary dimension is `2k`, its minimum Hamming weight is `d`, and the symplectic form is nondegenerate on `C`.  Write a binary generator matrix in paired coordinates as `(A | B)` and put

```
G = (A | B | A+B).
```

Every nonzero quaternary coordinate becomes a binary block of weight two, hence `G` generates a binary `[3n,2k,2d]` code.  Moreover,

```
G G^T = A B^T + B A^T,
```

which is nonsingular because the symplectic form is nonsingular.  Thus this binary code is LCD.

Consequently, a `[[19,3,14;16]]` code would give a binary LCD `[57,6,28]` code.  Liu and Li determine the maximum minimum distance of a binary LCD code of length 57 and dimension 6 to be 27, excluding `[57,6,28]`; see Theorem 20 and Table 2 of [arXiv:2406.02065](https://arxiv.org/abs/2406.02065).

## Reproducing the checks

Requires Python 3.10+ and `z3-solver`.

```shell
python -m pip install -r requirements.txt
python verify_lcd_constructions.py
python ea_maximal_parameter_screen.py
python ea_maximal_parameter_screen.py --table-ii-extra
```

`verify_lcd_constructions.py` enumerates all codewords of the three published GF(4) generator matrices and checks their rank, Hermitian Gram rank, minimum distance, and full weight distribution.

`ea_maximal_parameter_screen.py` checks necessary conditions on formal weight enumerators: quaternary MacWilliams identities, nonnegativity, hull packing, the quadratic Gauss sum, and quadratic Fourier layer constraints.  A satisfying result is not a construction.

## Sources

1. X. Lai and A. Ashikhmin, [arXiv:1602.00413](https://arxiv.org/abs/1602.00413), Table II.
2. Y. Liu and R. Li, [*On the largest minimum distances of [n,6] LCD codes*](https://arxiv.org/abs/2406.02065), especially Corollary 1 and Theorem 20.
3. L. Lu, R. Li, and Y. Ren, [*Optimal Quaternary Hermitian LCD Codes*](https://doi.org/10.3390/e26050373), which supplies the three GF(4) LCD matrices checked here.
4. J. Bierbrauer, S. Marcugini, and F. Pambianco, [*New results for additive quaternary codes*](https://arxiv.org/abs/1804.02468), for the classifications used in the first and third exclusions.
5. I. Bouyukliev and B. Bouyuklieva, [*Classification of Linear Codes by Extending Their Residuals*](https://doi.org/10.1007/978-3-030-50426-7_14), for the binary `[45,8,20]` classification used in the second exclusion.

## Scope

All assertions here concern **additive** binary EA stabilizer codes, unless a row explicitly says that it is a Hermitian LCD (thus GF(4)-linear) construction.  The two notions must not be conflated.
