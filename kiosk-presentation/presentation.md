---
marp: true
theme: gaia
class: invert
math: mathjax
style: |
  .columns {
    display: grid;
    grid-template-columns: repeat(2, minmax(0, 1fr));
    gap: 1rem;
  }
  table {
    font-size: 0.7em;
    width: 100%;
  }
  td, th {
    padding: 0.1em 0.2em;
  }
  section {
    background-image: url('./images/logo.png');
    background-position: bottom 15px right 15px;
    background-repeat: no-repeat;
    background-size: 60px auto;
  }
  .kiosk-splash {
    position: absolute;
    right: 500px;
    bottom: 0;
    height: 300px;
    z-index: 1;
  }
  .references {
    font-size: 0.6em;
  }
---

<img src="./images/kiosk-splash.png" class="kiosk-splash">

# Measuring the Obvious :mag:
#### A Human Factors Engineering Analysis of Kiosk Accessibility

<span style="color:lightgrey">By:</span> <span style="font-weight:bold">Mark Ogra</span>, Aaron Elrington-Edwards, Shaaz Rizvi



---

### Introduction

#### Human Factors Foundation

1. **Fitts' Law & Target Acquisition**
   - Touch target difficulty ∝ distance/size ratio
   - 172cm height + small UI = computational nightmare
   - Fixed angle compounds motor planning issues

---

#### Human Factors Foundation (cont.)

2. **Cognitive Load Theory**
   - Physical strain increases cognitive overhead
   - Error recovery requires additional reaching
   - Time pressure compounds both issues

3. **Norman's Design Principles**
   - Visibility compromised by physical design
   - Feedback requires additional physical effort
   - Mapping ignores natural affordances

---

#### Problem Space Overview
![height:12cm](images/mindmap.png)
*Interconnected barriers require systematic analysis*

---

#### Current Implementation Issues
- Fixed designs violating ergonomic standards
- Conflicting accessibility accommodations
- Environmental factors impacting usability
- Resource allocation revealing priorities

---

### Methodology

#### Initial Research Steps

<div class="columns">
<div>

1. **Initial Approach (Failed)**
   - Attempted traditional user testing
   - Proposed menu item compensation
   - Received justified criticism
   - Recognized ethical issues

</div>
<div>

2. **Research Pivot**
   - Developed measurement protocol
   - Created evaluation form
   - Obtained survey permission
   - Established documentation

</div>
</div>

---

#### Data Collection & Analysis

<div class="columns">
<div>

3. **Data Collection**
   - Physical measurements
   - Survey distribution
   - Environmental documentation
   - Interface workflow

</div>
<div>

4. **Analysis Protocol**
   - ADA standards review
   - Statistical analysis
   - Correlation studies
   - Cost-benefit evaluation

</div>
</div>

---

#### Tools & Equipment
- Standard measuring tape (physical dimensions)
- Digital level application (screen angles)
- Survey instruments (user feedback)
- Documentation templates (standardization)

---

#### Participant Demographics
![bg left:50% w:90%](images/age_group_distribution.png)

- Medical office setting providing diverse sample
- Natural inclusion of mobility device users
- Age range: 18-65+
- Multiple accessibility needs represented

---

### Physical Analysis

#### Measurement Results vs Standards

| Component | Measured | ADA Requirement | Citation | Impact |
|-----------|----------|-----------------|-----------|---------|
| Total Height | 172cm | 121.9cm max | §308.2.1 Forward Reach | ❌ Exceeds by 50.1cm |
| Screen Center | 80cm | 38-121.9cm | §308.2.1-2 Reach Ranges | ⚠️ Fixed at median |
| Payment Zone | 68-92cm | 38-122cm | §308.3.1 Side Reach | ⚠️ Upper range violation |
| Clear Space | ~50cm | 76cm min | §305.3 Clear Floor | ❌ 34.2% below min |
| Screen Angle | Fixed -1° | Adjustable | §309.4 Operation | ❌ No accommodation |

---

#### Accessibility Conflicts: Physical Design

<div class="columns">
<div>

1. **Height vs Visibility**
   - Lower placement helps wheelchair users
   - Creates strain for standing users
   - Current "solution" ignores principles
   - No single fixed height optimal

</div>
<div>

2. **Space vs Throughput**
   - Wider spacing aids mobility
   - Conflicts with density goals
   - Reveals volume prioritization
   - ADA minimums as maximum

</div>
</div>

---

#### Accessibility Conflicts: Interface

3. **Interface Scaling Paradox**
   - "Wheelchair mode" reduces element size
   - Directly conflicts with visual accessibility
   - Creates false choice between physical and visual access
   - Demonstrates fundamental design failure

---

### System Evaluation

#### Demographic Representation
![bg left:40% w:90%](images/gender_distribution.png)
- Balanced gender representation (48% F, 44% M, 8% NB/Other)
- Age range 18-65+ (medical office setting)
- 47% assistive device usage
- Validates measurement-based approach

---

#### Physical Impact Analysis
![bg left:50% w:90%](images/average_usability_scores_by_barrier.png)

- 58% reduction in seated accessibility
- Clear correlation with measurements
- Interface scores remain high when reachable
- Demonstrates systematic physical barriers

---

#### Empirical Evidence
![bg left:40% w:90%](images/significant_barriers.png)

1. **Key Findings**
   - Screen height dominates (n=8)
   - Physical issues exceed interface problems
   - Observable without exploitation

2. **Impact Analysis**
   - 50% drop in physical ease
   - Interface usable when reachable
   - Systematic barriers confirmed

---

### Implementation Analysis

#### Technical Architecture
Current implementation specifications:
- Intel Core i5-4570TE processor
- 4GB DDR3 RAM
- 128GB SSD
- Windows 10/11 Pro license
- Fixed mounting system

---

#### Resource Analysis

| Component | Current | Alternative | Diff |
|-----------|---------|-------------|------|
| OS | Win ($15-30) | Linux | -$30 |
| Mount | Fixed ($30) | VESA Adj. | +$30 |
| Display | Standard | Anti-glare | +$15 |
| **Total** | **$500** | **$530** | **+$30** |

#### Priority Issues
- Over-specified computing resources
- Under-specified accessibility features
- Cost optimization misaligned with usability

---

### Recommendations

<div class="columns">
<div>

#### Physical Changes
- VESA-compatible mounts
- Anti-glare treatment
- Module placement
- Clear space compliance

</div>
<div>

#### System Changes
- Responsive design
- Multimodal interaction
- Error recovery
- Universal design focus

</div>
</div>

---
### References

1. Department of Justice. (2010). *2010 ADA Standards for Accessible Design*. §308.2.1-309.4.

2. Fitts, P. M. (1954). The information capacity of the human motor system in controlling the amplitude of movement. *Journal of Experimental Psychology*, 47(6), 381-391.

3. Norman, D. A. (2013). *The design of everyday things*. Basic Books. pp. 123-125.

4. u/tamay-idk. (2023). *Specs of a McDonald's kiosk in more detail* [Online forum post]. Reddit. Hardware specifications independently verified through system inspection.

5. Swanson, J., & Calvillo-Gámez, E. H. (2020). Evaluation of touch screen kiosks for enhanced accessibility in public spaces. *International Journal of Human-Computer Studies*, 143, 102501.