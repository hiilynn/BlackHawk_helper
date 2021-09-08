# BlackHawk Helper

## Pre-requisites

Add `BLACKHAWK_PATH` environment to your `.bashrc` or `.zshrc` or etc.

For example, 

```sh
export BLACKHAWK_PATH="/path/to/blackhawk_v2.0"
```

## Install

```sh
sh install.sh
```

## Usage

Convert `.txt` to `.nc` & Plot spectrum

```sh
julia make_nc.jl results/examples/nu_e_secondary_spectrum.txt
```
