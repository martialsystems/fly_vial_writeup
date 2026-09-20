# fly_vial: assortative IBD F

Locks stay on the trees. Index: gist [12835f74](https://gist.github.com/martialsystems/12835f747d6360781f3cc7f91f243178).

## Abstract

Question: does a closed vial of 1,000 diploid flies, paired by genome similarity, raise IBD F faster than random mating at the same N, seed, and load?

Yes on the seed-1 lock. k=3, N=1,000, 80 generations: within-individual IBD F = 0.524 versus random F = 0.034. Census held. Courtship fell on both arms. Engine is closed-form. FlyWire and MaleCNS are templates, not the stepper. Science lock `@e2e22b7`. Logs: `logs/assort_80.json`, `logs/random_80.json`. Do not restamp 0.524 / 0.034.

Seeds 2 and 3 are a screen, not an effect-size estimate. Assortative F = 0.474 and 0.463. Random F = 0.035 and 0.035. All three assortative arms sit well above Wright's random-mating scale. n = 3 does not promote the row from Screen to an estimate.

The question was locked after the split (`pre_specified: false` in `METHODS.yaml`). Falsifier for the seed-1 lock: assortative F not greater than random F at the same N, seed, and load.

Methods card copied from [fly_vial](https://github.com/martialsystems/fly_vial) `METHODS.yaml`:

| Field | Value |
|-------|-------|
| Object | unconstrained evolutionary toy |
| Status | Screen |
| System | N=1,000; 80 generations; k=3 vs random |
| Dynamics | closed-form QTL scalars; no LIF |
| RNG | `numpy.random.default_rng(seed)` |
| n / seeds | 3 (seed 1 lock; seeds 2 and 3 audit files) |
| Locked metric | assortative t=80 F=0.524 vs random F=0.034 |
| Science lock | `e2e22b7` |

A second locked split on the same engine asked whether k=3 drives failure faster when census is allowed to move. `--cap off` still clipped from above. Realized viable births stayed above 1,000 on every generation. T_fail never fired. Collapse under similarity pairing remains untested.

## 1. Question

Does a closed vial of 1,000 diploid flies, paired by genome similarity, raise IBD F faster than random mating at the same N, seed, and load?

Object of study: unconstrained evolutionary toy. Connectome templates label circuit scalars. They do not step the vial. Status on the index row is Screen because n = 3. The seed-1 split is closed as a Yes.

## 2. Falsifier and protocol

Falsifier (seed-1 lock): assortative F not greater than random F at the same N, seed, and load.

Protocol copied from the locked JSON. N = 1,000 diploid adults. 80 non-overlapping generations. Mating is forced k=3 nearest-neighbor pairing on morphology plus courtship-circuit QTLs, or random. Hidden recessive load (16 lethals, 48 sublethals, h = 0) is excluded from similarity. Offspring genomes are Mendelian plus per-locus Gaussian mutation. Density cap samples viable adults uniformly down to 1,000. Recombination is free: each locus segregates independently.

F in the log is `1 - H_t / H_0` from within-individual founder-allele IBD. H_0 = 1, so H = 1 - F is the same number written twice. Heterozygosity is IBD on founder IDs, not a floating-point compare of QTL values. `mean_pairwise_phi` is mean kinship over unordered adult pairs. It is not F (assortative t = 80: F = 0.524, phi = 0.076).

RNG is `numpy.random.default_rng(seed)`. The eval-connectome hook uses `default_rng(seed + 1_000_003)` and does not step the vial. Seed-1 locked logs are hook-off. Seeds 2 and 3 may turn the hook on as an audit. They write new files. They do not replace seed 1.

Population-genetics prior: Wright's exact random-mating inbreeding `1 - (1 - 1/2N)^t` is the scale for the random arm (Wright, 1931, Genetics 16:97-159, doi 10.1093/genetics/16.2.97). At N = 1,000, t = 80 that form is about 0.039. The linear headline 80 / 2,000 = 0.04 is that scale. Logged random F = 0.034 sits a little under it. Assortative k-NN is the treatment.

## 3. Locked seed-1 table

Copied from `logs/assort_80.json` and `logs/random_80.json`. Courtship at t = 0 is omitted: founders have not paired.

Assortative:

| t | n | F | egg viability | fertility | courtship | accepted pairs | clusters |
|--:|--:|--:|----------------:|----------:|----------:|---------------:|---------:|
| 0 | 1,000 | 0.000 | 0.963 | 0.997 |  | 0 | 4 |
| 1 | 1,000 | 0.000 | 0.921 | 0.991 | 0.934 | 372 | 32 |
| 8 | 1,000 | 0.131 | 0.817 | 0.966 | 0.820 | 385 | 98 |
| 20 | 1,000 | 0.217 | 0.787 | 0.959 | 0.744 | 374 | 75 |
| 40 | 1,000 | 0.399 | 0.777 | 0.952 | 0.680 | 382 | 61 |
| 80 | 1,000 | 0.524 | 0.748 | 0.958 | 0.595 | 386 | 48 |

Random:

| t | n | F | egg viability | fertility | courtship | accepted pairs | clusters |
|--:|--:|--:|----------------:|----------:|----------:|---------------:|---------:|
| 0 | 1,000 | 0.000 | 0.963 | 0.997 |  | 0 | 4 |
| 1 | 1,000 | 0.000 | 0.918 | 0.990 | 0.930 | 493 | 10 |
| 8 | 1,000 | 0.005 | 0.871 | 0.979 | 0.861 | 493 | 77 |
| 20 | 1,000 | 0.008 | 0.832 | 0.969 | 0.772 | 488 | 25 |
| 40 | 1,000 | 0.021 | 0.784 | 0.959 | 0.690 | 481 | 7 |
| 80 | 1,000 | 0.034 | 0.791 | 0.959 | 0.599 | 485 | 2 |

Independent fitness numbers, egg-to-adult viability, t = 0 to t = 80: assortative 0.963 to 0.748; random 0.963 to 0.791. Fertility: 0.997 to 0.958 assortative, 0.997 to 0.959 random. Courtship uses the first generation that pairs (t = 1), then t = 80: 0.934 to 0.595 assortative, 0.930 to 0.599 random. Those two courtship series move together. The courtship drop is not the assortative signature.

## 4. Three-seed screen

Seeds 2 and 3 write `logs/assort_80_s2.json` and friends. Assortative F = 0.474 (seed 2) and 0.463 (seed 3), both much greater than Wright (~0.04). Random F = 0.035 and 0.035. Courtship still falls on both arms. Eval hook was on for those four runs only, as an audit. Title stays seed 1.

n = 3 is a screen. A later tree may rerun the locked protocol at n ≥ 10 and report the distribution. That run would write new files. It would not restamp `logs/assort_80.json`.

## 5. Cap-off split

Question: at the same seed, load, and k, does k=3 similarity pairing drive the vial to failure faster than random mating when census is allowed to move?

This run did not answer that. `--cap off` only refuses to invent adults when short. The 1,000 ceiling still clips from above. Realized viable births (`n_viable` before clip) stayed above 1,000 on every generation of every vial. Display n was pinned at 1,000 from the surplus. T_fail rules (n = 0, accepted pairs = 0, or n < 50 and egg viability < 0.20) never fired because they cannot fire while that surplus holds. Removing the cap did not make similarity pairing the faster route to failure.

| seed | knn T_fail | random T_fail | knn min n_viable | random min n_viable |
|-----:|-----------:|--------------:|-----------------:|--------------------:|
| 1 | 200 | 200 | 1,959 | 2,644 |
| 2 | 200 | 200 | 1,997 | 2,509 |
| 3 | 200 | 200 | 1,970 | 2,464 |

Two locked results, zero collapse results: capped k=3 raises F with census held and courtship falling on both arms; ceiling still binding, nobody dies by t=200.

## 6. Reduction

Female template: FlyWire 139,255 neurons, whole brain, no VNC (Dorkenwald et al., Nature 2024, doi 10.1038/s41586-024-07558-y). Male template: MaleCNS 166,691 neurons, brain plus ventral nerve cord (Berg et al., Cell 189:5504-5526, 2026-09-03, doi 10.1016/j.cell.2026.08.015). The tree locks 166,691. Female locomotion and copulation-motor scores are closed-form overlays on that brain map. vpoDN and song CPG names in the G2P map are circuit labels for those scalars.

Original `fly_vial` code is MIT. MaleCNS is CC BY 4.0. A citation file (`CITATION.cff`) lives on the tree. Artifact DOI is empty until a Zenodo (or other) deposit exists. Do not invent a DOI.

This note does not fold the vampire trees. Those questions live in [vial_vampire_writeup](https://github.com/martialsystems/vial_vampire_writeup) and halt at 0 of 3 on bite share and mosquito theft. The closed-vial block on the index gist states the same template rule for the whole arm.

## 7. Replay

Hash-check or rebuild in a temp path. Never overwrite the lock files.

```
.venv/bin/python -m pytest
.venv/bin/python scripts/reproduce_lock.py
.venv/bin/python scripts/reproduce_lock.py --rerun
```

Those commands run in [fly_vial](https://github.com/martialsystems/fly_vial) `@e2e22b7`. Pin: numpy 2.5.3, pytest 9.1.1, `numpy.random.default_rng`. Expected sha256 of `logs/assort_80.json`: `92a328278e62c4c607749c9358cdc733e1f06424a4b7f13c97c352ce4f4f759b`.

## Accountability (2026-09-20)

Results. Seed-1 metrics are Python engine output at tag `science-e2e22b7` (`logs/assort_80.json`, `logs/random_80.json`; display F = 0.524 vs 0.034). They were not generated by a language model. The drafting tool did not touch the engine.

Text. The computational note (`NOTE.md` / `docs/fly_vial_f_note.pdf`), the methods card, and the index gist prose were drafted with Grok (xAI). The depositor reviewed the text against the locked logs and takes responsibility for it. No AI tool is an author.

Release: https://github.com/martialsystems/fly_vial/releases/tag/science-e2e22b7

## Cite this lock (2026-09-20)

Martial Systems LLC. (2026). fly_vial assortative IBD F lock (science-e2e22b7) [Computer software]. https://github.com/martialsystems/fly_vial/releases/tag/science-e2e22b7

SWHID: swh:1:snp:1ca342b7bacb5c9f996cf97a39933df3eb6c056e

There is no DOI. The gist Artifact DOI cell stays empty until a `10.` identifier exists.

## Sources (2026-09-20)

Records checked on Crossref, 2026-09-20.

Berg, S., Beckett, I. R., Costa, M., Schlegel, P., Januszewski, M., Marin, E. C., Nern, A., et al. (2026). Sexual dimorphism in the complete Drosophila male central nervous system connectome. Cell, 189(18), 5504-5526.e15. https://doi.org/10.1016/j.cell.2026.08.015

Dorkenwald, S., Matsliah, A., Sterling, A. R., Schlegel, P., Yu, S. C., McKellar, C. E., Lin, A., et al. (2024). Neuronal wiring diagram of an adult brain. Nature, 634(8032), 124-138. https://doi.org/10.1038/s41586-024-07558-y

Wright, S. (1931). Evolution in Mendelian populations. Genetics, 16(2), 97-159. https://doi.org/10.1093/genetics/16.2.97

Figure 1 (`figures/stack.png`): F versus generation on the seed-1 lock, assortative versus random, with Wright's random-mating form at t = 80 as a scale mark.

Index (pointers only): https://gist.github.com/martialsystems/12835f747d6360781f3cc7f91f243178
