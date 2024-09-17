#! /bin/bash
gnuplot -p << EOF
set grid
set title 'Displacement of the wing Tip'
set xlabel 'Time [s]'
set ylabel 'Y-Displacement [m]'
# set style line 1 lt 2 lw 6
# set style line 1 lt 2 lw 6
# set linestyle  2 lt 2 lc 1 # red-dashed
# set linestyle  1 lt 2 lc 1 # red-dashed
plot "./Solid/precice-Solid-watchpoint-tip.log" using 1:9 title "tip" with lines, \
     "./Solid/precice-Solid-watchpoint-tip-trailing.log" using 1:9 title "tip TE" with lines, \
    "./Solid/precice-Solid-watchpoint-tip-leading.log" using 1:9 title "tip LE" with lines     
EOF

