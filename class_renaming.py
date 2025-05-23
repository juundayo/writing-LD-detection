# ----------------------------------------------------------------------------#

'''
This is the entire dataset containing 90+ classes.
Missing the capital tonos variants for now.

ORIGINAL_CLASSES = [
    'α_cap', 'α_cap_t', 'α_small', 'α_t', 'αι_cap', 'αι_small', 'αυ_cap', 'αυ_small', 'αυ_t',
    'β_cap', 'β_small', 'γ_cap', 'γ_small', 'γγ_cap', 'γγ_small', 'γκ_cap', 'γκ_small',
    'δ_cap', 'δ_small', 'ε_cap', 'ε_small', 'ε_t', 'ει_cap', 'ει_small', 'ει_t',
    'ευ_cap', 'ευ_small', 'ευ_t', 'ζ_cap', 'ζ_small', 'η_cap', 'η_small', 'η_t',
    'θ_cap', 'θ_small', 'ι_cap', 'ι_small', 'ι_t', 'ι_διαλ', 'ι_τον_διαλ', 'κ_cap',
    'κ_small', 'λ_cap', 'λ_small', 'μ_cap', 'μ_small', 'μπ_cap', 'μπ_small', 'ν_cap',
    'ν_small', 'ντ_cap', 'ντ_small', 'ξ_cap', 'ξ_small', 'ο_cap', 'ο_small', 'ο_t',
    'οι_cap', 'οι_small', 'οι_t', 'ου_cap', 'ου_small', 'ου_t', 'π_cap', 'π_small',
    'ρ_cap', 'ρ_small', 'ς_small', 'σ_cap', 'σ_small', 'στ_cap', 'στ_small', 'τ_cap',
    'τ_small', 'τζ_cap', 'τζ_small', 'τσ_cap', 'τσ_small', 'υ_cap', 'υ_small', 'υ_t',
    'υ_διαλ', 'υ_τον_διαλ', 'υι_cap', 'υι_small', 'φ_cap', 'φ_small', 'χ_cap', 'χ_small',
    'ψ_cap', 'ψ_small', 'ω_cap', 'ω_small', 'ω_t', 'space'
]
'''

# ----------------------------------------------------------------------------#

# Includes every possible single letter character + space. 
ORIGINAL_CLASSES = [
    'α_cap', 'α_cap_t', 'α_small', 'α_t', 
    'β_cap', 'β_small',
    'γ_cap', 'γ_small',
    'δ_cap', 'δ_small',
    'ε_cap', 'ε_cap_t', 'ε_small', 'ε_t', 
    'ζ_cap', 'ζ_small', 
    'η_cap', 'η_cap_t', 'η_small', 'η_t',
    'θ_cap', 'θ_small', 
    'ι_cap', 'ι_cap_t', 'ι_small', 'ι_t', 'ι_διαλ', 'ι_τον_διαλ', 
    'κ_cap', 'κ_small',
    'λ_cap', 'λ_small',
    'μ_cap', 'μ_small', 
    'ν_cap', 'ν_small',
    'ξ_cap', 'ξ_small',
    'ο_cap', 'ο_cap_t', 'ο_small', 'ο_t',
    'π_cap', 'π_small',
    'ρ_cap', 'ρ_small', 
    'σ_2_small', 'σ_cap', 'σ_small', 
    'τ_cap', 'τ_small',  
    'υ_cap', 'υ_cap_t', 'υ_small', 'υ_t',
    'υ_διαλ', 'υ_τον_διαλ',
    'φ_cap', 'φ_small',
    'χ_cap', 'χ_small',
    'ψ_cap', 'ψ_small', 
    'ω_cap', 'ω_cap_t', 'ω_small', 'ω_t', 
    'space'
]

# ----------------------------------------------------------------------------#

class_mapping = {cls: cls for cls in ORIGINAL_CLASSES}

''' Single letters. '''
class_mapping['α_cap'] = 'Α'
class_mapping['α_small'] = 'α'
class_mapping['β_cap'] = 'Β'
class_mapping['β_small'] = 'β'
class_mapping['γ_cap'] = 'Γ'
class_mapping['γ_small'] = 'γ'
class_mapping['δ_cap'] = 'Δ'
class_mapping['δ_small'] = 'δ'
class_mapping['ε_cap'] = 'Ε'
class_mapping['ε_small'] = 'ε'
class_mapping['ζ_cap'] = 'Ζ'
class_mapping['ζ_small'] = 'ζ'
class_mapping['η_cap'] = 'Η'
class_mapping['η_small'] = 'η'
class_mapping['θ_cap'] = 'Θ'
class_mapping['θ_small'] = 'θ'
class_mapping['ι_cap'] = 'Ι'
class_mapping['ι_small'] = 'ι'
class_mapping['κ_cap'] = 'Κ'
class_mapping['κ_small'] = 'κ'
class_mapping['λ_cap'] = 'Λ'
class_mapping['λ_small'] = 'λ'
class_mapping['μ_cap'] = 'Μ'
class_mapping['μ_small'] = 'μ'
class_mapping['ν_cap'] = 'Ν'
class_mapping['ν_small'] = 'ν'
class_mapping['ξ_cap'] = 'Ξ'
class_mapping['ξ_small'] = 'ξ'
class_mapping['ο_cap'] = 'Ο'
class_mapping['ο_small'] = 'ο'
class_mapping['π_cap'] = 'Π'
class_mapping['π_small'] = 'π'
class_mapping['ρ_cap'] = 'Ρ'
class_mapping['ρ_small'] = 'ρ'
class_mapping['σ_cap'] = 'Σ'
class_mapping['σ_small'] = 'σ'
class_mapping['σ_2_small'] = 'ς'
class_mapping['τ_cap'] = 'Τ'
class_mapping['τ_small'] = 'τ'
class_mapping['υ_cap'] = 'Υ'
class_mapping['υ_small'] = 'υ'
class_mapping['φ_cap'] = 'Φ'
class_mapping['φ_small'] = 'φ'
class_mapping['χ_cap'] = 'Χ'
class_mapping['χ_small'] = 'χ'
class_mapping['ψ_cap'] = 'Ψ'
class_mapping['ψ_small'] = 'ψ'
class_mapping['ω_cap'] = 'Ω'
class_mapping['ω_small'] = 'ω'


'''Double letters.'''
'''
class_mapping['αι_cap'] = 'ΑΙ'
class_mapping['αι_small'] = 'αι'
class_mapping['αυ_cap'] = 'ΑΥ'
class_mapping['αυ_small'] = 'αυ'
class_mapping['γγ_cap'] = 'ΓΓ'
class_mapping['γγ_small'] = 'γγ'
class_mapping['γκ_cap'] = 'ΓΚ'
class_mapping['γκ_small'] = 'γκ'
class_mapping['ει_cap'] = 'ΕΙ'
class_mapping['ει_small'] = 'ει'
class_mapping['ευ_cap'] = 'ΕΥ'
class_mapping['ευ_small'] = 'ευ'
class_mapping['μπ_cap'] = 'ΜΠ'
class_mapping['μπ_small'] = 'μπ'
class_mapping['ντ_cap'] = 'ΝΤ'
class_mapping['ντ_small'] = 'ντ'
class_mapping['οι_cap'] = 'ΟΙ'
class_mapping['οι_small'] = 'οι'
class_mapping['ου_cap'] = 'ΟΥ'
class_mapping['ου_small'] = 'ου'
class_mapping['στ_cap'] = 'ΣΤ'
class_mapping['στ_small'] = 'στ'
class_mapping['τζ_cap'] = 'ΤΖ'
class_mapping['τζ_small'] = 'τζ'
class_mapping['τσ_cap'] = 'ΤΣ'
class_mapping['τσ_small'] = 'τσ'
class_mapping['υι_cap'] = 'ΥΙ'
class_mapping['υι_small'] = 'υι'
'''


''' Tonos and dialytika variants. '''
# Single characters.
class_mapping['α_cap_t'] = 'Ά'
class_mapping['α_t'] = 'ά'
class_mapping['ε_cap_t'] = 'Έ'
class_mapping['ε_t'] = 'έ'
class_mapping['η_cap_t'] = 'Ή'
class_mapping['η_t'] = 'ή'
class_mapping['ι_cap_t'] = 'Ί'
class_mapping['ι_t'] = 'ί'
class_mapping['ο_cap_t'] = 'Ό'
class_mapping['ο_t'] = 'ό'
class_mapping['υ_cap_t'] = 'Ύ'
class_mapping['υ_t'] = 'ύ'
class_mapping['ω_cap_t'] = 'Ώ'
class_mapping['ω_t'] = 'ώ'
class_mapping['ι_διαλ'] = 'ϊ'
class_mapping['ι_τον_διαλ'] = 'ΐ'
class_mapping['υ_διαλ'] = 'ϋ'
class_mapping['υ_τον_διαλ'] = 'ΰ'

'''
# Double characters.
class_mapping['αυ_t'] = 'αύ'
class_mapping['ει_t'] = 'εί'
class_mapping['ευ_t'] = 'εύ'
class_mapping['οι_t'] = 'οί'
class_mapping['ου_t'] = 'ού'
'''

# Special characters.
class_mapping['space'] = ' '
