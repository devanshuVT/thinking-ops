---
name: TSFM calibration paper
status: blocked
owner: Claude
progress: 10
blocker: Claude sandbox cannot reach Hugging Face, price-data sites or arXiv. Run the experiment repo on Colab or a machine with internet.
next: Build experiment repo and LaTeX template; run once on Colab
done_when: PDF compiled from real results (CRPS, coverage, conformal tables on a pre-registered rolling split)
---
Goal: test whether pretrained time-series models (Chronos-2, TimesFM, Moirai) give calibrated quantile forecasts on daily returns, then add a conformal correction.
Gap: June 2026 finance studies report only MAE on about 5 stocks; no CRPS, coverage or conformal.
