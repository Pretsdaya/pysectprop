#%% Test Section

from IPython.display import display
from pysectprop.formed import CSection
csect1 = CSection(100,40,60,5,1) # Constant thickness 5mm
csect2 = CSection(100,50,50,[6,3,10],1) # Variable thickness [Lower=6mm,Web=3mm,Upper=10mm]

# Display Section Properties

display(csect1)
display(csect2)

# Plot Section

ax = csect1.plot()
ax = csect2.plot()

