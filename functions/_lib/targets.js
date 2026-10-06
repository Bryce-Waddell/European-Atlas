/* Optional reference figures for the appropriation data. Both start empty; fill them from published sources.

   AGE: the adult population's age structure in each region, used to weight respondents so that a region's
   figures are not dominated by whichever age group took the quiz. Shares in each region should sum to 1.
   Source suggestion: Eurostat demo_pjangroup (EU), national statistics offices elsewhere, UN World Population Prospects.
     AGE = { POL: { "18-29": 0.17, "30-49": 0.36, "50-64": 0.24, "65+": 0.23 }, ... }

   BENCH: a published share of adults who attend religious services at least monthly, per region, used to measure
   how far this self-selected sample over- or under-states practice. Source suggestion: European Social Survey
   (rlgatnd), Pew Research Center country surveys.
     BENCH = { POL: 0.42, ... }

   The numbers in the examples above are placeholders, not data. */
export const AGE = {};
export const BENCH = {};
