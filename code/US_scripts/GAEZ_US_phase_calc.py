#----------------------------------------------------------------------------------------------------
#                                GAEZ Phase Functions                                
#----------------------------------------------------------------------------------------------------

import pandas as pd
import numpy as np
import re


"""
==================================================================================================
GAEZ Soil Phases - Criteria and Required SSURGO Tables
==================================================================================================

==================================================================================================
| GAEZ Phase                   | Criteria (FAO)                                                 | Required SSURGO Tables                   |
|------------------------------|----------------------------------------------------------------|------------------------------------------|
| **Stony Phase**              | Coarse fragments 15% - 40%                                     | `component`, `chfrags`                   |
| **Lithic Phase**             | Bedrock within 50 cm                                           | `component`, `corestrictions`            |
| **Petric Phase**             | Coarse fragments ≥ 40% or cemented restrictive layer ≤ 100 cm  | `component`, `corestrictions`, `chfrags` |
| **Petrocalcic Phase**        | Cemented carbonate layer (calcrete) ≤ 100 cm                   | `component`, `corestrictions`            |
| **Petrogypsic Phase**        | Cemented gypsum layer ≤ 100 cm                                 | `component`, `corestrictions`            |
| **Petroferric Phase**        | Indurated ironstone or ferric horizon ≤ 100 cm                 | `component`, `corestrictions`            |
| **Fragipan Phase**           | Dense, root-restricting fragipan layer                         | `component`, `corestrictions`            |
| **Duripan Phase**            | Silica-cemented duripan layer ≤ 100 cm                         | `component`, `corestrictions`            |
| **Placic Phase**             | Presence of a thin, iron-cemented pan (placic horizon)         | `component`, `corestrictions`            |
| **Skeletic Phase**           | Coarse fragments ≥ 40% within 50 cm                            | `component`, `chfrags`                   |
| **Rudic Phase**              | Coarse fragments ≥ 40% or dominance of large boulders          | `component`, `chfrags`                   |
| **Gravelly Phase**           | Coarse fragments 15% - 40% within 100 cm                       | `component`, `chfrags`                   |
| **Concretionary Phase**      | Presence of ironstone or nodular concretions ≤ 100 cm          | `component`, `chfrags`                   |
| **Erosion Phase**            | Evidence of severe soil erosion (loss of A horizon)            | `component`, `chorizon`, `mapunit`       |
| **Saline Phase**             | Electrical conductivity (EC) ≥ 4 dS/m                          | `component`, `chorizon`                  |
| **Salic Phase**              | Electrical conductivity (EC) ≥ 15 dS/m                         | `component`, `chorizon`                  |
| **Sodic Phase**              | Exchangeable sodium percentage (ESP) ≥ 6% or SAR ≥ 13          | `component`, `chorizon`                  |
| **Anthraquic Phase**         | Water table ≤ 50 cm or frequent ponding                        | `component`, `muaggatt`, `comonth`       |
| **Inundic Phase**            | Frequently or permanently inundated                            | `component`, `muaggatt`, `comonth`       |
| **Flooded Phase**            | Frequent or permanent ponding                                  | `component`, `muaggatt`, `comonth`       |
| **Water Regime Phase**       | Seasonal water table presence and persistence                  | `muaggatt`                               |
| **Phreatic Phase**           | High water table (≤ 200 cm)                                    | `muaggatt`                               |
| **Excessively Drained Phase**| Soil drains too quickly (Excessively drained class)            | `component`                              |
| **Impermeable Layer Phase**  | Restrictive layer depth classification                         | `component`, `corestrictions`            |
| **Rooting Phase**            | Depth restrictions to root penetration                         | `component`, `corestrictions`            |
==================================================================================================


GAEZ Soil Phase Classification Criteria

This module defines classification criteria for various FAO soil phases based on SSURGO attributes.

1. **Stony Phase**
   - Identified when: `fragvol` (Coarse Fragment Volume) **≥ 35%**.

2. **Lithic Phase**
   - Identified when:
     - `reskind` contains **"lithic bedrock"**, **"paralithic bedrock"**, or **"densic bedrock"**.
     - **AND** `rd` (Depth to Restriction) **≤ 50 cm**.

3. **Petric-Gravelly Phase**
   - Identified when:
     - `fragvol` **≥ 40%**.
     - **AND** `rd` **≤ 100 cm**.

4. **Petrocalcic Phase**
   - Identified when:
     - `reskind` contains **"petrocalcic"**.
     - **AND** `rd` **≤ 100 cm**.

5. **Petrogypsic Phase**
   - Identified when:
     - `reskind` contains **"petrogypsic"**.
     - **AND** `rd` **≤ 100 cm**.

6. **Petroferric Phase**
   - Identified when:
     - `reskind` contains **"petroferric"**.
     - **AND** `rd` **≤ 100 cm**.

7. **Fragipan Phase**
   - Identified when:
     - `reskind` contains **"fragipan"**, **"plinthite"**, or **"ortstein"**.
     - **AND** `reshard` is **not** in the following categories:
       - `"noncemented"`, `"extremely weakly cemented"`, `"weakly cemented"`
       - `"noncoherent"`, `"extremely weakly coherent"`, `"very weakly coherent"`, `"weakly coherent"`.

8. **Duripan Phase**
   - Identified when:
     - `reskind` contains **"duripan"**.
     - **AND** `reshard` is **not** in the following categories:
       - `"noncemented"`, `"extremely weakly cemented"`, `"weakly cemented"`
       - `"noncoherent"`, `"extremely weakly coherent"`, `"very weakly coherent"`, `"weakly coherent"`.

9. **Placic Phase**
   - Identified when: `reskind` contains **"placic"**.

10. **Rudic Phase**
    - Identified when:
      - `fragvol` **≥ 35%**.
      - **OR** `fragkind` contains **"boulder"**, **"cobbles"**, or **"stones"**.

11. **Skeletic Phase**
    - Identified when:
      - `fragvol` **≥ 40%**.
      - **AND** `rd` **≤ 50 cm**.

12. **Concretionary Phase**
    - Identified when:
      - `fragvol` **≥ 40%**.
      - **AND** `fragkind` contains **"concretion"**.

13. **Erosion Phase**
    - Identified when: `erocl` is **2, 3, or 4** (indicating moderate to severe erosion).

14. **Phreatic Phase**
    - Identified when:
      - `watertable` **≤ 50 cm**.
      - **AND** `drainagecl` is **"poorly drained"** or **"very poorly drained"**.
      - **OR** `hydricrating` = `"yes"`.

15. **Anthraquic Phase**
    - Identified when:
      - **Either prolonged ponding OR flooding**:
        - `pondfreqcl` = **"frequent"** or **"occasional"**.
        - **AND** `ponddurcl` = **"long (7-30 days)"** or **"very long (>30 days)"**.
        - **OR**
        - `flodfreqcl` = **"frequent"** or **"occasional"**.
        - **AND** `floddurcl` = **"long (7-30 days)"** or **"very long (>30 days)"**.
      - **AND Waterlogged Soil Condition**:
        - `drainagecl` is **"poorly drained"** or **"very poorly drained"**.
        - **OR** `hydricrating` = `"yes"`.

16. **Inundic Phase**
    - Identified when:
      - **Flooding Criteria**:
        - `flodfreqcl` = **"frequent"** or **"very frequent"**.
        - **AND** `floddurcl` = **"long (7-30 days)"** or **"very long (>30 days)"**.
        - **OR**
        - `flodfreqcl` = **"occasional"**.
        - **AND** `floddurcl` = **"very long (>30 days)"**.
      - **OR Ponding Criteria**:
        - `pondfreqcl` = **"frequent"** or **"common"**.
        - **AND** `ponddurcl` = **"long (7-30 days)"** or **"very long (>30 days)"**.
        - **OR**
        - `pondfreqcl` = **"occasional"**.
        - **AND** `ponddurcl` = **"very long (>30 days)"**.

17. **Saline-Salic Phase**
    - Identified when:
      - `reskind` contains **"salic"**.
      - **OR** `ec_r` (Electrical Conductivity) **≥ 4 dS/m**.

18. **Sodic Phase**
    - Identified when:
      - `reskind` contains **"natric"**.
      - **OR** `esp_r` **≥ 6%**.
      - **OR** `sar_r` **≥ 13**.

19. **Excessively Drained Phase**
    - Identified when:
      - `drainagecl` contains **"excessively drained"** or **"somewhat excessively drained"**.

20. **Impermeable Layer Phase**
    - Classified based on `rd`:
      - **NaN** → Not classified.
      - **>150 cm** → Slight limitation.
      - **80–150 cm** → Moderate limitation.
      - **40–80 cm** → Severe limitation.
      - **≤40 cm** → Very severe limitation.

21. **Water Regime Phase**
    - Classified based on `wtdepannmin`:
      - **NaN** → Not classified.
      - **>80 cm** → No limitation.
      - **40–80 cm** → Moderate limitation.
      - **0–40 cm** → Severe limitation.
      - **=0 cm** → Extreme limitation.

22. **Rooting Phase**
    - Classified based on `rd`:
      - **NaN** → Not classified.
      - **>80 cm** → No limitation.
      - **60–80 cm** → Slight limitation.
      - **40–60 cm** → Moderate limitation.
      - **20–40 cm** → Severe limitation.
      - **≤20 cm** → Very severe limitation.

"""

def classify_gaez_v4_phases(df):
    """
    Classifies soils into GAEZ v4 phases using SSURGO attributes.  Assigns HWSD phase
    IDs to each row in the DataFrame based on soil phase conditions.Returns the
    DataFrame with an additional columns: 'phase_ids_list' containing a list of all 
    matching HWSD phase IDs, 'il', 'swr', 'roots', 'vertic', 'gelic'.

    GAEZ v4 Phases Included:
    - Phases: Stony, Lithic, Petric, Petrocalcic, Petrogypsic, Petroferric, Fragipan, Duripan
        Placic, Rudic, Skeletic, Gravelly, Concretionary, Erosion, Phreatic, Anthraquic,
        Inundic, Flooded, Saline, Salic, Sodic, Excessively Drained
    - Impermeable Layer
    - Soil Water Regime
    - Rooting Phase
    - Vertic
    - Gelic

    Inputs:
        'df' - dataframe created using GAEZ_SSURGO_data script from the following source tables:
            - df_component: SSURGO component table.
            - df_corestrictions: SSURGO corestrictions table.
            - df_chfrags: SSURGO chfrags table.
            - df_muaggatt: SSURGO map unit aggregate table.

    Returns:
        DataFrame with 'cokey' and classification columns for each GAEZ v4 phase.
    """

    # Define HWSD Phase IDs
    PHASE_IDS = {
        'stony': 1,
        'lithic': 2,
        'petric': 3,
        'gravelly': 25,
        'petrocalcic': 4,
        'petrogypsic': 5,
        'petroferric': 6,
        'fragipan': 8,
        'duripan': 9,
        'placic': 17,
        'rudic': 18,
        'skeletic': 20,
        'concretionary': 26,
        'phreatic': 7,
        'anthraquic': 13,
        'inundic': 16,
        'saline': 10,
        'salic': 19,
        'sodic': 11,
        'excessively_drained': 29
    }
    
    # List of conditions as (function, phase_id) tuples
    conditions = [
        (lambda row: row["fragvol"] >= 35, PHASE_IDS['stony']),
        (lambda row: (any(x in str(row["reskind"]).lower() for x in ["lithic bedrock", "paralithic bedrock", "densic bedrock"]) 
                      and row["rd"] <= 50), PHASE_IDS['lithic']),
        (lambda row: (row["fragvol"] >= 40) and (row["rd"] <= 100), PHASE_IDS['petric']),
        (lambda row: (row["fragvol"] >= 40) and (row["rd"] <= 100), PHASE_IDS['gravelly']),
        (lambda row: ("petrocalcic" in str(row["reskind"]).lower()) and (row["rd"] <= 100), PHASE_IDS['petrocalcic']),
        (lambda row: ("petrogypsic" in str(row["reskind"]).lower()) and (row["rd"] <= 100), PHASE_IDS['petrogypsic']),
        (lambda row: ("petroferric" in str(row["reskind"]).lower()) and (row["rd"] <= 100), PHASE_IDS['petroferric']),
        (lambda row: (any(x in str(row["reskind"]).lower() for x in ["fragipan", "plinthite", "ortstein"]) and 
                      str(row["reshard"]).lower() not in {
                          "noncemented", "extremely weakly cemented", "weakly cemented", "noncoherent",
                          "extremely weakly coherent", "very weakly coherent", "weakly coherent"
                      }), PHASE_IDS['fragipan']),
        (lambda row: ("duripan" in str(row["reskind"]).lower() and 
                      str(row["reshard"]).lower() not in {
                          "noncemented", "extremely weakly cemented", "weakly cemented", "noncoherent",
                          "extremely weakly coherent", "very weakly coherent", "weakly coherent"
                      }), PHASE_IDS['duripan']),
        (lambda row: "placic" in str(row["reskind"]).lower(), PHASE_IDS['placic']),
        (lambda row: ((row["fragvol"] >= 35) or 
                      ("boulders" in str(row["fragkind"]).lower() or "cobbles" in str(row["fragkind"]).lower() or "stones" in str(row["fragkind"]).lower())),
         PHASE_IDS['rudic']),
        (lambda row: (row["fragvol"] >= 40) and (row["rd"] <= 50), PHASE_IDS['skeletic']),
        (lambda row: (row["fragvol"] >= 40) and ("concretions" in str(row["fragkind"]).lower()), PHASE_IDS['concretionary']),
        (lambda row: (pd.to_numeric(row["wtdepannmin"], errors="coerce") <= 50) and (
                        str(row["drainagecl"]).lower() in {"poorly drained", "very poorly drained"} or 
                        str(row["hydricrating"]).lower() == "yes"), PHASE_IDS['phreatic']),
        (lambda row: (((str(row["pondfreqcl"]).lower() in {"frequent", "occasional"} and 
                         str(row["ponddurcl"]).lower() in {"long (7 to 30 days)", "very long (more than 30 days)"}) or
                        (str(row["flodfreqcl"]).lower() in {"frequent", "occasional"} and 
                         str(row["floddurcl"]).lower() in {"long (7 to 30 days)", "very long (more than 30 days)"}))
                       and 
                       (str(row["drainagecl"]).lower() in {"poorly drained", "very poorly drained"} or 
                        str(row["hydricrating"]).lower() == "yes")), PHASE_IDS['anthraquic']),
        (lambda row: (((str(row["flodfreqcl"]).lower() in {"frequent", "very frequent"} and 
                         str(row["floddurcl"]).lower() in {"long (7 to 30 days)", "very long (more than 30 days)"}) or
                        (str(row["flodfreqcl"]).lower() == "occasional" and 
                         str(row["floddurcl"]).lower() == "very long (more than 30 days)") or
                        (str(row["pondfreqcl"]).lower() in {"frequent", "common"} and 
                         str(row["ponddurcl"]).lower() in {"long (7 to 30 days)", "very long (more than 30 days)"}) or
                        (str(row["pondfreqcl"]).lower() == "occasional" and 
                         str(row["ponddurcl"]).lower() == "very long (more than 30 days)"))),
         PHASE_IDS['inundic']),
        (lambda row: ("salic" in str(row["reskind"]).lower()) or (row["ec"] >= 4), PHASE_IDS['saline']),
        (lambda row: ("salic" in str(row["reskind"]).lower()) or (row["ec"] >= 15) or (
                        (row["ec"] >= 4) and (row["ph"] >= 8.3)), PHASE_IDS['salic']),
        (lambda row: ("natric" in str(row["reskind"]).lower()) or (row["esp"] >= 6) or (row["sar"] >= 13), PHASE_IDS['sodic']),
        (lambda row: ("excessively drained" in str(row["drainagecl"]).lower() or 
                      "somewhat excessively drained" in str(row["drainagecl"]).lower()), PHASE_IDS['excessively_drained'])
    ]
    
    # Create the 'phase_ids_list' column with a list of matching phase IDs for each row
    df['phase_ids_list'] = df.apply(
        lambda row: [phase_id for condition, phase_id in conditions if condition(row)] or [0],
        axis=1
    )
    
    # Impermeable Layer Classification
    df["il"] = np.select(
        [
            (df["rd"].isna()),
            (df["rd"] > 150),
            (df["rd"] > 80) & (df["rd"] <= 150),
            (df["rd"] > 40) & (df["rd"] <= 80),
            (df["rd"] <= 40)
        ],
        [0, 1, 2, 3, 4],
        default=0
    )

    # Soil Water Regime Classification
    df["swr"] = np.select(
        [
            (df["wtdepannmin"].isna()),
            (df["wtdepannmin"] > 80),
            (df["wtdepannmin"] > 40) & (df["wtdepannmin"] <= 80),
            (df["wtdepannmin"] > 0) & (df["wtdepannmin"] <= 40),
            (df["wtdepannmin"] == 0)
        ],
        [0, 1, 2, 3, 4],
        default=0
    )

    # Rooting Phase Classification
    df["roots"] = np.select(
        [
            (df["rd"].isna()),
            (df["rd"] > 80),
            (df["rd"] > 60) & (df["rd"] <= 80),
            (df["rd"] > 40) & (df["rd"] <= 60),
            (df["rd"] > 20) & (df["rd"] <= 40),
            (df["rd"] <= 80),
            (df["rd"] <= 20)
        ],
        [0, 1, 2, 3, 4, 5, 6],
        default=0
    )

    # vertic/gelic classes
    df["vertic"] = df.apply(classify_gaez_vertic, axis=1)
    df["gelic"] = df.apply(classify_gaez_gelic, axis=1)

    return df


# def classify_gaez_v4_phases(df):
#     """
#     Classifies soils into GAEZ v4 phases using SSURGO attributes.

#     GAEZ v4 Phases Included:
#     - Stony, Lithic, Petric, Petrocalcic, Petrogypsic, Petroferric, Fragipan, Duripan
#     - Placic, Rudic, Skeletic, Gravelly, Concretionary, Erosion
#     - Phreatic, Anthraquic, Inundic, Flooded, Saline, Salic, Sodic
#     - Excessively Drained, Impermeable Layer, Water Regime, Rooting Phase

#     Inputs:
#         - df_component: SSURGO component table.
#         - df_corestrictions: SSURGO corestrictions table.
#         - df_chfrags: SSURGO chfrags table.
#         - df_muaggatt: SSURGO map unit aggregate table.

#     Returns:
#         DataFrame with 'cokey' and classification columns for each GAEZ v4 phase.
#     """

#     # Define classification conditions
#     df["stony_phase"] = (df["fragvol"] >= 35).astype(int)
#     df["lithic_phase"] = ((df["reskind"].str.contains("lithic bedrock|paralithic bedrock|densic bedrock", na=False)) & (df["rd"] <= 50)).astype(int)
#     df["petric_phase"] = ((df["fragvol"] >= 40) & (df["rd"] <= 100)).astype(int)
#     df["gravelly_phase"] = ((df["fragvol"] >= 40) & (df["rd"] <= 100)).astype(int)
#     df["petrocalcic_phase"] = (df["reskind"].str.contains("petrocalcic", na=False) & (df["rd"] <= 100)).astype(int)
#     df["petrogypsic_phase"] = (df["reskind"].str.contains("petrogypsic", na=False) & (df["rd"] <= 100)).astype(int)
#     df["petroferric_phase"] = (df["reskind"].str.contains("petroferric", na=False) & (df["rd"] <= 100)).astype(int)

#     df["fragipan_phase"] = df.apply(
#         lambda row: 1 if (
#             any(x in str(row["reskind"]).lower() for x in ["fragipan", "plinthite", "ortstein"]) and
#             str(row["reshard"]).lower() not in {
#                 "noncemented", "extremely weakly cemented", "weakly cemented", "noncoherent",
#                 "extremely weakly coherent", "very weakly coherent", "weakly coherent"
#             }
#         ) else 0,
#         axis=1
#     )

#     df["duripan_phase"] = df.apply(
#         lambda row: 1 if (
#             "duripan" in str(row["reskind"]) and
#             str(row["reshard"]) not in {
#                 "noncemented", "extremely weakly cemented", "weakly cemented", "noncoherent",
#                 "extremely weakly coherent", "very weakly coherent", "weakly coherent"
#             }
#         ) else 0,
#         axis=1
#     )

#     df["placic_phase"] = df["reskind"].str.contains("placic", na=False).astype(int)
#     df["rudic_phase"] = ((df["fragvol"] >= 35) | df["fragkind"].str.contains("boulders|cobbles|stones", na=False)).astype(int)
#     df["skeletic_phase"] = ((df["fragvol"] >= 40) & (df["rd"] <= 50)).astype(int)
#     df["concretionary_phase"] = ((df["fragvol"] >= 40) & df["fragkind"].str.contains("concretions", na=False)).astype(int)

#     # df["erosion_phase"] = df["erocl"].astype(str).isin(["2", "3", "4"]).astype(int)

#     df["phreatic_phase"] = df.apply(
#         lambda row: 1 if (
#             (pd.to_numeric(row["wtdepannmin"], errors="coerce") <= 50) and
#             (
#                 str(row["drainagecl"]).lower() in {"poorly drained", "very poorly drained"} or
#                 str(row["hydricrating"]).lower() == "yes"
#             )
#         ) else 0,
#         axis=1
#     )

#     df["anthraquic_phase"] = df.apply(
#         lambda row: 1 if (
#             (
#                 (str(row["pondfreqcl"]).lower() in {"frequent", "occasional"} and
#                  str(row["ponddurcl"]).lower() in {"long (7 to 30 days)", "very long (more than 30 days)"}) or
#                 (str(row["flodfreqcl"]).lower() in {"frequent", "occasional"} and
#                  str(row["floddurcl"]).lower() in {"long (7 to 30 days)", "very long (more than 30 days)"})
#             ) and
#             (
#                 str(row["drainagecl"]).lower() in {"poorly drained", "very poorly drained"} or
#                 str(row["hydricrating"]).lower() == "yes"
#             )
#         ) else 0,
#         axis=1
#     )

#     df["inundic_phase"] = df.apply(
#         lambda row: 1 if (
#             (
#                 (str(row["flodfreqcl"]).lower() in {"frequent", "very frequent"} and
#                  str(row["floddurcl"]).lower() in {"long (7 to 30 days)", "very long (more than 30 days)"}) or
#                 (str(row["flodfreqcl"]).lower() == "occasional" and
#                  str(row["floddurcl"]).lower() == "very long (more than 30 days)") or
#                 (str(row["pondfreqcl"]).lower() in {"frequent", "common"} and
#                  str(row["ponddurcl"]).lower() in {"long (7 to 30 days)", "very long (more than 30 days)"}) or
#                 (str(row["pondfreqcl"]).lower() == "occasional" and
#                  str(row["ponddurcl"]).lower() == "very long (more than 30 days)")
#             )
#         ) else 0,
#         axis=1
#     )

#     df["saline_phase"] = (df["reskind"].str.contains("salic", na=False) | (df["ec"] >= 4)).astype(int)
#     df["salic_phase"] = ((df["reskind"].str.contains("salic", na=False)) | (df["ec"] >= 15) | ((df["ec"] >= 4) & (df["ph"] >= 8.3))).astype(int)

#     # "sodic_phase" was a bit different because it used a short-circuited .map. We can break it out:
#     df["sodic_phase"] = (
#         df["reskind"].str.contains("natric", na=False) |
#         ( (df["esp"] >= 6) | (df["sar"] >= 13) )
#     ).astype(int)

#     df["excessively_drained_phase"] = df["drainagecl"].str.contains("excessively drained|somewhat excessively drained", na=False).astype(int)

#     # Impermeable Layer Classification
#     df["impermeable_layer_phase"] = np.select(
#         [
#             (df["rd"].isna()),
#             (df["rd"] > 150),
#             (df["rd"] > 80) & (df["rd"] <= 150),
#             (df["rd"] > 40) & (df["rd"] <= 80),
#             (df["rd"] <= 40)
#         ],
#         [0, 1, 2, 3, 4],
#         default=0
#     )

#     # Water Regime Classification
#     df["water_regime_phase"] = np.select(
#         [
#             (df["wtdepannmin"].isna()),
#             (df["wtdepannmin"] > 80),
#             (df["wtdepannmin"] > 40) & (df["wtdepannmin"] <= 80),
#             (df["wtdepannmin"] > 0) & (df["wtdepannmin"] <= 40),
#             (df["wtdepannmin"] == 0)
#         ],
#         [0, 1, 2, 3, 4],
#         default=0
#     )

#     # Rooting Phase Classification
#     df["rooting_phase"] = np.select(
#         [
#             (df["rd"].isna()),
#             (df["rd"] > 80),
#             (df["rd"] > 60) & (df["rd"] <= 80),
#             (df["rd"] > 40) & (df["rd"] <= 60),
#             (df["rd"] > 20) & (df["rd"] <= 40),
#             (df["rd"] <= 80),
#             (df["rd"] <= 20)
#         ],
#         [0, 1, 2, 3, 4, 5, 6],
#         default=0
#     )

#     # Assuming these two classification functions exist.
#     # If they return "yes"/"no" strings, you may need to cast them to int as well.
#     df["vertic"] = df.apply(classify_gaez_vertic, axis=1)
#     df["gelic"] = df.apply(classify_gaez_gelic, axis=1)

#     return df[[
#         "cokey", "stony_phase", "lithic_phase", "petric_phase", "petrocalcic_phase", "petrogypsic_phase",
#         "petroferric_phase", "fragipan_phase", "duripan_phase", "placic_phase", "rudic_phase",
#         "skeletic_phase", "gravelly_phase", "concretionary_phase", "phreatic_phase",
#         "anthraquic_phase", "inundic_phase", "saline_phase", "salic_phase", "sodic_phase",
#         "excessively_drained_phase", "impermeable_layer_phase", "water_regime_phase", "rooting_phase",
#         "vertic", "gelic"
#     ]]


def classify_gaez_vertic(row):
    """
    Determine if a soil exhibits vertic properties (1/0) for a single row,
    according to FAO criteria using SSURGO data merged into one record.

    Expected columns in the row:
      - taxminalogy (from cotaxfmmin table)
      - clay, pi, lep (from chorizon table)
      - plasticity, stickiness (from chconsistence table)

    Returns:
      int: 1 if the soil is classified as having vertic properties, 0 otherwise.
    """
    # 1. Taxonomic Check (from cotaxfmmin):
    tax = row.get('taxminalogy', '')
    if isinstance(tax, str):
        if re.search(r'\b(smectitic|montmorillonitic|montmorillonitic \(calcareous\))\b', 
                     tax, flags=re.IGNORECASE):
            return 1

    # 2. Define threshold values (from chorizon):
    clay_threshold = 40    # clay must be at least 40%
    pi_threshold = 20      # plasticity index (pi) must be at least 20
    lep_threshold = 15     # lep must be at least 15%

    # 2a. Evaluate numeric criteria (from chorizon):
    numeric_flag = False
    try:
        clay_value = float(row['clay'])
        pi_value = float(row['pi'])
        lep_value = float(row['lep'])
        numeric_flag = (clay_value >= clay_threshold and 
                        pi_value >= pi_threshold and 
                        lep_value >= lep_threshold)
    except (KeyError, ValueError, TypeError):
        numeric_flag = False

    # 2b. Evaluate consistency criteria (from chconsistence):
    consistency_flag = False
    try:
        plasticity_value = str(row['plasticity']).lower()
        stickiness_value = str(row['stickiness']).lower()
        consistency_flag = ('high' in plasticity_value and 'high' in stickiness_value)
    except KeyError:
        consistency_flag = False

    # 3. Decision: if either criteria are met, classify as vertic.
    if numeric_flag or consistency_flag:
        return 1
    else:
        return 0


def classify_gaez_gelic(row):
    """
    Classify GAEZ Gelic Properties for a single row of SSURGO data.
    
    Expected keys in the row:
      - 'taxtempcl': Taxonomic temperature class.
      - 'reskind'  : Permafrost indicator.
      - 'frostact' : Frost action level.
    
    Returns
    -------
    int
        1 if the soil is classified as Gelic based on any of the following:
          - taxtempcl is "subgelic" or "pergelic"
          - reskind equals "permafrost" (case-insensitive)
          - frostact equals "high" (case-insensitive)
        Otherwise, returns 0.
    """
    # Step 1: Check Taxonomic Temperature Class (taxtempcl)
    taxtempcl = str(row.get('taxtempcl', '')).strip().lower()
    if taxtempcl in ['subgelic', 'pergelic']:
        return 1
    
    # Step 2: Check Permafrost Indicator (reskind)
    reskind = str(row.get('reskind', '')).strip().lower()
    if reskind == "permafrost":
        return 1
    
    # Step 3: Check Frost Action (frostact)
    frostact = str(row.get('frostact', '')).strip().lower()
    if frostact == "high":
        return 1
    
    return 0
