from netCDF4 import Dataset
import matplotlib.pyplot as plt
import sys, os

file = sys.argv[1]

dirname = os.path.dirname(file)
basename = os.path.basename(file)
new_basename = basename.split('.')[0] + '.png'
new_filename = os.path.join(dirname, new_basename)

basename_without_extension = os.path.basename(file).split('.')[0]
names = basename_without_extension.split('_')

new_name = r""
latex_dict = {
    "muon": r"$\mu$",
    "electron": r"$e$",
    "proton": r"$p$",
    "neutron": r"$n$",
    "photon": r"$\gamma$",
    "nu": r"$\nu$",
    "tau": r"$\tau$",
    "up": r"$u$",
    "down": r"$d$",
    "charm": r"$c$",
    "strange": r"$s$",
    "top": r"$t$",
    "bottom": r"$b$",
    "gluon": r"$g$",
    "higgs": r"$h$",
    "mu": r"$\mu$",
    "neutrinos": r"$\nu$",
    "e": r"$e$",
    "nu_e": r"$\nu_e$",
    "nu_mu": r"$\nu_\mu$",
    "nu_tau": r"$\nu_\tau$",
}

previous_name = ""
symbol = ""
for name in names:
    if name in latex_dict:
        if previous_name == "nu":
            temp = previous_name + "_" + name
            new_name = latex_dict[temp]
            symbol = latex_dict[temp]
        else:
            new_name += latex_dict[name]
            previous_name = name
            symbol = latex_dict[name]
    else:
        new_name += name.capitalize()
    new_name += " "

# Import netCDF file
ncfile = file
data = Dataset(ncfile)
var = data.variables

# Use latex
plt.rc('text', usetex=True)
plt.rc('font', family='serif')

# Prepare Plot
plt.figure(figsize=(10,6), dpi=300)
plt.title(new_name, fontsize=16)
plt.xlabel(r'$E$ (GeV)', fontsize=14)
plt.ylabel(r'${\rm d}^2n/{\rm d}E{\rm d}t~({\rm GeV}^{-1}\cdot{\rm s}^{-1}\cdot{\rm cm}^{-3})$', fontsize=14)

# Prepare Data to Plot
x = var['E'][:]
y = var['dNdE'][:]  

# Plot with Legends
plt.loglog(x, y, label=symbol)

# Other options
plt.legend(fontsize=12)
plt.grid()
plt.savefig(new_filename, dpi=300)
