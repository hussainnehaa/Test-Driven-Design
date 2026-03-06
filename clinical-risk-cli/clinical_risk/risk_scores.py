# TODO: First write the purpose, the ins and outs, and the placeholder function for the qSOFA score.
# The function name should be qsofa_score, and it should take the following parameters: rr (respiratory rate) (int),
# sbp (systolic blood pressure) (int), and ams (altered mental status) (bool).
# The function should return an int representing the qSOFA score (0-3).

# purpose: qsofa_score accepts respiratory rate, systolic blood pressure and altered mental status
# ins % outs: rr (int), sbp (int), ams (bool) -> score (int)

def qsofa_score(rr: int, sbp: int, ams: bool) -> int:
    if not isinstance(rr, int) or rr <= 0:
        raise ValueError("Invalid respiratory rate")
    if not isinstance(sbp, int) or sbp <= 0:
        raise ValueError("Invalid systolic blood pressure")
    if not isinstance(ams, bool):
        raise ValueError("Altered mental status must be boolean")
    score = 0
    if rr >= 22:
        score += 1
    if sbp <= 100:
        score += 1
    if ams:
        score += 1
    return score

# TODO: First write the purpose, the ins and outs, and the placeholder function for the CHA2DS2-VASc score.
# The function name should be cha2ds2_vasc_score, and it should take the following parameters: age (int), female (bool),
# chf (congestive heart failure) (bool), htn (hypertension) (bool), dm (diabetes) (bool), stroke (bool),
# vascular (bool).
# The function should return an int representing the CHA2DS2-VASc score.

# purpose: cha2ds2_vasc_score calculates the CHA2DS2-VASc score for stroke risk in atrial fibrillation
# ins: age (int), female (bool), chf (bool), htn (bool), dm (bool), stroke (bool), vascular (bool)
# outs: score (int)
def cha2ds2_vasc_score(age: int, female: bool, chf: bool, htn: bool, dm: bool, stroke: bool, vascular: bool) -> int:
    if not isinstance(age, int) or age <= 0:
        raise ValueError("Invalid age")
    if not isinstance(female, bool):
        raise ValueError("Female must be boolean")
    if not isinstance(chf, bool):
        raise ValueError("CHF must be boolean")
    if not isinstance(htn, bool):
        raise ValueError("HTN must be boolean")
    if not isinstance(dm, bool):
        raise ValueError("DM must be boolean")
    if not isinstance(stroke, bool):
        raise ValueError("Stroke must be boolean")
    if not isinstance(vascular, bool):
        raise ValueError("Vascular must be boolean")
    score = 0
    if chf:
        score += 1
    if htn:
        score += 1
    if dm:
        score += 1
    if stroke:
        score += 2
    if vascular:
        score += 1
    if female:
        score += 1
    if age >= 75:
        score += 2
    elif age >= 65:
        score += 1
    return score
