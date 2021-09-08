using NCDataFrame, DataFrames, DelimitedFiles

target_file = ARGS[1]
file = readdlm(target_file)

E = Vector{Float64}(file[2,:][2:end])
t_total = Vector{Float64}(file[:,1][3:end])
total_spectrum = Matrix{Float64}(file[3:end,2:end])
present_spectrum = total_spectrum[1,:]

df = DataFrame(
    "E" => E,
    "dNdE" => present_spectrum
)

t = t_total[1]

show(df)

new_file_name = joinpath(dirname(target_file), replace(basename(target_file), ".txt" => ".nc"))
writenc(df, new_file_name)

println("\nSave NetCDF file to $new_file_name")

cmd = `python nc_plot.py $new_file_name`

run(cmd)

new_plot_name = joinpath(dirname(target_file), replace(basename(target_file), ".txt" => ".png"))

println("Save Plot to $new_plot_name")

