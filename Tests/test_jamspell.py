import jamspell
from pathlib import Path

corrector = jamspell.TSpellCorrector()

# corrector.LoadLangModel("fr.bin")
print(corrector.LoadLangModel(str(Path(__file__).resolve().parent/"fr.bin")))

mot = "conjecdture"
corr = corrector.FixFragment(mot)

print(corr != mot)
print(mot, corr)
print(corrector)

print(str(Path(__file__).resolve().parent/"fr.bin"))