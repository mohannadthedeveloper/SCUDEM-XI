# Cooperative Foraging Model — SCUDEM XI 2026

A mathematical modelling project investigating how information sharing, deception, and exploration influence cooperative foraging in spider monkeys.

## Overview

This project develops a mathematical model of two spider monkeys searching for a food source while maintaining communication with one another.

The model explores how information detail and deception influence movement, how the monkeys distribute themselves over our habitat, and how changes in search width affect the time required to locate food.

A sensitivity analysis is also conducted to investigate how variations in information detail and spreading rate affect foraging success.

## Research Question

**How do information detail, deception, and spatial coordination influence the time required for two monkeys to locate food?**


## Sensitivity Analysis

A two-parameter sensitivity analysis investigates the combined effects of:

- **Information detail (\(I\))**
- **Spreading rate (\(q\))**

The resulting heatmap represents the time to first foraging success for different parameter combinations.

### Main observations

- Increasing information detail generally reduces the time to first success.
- Increasing spreading rate generally increases the time to first success across the successful regions shown.
- The shortest success times occur at higher information detail and lower spreading rates.
- Some parameter combinations produce no plotted success time within the simulation.

These results illustrate how information availability and spatial coordination interact to influence the model's predicted foraging performance.

## Model Assumptions

1. The system consists of two cooperating monkeys.
2. Both monkeys begin at the same initial position.
3. Both monkeys have identical initial search widths.
4. Both monkeys use the same search-width contraction equation.
5. The monkeys maintain a maximum communication distance \(R\).
6. Their initial spreading is symmetric.
7. Information and deception influence movement through simplified mathematical relationships.
8. The model represents foraging in a simplified spatial environment i.e a one dimensional ecosystem.

## Visualisations and Results

The project includes four principal result plots:

1. **Deception vs. Time to Success** — Investigates how deception influences foraging time.
2. **Information Detail vs. Time to Success** — Examines the effect of information detail on foraging performance.
3. **Position vs. Time** — Illustrates the movement and spatial separation of both monkeys.
4. **Search Width vs. Time** — Shows the exponential contraction of the monkeys' search regions.

An additional sensitivity-analysis heatmap examines the effects of information detail and spreading rate together.



## Running the Project

Clone the repository:

```bash
git clone <your-repository-url>
```

Navigate into the project directory:

```bash
cd cooperative-foraging-model
```


## Project Context

This project was developed for the **SCUDEM XI 2026** mathematical modelling competition.

Its objective is to explore how mathematical modelling can be used to investigate cooperative behaviour, information sharing, and spatial coordination in animal foraging systems.

## Authors

- Mohannad Kahie

**Competition:** SCUDEM XI 2026

**Institution:** Premier Academy

---
